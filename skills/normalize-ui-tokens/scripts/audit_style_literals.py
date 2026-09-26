#!/usr/bin/env python3
"""Inventory raw visual literals in frontend source files.

This deliberately favors a transparent, dependency-free first pass over parsing
every supported language. Review each reported value in context before migrating it.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys
from typing import Iterable


DEFAULT_EXTENSIONS = {
    ".css",
    ".html",
    ".htm",
    ".js",
    ".jsx",
    ".less",
    ".pcss",
    ".sass",
    ".scss",
    ".svelte",
    ".ts",
    ".tsx",
    ".vue",
}

IGNORED_DIRECTORIES = {
    ".git",
    ".next",
    ".nuxt",
    ".output",
    ".svelte-kit",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
    "vendor",
}

COLOR_RE = re.compile(
    r"#[0-9a-fA-F]{3,8}\b"
    r"|(?:rgba?|hsla?|oklch|oklab|lab|lch|color)\([^;\n{}]+\)",
    re.IGNORECASE,
)
LENGTH_RE = re.compile(
    r"(?<![\w.-])-?(?:\d+\.\d+|\d+)(?:px|rem|em|ch|ex|vw|vh|vmin|vmax)\b",
    re.IGNORECASE,
)
ARBITRARY_UTILITY_RE = re.compile(r"(?<=[\w:-])-\[[^\]\n]+\]")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inventory repeated color, length, and arbitrary utility literals."
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to scan")
    parser.add_argument(
        "--extensions",
        default=",".join(sorted(DEFAULT_EXTENSIONS)),
        help="Comma-separated extensions to include (default: common frontend sources)",
    )
    parser.add_argument("--top", type=int, default=60, help="Maximum rows per category")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def normalized_extensions(raw: str) -> set[str]:
    result = set()
    for item in raw.split(","):
        item = item.strip().lower()
        if item:
            result.add(item if item.startswith(".") else f".{item}")
    return result


def is_ignored(path: Path) -> bool:
    parts = path.parts
    return any(part in IGNORED_DIRECTORIES for part in parts)


def iter_files(paths: Iterable[Path], extensions: set[str]) -> Iterable[Path]:
    seen: set[Path] = set()
    for candidate in paths:
        if not candidate.exists():
            print(f"warning: path does not exist: {candidate}", file=sys.stderr)
            continue
        files = [candidate] if candidate.is_file() else candidate.rglob("*")
        for path in files:
            if (
                path.is_file()
                and not path.is_symlink()
                and path.suffix.lower() in extensions
                and not is_ignored(path)
            ):
                resolved = path.resolve()
                if resolved not in seen:
                    seen.add(resolved)
                    yield path


def collect(
    files: Iterable[Path],
) -> tuple[dict[str, Counter[str]], dict[str, dict[str, list[str]]], int]:
    counts: dict[str, Counter[str]] = {
        "colors": Counter(),
        "lengths": Counter(),
        "arbitrary_utilities": Counter(),
    }
    examples: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    scanned = 0

    for path in files:
        scanned += 1
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError as exc:
            print(f"warning: could not read {path}: {exc}", file=sys.stderr)
            continue

        for line_number, line in enumerate(lines, start=1):
            matches = {
                "colors": COLOR_RE.findall(line),
                "lengths": LENGTH_RE.findall(line),
                "arbitrary_utilities": ARBITRARY_UTILITY_RE.findall(line),
            }
            for category, values in matches.items():
                for raw_value in values:
                    value = raw_value.strip()
                    counts[category][value] += 1
                    bucket = examples[category][value]
                    if len(bucket) < 3:
                        bucket.append(f"{path}:{line_number}")

    return counts, examples, scanned


def rows_for(
    category: str,
    counts: dict[str, Counter[str]],
    examples: dict[str, dict[str, list[str]]],
    top: int,
) -> list[dict[str, object]]:
    return [
        {"value": value, "count": count, "examples": examples[category][value]}
        for value, count in counts[category].most_common(max(top, 0))
    ]


def main() -> int:
    args = parse_args()
    extensions = normalized_extensions(args.extensions)
    counts, examples, scanned = collect(iter_files(args.paths, extensions))
    categories = {
        category: rows_for(category, counts, examples, args.top)
        for category in counts
    }

    if args.json:
        print(json.dumps({"files_scanned": scanned, "categories": categories}, indent=2))
        return 0

    print(f"Files scanned: {scanned}")
    for category, rows in categories.items():
        print(f"\n{category.replace('_', ' ').title()} ({len(counts[category])} unique)")
        if not rows:
            print("  none")
            continue
        for row in rows:
            locations = ", ".join(row["examples"])
            print(f"  {row['count']:>5}  {row['value']:<28}  {locations}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
