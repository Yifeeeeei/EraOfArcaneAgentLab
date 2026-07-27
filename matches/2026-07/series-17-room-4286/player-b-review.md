# Player B Review — series-17 / room 4286

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Player/deck: B, `WIND-RUSH-005`
- Opponent: `FIRE-BURN-004`
- Result: B loss; player 0 won, game over on turn 10. B hero 0 life, A hero 5.
- Transcript: `player-b.jsonl`

## Summary

- B opened with a rapid Slayer and immediately attacked the fire hero from 6 to 5, but Fireball removed it before it generated further pressure.
- Lightning Strike, Lightning Chain, Lightning Golem, Bee Knight, Karina, Wind Horse, and Slayer Warrior were developed in sequence, but fire's repeated removal prevented B from maintaining a resource board.
- B generally declined to overexert the hero to preserve low-life units. On turn 10, with the hero at 1 life, B did overexert it to fund Lightning Chain and successfully defend a Burn aimed at the 1-life Bee Knight.
- A followed with Fireball, which B could not defend after resources were exhausted; the Bee Knight died. A then used a second Sketch Scroll to copy Fireball, selected the exposed B hero, and dealt lethal damage.

## Reusable lessons

- Wind rush needs at least one durable or redundant element source. A sequence of 1–3 life companions lets fire trade removal for the entire resource engine.
- Early direct pressure is real, but reducing the opposing hero by only 1 does not justify losing all board development; the rapid Slayer is strongest when follow-up threats can exploit the opened lane.
- Refusing hero overexertion to save disposable units was usually correct. The late Lightning Chain defense was also correct because it preserved the final blocker, but it left no answer to the next spell.
- Against a deck with Sketch Scroll, count each learned attack spell as potentially usable again even when horizontal. A final blocker is not safe merely because the visible Fireball and Burn have already been consumed.

## Bugs / suspicious behavior

- Normal `焚烧` targeting the enemy hero was rejected earlier with `spell cannot target hero`, but `速写卷轴` copying `焚烧` produced the exposed enemy hero as its only candidate and successfully dealt 2 damage to it. The copied-spell path appears to bypass or disagree with the normal spell target restriction.
- The same pattern occurred for the lethal copied `火球术`: after the final front-row unit died, Sketch Scroll offered the enemy hero and the copied Fireball killed it. This may be the same copied-spell targeting defect rather than a separate card-specific issue.
