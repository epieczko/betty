#!/usr/bin/env python3
"""
Metrics and telemetry system for risk.review skill

Tracks usage, costs, performance, and error rates for continuous improvement.
"""

import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List
from collections import defaultdict
import threading


class MetricsCollector:
    """Thread-safe metrics collection and persistence"""

    def __init__(self, metrics_dir: Optional[Path] = None):
        """
        Initialize metrics collector

        Args:
            metrics_dir: Directory to store metrics (default: ~/.betty/metrics/risk_review)
        """
        self.metrics_dir = metrics_dir or Path.home() / '.betty' / 'metrics' / 'risk_review'
        self.metrics_dir.mkdir(parents=True, exist_ok=True)

        self.metrics_file = self.metrics_dir / 'metrics.json'
        self.session_file = self.metrics_dir / f'session_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'

        self.lock = threading.Lock()
        self.session_metrics = {
            'session_start': datetime.now().isoformat(),
            'assessments': [],
            'errors': [],
            'summary': {
                'total_assessments': 0,
                'total_cost': 0.0,
                'total_duration': 0.0,
                'mode_counts': defaultdict(int),
                'error_count': 0,
                'cache_hits': 0,
                'cache_misses': 0
            }
        }

        # Load historical metrics
        self.historical_metrics = self._load_historical_metrics()

    def _load_historical_metrics(self) -> Dict[str, Any]:
        """Load historical metrics from disk"""
        if not self.metrics_file.exists():
            return {
                'total_assessments': 0,
                'total_cost': 0.0,
                'total_duration': 0.0,
                'mode_usage': defaultdict(int),
                'error_rate': 0.0,
                'cache_stats': {
                    'hits': 0,
                    'misses': 0,
                    'hit_rate': 0.0
                },
                'cost_by_mode': defaultdict(float),
                'avg_duration_by_mode': defaultdict(float),
                'last_updated': None
            }

        try:
            with open(self.metrics_file, 'r') as f:
                data = json.load(f)
                # Convert defaultdicts
                data['mode_usage'] = defaultdict(int, data.get('mode_usage', {}))
                data['cost_by_mode'] = defaultdict(float, data.get('cost_by_mode', {}))
                data['avg_duration_by_mode'] = defaultdict(float, data.get('avg_duration_by_mode', {}))
                return data
        except Exception as e:
            print(f"⚠️  Failed to load historical metrics: {e}")
            return self._load_historical_metrics.__defaults__[0]

    def record_assessment(
        self,
        mode: str,
        duration: float,
        risk_score: int,
        findings_count: int,
        cost: float = 0.0,
        cache_hit: bool = False,
        error: Optional[str] = None
    ):
        """
        Record assessment metrics

        Args:
            mode: Assessment mode used
            duration: Assessment duration in seconds
            risk_score: Risk score (0-100)
            findings_count: Number of findings
            cost: API cost in USD
            cache_hit: Whether cache was used
            error: Error message if assessment failed
        """
        with self.lock:
            assessment_data = {
                'timestamp': datetime.now().isoformat(),
                'mode': mode,
                'duration': duration,
                'risk_score': risk_score,
                'findings_count': findings_count,
                'cost': cost,
                'cache_hit': cache_hit,
                'error': error
            }

            self.session_metrics['assessments'].append(assessment_data)

            # Update summary
            summary = self.session_metrics['summary']
            summary['total_assessments'] += 1
            summary['total_cost'] += cost
            summary['total_duration'] += duration
            summary['mode_counts'][mode] += 1

            if cache_hit:
                summary['cache_hits'] += 1
            else:
                summary['cache_misses'] += 1

            if error:
                summary['error_count'] += 1
                self.session_metrics['errors'].append({
                    'timestamp': datetime.now().isoformat(),
                    'mode': mode,
                    'error': error
                })

    def record_error(self, error_type: str, error_message: str, context: Dict[str, Any] = None):
        """
        Record error occurrence

        Args:
            error_type: Type of error (api_error, parse_error, etc.)
            error_message: Error message
            context: Additional context
        """
        with self.lock:
            self.session_metrics['errors'].append({
                'timestamp': datetime.now().isoformat(),
                'error_type': error_type,
                'message': error_message,
                'context': context or {}
            })
            self.session_metrics['summary']['error_count'] += 1

    def get_session_summary(self) -> Dict[str, Any]:
        """Get current session summary"""
        with self.lock:
            summary = self.session_metrics['summary'].copy()

            # Calculate cache hit rate
            total_cache_ops = summary['cache_hits'] + summary['cache_misses']
            summary['cache_hit_rate'] = (summary['cache_hits'] / total_cache_ops * 100) if total_cache_ops > 0 else 0.0

            # Calculate error rate
            summary['error_rate'] = (summary['error_count'] / max(summary['total_assessments'], 1)) * 100

            # Calculate average cost per assessment
            summary['avg_cost_per_assessment'] = summary['total_cost'] / max(summary['total_assessments'], 1)

            # Calculate average duration
            summary['avg_duration'] = summary['total_duration'] / max(summary['total_assessments'], 1)

            return summary

    def get_historical_summary(self) -> Dict[str, Any]:
        """Get historical metrics summary"""
        with self.lock:
            return self.historical_metrics.copy()

    def save_session(self):
        """Save current session metrics to disk"""
        with self.lock:
            try:
                # Save session file
                with open(self.session_file, 'w') as f:
                    json.dump(self.session_metrics, f, indent=2, default=str)

                # Update historical metrics
                self._update_historical_metrics()

            except Exception as e:
                print(f"⚠️  Failed to save metrics: {e}")

    def _update_historical_metrics(self):
        """Update historical metrics with current session"""
        summary = self.session_metrics['summary']

        # Update totals
        self.historical_metrics['total_assessments'] += summary['total_assessments']
        self.historical_metrics['total_cost'] += summary['total_cost']
        self.historical_metrics['total_duration'] += summary['total_duration']

        # Update mode usage
        for mode, count in summary['mode_counts'].items():
            self.historical_metrics['mode_usage'][mode] += count

        # Update cache stats
        cache_stats = self.historical_metrics['cache_stats']
        cache_stats['hits'] += summary['cache_hits']
        cache_stats['misses'] += summary['cache_misses']
        total_ops = cache_stats['hits'] + cache_stats['misses']
        cache_stats['hit_rate'] = (cache_stats['hits'] / total_ops * 100) if total_ops > 0 else 0.0

        # Update error rate
        total_errors = sum(1 for a in self.session_metrics['assessments'] if a.get('error'))
        self.historical_metrics['error_rate'] = (total_errors / max(self.historical_metrics['total_assessments'], 1)) * 100

        # Update cost by mode
        for assessment in self.session_metrics['assessments']:
            mode = assessment['mode']
            self.historical_metrics['cost_by_mode'][mode] += assessment['cost']

        # Update average duration by mode
        mode_durations = defaultdict(list)
        for assessment in self.session_metrics['assessments']:
            mode_durations[assessment['mode']].append(assessment['duration'])

        for mode, durations in mode_durations.items():
            self.historical_metrics['avg_duration_by_mode'][mode] = sum(durations) / len(durations)

        self.historical_metrics['last_updated'] = datetime.now().isoformat()

        # Save to disk
        try:
            with open(self.metrics_file, 'w') as f:
                json.dump(self.historical_metrics, f, indent=2, default=str)
        except Exception as e:
            print(f"⚠️  Failed to save historical metrics: {e}")

    def print_summary(self, show_historical: bool = False):
        """
        Print metrics summary

        Args:
            show_historical: Show historical metrics in addition to session
        """
        session = self.get_session_summary()

        print(f"\n{'='*80}")
        print(f"SESSION METRICS SUMMARY")
        print(f"{'='*80}")
        print(f"Total Assessments:        {session['total_assessments']}")
        print(f"Total Cost:               ${session['total_cost']:.4f}")
        print(f"Total Duration:           {session['total_duration']:.1f}s")
        print(f"Avg Cost/Assessment:      ${session['avg_cost_per_assessment']:.4f}")
        print(f"Avg Duration:             {session['avg_duration']:.1f}s")
        print(f"")
        print(f"Mode Usage:")
        for mode, count in session['mode_counts'].items():
            print(f"  {mode:10s}: {count:3d} ({count/max(session['total_assessments'], 1)*100:.0f}%)")
        print(f"")
        print(f"Cache Performance:")
        print(f"  Hits:      {session['cache_hits']}")
        print(f"  Misses:    {session['cache_misses']}")
        print(f"  Hit Rate:  {session['cache_hit_rate']:.1f}%")
        print(f"")
        print(f"Error Rate:               {session['error_rate']:.1f}%")
        print(f"{'='*80}\n")

        if show_historical:
            historical = self.get_historical_summary()
            print(f"\n{'='*80}")
            print(f"HISTORICAL METRICS (All Time)")
            print(f"{'='*80}")
            print(f"Total Assessments:        {historical['total_assessments']}")
            print(f"Total Cost:               ${historical['total_cost']:.2f}")
            print(f"Total Duration:           {historical['total_duration']/3600:.1f}h")
            print(f"")
            print(f"Mode Usage:")
            for mode, count in historical['mode_usage'].items():
                print(f"  {mode:10s}: {count:5d} ({count/max(historical['total_assessments'], 1)*100:.0f}%)")
            print(f"")
            print(f"Cost by Mode:")
            for mode, cost in historical['cost_by_mode'].items():
                print(f"  {mode:10s}: ${cost:.2f}")
            print(f"")
            print(f"Avg Duration by Mode:")
            for mode, duration in historical['avg_duration_by_mode'].items():
                print(f"  {mode:10s}: {duration:.1f}s")
            print(f"")
            print(f"Cache Stats:")
            print(f"  Hit Rate:  {historical['cache_stats']['hit_rate']:.1f}%")
            print(f"  Hits:      {historical['cache_stats']['hits']}")
            print(f"  Misses:    {historical['cache_stats']['misses']}")
            print(f"")
            print(f"Error Rate:               {historical['error_rate']:.2f}%")
            print(f"Last Updated:             {historical.get('last_updated', 'Never')}")
            print(f"{'='*80}\n")

    def export_metrics(self, output_path: Path, format: str = 'json'):
        """
        Export metrics to file

        Args:
            output_path: Output file path
            format: Export format (json or csv)
        """
        with self.lock:
            if format == 'json':
                with open(output_path, 'w') as f:
                    json.dump({
                        'session': self.session_metrics,
                        'historical': self.historical_metrics
                    }, f, indent=2, default=str)
                print(f"✓ Metrics exported to {output_path}")

            elif format == 'csv':
                import csv
                with open(output_path, 'w', newline='') as f:
                    if self.session_metrics['assessments']:
                        writer = csv.DictWriter(f, fieldnames=self.session_metrics['assessments'][0].keys())
                        writer.writeheader()
                        writer.writerows(self.session_metrics['assessments'])
                print(f"✓ Assessment data exported to {output_path}")


# Global metrics collector instance
_metrics_collector = None
_metrics_lock = threading.Lock()


def get_metrics_collector() -> MetricsCollector:
    """Get global metrics collector instance (singleton)"""
    global _metrics_collector
    with _metrics_lock:
        if _metrics_collector is None:
            _metrics_collector = MetricsCollector()
        return _metrics_collector


def record_assessment(*args, **kwargs):
    """Convenience function to record assessment"""
    get_metrics_collector().record_assessment(*args, **kwargs)


def record_error(*args, **kwargs):
    """Convenience function to record error"""
    get_metrics_collector().record_error(*args, **kwargs)


def save_metrics():
    """Convenience function to save metrics"""
    get_metrics_collector().save_session()


def print_metrics_summary(show_historical: bool = False):
    """Convenience function to print metrics summary"""
    get_metrics_collector().print_summary(show_historical=show_historical)
