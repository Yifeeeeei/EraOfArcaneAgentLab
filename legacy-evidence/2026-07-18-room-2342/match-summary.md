# Match 2026-07-18-room-2342

- Room: 2342
- Tested commit: `4a67727c640719fde85fdc4a79126c0ad38791ed`
- Players: CodexA (player 0) vs CodexB (player 1)
- Decks: both `SAMPLE-ARCANE-001`
- Result: CodexB won, 6 life to 0
- End reason: hero killed
- Turns: 19
- Approximate duration: 65 minutes
- Key process: CodexB built a full board, repeatedly cleared CodexA's front row,
  reduced the hero from 6 to 1 across several turns, then used `屠魔者武士` for
  the final direct attack.

## Findings

- High-confidence bug: a dead `屠魔者杀手` returned by `回收小精灵` retained
  zero life, old position, and lethal-source status, and could be summoned at
  zero life.
- Card-text mismatch: `元素附魔` text lists `麻痹`, but its pending candidates
  list `眩晕`.
- Tooling: the protocol supported a full match, but compact decision
  observations would reduce context usage.

## Issues

- Zone-transition state reset:
  https://github.com/Yifeeeeei/EraOfArcaneGame/issues/106
- `元素附魔` terminology:
  https://github.com/Yifeeeeei/EraOfArcaneGame/issues/107
