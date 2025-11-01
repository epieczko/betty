#!/usr/bin/env python3
"""
Human review workflow for risk.review skill

Flags low-confidence AI findings for manual review by security professionals.
"""

import json
import threading
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional
from enum import Enum


class ReviewStatus(Enum):
    """Review status for findings"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    NEEDS_INFO = "needs_more_info"


class ReviewPriority(Enum):
    """Priority for human review"""
    CRITICAL = "critical"  # Low confidence critical/high findings
    HIGH = "high"          # Low confidence medium findings or borderline scores
    MEDIUM = "medium"      # Medium confidence findings
    LOW = "low"            # High confidence but flagged for review


class HumanReviewQueue:
    """Manages queue of findings requiring human review"""

    def __init__(self, review_dir: Optional[Path] = None):
        """
        Initialize review queue

        Args:
            review_dir: Directory to store review queue (default: ~/.betty/review/risk_review)
        """
        self.review_dir = review_dir or Path.home() / '.betty' / 'review' / 'risk_review'
        self.review_dir.mkdir(parents=True, exist_ok=True)

        self.queue_file = self.review_dir / 'review_queue.json'
        self.lock = threading.Lock()

        # Load existing queue
        self.queue = self._load_queue()

    def _load_queue(self) -> List[Dict[str, Any]]:
        """Load review queue from disk"""
        if not self.queue_file.exists():
            return []

        try:
            with open(self.queue_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️  Failed to load review queue: {e}")
            return []

    def _save_queue(self):
        """Save review queue to disk"""
        try:
            with open(self.queue_file, 'w') as f:
                json.dump(self.queue, f, indent=2, default=str)
        except Exception as e:
            print(f"⚠️  Failed to save review queue: {e}")

    def add_for_review(
        self,
        finding: Dict[str, Any],
        artifact_path: str,
        reason: str,
        priority: ReviewPriority = ReviewPriority.MEDIUM,
        context: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Add finding to review queue

        Args:
            finding: The finding to review
            artifact_path: Path to artifact
            reason: Reason for review
            priority: Review priority
            context: Additional context

        Returns:
            Review ID
        """
        with self.lock:
            review_id = f"review_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.queue)}"

            review_item = {
                'review_id': review_id,
                'timestamp': datetime.now().isoformat(),
                'artifact_path': artifact_path,
                'finding': finding,
                'reason': reason,
                'priority': priority.value,
                'status': ReviewStatus.PENDING.value,
                'context': context or {},
                'reviewed_by': None,
                'reviewed_at': None,
                'review_notes': None
            }

            self.queue.append(review_item)
            self._save_queue()

            return review_id

    def mark_reviewed(
        self,
        review_id: str,
        status: ReviewStatus,
        reviewed_by: str,
        notes: Optional[str] = None
    ) -> bool:
        """
        Mark finding as reviewed

        Args:
            review_id: Review ID
            status: Review status
            reviewed_by: Reviewer name/email
            notes: Review notes

        Returns:
            True if successful
        """
        with self.lock:
            for item in self.queue:
                if item['review_id'] == review_id:
                    item['status'] = status.value
                    item['reviewed_by'] = reviewed_by
                    item['reviewed_at'] = datetime.now().isoformat()
                    item['review_notes'] = notes
                    self._save_queue()
                    return True

            return False

    def get_pending_reviews(
        self,
        priority: Optional[ReviewPriority] = None
    ) -> List[Dict[str, Any]]:
        """
        Get pending reviews

        Args:
            priority: Filter by priority (optional)

        Returns:
            List of pending review items
        """
        with self.lock:
            pending = [item for item in self.queue if item['status'] == ReviewStatus.PENDING.value]

            if priority:
                pending = [item for item in pending if item['priority'] == priority.value]

            # Sort by priority (critical first)
            priority_order = {
                ReviewPriority.CRITICAL.value: 0,
                ReviewPriority.HIGH.value: 1,
                ReviewPriority.MEDIUM.value: 2,
                ReviewPriority.LOW.value: 3
            }

            pending.sort(key=lambda x: priority_order.get(x['priority'], 999))

            return pending

    def get_review_summary(self) -> Dict[str, Any]:
        """Get summary of review queue"""
        with self.lock:
            total = len(self.queue)
            pending = sum(1 for item in self.queue if item['status'] == ReviewStatus.PENDING.value)
            approved = sum(1 for item in self.queue if item['status'] == ReviewStatus.APPROVED.value)
            rejected = sum(1 for item in self.queue if item['status'] == ReviewStatus.REJECTED.value)
            needs_info = sum(1 for item in self.queue if item['status'] == ReviewStatus.NEEDS_INFO.value)

            # Count by priority
            priority_counts = {
                'critical': sum(1 for item in self.queue if item['priority'] == ReviewPriority.CRITICAL.value and item['status'] == ReviewStatus.PENDING.value),
                'high': sum(1 for item in self.queue if item['priority'] == ReviewPriority.HIGH.value and item['status'] == ReviewStatus.PENDING.value),
                'medium': sum(1 for item in self.queue if item['priority'] == ReviewPriority.MEDIUM.value and item['status'] == ReviewStatus.PENDING.value),
                'low': sum(1 for item in self.queue if item['priority'] == ReviewPriority.LOW.value and item['status'] == ReviewStatus.PENDING.value)
            }

            return {
                'total_items': total,
                'pending': pending,
                'approved': approved,
                'rejected': rejected,
                'needs_info': needs_info,
                'pending_by_priority': priority_counts
            }

    def print_summary(self):
        """Print review queue summary"""
        summary = self.get_review_summary()

        print(f"\n{'='*80}")
        print(f"HUMAN REVIEW QUEUE SUMMARY")
        print(f"{'='*80}")
        print(f"Total Items:          {summary['total_items']}")
        print(f"Pending Review:       {summary['pending']}")
        print(f"  Critical Priority:  {summary['pending_by_priority']['critical']}")
        print(f"  High Priority:      {summary['pending_by_priority']['high']}")
        print(f"  Medium Priority:    {summary['pending_by_priority']['medium']}")
        print(f"  Low Priority:       {summary['pending_by_priority']['low']}")
        print(f"")
        print(f"Reviewed:             {summary['total_items'] - summary['pending']}")
        print(f"  Approved:           {summary['approved']}")
        print(f"  Rejected:           {summary['rejected']}")
        print(f"  Needs More Info:    {summary['needs_info']}")
        print(f"{'='*80}\n")

    def print_pending_reviews(self, limit: int = 10):
        """Print pending reviews"""
        pending = self.get_pending_reviews()

        print(f"\n{'='*80}")
        print(f"PENDING HUMAN REVIEWS (Showing {min(limit, len(pending))} of {len(pending)})")
        print(f"{'='*80}\n")

        for i, item in enumerate(pending[:limit], 1):
            finding = item['finding']
            priority_marker = {
                ReviewPriority.CRITICAL.value: "🔴",
                ReviewPriority.HIGH.value: "🟠",
                ReviewPriority.MEDIUM.value: "🟡",
                ReviewPriority.LOW.value: "🟢"
            }.get(item['priority'], "⚪")

            print(f"{priority_marker} Review #{i} - {item['review_id']}")
            print(f"   Priority: {item['priority'].upper()}")
            print(f"   Artifact: {item['artifact_path']}")
            print(f"   Timestamp: {item['timestamp']}")
            print(f"   Reason: {item['reason']}")
            print(f"")
            print(f"   Finding: [{finding.get('severity', 'unknown').upper()}] {finding.get('finding', 'N/A')}")
            if finding.get('confidence'):
                print(f"   Confidence: {finding['confidence']:.0%}")
            if finding.get('evidence'):
                evidence = finding['evidence'][:100] + ('...' if len(finding['evidence']) > 100 else '')
                print(f"   Evidence: {evidence}")
            print(f"   Impact: {finding.get('impact', 'N/A')}")
            print()

        if len(pending) > limit:
            print(f"... and {len(pending) - limit} more pending reviews")
            print(f"Use the review queue file for full list: {self.queue_file}")

        print(f"{'='*80}\n")

    def export_reviews(self, output_path: Path, status: Optional[ReviewStatus] = None):
        """
        Export review queue to file

        Args:
            output_path: Output file path
            status: Filter by status (optional)
        """
        with self.lock:
            reviews = self.queue

            if status:
                reviews = [item for item in reviews if item['status'] == status.value]

            with open(output_path, 'w') as f:
                json.dump(reviews, f, indent=2, default=str)

            print(f"✓ Exported {len(reviews)} review(s) to {output_path}")


