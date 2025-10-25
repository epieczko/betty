#!/usr/bin/env python3
"""
Tests for Hello World Skill.

This test suite demonstrates best practices for testing Betty Framework skills:
- Unit tests for core functionality
- Input validation tests
- Error handling tests
- Output verification tests
"""

import pytest
import json
from pathlib import Path
from hello_world import HelloWorld


class TestHelloWorld:
    """Test suite for Hello World skill."""

    @pytest.fixture
    def skill(self, tmp_path):
        """Create a HelloWorld skill instance with temporary output directory."""
        return HelloWorld(base_dir=tmp_path)

    @pytest.fixture
    def output_dir(self, tmp_path):
        """Get the output directory for the skill."""
        return tmp_path / "output" / "hello.world"

    def test_casual_greeting(self, skill):
        """Test casual greeting style."""
        result = skill.execute("Alice", "casual")

        assert result["ok"] is True
        assert result["status"] == "success"
        assert "Alice" in result["greeting"]
        assert "Hey Alice!" in result["greeting"]
        assert result["greeting_style"] == "casual"
        assert result["name"] == "Alice"

    def test_formal_greeting(self, skill):
        """Test formal greeting style."""
        result = skill.execute("Bob", "formal")

        assert result["ok"] is True
        assert result["status"] == "success"
        assert "Bob" in result["greeting"]
        assert "Good day, Bob" in result["greeting"]
        assert result["greeting_style"] == "formal"

    def test_enthusiastic_greeting(self, skill):
        """Test enthusiastic greeting style."""
        result = skill.execute("Charlie", "enthusiastic")

        assert result["ok"] is True
        assert result["status"] == "success"
        assert "Charlie" in result["greeting"]
        assert "🎉" in result["greeting"]
        assert result["greeting_style"] == "enthusiastic"

    def test_default_greeting_style(self, skill):
        """Test default greeting style (casual)."""
        result = skill.execute("Diana")

        assert result["ok"] is True
        assert result["greeting_style"] == "casual"
        assert "Hey Diana!" in result["greeting"]

    def test_output_file_created(self, skill, output_dir):
        """Test that output file is created with correct content."""
        result = skill.execute("Eve", "casual")

        assert result["ok"] is True

        output_file = Path(result["output_file"])
        assert output_file.exists()
        assert output_file.parent == output_dir

        content = output_file.read_text(encoding="utf-8")
        assert content == result["greeting"]
        assert "Eve" in content

    def test_empty_name_error(self, skill):
        """Test error handling for empty name."""
        result = skill.execute("", "casual")

        assert result["ok"] is False
        assert result["status"] == "error"
        assert "empty" in result["error"].lower()

    def test_whitespace_name_error(self, skill):
        """Test error handling for whitespace-only name."""
        result = skill.execute("   ", "casual")

        assert result["ok"] is False
        assert result["status"] == "error"
        assert "empty" in result["error"].lower()

    def test_invalid_greeting_style_error(self, skill):
        """Test error handling for invalid greeting style."""
        result = skill.execute("Frank", "invalid_style")

        assert result["ok"] is False
        assert result["status"] == "error"
        assert "invalid" in result["error"].lower()
        assert "greeting style" in result["error"].lower()

    def test_name_with_whitespace(self, skill):
        """Test that names with leading/trailing whitespace are trimmed."""
        result = skill.execute("  Grace  ", "casual")

        assert result["ok"] is True
        assert result["name"] == "Grace"
        assert "Grace" in result["greeting"]

    def test_multiple_executions(self, skill):
        """Test multiple executions with different inputs."""
        names = ["Alice", "Bob", "Charlie"]
        styles = ["casual", "formal", "enthusiastic"]

        for name, style in zip(names, styles):
            result = skill.execute(name, style)
            assert result["ok"] is True
            assert name in result["greeting"]
            assert result["greeting_style"] == style

    def test_output_file_overwrite(self, skill, output_dir):
        """Test that output file is overwritten on subsequent runs."""
        # First execution
        result1 = skill.execute("First", "casual")
        assert result1["ok"] is True
        output_file = Path(result1["output_file"])
        content1 = output_file.read_text()

        # Second execution
        result2 = skill.execute("Second", "formal")
        assert result2["ok"] is True
        content2 = output_file.read_text()

        # Verify file was overwritten
        assert content1 != content2
        assert "Second" in content2
        assert "First" not in content2

    def test_special_characters_in_name(self, skill):
        """Test handling of special characters in names."""
        special_names = [
            "Alice-Marie",
            "O'Brien",
            "José",
            "Smith, Jr."
        ]

        for name in special_names:
            result = skill.execute(name, "casual")
            assert result["ok"] is True
            assert name in result["greeting"]

    def test_result_structure(self, skill):
        """Test that result has the expected structure."""
        result = skill.execute("Test", "casual")

        assert "ok" in result
        assert "status" in result
        assert "greeting" in result
        assert "output_file" in result
        assert "greeting_style" in result
        assert "name" in result

        assert isinstance(result["ok"], bool)
        assert isinstance(result["status"], str)
        assert isinstance(result["greeting"], str)
        assert isinstance(result["output_file"], str)

    def test_error_result_structure(self, skill):
        """Test that error result has the expected structure."""
        result = skill.execute("", "casual")

        assert "ok" in result
        assert "status" in result
        assert "error" in result

        assert result["ok"] is False
        assert result["status"] == "error"
        assert isinstance(result["error"], str)


class TestHelloWorldCLI:
    """Test suite for CLI interface."""

    def test_cli_import(self):
        """Test that CLI module can be imported."""
        try:
            import hello_world
            assert hasattr(hello_world, 'main')
            assert hasattr(hello_world, 'HelloWorld')
        except ImportError:
            pytest.fail("Could not import hello_world module")

    def test_greeting_styles_constant(self):
        """Test that greeting styles are properly defined."""
        from hello_world import HelloWorld

        assert hasattr(HelloWorld, 'GREETING_STYLES')
        assert isinstance(HelloWorld.GREETING_STYLES, dict)
        assert "casual" in HelloWorld.GREETING_STYLES
        assert "formal" in HelloWorld.GREETING_STYLES
        assert "enthusiastic" in HelloWorld.GREETING_STYLES


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
