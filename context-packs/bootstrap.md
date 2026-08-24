# Bootstrap Context

This repository contains shared play knowledge, not game implementation.

- Game repository: `https://github.com/Yifeeeeei/EraOfArcaneGame`
- Headless match protocol: `EraOfArcaneGame/docs/agent-player-protocol.md`
- Shared history: 29 official matches. The latest eight were played on game
  commit `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`.
- Current score: Player A 16 wins, Player B 11 wins, 2 adjudicated draws.

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

Series 25–26 started a new-deck exploration track. Earth shield versus Shadow
growth first produced a stable loop, then both lists added proactive attack
bridges and Shadow won on turn 10. Empty-deck stable loops are tracked in
EraOfArcaneGame Issue #146.

Series 27–29 added Earth 003, Light Grace 001/002, and Water-Shadow Grave
Clock. Series 27–28 are contaminated by Giant Sandworm Issue #147 and must not
be used as clean matchup results. Light 002 won the clean Series 29 on turn 28;
the Water-Shadow value engine dealt no physical hero damage. New defects are
tracked in Issues #148 and #149.