def flag_findings_for_review(
    findings: List[Dict[str, Any]],
    artifact_path: str,
    risk_score: int,
    review_queue: HumanReviewQueue
) -> Dict[str, Any]:
    """
    Analyze findings and flag those requiring human review

    Args:
        findings: List of findings
        artifact_path: Path to artifact
        risk_score: Overall risk score
        review_queue: Review queue instance

    Returns:
        Summary of flagged findings
    """
    flagged_count = 0
    critical_flagged = 0
    high_flagged = 0

    for finding in findings:
        confidence = finding.get('confidence')
        severity = finding.get('severity', 'unknown')

        # Determine if finding needs review
        needs_review = False
        reason = None
        priority = ReviewPriority.MEDIUM

        # Low confidence findings
        if confidence and confidence < 0.7:
            needs_review = True
            reason = f"Low confidence score ({confidence:.0%})"

            # High severity + low confidence = critical priority
            if severity in ['critical', 'high']:
                priority = ReviewPriority.CRITICAL
                critical_flagged += 1
            else:
                priority = ReviewPriority.HIGH
                high_flagged += 1

        # Borderline confidence on critical findings
        elif confidence and 0.7 <= confidence < 0.8 and severity in ['critical', 'high']:
            needs_review = True
            reason = f"Borderline confidence ({confidence:.0%}) on {severity} severity finding"
            priority = ReviewPriority.HIGH
            high_flagged += 1

        # High risk score disagreement (if hybrid mode was used)
        elif severity in ['critical', 'high'] and confidence and confidence >= 0.9:
            # Optional: flag high-confidence critical findings for spot checks
            # Uncomment to enable:
            # needs_review = True
            # reason = f"High-confidence critical finding - recommended spot check"
            # priority = ReviewPriority.LOW
            pass

        if needs_review:
            review_queue.add_for_review(
                finding=finding,
                artifact_path=artifact_path,
                reason=reason,
                priority=priority,
                context={
                    'overall_risk_score': risk_score,
                    'flagged_at': datetime.now().isoformat()
                }
            )
            flagged_count += 1

    return {
        'total_flagged': flagged_count,
        'critical_priority': critical_flagged,
        'high_priority': high_flagged
    }


# Global review queue instance
_review_queue = None
_review_lock = threading.Lock()


def get_review_queue() -> HumanReviewQueue:
    """Get global review queue instance (singleton)"""
    global _review_queue
    with _review_lock:
        if _review_queue is None:
            _review_queue = HumanReviewQueue()
        return _review_queue
