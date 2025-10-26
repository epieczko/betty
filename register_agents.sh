#!/bin/bash
# Register all agents in the Betty Framework

export PYTHONPATH=/home/user/betty:$PYTHONPATH

agents=(
  "agents/code.reviewer/agent.yaml"
  "agents/data.architect/agent.yaml"
  "agents/data.validator/agent.yaml"
  "agents/deployment.engineer/agent.yaml"
  "agents/file.processor/agent.yaml"
  "agents/governance.manager/agent.yaml"
  "agents/meta.artifact/agent.yaml"
  "agents/meta.command/agent.yaml"
  "agents/meta.compatibility/agent.yaml"
  "agents/meta.create/agent.yaml"
  "agents/meta.hook/agent.yaml"
  "agents/meta.suggest/agent.yaml"
  "agents/security.architect/agent.yaml"
  "agents/strategy.architect/agent.yaml"
  "agents/test.engineer/agent.yaml"
)

echo "Registering ${#agents[@]} agents..."
echo ""

success=0
failed=0

for agent in "${agents[@]}"; do
  echo "Registering: $agent"
  if python3 skills/agent.define/agent_define.py "$agent" > /tmp/agent_reg.log 2>&1; then
    echo "  ✓ Success"
    ((success++))
  else
    echo "  ✗ Failed"
    cat /tmp/agent_reg.log | grep -i error | head -2
    ((failed++))
  fi
  echo ""
done

echo "================================"
echo "Registration complete:"
echo "  Success: $success"
echo "  Failed: $failed"
echo "================================"
