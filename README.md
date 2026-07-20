# Era of Arcane Agent Lab

Shared, versioned knowledge produced by Codex agents playing
[EraOfArcaneGame](https://github.com/Yifeeeeei/EraOfArcaneGame) through its
headless backend API.

This repository stores reproducible match summaries, deck experiments, compact
strategy knowledge, and bounded context packs. It deliberately does not store
the game implementation or routine raw WebSocket/server logs.

The initial import contains 13 numbered iteration matches. A pre-series sample
match (`2026-07-18-room-2342`) is retained separately under `legacy-evidence/`
because several early promoted rules cite it; it is not counted in the 13-match
series ledger.

## Start here

Agents must read, in order:

1. `AGENTS.md`
2. `context-packs/bootstrap.md`
3. `context-packs/next-match.md`
4. only the relevant deck or match files

Do not read every historical match before playing. Use `ledger/matches.csv` as
the retrieval index and open cold evidence only when a relevant row points to
it.

## Repository relationship

Recommended sibling checkout:

```text
Workspace/
  EraOfArcaneGame/
  EraOfArcaneAgentLab/
```

From `EraOfArcaneGame/server`:

```bash
go run ./cmd/agent-player init-data \
  -root ../../EraOfArcaneAgentLab/local
```

The tracked shared knowledge is read from this repository. Runtime transcripts
go under ignored `local/` or `raw/`; after a match, promote only the compact,
reviewable artifacts described in `AGENTS.md`.

## Validation

```bash
python3 scripts/validate_repo.py
python3 scripts/build_ledger.py --check
python3 scripts/build_context_pack.py --check
```
