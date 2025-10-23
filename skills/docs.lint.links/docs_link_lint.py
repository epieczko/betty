#!/usr/bin/env python3
"""
docs_link_lint.py - Implementation of the docs.lint.links Skill.

Validates Markdown links to detect broken internal or external links.
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# Ensure project root on path for betty imports when executed directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from betty.errors import BettyError  # noqa: E402
from betty.logging_utils import setup_logger  # noqa: E402

logger = setup_logger(__name__)

# Regex patterns for finding links in markdown
# Matches [text](url) format
MARKDOWN_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
# Matches <url> format
ANGLE_LINK_PATTERN = re.compile(r'<(https?://[^>]+)>')
# Matches reference-style links [text][ref]
REFERENCE_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\[([^\]]*)\]')
# Matches reference definitions [ref]: url
REFERENCE_DEF_PATTERN = re.compile(r'^\[([^\]]+)\]:\s+(.+)$', re.MULTILINE)


class LinkIssue:
    """Represents a broken or problematic link."""

    def __init__(
        self,
        file: str,
        line: int,
        link: str,
        issue_type: str,
        message: str,
        suggested_fix: Optional[str] = None
    ):
        self.file = file
        self.line = line
        self.link = link
        self.issue_type = issue_type
        self.message = message
        self.suggested_fix = suggested_fix

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON output."""
        result = {
            "file": self.file,
            "line": self.line,
            "link": self.link,
            "issue_type": self.issue_type,
            "message": self.message
        }
        if self.suggested_fix:
            result["suggested_fix"] = self.suggested_fix
        return result


def find_markdown_files(root_dir: str, exclude_patterns: Optional[List[str]] = None) -> List[Path]:
    """
    Find all .md files in the directory tree.

    Args:
        root_dir: Root directory to search
        exclude_patterns: List of path patterns to exclude (e.g., 'node_modules', '.git')

    Returns:
        List of Path objects for markdown files
    """
    exclude_patterns = exclude_patterns or ['.git', 'node_modules', '.venv', 'venv', '__pycache__']
    md_files = []

    root_path = Path(root_dir).resolve()

    for path in root_path.rglob('*.md'):
        # Skip excluded directories
        if any(excluded in path.parts for excluded in exclude_patterns):
            continue
        md_files.append(path)

    logger.info(f"Found {len(md_files)} markdown files")
    return md_files


def is_in_code_block(line: str) -> bool:
    """
    Check if a line contains inline code that might contain false positive links.

    Args:
        line: Line to check

    Returns:
        True if we should skip this line for link extraction
    """
    # Count backticks - if odd number, we're likely inside inline code
    # This is a simple heuristic
    backtick_count = line.count('`')

    # If we have backticks, we need to be more careful
    # For simplicity, we'll extract the content outside of backticks
    return False  # We'll handle this differently


def extract_links_from_markdown(content: str) -> List[Tuple[int, str, str]]:
    """
    Extract all links from markdown content.

    Args:
        content: Markdown file content

    Returns:
        List of tuples: (line_number, link_text, link_url)
    """
    lines = content.split('\n')
    links = []

    # First, extract reference definitions
    references = {}
    for match in REFERENCE_DEF_PATTERN.finditer(content):
        ref_name = match.group(1).lower()
        ref_url = match.group(2).strip()
        references[ref_name] = ref_url

    # Track if we're in a code block
    in_code_block = False

    # Process each line
    for line_num, line in enumerate(lines, start=1):
        # Check for code block delimiters
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        # Skip lines inside code blocks
        if in_code_block:
            continue

        # Remove inline code blocks from the line before processing
        # This prevents false positives from code examples
        processed_line = re.sub(r'`[^`]+`', '', line)

        # Find standard markdown links [text](url)
        for match in MARKDOWN_LINK_PATTERN.finditer(processed_line):
            # Check if this match is actually in the original line
            # (not removed by our inline code filter)
            match_pos = processed_line.find(match.group(0))
            if match_pos >= 0:
                text = match.group(1)
                url = match.group(2)
                links.append((line_num, text, url))

        # Find angle bracket links <url>
        for match in ANGLE_LINK_PATTERN.finditer(processed_line):
            url = match.group(1)
            links.append((line_num, url, url))

        # Find reference-style links [text][ref] or [text][]
        for match in REFERENCE_LINK_PATTERN.finditer(processed_line):
            text = match.group(1)
            ref = match.group(2) if match.group(2) else text
            ref_lower = ref.lower()
            if ref_lower in references:
                url = references[ref_lower]
                links.append((line_num, text, url))

    return links


