# Series 26 Player B review — WINDLESS-BLOOD-GARDEN-002

- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Match: `series-26-room-4685`
- Result: Player B win (`winner=0`, B occupied slot 0)
- Official end: turn 10, `phase=game_over`, Jade 0 life, Hubert 6 life
- Transcript: `agent-data/matches/series-26-room-4685/player-b.jsonl`
- Wall-clock span: 2026-08-21 17:34:26Z–17:51:38Z (about 17m12s)

## Exact deck

Deck ID: `WINDLESS-BLOOD-GARDEN-002`

```text
4611101 // 1021011 1021011 1021013 1021013 1611102 1611102 1611103 1611103 1621001 1621006 1621006 1621011 1621011 1621016 1621016 1621107 1621107 1621112 1621112 1621113 2611001 2611001 2621005 2621006 2621101 2621101 2621108 2621108 2621109 2621109 // 3021001 3021008 3621001 3621003 3621004 3621010 3621013 3621101 3621102 3621103 //
```

## Outcome and decisive sequence

The revised deck converted its engine into a real clock and won before the Earth fortress reached its late prevention lock.

- Turn 2: Rose Reaper entered center front, not the rear.
- Turns 3–6: Reaper killed two Xinkes and two Rapid Killers while Robert used two White Bone Knight Feast cycles to reach six markers and 1 attack.
- Turn 7: Spatial Shift moved 1-attack Robert from right front to center front; Robert hit Jade 5→4 through shield 2. Death Magic Stone then funded a durable Demon Slayer Warrior.
- Turn 9: Blood Demon Blast sacrificed Blood Thorn to kill the central 2-life Warrior; Spatial Shift moved our Warrior into center and it hit Jade 4→3.
- Turn 10: the established Warrior hit Jade 3→2. Spatial Shift moved it aside, Rapid Killer entered the now-open center with haste and hit Jade 2→1. Blood Feast killed Whisper Hunter, whose deathrattle hit Jade 1→0. The server emitted official `game_over`.

Physical hero attacks and Whisper Hunter's deathrattle both bypassed Jade's shield in this match; the shield remained at 2 while hero life fell.

## Pre-match deductions versus play

| Pre-match deduction | Result | Evidence |
|---|---|---|
| Ordinary front-row attackers should be the primary win condition | Confirmed | Reaper, Robert, Warrior, and Rapid Killer created the entire physical clock. |
| Rose Reaper must occupy a front square | Confirmed | Center-front Reaper immediately traded into four relevant opposing attackers/blockers. The Series 25 rear-row failure did not recur. |
| Robert needs six markers/two attack upgrades to reach 1 attack | Confirmed exactly | Each Feast kill of White Bone Knight produced three markers. First upgrade moved -1→0; second moved 0→1. |
| Robert is secondary scaling, not the only attacker | Confirmed | Robert dealt one hero damage, then died; Warrior, Killer, and Hunter still completed the win. |
| Spatial Shift is a correction tool for attack lanes | Strongly confirmed | It moved Robert to center for its first hit, moved Warrior to center after Blood Demon Blast, and moved the already-used Warrior aside so a hasty Killer could use center on the lethal turn. |
| Reduce zero-attack engine density | Confirmed | Mulligan rejected a utility-only hand. Only bodies with immediate deathrattle value were used; the final board clock came from positive attackers. |
| Stop self-harm once a clock exists | Mostly confirmed | After Robert reached 1 attack, sacrifices were used only to clear the center lane or supply direct lethal damage. No turn was spent gaining dark merely because it was available. |
| Nightmare would convert friendly deaths into pressure | Not observed | Neither copy was drawn/played. The hypothesis remains untested. |
| Disarm answers prevention equipment | Not observed | It was not needed because the game ended before Emerald Eternity appeared. |
| Preserve an open slot for Rapid Killer | Confirmed | The lethal turn deliberately moved Warrior out of center before summoning the hasty Killer there. |

