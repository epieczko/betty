#!/usr/bin/env python3
"""
Performance benchmarks for artifact.validate.types

Tests validation performance with different numbers of artifact types
to verify <1s for 20 types and <100ms for single type claims.
"""

import json
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from artifact_validate_types import validate_artifact_types


def benchmark_validation(artifact_types: list, iterations: int = 5) -> dict:
    """Benchmark validation performance."""
    times = []

    for _ in range(iterations):
        start = time.perf_counter()
        result = validate_artifact_types(
            artifact_types=artifact_types,
            check_schemas=False,  # Skip filesystem checks for pure validation speed
            suggest_alternatives=True,
            max_suggestions=3,
            registry_path="registry/artifact_types.json"
        )
        end = time.perf_counter()
        times.append((end - start) * 1000)  # Convert to milliseconds

    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)

    return {
        'count': len(artifact_types),
        'iterations': iterations,
        'avg_ms': round(avg_time, 2),
        'min_ms': round(min_time, 2),
        'max_ms': round(max_time, 2),
        'times_ms': [round(t, 2) for t in times]
    }


def main():
    """Run performance benchmarks."""
    print("=== artifact.validate.types Performance Benchmarks ===\n")

    # Load actual artifact types from registry
    with open("registry/artifact_types.json") as f:
        registry = json.load(f)
        all_types = [a['name'] for a in registry['artifact_types']]

    print(f"Registry contains {len(all_types)} artifact types\n")

    # Benchmark different scenarios
    scenarios = [
        ("Single type", [all_types[0]]),
        ("5 types", all_types[:5]),
        ("10 types", all_types[:10]),
        ("20 types", all_types[:20]),
        ("50 types", all_types[:50]),
        ("100 types", all_types[:100]),
        ("All types (409)", all_types),
    ]

    results = []

    for name, types in scenarios:
        print(f"Benchmarking: {name} ({len(types)} types)")
        result = benchmark_validation(types, iterations=5)
        results.append({'name': name, **result})

        avg = result['avg_ms']
        status = "✅ " if avg < 1000 else "⚠️ "
        print(f"  {status}Average: {avg}ms (min: {result['min_ms']}ms, max: {result['max_ms']}ms)")
        print()

    # Print summary
    print("\n=== Summary ===\n")

    # Check claims
    single_result = results[0]
    twenty_result = results[3]

    print("Claim Verification:")
    if single_result['avg_ms'] < 100:
        print(f"  ✅ Single type < 100ms: {single_result['avg_ms']}ms")
    else:
        print(f"  ❌ Single type < 100ms: {single_result['avg_ms']}ms (MISSED TARGET)")

    if twenty_result['avg_ms'] < 1000:
        print(f"  ✅ 20 types < 1s: {twenty_result['avg_ms']}ms")
    else:
        print(f"  ❌ 20 types < 1s: {twenty_result['avg_ms']}ms (MISSED TARGET)")

    all_result = results[-1]
    print(f"\nAll 409 types: {all_result['avg_ms']}ms")

    # Calculate throughput
    throughput = len(all_types) / (all_result['avg_ms'] / 1000)
    print(f"Throughput: {int(throughput)} types/second")

    # Save results
    output_path = "skills/artifact.validate.types/benchmark_results.json"
    with open(output_path, 'w') as f:
        json.dump({
            'benchmark_date': time.strftime('%Y-%m-%d %H:%M:%S'),
            'registry_size': len(all_types),
            'results': results,
            'claims_verified': {
                'single_type_under_100ms': single_result['avg_ms'] < 100,
                'twenty_types_under_1s': twenty_result['avg_ms'] < 1000
            }
        }, f, indent=2)

    print(f"\nResults saved to: {output_path}")


if __name__ == '__main__':
    main()
