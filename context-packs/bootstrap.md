# Bootstrap Context

This repository contains shared play knowledge, not game implementation.

- Game repository: `https://github.com/Yifeeeeei/EraOfArcaneGame`
- Headless match protocol: `EraOfArcaneGame/docs/agent-player-protocol.md`
- Shared history: 24 official matches. The latest three were played on game
  commit `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`.
- Current score: Player A 15 wins, Player B 9 wins.

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

Series 22–24 established a current-main matchup baseline: Kran survival Fire
won all three games against Wind Rush variants. Wind improved when it restored
real rapid attackers, but repeated `烈焰反噬` burn still won the race. Read
`context-packs/next-match.md` for the bounded follow-up experiments.