def is_external_link(url: str) -> bool:
    """Check if a URL is external (http/https)."""
    return url.startswith('http://') or url.startswith('https://')


def check_external_link(url: str, timeout: int = 10) -> Optional[str]:
    """
    Check if an external URL is accessible.

    Args:
        url: URL to check
        timeout: Timeout in seconds

    Returns:
        Error message if link is broken, None if OK
    """
    try:
        # Create request with a user agent to avoid 403s from some sites
        req = Request(
            url,
            headers={
                'User-Agent': 'Betty/1.0 (Link Checker)',
                'Accept': '*/*'
            }
        )

        with urlopen(req, timeout=timeout) as response:
            if response.status >= 400:
                return f"HTTP {response.status}"
            return None

    except HTTPError as e:
        return f"HTTP {e.code}"
    except URLError as e:
        return f"URL Error: {e.reason}"
    except Exception as e:
        return f"Error: {str(e)}"


def resolve_relative_path(md_file_path: Path, relative_url: str) -> Path:
    """
    Resolve a relative URL from a markdown file.

    Args:
        md_file_path: Path to the markdown file containing the link
        relative_url: Relative URL/path from the link

    Returns:
        Resolved absolute path
    """
    # Remove anchor/hash fragment
    url_without_anchor = relative_url.split('#')[0]

    if not url_without_anchor:
        # Just an anchor to current file
        return md_file_path

    # Resolve relative to the markdown file's directory
    base_dir = md_file_path.parent
    resolved = (base_dir / url_without_anchor).resolve()

    return resolved


def check_internal_link(
    md_file_path: Path,
    relative_url: str,
    root_dir: Path
) -> Tuple[Optional[str], Optional[str]]:
    """
    Check if an internal link is valid.

    Args:
        md_file_path: Path to the markdown file containing the link
        relative_url: Relative URL from the link
        root_dir: Repository root directory

    Returns:
        Tuple of (error_message, suggested_fix)
    """
    # Remove query string and anchor
    clean_url = relative_url.split('?')[0].split('#')[0]

    if not clean_url:
        # Just an anchor or query, assume valid
        return None, None

    resolved = resolve_relative_path(md_file_path, clean_url)

    # Check if file exists
    if resolved.exists():
        return None, None

    # File doesn't exist - try to suggest fixes
    error_msg = f"File not found: {relative_url}"
    suggested_fix = None

    # Try case-insensitive match
    if resolved.parent.exists():
        for file in resolved.parent.iterdir():
            if file.name.lower() == resolved.name.lower():
                relative_to_md = os.path.relpath(file, md_file_path.parent)
                suggested_fix = relative_to_md
                error_msg += f" (found case mismatch: {file.name})"
                break

    # Try without .md extension if it has one
    if not suggested_fix and clean_url.endswith('.md'):
        url_without_ext = clean_url[:-3]
        resolved_without_ext = resolve_relative_path(md_file_path, url_without_ext)
        if resolved_without_ext.exists():
            relative_to_md = os.path.relpath(resolved_without_ext, md_file_path.parent)
            suggested_fix = relative_to_md
            error_msg += f" (file exists without .md extension)"

    # Try adding .md extension if it doesn't have one
    if not suggested_fix and not clean_url.endswith('.md'):
        url_with_ext = clean_url + '.md'
        resolved_with_ext = resolve_relative_path(md_file_path, url_with_ext)
        if resolved_with_ext.exists():
            relative_to_md = os.path.relpath(resolved_with_ext, md_file_path.parent)
            suggested_fix = relative_to_md
            error_msg += f" (file exists with .md extension)"

    return error_msg, suggested_fix