## Execution errors and corrections

1. **Turn 8 new-skill timing error.** Blood Demon Blast was learned and immediately cast, but newly learned non-haste skills enter horizontal; the backend correctly returned `skill is horizontal (already used)`. The fallback double physical attack reduced the blocker from 4 to 2, and the spell was used correctly next turn.
2. **Initial Blood Feast activation path was misremembered.** The generated Feast first had to be learned, then its `绑定` per-turn ability paid another dark to transfer it to Hubert. Calling `use_ability` while it was only in the skill pool correctly returned `card not found on field or skill area`.
3. **Rose Reaper could not attack Jade while any opposing front unit remained.** The direct attack was rejected, then Reaper legally attacked the right-front Rapid Killer. Read the whole enemy front row as blocking hero attacks, not only the matching column.
4. **Blood Thorn did not recur when sacrificed as Blood Demon Blast's activation cost.** Its text requires death from a friendly card's attack/effect. A sacrifice cost is distinct; no return window appeared. This is consistent with the rules distinction and is not reported as a bug.
5. **The abandoned room 2082 is not part of this result.** The official transcript/result is room 4685 only.

## What the revised cards changed

- `移形换影` was the most important addition. It turned position from a permanent construction mistake into a tactical resource and enabled three separate attack-lane conversions.
- `屠魔者武士` provided a durable independent attacker after Robert died.
- `屠魔者杀手` converted an open center into immediate damage and was essential to the lethal turn.
- Cutting redundant Pain Souls/Blood Puppets prevented the hand and board from becoming a resource engine with no attack value.
- Death Magic Stone remained excellent, but its 4-dark turn-10 output was spent immediately on the lethal multi-card sequence rather than banked conceptually as value.

## General “read the deck” rules

1. **Count attack-ready bodies, not companions.** A hand with four companions can still have zero pressure. Identify printed positive attack, haste, and the exact number of turns before each unit can hit.
2. **For negative-base scaling attackers, compute the real threshold.** Robert's first `+1攻` is only debt repayment. Six markers—not three—means “attacker online.”
3. **Treat the center-front square as a consumable tactical asset.** Ask who needs it now, who needs it after attacking, and whether movement can recycle it for a hasty follow-up.
4. **Position-changing cards increase effective attacker density.** Spatial Shift did more than rescue a misplaced unit: it allowed multiple attackers to use the same premium lane in successive actions/turns.
5. **Once a two-turn clock exists, every sacrifice needs a clock justification.** Valid reasons are clearing the blocker, reaching the next attack threshold, or dealing direct lethal damage. Extra dark alone is not enough.
6. **Separate play cost, newly-learned state, and cast cost.** A non-haste skill learned this turn is setup for the next turn, even if enough elements remain to pay its cast expense.
7. **Read death conditions literally.** “Friendly attack/effect death” does not automatically include sacrifice/devour costs.
8. **Against Jade, shield is not necessarily the life clock.** In the observed implementation, physical hero attacks and Whisper Hunter deathrattles reduced hero life without reducing shield. Preserve those routes instead of spending turns trying to peel shield with low attack spells.

## Next iteration

- Preserve the Series 26 positive-attacker package and both Spatial Shift / Disarm.
- Keep two Reapers only if the curve can still produce six dark by turn 2–3; this match proved that early center-front Reaper is worth the cost.
- Retain the Robert + White Bone Knight package, but mulligan Robert without a visible six-marker line.
- Consider replacing one additional slow resource item with another hasty/positive attacker if later matches again draw utility-heavy opening hands.
- Explicitly plan non-haste learned skills one turn ahead. If same-turn lane removal is required, learn Blood Demon Blast before the blocker arrives or use an already-learned spell.

## Bug assessment

No issue-worthy gameplay bug was established by Player B in this match. All encountered errors matched authoritative rules/action timing, and the game reached official `game_over`.
