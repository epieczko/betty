#!/usr/bin/env python3
"""
Simple HTTP server for Betty Marketplace

Serves the .claude-plugin/marketplace.json file and marketplace/* catalogs
for Claude Code plugin marketplace integration.

Usage:
    python serve_marketplace.py
    python serve_marketplace.py --port 8080
    python serve_marketplace.py --host 0.0.0.0 --port 9090
"""

import argparse
import http.server
import os
import socketserver
from pathlib import Path


class MarketplaceHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom HTTP request handler for serving Betty marketplace files.

    Serves:
    - /.claude-plugin/marketplace.json - Claude Code marketplace format
    - /marketplace/*.json - Betty catalog files (skills, agents, commands, hooks)
    - / - Root redirects to marketplace.json
    """

    def __init__(self, *args, **kwargs):
        # Set the base directory to the Betty repository root
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)

    def end_headers(self):
        # Add CORS headers to allow cross-origin requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        """Handle GET requests."""
        # Redirect root to marketplace.json
        if self.path == '/':
            self.path = '/.claude-plugin/marketplace.json'

        return super().do_GET()

    def do_OPTIONS(self):
        """Handle OPTIONS requests for CORS preflight."""
        self.send_response(200)
        self.end_headers()


def main():
    """Start the marketplace HTTP server."""
    parser = argparse.ArgumentParser(
        description='Serve Betty Marketplace files via HTTP'
    )
    parser.add_argument(
        '--host',
        default='0.0.0.0',
        help='Host to bind to (default: 0.0.0.0)'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8080,
        help='Port to listen on (default: 8080)'
    )

    args = parser.parse_args()

    # Ensure marketplace files exist
    base_dir = Path(__file__).parent
    marketplace_file = base_dir / '.claude-plugin' / 'marketplace.json'

    if not marketplace_file.exists():
        print(f"⚠️  Warning: {marketplace_file} not found")
        print("   Run: python skills/generate.marketplace/generate_marketplace.py")
        print()

    print("=" * 60)
    print("  Betty Marketplace HTTP Server")
    print("=" * 60)
    print(f"  Host: {args.host}")
    print(f"  Port: {args.port}")
    print(f"  Base: {base_dir}")
    print()
    print("  Endpoints:")
    print(f"    http://{args.host}:{args.port}/.claude-plugin/marketplace.json")
    print(f"    http://{args.host}:{args.port}/marketplace/skills.json")
    print(f"    http://{args.host}:{args.port}/marketplace/agents.json")
    print(f"    http://{args.host}:{args.port}/marketplace/commands.json")
    print(f"    http://{args.host}:{args.port}/marketplace/hooks.json")
    print()
    print("  Press Ctrl+C to stop")
    print("=" * 60)
    print()

    # Start server
    with socketserver.TCPServer((args.host, args.port), MarketplaceHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped")


if __name__ == '__main__':
    main()
