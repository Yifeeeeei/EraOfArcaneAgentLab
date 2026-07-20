# AGENTS.md

This repository is the shared memory for Codex agents that build decks and play
EraOfArcane. It is independent from the game code and changes more frequently.

## Required reading order

For a normal match, read only:

1. `context-packs/bootstrap.md`
2. `context-packs/next-match.md`
3. the two relevant files under `decks/`
4. at most 3–5 match summaries selected through `ledger/matches.csv`

Do not preload every review or historical match. Raw logs are cold evidence,
not normal context.

## Source-of-truth layers

- `matches/**/match.json`: append-only factual metadata for one completed match.
- `matches/**/match-summary.md`: concise account of the decisive sequence and
  experiment result.
- `matches/**/player-*-review.md`: player-specific evidence and reflection.
- `decks/*.json`: canonical reproducible deck versions and lineage.
- `knowledge/`: promoted, reusable conclusions supported by multiple matches.
- `context-packs/`: bounded entry points generated or curated for the next run.
- `ledger/matches.csv`: generated retrieval index; never edit it by hand.
- `legacy-evidence/`: pre-series evidence cited by knowledge but excluded from
  the numbered-series ledger.
- `raw/` and `local/`: ignored runtime data.

## Match lifecycle

1. Sync the game repository and record its exact commit.
2. Create a unique match ID and branch in this repository.
3. Validate both decks against the running game server.
4. Play to an official `game_over` unless the match is explicitly a regression
   friendly.
5. Add one match directory with `match.json`, summary, exact deck files, and
   independent reviews.
6. Update or add deck JSON only when the match tested that deck.
7. Treat new lessons as candidates. Promote them to `knowledge/` only after
   repeated evidence or a rules/code confirmation.
8. Run all validation commands before committing.

## Version boundaries

Every match and deck must record:

- game repository URL;
- exact game commit;
- protocol version;
- parent deck/version when applicable.

Never apply an old conclusion blindly after the game commit changes. Resolved
bugs and contradicted lessons move to `knowledge/retired-lessons.md`.

## Collaboration

Use one unique match directory per branch to avoid conflicts. Do not let two
agents concurrently rewrite the same knowledge file. Match-data PRs and
knowledge-promotion PRs should normally be separate.

Game bugs belong in the EraOfArcaneGame GitHub Issues. This repository stores
only the issue URL and the match evidence that discovered it.

## What not to commit

- full WebSocket transcripts for routine matches;
- server room JSONL logs;
- generated XLSX workbooks;
- secrets, tokens, or personal machine paths;
- conclusions based only on known broken behavior.
