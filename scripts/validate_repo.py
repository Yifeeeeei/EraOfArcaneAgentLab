#!/usr/bin/env python3
"""Validate repository invariants without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r"^[0-9a-f]{40}$")
MATCH_REQUIRED = {
    "schema_version",
    "match_id",
    "game_repo",
    "game_commit",
    "protocol_version",
    "completed",
    "turns",
    "winner",
    "players",
    "key_process",
}
DECK_REQUIRED = {
    "schema_version",
    "deck_id",
    "game_repo",
    "game_commit",
    "deck_code",
    "plan",
    "evidence_matches",
}


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def main() -> int:
    errors: list[str] = []
    match_ids: set[str] = set()
    for path in sorted((ROOT / "matches").glob("**/match.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, path, f"invalid JSON: {exc}")
            continue
        missing = MATCH_REQUIRED - data.keys()
        if missing:
            fail(errors, path, f"missing fields: {sorted(missing)}")
            continue
        if data["schema_version"] != 1 or data["protocol_version"] < 1:
            fail(errors, path, "unsupported schema/protocol version")
        if not SHA.fullmatch(data["game_commit"]):
            fail(errors, path, "game_commit must be a 40-character SHA")
        if not data["completed"]:
            fail(errors, path, "only completed matches belong in shared history")
        if data["match_id"] in match_ids:
            fail(errors, path, "duplicate match_id")
        match_ids.add(data["match_id"])
        if path.parent.name != data["match_id"]:
            fail(errors, path, "directory name must equal match_id")
        for player in ("player_a", "player_b"):
            player_data = data["players"].get(player, {})
            deck_file = path.parent / player_data.get("deck_file", "")
            if not player_data.get("deck_file") or not deck_file.is_file():
                fail(errors, path, f"missing {player} deck file")
        if not (path.parent / "match-summary.md").is_file():
            fail(errors, path, "missing match-summary.md")

    for path in sorted((ROOT / "decks").glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, path, f"invalid JSON: {exc}")
            continue
        missing = DECK_REQUIRED - data.keys()
        if missing:
            fail(errors, path, f"missing fields: {sorted(missing)}")
            continue
        if data["schema_version"] != 1 or not SHA.fullmatch(data["game_commit"]):
            fail(errors, path, "invalid schema version or game_commit")
        unknown = set(data["evidence_matches"]) - match_ids
        if unknown:
            fail(errors, path, f"unknown evidence matches: {sorted(unknown)}")

    if len(match_ids) != 13:
        errors.append(f"expected 13 imported completed matches, found {len(match_ids)}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(match_ids)} matches and shared deck profiles.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
