#!/usr/bin/env python3
"""
notify_human.py - Implementation of the notify.human Skill

Sends notifications to human operators via console, logs, or configured channels.
For production, can be extended to send emails, Slack messages, PagerDuty alerts, etc.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
import uuid

# Betty imports
from betty.config import BASE_DIR
from betty.logging_utils import setup_logger

logger = setup_logger(__name__)


def get_notification_log_path() -> Path:
    """Get path to notification log file."""
    log_dir = Path(BASE_DIR) / "registry"
    log_dir.mkdir(exist_ok=True)
    return log_dir / "notifications.log"


def send_console_notification(summary: str, severity: str, suggested_action: str = None, metadata: dict = None):
    """
    Send notification to console with formatting.

    Args:
        summary: Notification summary
        severity: Severity level
        suggested_action: Optional suggested action
        metadata: Optional metadata
    """
    # Severity icons and colors (for terminal output)
    severity_map = {
        "info": "ℹ️  INFO",
        "warning": "⚠️  WARNING",
        "high": "🔴 HIGH",
        "critical": "🚨 CRITICAL"
    }

    severity_label = severity_map.get(severity, "📢 NOTICE")

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"{severity_label}: HUMAN NOTIFICATION", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    print(f"\n{summary}\n", file=sys.stderr)

    if suggested_action:
        print(f"Suggested Action: {suggested_action}\n", file=sys.stderr)

    if metadata:
        print(f"Additional Details:", file=sys.stderr)
        for key, value in metadata.items():
            print(f"  {key}: {value}", file=sys.stderr)

    print(f"{'='*60}\n", file=sys.stderr)


def log_notification(notification_id: str, summary: str, severity: str, channel: str,
                     suggested_action: str = None, metadata: dict = None) -> None:
    """
    Log notification to notification log file.

    Args:
        notification_id: Unique notification ID
        summary: Notification summary
        severity: Severity level
        channel: Notification channel
        suggested_action: Optional suggested action
        metadata: Optional metadata
    """
    log_path = get_notification_log_path()

    log_entry = {
        "notification_id": notification_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "summary": summary,
        "severity": severity,
        "channel": channel,
        "delivery_status": "sent"
    }

    if suggested_action:
        log_entry["suggested_action"] = suggested_action

    if metadata:
        log_entry["metadata"] = metadata

    try:
        with open(log_path, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
    except Exception as e:
        logger.error(f"Failed to write notification log: {e}")


def notify_human(
    summary: str,
    severity: str = "info",
    channel: str = "console",
    suggested_action: str = None,
    metadata: dict = None
) -> dict:
    """
    Send notification to human operator.

    Args:
        summary: Notification summary
        severity: Severity level (info, warning, high, critical)
        channel: Notification channel (console, email, slack, etc.)
        suggested_action: Suggested action for human
        metadata: Additional metadata

    Returns:
        Dict with notification_id and delivery_status
    """
    notification_id = str(uuid.uuid4())

    # Currently only console channel is implemented
    # Future: Add email, Slack, PagerDuty, etc.
    if channel == "console":
        send_console_notification(summary, severity, suggested_action, metadata)
    else:
        logger.warning(f"Channel '{channel}' not implemented, using console")
        send_console_notification(summary, severity, suggested_action, metadata)

    # Log notification
    log_notification(notification_id, summary, severity, channel, suggested_action, metadata)

    return {
        "notification_id": notification_id,
        "delivery_status": "sent",
        "channel": channel,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Send notifications to human operators"
    )
    parser.add_argument(
        'summary',
        help="Notification summary"
    )
    parser.add_argument(
        '--severity',
        default='info',
        choices=['info', 'warning', 'high', 'critical'],
        help="Severity level"
    )
    parser.add_argument(
        '--channel',
        default='console',
        help="Notification channel"
    )
    parser.add_argument(
        '--action',
        dest='suggested_action',
        help="Suggested action for the human"
    )
    parser.add_argument(
        '--metadata',
        help="Additional metadata as JSON string"
    )

    args = parser.parse_args()

    try:
        # Parse metadata if provided
        metadata = None
        if args.metadata:
            metadata = json.loads(args.metadata)

        # Send notification
        result = notify_human(
            summary=args.summary,
            severity=args.severity,
            channel=args.channel,
            suggested_action=args.suggested_action,
            metadata=metadata
        )

        # Output result as JSON
        print(json.dumps({
            "success": True,
            "notification_id": result["notification_id"],
            "delivery_status": result["delivery_status"],
            "channel": result["channel"],
            "timestamp": result["timestamp"]
        }, indent=2))

        sys.exit(0)

    except Exception as e:
        logger.error(f"Failed to send notification: {e}")
        error_result = {
            "success": False,
            "error": str(e),
            "message": f"Failed to send notification: {e}"
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
