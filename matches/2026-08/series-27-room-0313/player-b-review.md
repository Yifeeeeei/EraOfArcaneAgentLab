# Series27 Player B Review

- Match: `series-27-room-0313`
- Game commit: `e6908601`
- Deck: `WINDLESS-BLOOD-GARDEN-002`（与 Series26 完全相同）
- Result: loss, official `game_over`, winner player 0, `hero_killed`
- Final turn: 12
- Transcript: `agent-data/matches/series-27-room-0313/player-b.jsonl`

## Exact deck code

`4611101 // 1021011 1021011 1021013 1021013 1611102 1611102 1611103 1611103 1621001 1621006 1621006 1621011 1621011 1621016 1621016 1621107 1621107 1621112 1621112 1621113 2611001 2611001 2621005 2621006 2621101 2621101 2621108 2621108 2621109 2621109 // 3021001 3021008 3621001 3621003 3621004 3621010 3621013 3621101 3621102 3621103 //`

## Hero-damage attribution

Damage dealt to Jade was exactly 4:

- Robert growth: **0**. Robert entered on turn 11 only as a two-life blocker and died before gaining markers or attacking.
- Generic attackers: **0**. Both Warriors and the hasty Killer spent their attacks trading into blockers; none reached the hero.
- Deathrattle reach: **4**. Opening Whisper Hunter dealt 1, Vengeful Dead dealt 2, late Whisper Hunter dealt 1.

The pre-match estimate (Robert 0–2 / generic 2–4 / deathrattle 1–3) therefore got the dominant source wrong. Deathrattle was not supplemental reach; it was the entire clock.

## Five-layer model: prediction versus evidence

### Engine

Predicted: Hubert plus Death Magic Stone and cheap bodies would sustain dark resources and self-damage conversion.

Observed: the engine generated plenty of dark, but resources were not the bottleneck. The opponent continuously presented blockers and three attackers. A second Stone was redundant because same-subtype equipment replacement prevented stacking. Engine evaluation must ask what the resources convert into, not merely whether they are abundant.

### Clock

Predicted: Robert growth plus ordinary attackers would create the primary clock.

Observed: Robert never became a clock, and generic attackers dealt zero hero damage. The actual clock was four points of deathrattle reach. Robert needs an early safe attack cell plus repeated friendly-damage events; drawing him after the board is lost makes him only a blocker.

### Bridge

Predicted: Spatial Shift would preserve center-front access and turn rear development into attacks.

Observed: Shift did improve one tactical sequence (moving Vengeful Dead and opening center for a hasty attacker), but could not bridge through the opponent's renewable Xinke/Sandworm wall. A bridge only works if the destination attack is legally interactive; movement cannot solve untargetable blockers.

### Breakpoint

Predicted: after stable dark production and a growth body, stop investing in support and turn toward attacks.

Observed: the deck reached resource sufficiency but never reached interaction sufficiency. The missing breakpoint was **legal removal access**. Blood Demon Blast sacrificed a two-life Blood Thorn into Xinke, but the authoritative state left Xinke at two life; Desert Leggings simultaneously changed to `ultimate_used=true`, consistent with its once-per-game two-damage reduction. Thus this exchange spent a body without opening the lane.

### Cadence

Predicted: stage an attacker in center/front every turn and replace it with Shift or hasty bodies.

Observed: cadence was repeatedly broken by free Xinke replacement and two Giant Sandworms. The opponent's cadence was stronger: it kept one current attacker and one replacement, then used Shift to move an already-attacked unit away and bring the next attacker forward. Our model must count both attack readiness and blocker replacement cadence.

## Driving decisions

- The opening Warrior plan missed because B was first player and Hubert generated only two on turn 1. Whisper Hunter was the correct fallback, but the pre-match curve model should explicitly branch on first-player reduced production.
- Warriors correctly traded rather than forcing impossible hero attacks, but the deck lacked a way to convert those trades into a clear lane.
- Vengeful Dead plus Shift was the best bridge sequence; its deathrattle supplied two of the four total damage.
- Late Robert and Whisper Hunter were correct survival plays. Robert absorbed two attacks; Hunter absorbed one and added the final deathrattle damage.
- Once the opponent had three ready attackers and Hubert at two, there was no hand line that both survived and produced lethal through shield two.

## Bugs / rule doubts observed

1. **High-confidence anomaly: Giant Sandworm hidden marks increased from unrelated damage.** Both Sandworms' `隐蔽` values rose together on many damage events not dealt to those Sandworms, eventually reaching values above 20. Printed text says each gains hidden when *this card* takes damage. This made both permanently illegal targets and materially altered the match.
2. **Blood Demon Blast into Xinke is likely not a bug.** Xinke remained at two life, while Desert Leggings became `ultimate_used=true`; that is consistent with reducing the two-damage event to zero. It should be checked against the detailed damage events, but is not independently actionable from this review.

## General deck-reading rules learned

1. Identify the first-player branch before judging the curve: a four-load hero may produce only two on the opening turn.
2. Separate resource engine from conversion engine. Excess elements without legal targets, attack cells, or finishers do not advance victory.
3. Classify clock by demonstrated hero-damage route, not card labels. In this list, deathrattles proved to be the real clock while the named growth threat dealt zero.
4. Add an interaction-legality gate to the breakpoint: before turning support into pressure, verify that the opposing front can actually be targeted and removed.
5. Cadence is two-sided. Count the opponent's free/rear replacement attackers and movement bridge, not only your own next attacker.
6. Robert should be treated as a conditional engine-clock hybrid: if he cannot enter early with a protected front attack square and at least two imminent friendly-damage triggers, do not assume he will become a win condition.

## Next controlled iteration

Keep the Series26 list fixed only if the goal is another driver test. For a deck iteration, reduce redundant equipment/self-damage conversion and add interaction that remains useful against protected or hard-to-target fronts, plus more independent attack bodies. The primary driver change is to mulligan more aggressively for an early Robert **only when** the same hand also provides a safe attack cell and immediate marker cadence; otherwise treat deathrattle reach as Plan A and stop spending bodies merely to manufacture dark.