def lint_markdown_file(
    md_file: Path,
    root_dir: Path,
    check_external: bool = True,
    external_timeout: int = 10
) -> List[LinkIssue]:
    """
    Lint a single markdown file for broken links.

    Args:
        md_file: Path to markdown file
        root_dir: Repository root directory
        check_external: Whether to check external links
        external_timeout: Timeout for external link checks

    Returns:
        List of LinkIssue objects
    """
    issues = []

    try:
        content = md_file.read_text(encoding='utf-8')
    except Exception as e:
        logger.warning(f"Could not read {md_file}: {e}")
        return issues

    links = extract_links_from_markdown(content)

    for line_num, link_text, url in links:
        # Skip empty URLs
        if not url or url.strip() == '':
            continue

        # Skip mailto and other special schemes
        if url.startswith('mailto:') or url.startswith('tel:'):
            continue

        relative_path = os.path.relpath(md_file, root_dir)

        if is_external_link(url):
            if check_external:
                logger.debug(f"Checking external link: {url}")
                error = check_external_link(url, timeout=external_timeout)
                if error:
                    issues.append(LinkIssue(
                        file=relative_path,
                        line=line_num,
                        link=url,
                        issue_type="external_broken",
                        message=f"External link is broken: {error}"
                    ))
        else:
            # Internal link
            logger.debug(f"Checking internal link: {url}")
            error, suggested_fix = check_internal_link(md_file, url, root_dir)
            if error:
                issues.append(LinkIssue(
                    file=relative_path,
                    line=line_num,
                    link=url,
                    issue_type="internal_broken",
                    message=error,
                    suggested_fix=suggested_fix
                ))

    return issues


def autofix_markdown_file(
    md_file: Path,
    root_dir: Path
) -> Tuple[int, List[str]]:
    """
    Automatically fix common link issues in a markdown file.

    Args:
        md_file: Path to markdown file
        root_dir: Repository root directory

    Returns:
        Tuple of (number_of_fixes, list_of_fix_descriptions)
    """
    try:
        content = md_file.read_text(encoding='utf-8')
    except Exception as e:
        logger.warning(f"Could not read {md_file}: {e}")
        return 0, []

    original_content = content
    links = extract_links_from_markdown(content)
    fixes = []
    fix_count = 0

    for line_num, link_text, url in links:
        if is_external_link(url):
            continue

        # Check if internal link is broken
        error, suggested_fix = check_internal_link(md_file, url, root_dir)

        if error and suggested_fix:
            # Apply the fix
            # Preserve any anchor/hash
            anchor = ''
            if '#' in url:
                anchor = '#' + url.split('#', 1)[1]

            new_url = suggested_fix + anchor

            # Replace in content
            content = content.replace(f']({url})', f']({new_url})')
            fix_count += 1
            fixes.append(f"Line {line_num}: {url} -> {new_url}")

    # Write back if changes were made
    if fix_count > 0:
        try:
            md_file.write_text(content, encoding='utf-8')
            logger.info(f"Applied {fix_count} fixes to {md_file}")
        except Exception as e:
            logger.error(f"Could not write fixes to {md_file}: {e}")
            return 0, []

    return fix_count, fixes


