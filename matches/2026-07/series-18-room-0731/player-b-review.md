# Player B Review — series-18 / room 0731

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Player/deck: B, `WIND-RUSH-005`
- Opponent: `WATER-PRESSURE-SCRY-001`
- Result: B win; player 1, game over on turn 26. B hero 2 life, A hero 0.
- Transcript: `player-b.jsonl`

## Summary

- B opened with a mulligan into cheap air units, then built Traveller, Bee Knight, Raven Messenger, Lightning Spirit, Karina, Lightning Strike, and Chain Lightning. An early Bee attack reduced the water hero from 6 to 5.
- Water repeatedly placed durable center-front blockers backed by Dolphin Companion. B needed several one-damage hits to remove each South Sea Kraken; Su's ultimate supplied the final hit after the dolphins had been exhausted.
- The midgame became a long resource-and-defense contest. Chain Lightning's extra target repeatedly damaged the water hero while its main target pressured the front row. Raven Messenger supplied cards until B's deck reached zero.
- Teleport Mage and Spatial Shift corrected formation mistakes and kept a front-row attacker available. Two rapid Slayers and two Bee Knights were eventually removed, leaving B with no direct attacker late in the game.
- Manes's Staff raised water's defense ceiling. B eventually combined Chain Lightning with Lightning Strike for 7 piercing power, cleared low-life front units, and reduced the water hero to 1 through the extra target.
- On turn 26, the same 7-power Chain Lightning plus Lightning Strike combination targeted Ice Spike Fortress and the water hero as the extra target. Water declined defense and the extra hit ended the game.

## Reusable lessons

- Wind should preserve a single center/front attacker and keep other resource units behind it. Filling the front row with non-attackers makes the final hero lane difficult to exploit.
- Chain Lightning's extra target is the deck's most reliable hero clock. It remains useful even when the main target survives or is protected.
- Against Dolphin Companion, count damage instances rather than total power. High power wins the defense comparison, but these wind spells usually deal only 1 damage per hit.
- Karina's piercing aura is strong but adds 1 air to every targeted air skill, including boost skills and defensive casts. Multi-skill combinations can become resource-constrained very quickly.
- A newly learned non-rapid skill is horizontal and cannot be cast that turn. B wasted a Mana Enhancer by learning Chain Lightning and then attempting to cast it immediately.
- Teleport Mage should be called with explicit `target_id`, `target_col`, and `target_row`. Omitting the target caused an unintended friendly move; the explicit form later moved the rapid Slayer correctly.
- Do not repeatedly overexert the hero merely to save expendable 1-life units. It removes the four-air engine from the following turn and can stall offense.

## Bugs / suspicious behavior

- Both players reached an empty deck without fatigue damage, automatic loss, or another deck-exhaustion result. The match continued to turn 26 and could plausibly have become a much longer defensive loop. This may be an intentional rule, but it is a significant termination risk for automated matches.
- No new confirmed card-text/implementation mismatch was observed from B's authoritative state.
