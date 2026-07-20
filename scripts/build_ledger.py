#!/usr/bin/env python3
"""Build the Git-friendly match ledger from append-only match.json files."""

from __future__ import annotations

import argparse
import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "ledger" / "matches.csv"
FIELDS = [
    "match_id",
    "game_commit",
    "turns",
    "duration_seconds",
    "winner",
    "result_reason",
    "player_a_deck_id",
    "player_b_deck_id",
    "player_a_life",
    "player_b_life",
    "issues_found",
    "path",
]


def render() -> str:
    rows = []
    for path in sorted((ROOT / "matches").glob("**/match.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        rows.append(
            {
                "match_id": data["match_id"],
                "game_commit": data["game_commit"],
                "turns": data["turns"],
                "duration_seconds": data.get("duration_seconds"),
                "winner": data["winner"],
                "result_reason": data.get("result_reason", ""),
                "player_a_deck_id": data["players"]["player_a"].get("deck_id") or "",
                "player_b_deck_id": data["players"]["player_b"].get("deck_id") or "",
                "player_a_life": data.get("final_life", {}).get("player_a", ""),
                "player_b_life": data.get("final_life", {}).get("player_b", ""),
                "issues_found": " ".join(data.get("issues_found", [])),
                "path": str(path.parent.relative_to(ROOT)),
            }
        )
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != expected:
            print(f"{OUTPUT.relative_to(ROOT)} is stale; run scripts/build_ledger.py")
            return 1
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(expected, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
