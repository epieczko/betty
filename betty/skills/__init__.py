"""betty.skills namespace exposing packaged skill modules."""
from __future__ import annotations

import importlib.abc
import importlib.machinery
import importlib.util
import sys
from pathlib import Path
from typing import Iterable, Optional

_SKILLS_ROOT = Path(__file__).resolve().parents[2] / "skills"
_PREFIX = __name__ + "."
_PATH_MARKER = "betty_skills_prefix:"


def _iter_skill_dirs() -> Iterable[Path]:
    if not _SKILLS_ROOT.exists():
        return []
    return (p for p in _SKILLS_ROOT.iterdir() if p.is_dir())


def _has_matching_skill_dir(name: str) -> Optional[Path]:
    candidate = _SKILLS_ROOT / name
    if candidate.is_dir():
        return candidate
    return None


def _has_children_with_prefix(prefix: str) -> bool:
    target = f"{prefix}." if prefix else ""
    for path in _iter_skill_dirs():
        if prefix:
            if path.name.startswith(target):
                return True
        else:
            if "." in path.name:
                return True
    return False


class _SkillNamespaceLoader(importlib.abc.Loader):
    def __init__(self, fullname: str, prefix: str):
        self.fullname = fullname
        self.prefix = prefix

    def create_module(self, spec):  # type: ignore[override]
        return None  # use default module creation

    def exec_module(self, module):  # type: ignore[override]
        module.__path__ = [f"{_PATH_MARKER}{self.prefix}"]
        module.__package__ = module.__name__


class _SkillPackageFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname: str, path: Optional[Iterable[str]] = None, target=None):  # type: ignore[override]
        if not fullname.startswith(_PREFIX):
            return None

        suffix = fullname[len(_PREFIX):]
        if not suffix:
            return None

        prefix = ""
        if path:
            for entry in path:
                if entry.startswith(_PATH_MARKER):
                    prefix = entry[len(_PATH_MARKER):]
                    break

        candidate = suffix
        if prefix and not candidate.startswith(prefix):
            candidate = f"{prefix}.{suffix}"

        skill_dir = _has_matching_skill_dir(candidate)
        if skill_dir is not None:
            init_file = skill_dir / "__init__.py"
            if not init_file.exists():
                # fall back to namespace if the directory only contains resources
                return None
            loader = importlib.machinery.SourceFileLoader(fullname, str(init_file))
            spec = importlib.util.spec_from_file_location(
                fullname,
                str(init_file),
                loader=loader,
                submodule_search_locations=[str(skill_dir)],
            )
            return spec

        if _has_children_with_prefix(candidate):
            loader = _SkillNamespaceLoader(fullname, candidate)
            spec = importlib.machinery.ModuleSpec(fullname, loader, is_package=True)
            spec.submodule_search_locations = [f"{_PATH_MARKER}{candidate}"]
            return spec

        return None


def _register_finder():
    # Remove any previously-registered skill finders to avoid stale configuration
    sys.meta_path[:] = [f for f in sys.meta_path if not isinstance(f, _SkillPackageFinder)]
    sys.meta_path.insert(0, _SkillPackageFinder())


_register_finder()

# Mark this module as a package whose path is interpreted by the finder above.
__path__ = [f"{_PATH_MARKER}"]
