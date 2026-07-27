# Player B Review — series-19-room-3718

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Player: B / `WATER-PRESSURE-SCRY-001`
- Opponent: A / `WIND-RUSH-005`
- Result: B won on turn 12 (`winner: 1`), 4 life to 0.

## What worked

- The opening mulligan produced an aggressive line: rapid Slayer dealt the first hero damage, while Flying Fish, Water Cat, and Manes Staff established a large repeatable water engine.
- Manes Staff made Ice Burst and Ice Blade meaningfully difficult to defend. Two Ice Burst scrolls repeatedly froze the opposing hero and Bee, buying tempo and reducing defensive payment availability.
- Water Scry was best used proactively. It first found a South Sea Kraken, then later found the second Kraken that was placed center-front and became the actual finisher.
- The deck should not consume every attacker automatically. Preserving a vertical attacker when it has a valid lane matters more than one or two extra elements.
- The double-spell sequence was effective: force the opponent to spend hero overexertion and multiple skills on the first high-power spell, then use the second spell to remove the exposed unit.

## Mistakes and adjustments

- The first South Sea Kraken was placed right-front. With mirrored attack lanes, it could attack the opponent's left lane but could not attack the center hero. This delayed the win. Future finishers should normally be placed center-front unless a specific side-lane target is intended.
- Attempting `use_ability` on Water Scry was incorrect; sorcery skills use `cast_spell`.
- Attempting `play_item` was incorrect; equipment uses `equip`. A second weapon also could not replace the existing Manes Staff while the existing weapon was horizontal.
- Ice Blade correctly rejected a hero target. The deck needs board attackers, splash positioning, or an explicitly hero-legal effect to finish; it should not assume ordinary single-target spells can hit heroes.

## Suspicious behavior / bug evidence

- On A turn 9, Sketch Scroll copied Lightning Strike and selected South Sea Kraken `ci_55`, but the flow cleared its pending action without creating a defense window or resolving damage. `ci_55` remained at 4 life, and B's `no_defend` was rejected with `not in defense window`. A retry reported no pending action. The copied Lightning Strike may have been silently swallowed because the source Lightning Strike was horizontal. This deserves reproduction from the room transcript.

## Next-match guidance

- Keep at least one active attacker in the center lane; do not let Water become a pure defense/resource board.
- Prefer Water Scry candidates that immediately create pressure: rapid attackers first, then center-lane Kraken, then spell-power engines.
- Manes Staff plus two learned attack spells is a strong resource-exhaustion package, but the final life points still require a legal hero-damage route.
