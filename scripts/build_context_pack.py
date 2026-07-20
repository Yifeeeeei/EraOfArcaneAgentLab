#!/usr/bin/env python3
"""Build a bounded retrieval-oriented snapshot, not a full-history prompt."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "context-packs" / "latest.generated.md"
MAX_KNOWLEDGE_CHARS = 3500
MAX_SUMMARY_CHARS = 900
LATEST_MATCHES = 3


def clip(text: str, limit: int) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    clipped = text[:limit].rsplit("\n", 1)[0].rstrip()
    return clipped + "\n\n[truncated; retrieve the source file for more]"


def render() -> str:
    match_files = sorted((ROOT / "matches").glob("**/match.json"))
    recent = []
    for path in match_files[-LATEST_MATCHES:]:
        data = json.loads(path.read_text(encoding="utf-8"))
        summary_path = path.parent / "match-summary.md"
        summary = summary_path.read_text(encoding="utf-8") if summary_path.exists() else ""
        recent.append((data, path, summary))

    principles = (ROOT / "knowledge" / "gameplay-principles.md").read_text(
        encoding="utf-8"
    )
    core_rules = (ROOT / "knowledge" / "core-rules.md").read_text(encoding="utf-8")
    lines = [
        "# Latest Generated Context",
        "",
        "Generated from shared facts. Read specific reviews only when needed.",
        "",
        "## Stable knowledge",
        "",
        clip(core_rules + "\n\n" + principles, MAX_KNOWLEDGE_CHARS),
        "",
        "## Recent completed matches",
        "",
    ]
    for data, path, summary in recent:
        lines.extend(
            [
                f"### {data['match_id']}",
                "",
                f"- Game commit: `{data['game_commit']}`",
                f"- Result: `{data['winner']}`, turn {data['turns']}",
                f"- Evidence: `{path.parent.relative_to(ROOT)}`",
                "",
                clip(summary, MAX_SUMMARY_CHARS),
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != expected:
            print(
                f"{OUTPUT.relative_to(ROOT)} is stale; "
                "run scripts/build_context_pack.py"
            )
            return 1
        return 0
    OUTPUT.write_text(expected, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
