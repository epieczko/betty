#!/usr/bin/env python3
"""
Build Optimization Skill

Analyzes and optimizes build processes and speed across various build systems.

Supports:
- Webpack, Vite, Rollup, esbuild
- TypeScript compilation
- Node.js build processes
- General build optimization strategies
"""

import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
import re
import time

# Add betty module to path

from betty.logging_utils import setup_logger
from betty.errors import format_error_response, BettyError
from betty.telemetry_capture import telemetry_decorator

logger = setup_logger(__name__)


class BuildOptimizer:
    """Comprehensive build optimization analyzer and executor"""

    def __init__(self, project_path: str):
        """
        Initialize build optimizer

        Args:
            project_path: Path to project root directory
        """
        self.project_path = Path(project_path).resolve()

        if not self.project_path.exists():
            raise BettyError(f"Project path does not exist: {project_path}")

        if not self.project_path.is_dir():
            raise BettyError(f"Project path is not a directory: {project_path}")

        self.build_system = None
        self.package_json = None
        self.analysis_results = {}
        self.recommendations = []

    def analyze(self, args: str = "") -> Dict[str, Any]:
        """
        Comprehensive build analysis

        Args:
            args: Optional arguments for analysis

        Returns:
            Dict with analysis results and recommendations
        """
        logger.info(f"Starting build optimization analysis for {self.project_path}")

        results = {
            "project_path": str(self.project_path),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "build_system": None,
            "analysis": {},
            "recommendations": [],
            "estimated_improvement": "unknown"
        }

        try:
            # Step 1: Identify build system
            build_system_info = self._identify_build_system()
            results["build_system"] = build_system_info
            logger.info(f"Build system: {build_system_info['type']}")

            # Step 2: Analyze dependencies
            dep_analysis = self._analyze_dependencies()
            results["analysis"]["dependencies"] = dep_analysis

            # Step 3: Analyze caching
            cache_analysis = self._analyze_caching()
            results["analysis"]["caching"] = cache_analysis

            # Step 4: Analyze bundle configuration
            bundle_analysis = self._analyze_bundling()
            results["analysis"]["bundling"] = bundle_analysis

            # Step 5: Analyze TypeScript configuration
            ts_analysis = self._analyze_typescript()
            results["analysis"]["typescript"] = ts_analysis

            # Step 6: Analyze parallelization
            parallel_analysis = self._analyze_parallelization()
            results["analysis"]["parallelization"] = parallel_analysis

            # Generate recommendations based on analysis
            recommendations = self._generate_recommendations(results["analysis"])
            results["recommendations"] = recommendations

            # Estimate potential improvement
            results["estimated_improvement"] = self._estimate_improvement(
                results["analysis"], recommendations
            )

            logger.info(f"Analysis complete. Found {len(recommendations)} optimization opportunities")

            return results

        except Exception as e:
            logger.error(f"Analysis failed: {e}")
            raise BettyError(f"Build analysis failed: {e}")

    def _identify_build_system(self) -> Dict[str, Any]:
        """
        Step 1: Identify the build system in use
        """
        logger.info("Identifying build system...")

        package_json_path = self.project_path / "package.json"

        if not package_json_path.exists():
            return {
                "type": "unknown",
                "detected": False,
                "message": "No package.json found"
            }

        # Load package.json
        with open(package_json_path, 'r') as f:
            self.package_json = json.load(f)

        build_system = {"type": "unknown", "detected": True, "configs": []}

        # Check for build tools in dependencies and config files
        deps = {
            **self.package_json.get("dependencies", {}),
            **self.package_json.get("devDependencies", {})
        }

        # Check for Vite
        if "vite" in deps or (self.project_path / "vite.config.js").exists() or \
           (self.project_path / "vite.config.ts").exists():
            build_system["type"] = "vite"
            build_system["configs"].append("vite.config.js/ts")

        # Check for Webpack
        elif "webpack" in deps or (self.project_path / "webpack.config.js").exists():
            build_system["type"] = "webpack"
            build_system["configs"].append("webpack.config.js")

        # Check for Rollup
        elif "rollup" in deps or (self.project_path / "rollup.config.js").exists():
            build_system["type"] = "rollup"
            build_system["configs"].append("rollup.config.js")

        # Check for esbuild
        elif "esbuild" in deps:
            build_system["type"] = "esbuild"

        # Check for TypeScript
        elif "typescript" in deps or (self.project_path / "tsconfig.json").exists():
            build_system["type"] = "typescript"
            build_system["configs"].append("tsconfig.json")

        else:
            build_system["type"] = "generic"

        # Check build scripts
        scripts = self.package_json.get("scripts", {})
        build_system["scripts"] = {
            "build": scripts.get("build"),
            "dev": scripts.get("dev"),
            "test": scripts.get("test")
        }

        return build_system

    def _analyze_dependencies(self) -> Dict[str, Any]:
        """
        Step 2: Analyze build dependencies and their impact
        """
        logger.info("Analyzing dependencies...")

        if not self.package_json:
            return {"analyzed": False, "message": "No package.json"}

        deps = self.package_json.get("dependencies", {})
        dev_deps = self.package_json.get("devDependencies", {})

        analysis = {
            "total_dependencies": len(deps),
            "total_dev_dependencies": len(dev_deps),
            "outdated": [],
            "unused": [],
            "large_dependencies": [],
            "recommendations": []
        }

        # Check for common heavy dependencies
        heavy_deps = ["moment", "lodash", "core-js"]
        for dep in heavy_deps:
            if dep in deps:
                analysis["large_dependencies"].append({
                    "name": dep,
                    "suggestion": f"Consider replacing {dep} with lighter alternative"
                })

        # Recommendations
        if "moment" in deps:
            analysis["recommendations"].append(
                "Replace 'moment' with 'date-fns' or 'dayjs' for smaller bundle size"
            )

        if "lodash" in deps:
            analysis["recommendations"].append(
                "Use 'lodash-es' with tree-shaking or import specific lodash functions"
            )

        return analysis

    def _analyze_caching(self) -> Dict[str, Any]:
        """
        Step 3: Analyze caching strategy
        """
        logger.info("Analyzing caching strategy...")

        analysis = {
            "cache_enabled": False,
            "cache_type": "none",
            "recommendations": []
        }

        # Check for cache directories
        cache_dirs = [
            ".cache",
            "node_modules/.cache",
            ".webpack-cache",
            ".vite"
        ]

        for cache_dir in cache_dirs:
            if (self.project_path / cache_dir).exists():
                analysis["cache_enabled"] = True
                analysis["cache_type"] = cache_dir
                break

        if not analysis["cache_enabled"]:
            analysis["recommendations"].append(
                "Enable persistent caching for faster incremental builds"
            )

        # Check for CI cache configuration
        if (self.project_path / ".github" / "workflows").exists():
            analysis["ci_cache"] = "github-actions"

        return analysis

    def _analyze_bundling(self) -> Dict[str, Any]:
        """
        Step 4: Analyze bundle configuration
        """
        logger.info("Analyzing bundling configuration...")

        analysis = {
            "code_splitting": "unknown",
            "tree_shaking": "unknown",
            "minification": "unknown",
            "recommendations": []
        }

        # Check for build output
        dist_dir = self.project_path / "dist"
        build_dir = self.project_path / "build"

        output_dir = dist_dir if dist_dir.exists() else build_dir

        if output_dir and output_dir.exists():
            js_files = list(output_dir.glob("**/*.js"))
            analysis["output_files"] = len(js_files)

            # Estimate if code splitting is used
            if len(js_files) > 3:
                analysis["code_splitting"] = "enabled"
            elif len(js_files) <= 1:
                analysis["code_splitting"] = "disabled"
                analysis["recommendations"].append(
                    "Enable code splitting to reduce initial bundle size"
                )

        return analysis

    def _analyze_typescript(self) -> Dict[str, Any]:
        """
        Step 5: Analyze TypeScript configuration
        """
        logger.info("Analyzing TypeScript configuration...")

        tsconfig_path = self.project_path / "tsconfig.json"

        if not tsconfig_path.exists():
            return {
                "enabled": False,
                "message": "No TypeScript configuration found"
            }

        with open(tsconfig_path, 'r') as f:
            # Remove comments from JSON (basic approach)
            content = f.read()
            content = re.sub(r'//.*?\n', '\n', content)
            content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
            tsconfig = json.loads(content)

        compiler_options = tsconfig.get("compilerOptions", {})

        analysis = {
            "enabled": True,
            "incremental": compiler_options.get("incremental", False),
            "skipLibCheck": compiler_options.get("skipLibCheck", False),
            "composite": compiler_options.get("composite", False),
            "recommendations": []
        }

        # Recommendations for faster compilation
        if not analysis["incremental"]:
            analysis["recommendations"].append(
                "Enable 'incremental: true' in tsconfig.json for faster rebuilds"
            )

        if not analysis["skipLibCheck"]:
            analysis["recommendations"].append(
                "Enable 'skipLibCheck: true' to skip type checking of declaration files"
            )

        return analysis

    def _analyze_parallelization(self) -> Dict[str, Any]:
        """
        Step 6: Analyze parallel processing opportunities
        """
        logger.info("Analyzing parallelization opportunities...")

        analysis = {
            "cpu_cores": self._get_cpu_count(),
            "parallel_build": "unknown",
            "recommendations": []
        }

        if self.build_system and self.build_system.get("type") == "webpack":
            analysis["recommendations"].append(
                "Consider using 'thread-loader' for parallel processing in Webpack"
            )

        if self.build_system and self.build_system.get("type") == "typescript":
            analysis["recommendations"].append(
                "Use 'ts-loader' with 'transpileOnly: true' or 'esbuild-loader' for faster TypeScript compilation"
            )

        return analysis

    def _generate_recommendations(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate prioritized recommendations based on analysis
        """
        recommendations = []

        # Collect all recommendations from analysis
        for section, data in analysis.items():
            if isinstance(data, dict) and "recommendations" in data:
                for rec in data["recommendations"]:
                    recommendations.append({
                        "category": section,
                        "priority": "medium",
                        "description": rec
                    })

        # Add high-priority recommendations
        if analysis.get("caching", {}).get("cache_enabled") == False:
            recommendations.insert(0, {
                "category": "caching",
                "priority": "high",
                "description": "Enable persistent caching for significant build speed improvements"
            })

        if analysis.get("typescript", {}).get("incremental") == False:
            recommendations.insert(0, {
                "category": "typescript",
                "priority": "high",
                "description": "Enable incremental TypeScript compilation"
            })

        return recommendations

    def _estimate_improvement(
        self,
        analysis: Dict[str, Any],
        recommendations: List[Dict[str, Any]]
    ) -> str:
        """
        Estimate potential build time improvement
        """
        high_priority = sum(1 for r in recommendations if r.get("priority") == "high")
        total = len(recommendations)

        if high_priority >= 3:
            return "40-60% faster (multiple high-impact optimizations)"
        elif high_priority >= 1:
            return "20-40% faster (some high-impact optimizations)"
        elif total >= 5:
            return "10-20% faster (many small optimizations)"
        elif total >= 1:
            return "5-10% faster (few optimizations available)"
        else:
            return "Already well optimized"

    def _get_cpu_count(self) -> int:
        """Get number of CPU cores"""
        try:
            import os
            return os.cpu_count() or 1
        except:
            return 1

    def apply_optimizations(self, recommendations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Apply recommended optimizations (interactive mode)

        Args:
            recommendations: List of recommendations to apply

        Returns:
            Results of optimization application
        """
        results = {
            "applied": [],
            "skipped": [],
            "failed": []
        }

        logger.info("Optimization application would happen here in full implementation")
        logger.info("This is a demonstration skill showing the structure")

        return results


@telemetry_decorator(skill_name="build.optimize")
def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Analyze and optimize build processes"
    )
    parser.add_argument(
        "project_path",
        nargs="?",
        default=".",
        help="Path to project root (default: current directory)"
    )
    parser.add_argument(
        "--format",
        choices=["json", "human"],
        default="human",
        help="Output format (default: human)"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply recommended optimizations (interactive)"
    )

    args = parser.parse_args()

    try:
        # Create optimizer
        optimizer = BuildOptimizer(args.project_path)

        # Run analysis
        results = optimizer.analyze()

        # Output results
        if args.format == "json":
            print(json.dumps(results, indent=2))
        else:
            # Human-readable output
            print(f"\n🔍 Build Optimization Analysis")
            print(f"=" * 60)
            print(f"Project: {results['project_path']}")
            print(f"Build System: {results['build_system']['type']}")
            print()

            # Dependencies
            if "dependencies" in results["analysis"]:
                dep = results["analysis"]["dependencies"]
                print(f"📦 Dependencies:")
                print(f"   Total: {dep.get('total_dependencies', 0)}")
                print(f"   Dev: {dep.get('total_dev_dependencies', 0)}")
                if dep.get("large_dependencies"):
                    print(f"   Large deps: {len(dep['large_dependencies'])}")
                print()

            # Caching
            if "caching" in results["analysis"]:
                cache = results["analysis"]["caching"]
                print(f"💾 Caching:")
                print(f"   Enabled: {cache.get('cache_enabled', False)}")
                print(f"   Type: {cache.get('cache_type', 'none')}")
                print()

            # TypeScript
            if "typescript" in results["analysis"]:
                ts = results["analysis"]["typescript"]
                if ts.get("enabled"):
                    print(f"📘 TypeScript:")
                    print(f"   Incremental: {ts.get('incremental', False)}")
                    print(f"   Skip Lib Check: {ts.get('skipLibCheck', False)}")
                    print()

            # Recommendations
            if results["recommendations"]:
                print(f"💡 Recommendations ({len(results['recommendations'])}):")
                print()
                for i, rec in enumerate(results["recommendations"], 1):
                    priority_emoji = "🔴" if rec['priority'] == "high" else "🟡"
                    print(f"   {i}. {priority_emoji} {rec['description']}")
                    print(f"      Category: {rec['category']}")
                    print()

            print(f"⚡ Estimated Improvement: {results['estimated_improvement']}")
            print()

            if args.apply:
                print("Would you like to apply these optimizations?")
                print("(Interactive application not yet implemented)")

        sys.exit(0)

    except BettyError as e:
        print(format_error_response(str(e), "build.optimize"))
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        print(format_error_response(f"Unexpected error: {e}", "build.optimize"))
        sys.exit(1)


if __name__ == "__main__":
    main()
