# Player A Review — series-21 / room 8085

- Tested commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Seat: player 0 / first player
- Deck: `WATER-PRESSURE-SCRY-001`
- Opponent: player 1, `FIRE-BURN-004`
- Result: win, turn 20, `hero_killed`
- Final visible hero life: Water 4, Fire 0

## Match summary

Water opened with `水占术`, an early `南海海怪`, and `海豚伙伴`, but the first sea monster was eventually removed after Fire chained several spells. Water then developed a nearly full board, `玛涅斯之杖`, and five learned skills. Repeated `水占术` activations found the second `南海海怪` on turn 11. Water used high-power spell sequences to clear Fire's blockers, then attacked the opposing hero once per turn from turn 15 onward. At one life, the second sea monster survived repeated three-spell turns because Water could separately pay for `寒冰屏障`, `霜冻射线`, and `冰霜利刃` through overexertion. It dealt the final point on Water turn 20.

## What worked

- `水占术` was worth building around. It eventually found the second sea monster and let the deck recover after losing the first copy.
- `唤雨师` plus `玛涅斯之杖` made even cheap defensive skills strong enough to cover Fire's main attacks.
- A wide field converted otherwise idle load into defensive payments. Using a different unit to overexert for each defense let Water withstand three consecutive spells without spending pooled elements.
- `海豚伙伴` behind the one-life sea monster forced Fire to account for an additional lethal-prevention layer, even though the ordinary defenses were sufficient.
- Clearing every opposing front-row unit was necessary before attempting direct hero attacks. Once the field was empty, the sea monster provided a reliable clock.

## Strategy adjustments for the next match

- Do not cast a skill immediately after learning it unless its orientation explicitly permits it. The turn-1 failed `水占术` cast wasted a water payment and prevented the planned three-cost summon.
- Preserve three distinct defense skills and three vertical payment bodies when protecting a fragile finisher against Fire. This exact arrangement defeated repeated `焚烧` / `火球术` / copied-fireball sequences.
- Prefer building the support engine before exposing the first sea monster. The second copy performed much better because the board and defensive skill suite were already established.
- When issuing a hero attack, include the hero coordinates (`target_col: 1`, `target_row: 1`); omitting them was interpreted as a missing unit target.
- Send one action at a time and wait for authoritative state. Delayed state delivery made duplicate submissions and stale-target attempts common.

## Suspected bugs and protocol friction

1. **Failed actions appear to consume payment before legality validation.** On turn 1, casting newly learned horizontal `水占术` returned `skill is horizontal (already used)`, but the submitted water payment was deducted. On turn 16, failed spell attempts against an absent unit and an invalid hero target likewise appeared to reduce the pool. Payment should be committed only after all non-payment legality checks pass, or the API should explicitly document otherwise.

2. **Orientation/reset behavior was difficult to reconcile with the rules.** The first `南海海怪` remained horizontal across multiple apparent owner-turn cycles without a visible status. The second sea monster was still horizontal at the start of turn 16 after attacking on turn 15, then became vertical only after turn 16's end-of-turn discard resolved. This deserves a room-log audit against the intended "reset at the end of the owner's turn" order.

3. **End-turn is not complete until a private discard pending action resolves.** The opponent can report `end_turn`, while the other player still sees the old `current_turn` and receives turn errors. The CLI should surface this as `end_turn_pending_discard`, and orchestration should treat the authoritative turn change—not command acceptance—as completion.

4. **Hero attacks require redundant board coordinates.** `target_type: "hero"` plus `target_owner` returned `no unit at target position`; adding center-hero coordinates succeeded. The protocol reference and validation error should make this requirement clear, or the backend should derive the fixed hero position.

5. **Fast batched submissions race authoritative state.** Several announced opponent summons/attacks never materialized, while duplicate retries sometimes failed because the first command actually succeeded after delayed state delivery. A command acknowledgement/action ID would make headless play substantially more reliable.

## Card-text/behavior observations

- `海豚伙伴` was exposed as an automatic/private lethal-prevention decision layer and was understandable from state, although it did not need to trigger in the final sequence.
- `寒冰屏障`, `霜冻射线`, and `冰霜利刃` behaved consistently with their visible attack/defense powers and costs during the late defensive chain.
- `南海海怪` dealt one damage per attack as printed by its current attack value. Its reset timing, rather than its damage effect, is the suspicious part.
- No definite card-text/effect mismatch was proven in this game beyond the reset-timing concern above.
