#!/bin/bash
# Performance Analysis Script
# Analyzes Claude Code performance monitoring data

PERF_FILE="$HOME/.claude/performance.csv"

if [[ ! -f "$PERF_FILE" ]]; then
    echo "❌ Performance data not found: $PERF_FILE"
    echo "Run Claude Code with performance monitoring hooks enabled first."
    exit 1
fi

echo "📊 Claude Code Performance Analysis"
echo "===================================="
echo ""

# Total entries
TOTAL_ENTRIES=$(wc -l < "$PERF_FILE")
echo "Total log entries: $TOTAL_ENTRIES"
echo ""

# Tool usage breakdown
echo "Tool Usage Count:"
echo "-----------------"
cut -d',' -f4 "$PERF_FILE" | sort | uniq -c | sort -rn | head -n 10
echo ""

# Average CPU by tool
echo "Average CPU Usage by Tool:"
echo "--------------------------"
for tool in $(cut -d',' -f4 "$PERF_FILE" | sort -u | grep -v "tool_name"); do
    avg=$(grep ",$tool," "$PERF_FILE" | \
          awk -F',' '{sum+=$2; count++} END {if(count>0) printf "%.2f", sum/count; else print "0"}')
    if [[ -n "$avg" && "$avg" != "0" ]]; then
        printf "%-20s %s%%\n" "$tool:" "$avg"
    fi
done
echo ""

# Average Memory by tool
echo "Average Memory Usage by Tool (KB):"
echo "-----------------------------------"
for tool in $(cut -d',' -f4 "$PERF_FILE" | sort -u | grep -v "tool_name"); do
    avg=$(grep ",$tool," "$PERF_FILE" | \
          awk -F',' '{sum+=$3; count++} END {if(count>0) printf "%.0f", sum/count; else print "0"}')
    if [[ -n "$avg" && "$avg" != "0" ]]; then
        printf "%-20s %s KB\n" "$tool:" "$avg"
    fi
done
echo ""

# Peak CPU usage
echo "Peak CPU Usage:"
echo "---------------"
sort -t',' -k2 -nr "$PERF_FILE" | head -n 5 | \
    awk -F',' '{printf "%-15s %s%% at %s\n", $4, $2, $1}'
echo ""

# Peak Memory usage
echo "Peak Memory Usage:"
echo "------------------"
sort -t',' -k3 -nr "$PERF_FILE" | head -n 5 | \
    awk -F',' '{printf "%-15s %s KB at %s\n", $4, $3, $1}'
echo ""

# Recent activity (last 10 events)
echo "Recent Activity (last 10 events):"
echo "----------------------------------"
tail -n 10 "$PERF_FILE" | \
    awk -F',' '{printf "%-15s %-8s CPU: %s%% MEM: %s KB\n", $4, $5, $2, $3}'
echo ""

echo "✅ Analysis complete"
echo ""
echo "View full data: cat $PERF_FILE"
echo "Clear data: rm $PERF_FILE"
