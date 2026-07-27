# Open Questions and Active Defects

Read only the entries relevant to the current cards, deck hypothesis, or
matchup. Remove resolved entries after promoting the confirmed result to
`core-rules.md`, `gameplay-principles.md`, or `deck-lab.md`.

## 元素附魔 terminology

- Match: `2026-07-18-room-2342`
- Issue: https://github.com/Yifeeeeei/EraOfArcaneGame/issues/107
- Question: should the canonical status name be `麻痹` or `眩晕`?
- Recheck after: card data or runtime candidate terminology changes.

## 速写卷轴 copied-spell target validation

- Match: `series-17-room-4286`
- Issue: https://github.com/Yifeeeeei/EraOfArcaneGame/issues/124
- Confirmed: copied 焚烧/火球术 classified the hero as a unit and bypassed
  the normal hero-target restriction.
- Do not use the broken interaction as strategy; recheck after the issue is
  fixed.

## 速写卷轴 copied horizontal skill silently clears

- Match: `series-19-room-3718`
- Issue: https://github.com/Yifeeeeei/EraOfArcaneGame/issues/125
- Confirmed: after the scroll consumed the only resources, the copied spell's
  later payment failure was swallowed by a callback with no error channel; the
  pending action cleared without damage, defense, or feedback.
- The horizontal 雷击 was legal under “无需消耗”; insufficient remaining
  resources, not orientation, caused the silent failure.

## Empty-deck end condition

- Match: `series-18-room-0731`
- Observation: both decks reached zero without fatigue damage or automatic
  defeat, and the match continued to turn 26.
- Question: confirm whether this is the intended tabletop rule; if it is,
  headless orchestration needs a draw/loop policy for defensive stalemates.