def lint_all_markdown(
    root_dir: str,
    check_external: bool = True,
    autofix: bool = False,
    external_timeout: int = 10,
    exclude_patterns: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Lint all markdown files in a directory.

    Args:
        root_dir: Root directory to search
        check_external: Whether to check external links (can be slow)
        autofix: Whether to automatically fix common issues
        external_timeout: Timeout for external link checks
        exclude_patterns: Patterns to exclude from search

    Returns:
        Result dictionary with issues and statistics
    """
    root_path = Path(root_dir).resolve()
    md_files = find_markdown_files(root_dir, exclude_patterns)

    all_issues = []
    all_fixes = []
    files_checked = 0
    files_with_issues = 0
    total_fixes = 0

    for md_file in md_files:
        files_checked += 1

        if autofix:
            fix_count, fixes = autofix_markdown_file(md_file, root_path)
            total_fixes += fix_count
            if fixes:
                relative_path = os.path.relpath(md_file, root_path)
                all_fixes.append({
                    "file": relative_path,
                    "fixes": fixes
                })

        # Check for issues (after autofix if enabled)
        issues = lint_markdown_file(
            md_file,
            root_path,
            check_external=check_external,
            external_timeout=external_timeout
        )

        if issues:
            files_with_issues += 1
            all_issues.extend(issues)

    result = {
        "status": "success",
        "summary": {
            "files_checked": files_checked,
            "files_with_issues": files_with_issues,
            "total_issues": len(all_issues),
            "autofix_enabled": autofix,
            "total_fixes_applied": total_fixes
        },
        "issues": [issue.to_dict() for issue in all_issues]
    }

    if autofix and all_fixes:
        result["fixes"] = all_fixes

    return result


def main(argv: Optional[List[str]] = None) -> int:
    """Entry point for CLI execution."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Lint Markdown files to detect broken internal or external links"
    )
    parser.add_argument(
        "root_dir",
        nargs='?',
        default='.',
        help="Root directory to search for Markdown files (default: current directory)"
    )
    parser.add_argument(
        "--no-external",
        action="store_true",
        help="Skip checking external links (faster)"
    )
    parser.add_argument(
        "--autofix",
        action="store_true",
        help="Automatically fix common issues (case, .md extension)"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="Timeout for external link checks in seconds (default: 10)"
    )
    parser.add_argument(
        "--exclude",
        type=str,
        help="Comma-separated list of patterns to exclude (e.g., 'node_modules,.git')"
    )
    parser.add_argument(
        "--output",
        type=str,
        choices=['json', 'text'],
        default='json',
        help="Output format (default: json)"
    )

    args = parser.parse_args(argv)

    exclude_patterns = None
    if args.exclude:
        exclude_patterns = [p.strip() for p in args.exclude.split(',')]

    try:
        result = lint_all_markdown(
            root_dir=args.root_dir,
            check_external=not args.no_external,
            autofix=args.autofix,
            external_timeout=args.timeout,
            exclude_patterns=exclude_patterns
        )

        if args.output == 'json':
            print(json.dumps(result, indent=2))
        else:
            # Text output
            summary = result['summary']
            print(f"Markdown Link Lint Results")
            print(f"=" * 50)
            print(f"Files checked: {summary['files_checked']}")
            print(f"Files with issues: {summary['files_with_issues']}")
            print(f"Total issues: {summary['total_issues']}")

            if summary['autofix_enabled']:
                print(f"Fixes applied: {summary['total_fixes_applied']}")

            if result['issues']:
                print(f"\nIssues found:")
                print(f"-" * 50)
                for issue in result['issues']:
                    print(f"\n{issue['file']}:{issue['line']}")
                    print(f"  Link: {issue['link']}")
                    print(f"  Issue: {issue['message']}")
                    if issue.get('suggested_fix'):
                        print(f"  Suggested fix: {issue['suggested_fix']}")
            else:
                print("\n✓ No issues found!")

        # Return non-zero if issues found
        return 1 if result['issues'] else 0

    except BettyError as e:
        logger.error(f"Linting failed: {e}")
        result = {
            "status": "error",
            "error": str(e)
        }
        print(json.dumps(result, indent=2))
        return 1
    except Exception as e:
        logger.exception("Unexpected error during linting")
        result = {
            "status": "error",
            "error": str(e)
        }
        print(json.dumps(result, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())
