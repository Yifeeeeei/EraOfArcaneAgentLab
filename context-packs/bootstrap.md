# Bootstrap Context

This repository contains shared play knowledge, not game implementation.

- Game repository: `https://github.com/Yifeeeeei/EraOfArcaneGame`
- Headless match protocol: `EraOfArcaneGame/docs/agent-player-protocol.md`
- Shared history: 21 official matches. The latest eight were played on game
  commit `261247af08dd681f738c8ea0ccb2f01cba5abfad`.
- Current score: Player A 12 wins, Player B 9 wins.

Read `knowledge/core-rules.md` and `knowledge/gameplay-principles.md`, then only
the deck profiles relevant to the next match. Use `ledger/matches.csv` to
retrieve specific evidence.

Known card-effect defects #106, #109, #110, #111, and #112 were fixed and
regression-tested on game commit
`2d9538bab48a2e8e2be384aa0f9ae63e0c4b8f1f`. Their broken behavior is not valid
strategy. Terminology issue #107 remains separate.

Issue #124 was discovered in `series-17-room-4286`: copied attack spells can
misclassify the hero as a unit target. Do not treat that broken path as legal
strategy.
