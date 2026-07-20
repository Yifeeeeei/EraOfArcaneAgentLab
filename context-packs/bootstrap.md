# Bootstrap Context

This repository contains shared play knowledge, not game implementation.

- Game repository: `https://github.com/Yifeeeeei/EraOfArcaneGame`
- Headless match protocol: `EraOfArcaneGame/docs/agent-player-protocol.md`
- Historical import: 13 official matches from game commit
  `05be3b6074b2d83e8b1bb83fc3c20c204ad37d5d`
- Current imported score: Player A 8 wins, Player B 5 wins

Read `knowledge/core-rules.md` and `knowledge/gameplay-principles.md`, then only
the deck profiles relevant to the next match. Use `ledger/matches.csv` to
retrieve specific evidence.

Known card-effect defects #106, #109, #110, #111, and #112 were fixed and
regression-tested on game commit
`2d9538bab48a2e8e2be384aa0f9ae63e0c4b8f1f`. Their broken behavior is not valid
strategy. Terminology issue #107 remains separate.
