#!/usr/bin/env python3
"""
Betty Traceability System

Provides complete audit trail linking requirements to verification results.
All records stored as JSON files for easy loading into document databases.
"""

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

# Add parent directory to path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


@dataclass
class RequirementInfo:
    """Requirement linkage information"""
    id: str
    description: str
    source: Optional[str] = None
    issue_id: Optional[str] = None
    requested_by: Optional[str] = None
    rationale: Optional[str] = None
    acceptance_criteria: Optional[List[str]] = None


@dataclass
class VerificationCheck:
    """Individual verification check result"""
    timestamp: str
    check_type: str  # validation, compatibility, integration_test, etc.
    tool: str
    result: str  # passed, failed, warning, skipped
    details: Optional[Dict[str, Any]] = None
    evidence: Optional[str] = None


class TraceabilityLogger:
    """
    Records component lifecycle events for audit trail.

    Stores traceability records as JSON files in .betty-traces/
    for easy loading into document databases (MongoDB, CouchDB, etc.)
    """

    def __init__(self, base_dir: str = BASE_DIR):
        """Initialize traceability logger"""
        self.base_dir = Path(base_dir)
        self.traces_dir = self.base_dir / ".betty-traces"
        self.evidence_dir = self.traces_dir / "evidence"

        # Create directories
        self.traces_dir.mkdir(exist_ok=True)
        self.evidence_dir.mkdir(exist_ok=True)

        # Load Betty version
        try:
            from betty.config import VERSION
            self.betty_version = VERSION
        except:
            self.betty_version = "1.0.0"

    def generate_trace_id(self, component_id: str) -> str:
        """Generate unique trace ID"""
        date_str = datetime.utcnow().strftime("%Y%m%d")
        return f"trace-{date_str}-{component_id}"

    def compute_file_hash(self, file_path: str) -> str:
        """Compute SHA-256 hash of file"""
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            return f"sha256:{file_hash}"
        except Exception as e:
            logger.warning(f"Could not hash file {file_path}: {e}")
            return "sha256:unknown"

    def log_creation(
        self,
        component_id: str,
        component_name: str,
        component_type: str,
        component_version: str,
        component_file_path: str,
        input_source_path: str,
        created_by_tool: str,
        created_by_version: str,
        requirement: RequirementInfo,
        user: Optional[str] = None,
        tags: Optional[List[str]] = None,
        project: Optional[str] = None,
        team: Optional[str] = None
    ) -> str:
        """
        Log component creation with requirement linkage.

        Args:
            component_id: Component identifier (e.g., "code.reviewer")
            component_name: Human-readable name
            component_type: Type (agent, skill, hook, artifact-type)
            component_version: Semantic version
            component_file_path: Path to component definition file
            input_source_path: Path to input description file
            created_by_tool: Tool that created component (e.g., "meta.agent")
            created_by_version: Version of creation tool
            requirement: Requirement information
            user: User who initiated creation (optional)
            tags: Tags for categorization (optional)
            project: Project name (optional)
            team: Team name (optional)

        Returns:
            trace_id: Unique traceability record ID
        """
        try:
            trace_id = self.generate_trace_id(component_id)
            timestamp = datetime.utcnow().isoformat() + "Z"

            # Compute input file hash
            input_hash = self.compute_file_hash(input_source_path)

            # Get content preview
            try:
                with open(input_source_path, 'r') as f:
                    content = f.read(200)
                    content_preview = content if len(content) < 200 else content + "..."
            except:
                content_preview = None

            # Build traceability record
            trace_record = {
                "trace_id": trace_id,
                "component": {
                    "id": component_id,
                    "name": component_name,
                    "type": component_type,
                    "version": component_version,
                    "file_path": component_file_path
                },
                "creation": {
                    "timestamp": timestamp,
                    "created_by": {
                        "tool": created_by_tool,
                        "version": created_by_version
                    },
                    "input_source": {
                        "path": input_source_path,
                        "hash": input_hash
                    },
                    "betty_version": self.betty_version
                },
                "requirement": asdict(requirement),
                "verification": {
                    "status": "pending",
                    "checks": [],
                    "summary": {
                        "total_checks": 0,
                        "passed": 0,
                        "failed": 0,
                        "warnings": 0
                    }
                },
                "metadata": {}
            }

            # Add optional fields
            if user:
                trace_record["creation"]["created_by"]["user"] = user

            if content_preview:
                trace_record["creation"]["input_source"]["content_preview"] = content_preview

            if tags:
                trace_record["metadata"]["tags"] = tags

            if project:
                trace_record["metadata"]["project"] = project

            if team:
                trace_record["metadata"]["team"] = team

            # Save trace record
            trace_file = self.traces_dir / f"{trace_id}.json"
            with open(trace_file, 'w') as f:
                json.dump(trace_record, f, indent=2)

            logger.info(f"Created traceability record: {trace_id}")
            return trace_id

        except Exception as e:
            logger.error(f"Failed to log creation: {e}", exc_info=True)
            raise

    def log_verification(
        self,
        component_id: str,
        check_type: str,
        tool: str,
        result: str,
        details: Optional[Dict[str, Any]] = None,
        evidence_data: Optional[str] = None
    ) -> bool:
        """
        Log verification check result.

        Args:
            component_id: Component identifier
            check_type: Type of check (validation, compatibility, integration_test, etc.)
            tool: Tool that performed check
            result: Result (passed, failed, warning, skipped)
            details: Check-specific details (optional)
            evidence_data: Detailed logs/results to save (optional)

        Returns:
            Success status
        """
        try:
            # Find trace record
            trace_id = self.find_trace_id(component_id)
            if not trace_id:
                logger.warning(f"No trace record found for {component_id}")
                return False

            trace_file = self.traces_dir / f"{trace_id}.json"

            # Load existing record
            with open(trace_file, 'r') as f:
                trace_record = json.load(f)

            # Create verification check
            timestamp = datetime.utcnow().isoformat() + "Z"
            check = {
                "timestamp": timestamp,
                "check_type": check_type,
                "tool": tool,
                "result": result
            }

            if details:
                check["details"] = details

            # Save evidence if provided
            if evidence_data:
                evidence_file = f"{trace_id}-{check_type}-{timestamp}.log"
                evidence_path = self.evidence_dir / evidence_file
                with open(evidence_path, 'w') as f:
                    f.write(evidence_data)
                check["evidence"] = str(evidence_path)

            # Add check to record
            trace_record["verification"]["checks"].append(check)

            # Update summary
            checks = trace_record["verification"]["checks"]
            summary = {
                "total_checks": len(checks),
                "passed": len([c for c in checks if c["result"] == "passed"]),
                "failed": len([c for c in checks if c["result"] == "failed"]),
                "warnings": len([c for c in checks if c["result"] == "warning"]),
                "last_verified": timestamp
            }
            trace_record["verification"]["summary"] = summary

            # Update overall status
            if summary["failed"] > 0:
                trace_record["verification"]["status"] = "failed"
            elif summary["passed"] == summary["total_checks"]:
                trace_record["verification"]["status"] = "passed"
            else:
                trace_record["verification"]["status"] = "partial"

            # Save updated record
            with open(trace_file, 'w') as f:
                json.dump(trace_record, f, indent=2)

            logger.info(f"Logged verification check for {component_id}: {check_type} = {result}")
            return True

        except Exception as e:
            logger.error(f"Failed to log verification: {e}", exc_info=True)
            return False

    def find_trace_id(self, component_id: str) -> Optional[str]:
        """Find trace ID for component"""
        # Search for most recent trace file
        pattern = f"trace-*-{component_id}.json"
        trace_files = sorted(self.traces_dir.glob(pattern), reverse=True)

        if trace_files:
            trace_file = trace_files[0]
            return trace_file.stem

        return None

    def get_trace(self, component_id: str) -> Optional[Dict[str, Any]]:
        """Get traceability record for component"""
        trace_id = self.find_trace_id(component_id)
        if not trace_id:
            return None

        trace_file = self.traces_dir / f"{trace_id}.json"
        try:
            with open(trace_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to read trace: {e}")
            return None

    def list_all_traces(self) -> List[Dict[str, Any]]:
        """List all traceability records"""
        traces = []
        for trace_file in self.traces_dir.glob("trace-*.json"):
            try:
                with open(trace_file, 'r') as f:
                    traces.append(json.load(f))
            except Exception as e:
                logger.warning(f"Failed to read {trace_file}: {e}")

        return sorted(traces, key=lambda t: t["creation"]["timestamp"], reverse=True)

    def search_by_requirement(self, requirement_id: str) -> List[Dict[str, Any]]:
        """Find all components for a requirement"""
        all_traces = self.list_all_traces()
        return [t for t in all_traces if t["requirement"]["id"] == requirement_id]

    def export_for_database(self, output_file: str):
        """
        Export all traces as JSON array for bulk loading into document database.

        Args:
            output_file: Path to output JSON file
        """
        all_traces = self.list_all_traces()

        with open(output_file, 'w') as f:
            json.dump(all_traces, f, indent=2)

        logger.info(f"Exported {len(all_traces)} traces to {output_file}")
        return len(all_traces)


# Global instance
_tracer = None

def get_tracer() -> TraceabilityLogger:
    """Get global traceability logger instance"""
    global _tracer
    if _tracer is None:
        _tracer = TraceabilityLogger()
    return _tracer
