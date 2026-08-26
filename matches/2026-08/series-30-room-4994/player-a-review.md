# Series 30 Player A review

- Game commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Room: `4994`
- Deck: `EARTH-MOBILE-BEATDOWN-003`, unchanged
- Result: Player B won. Player A made a strategic concession on A turn 21; the backend emitted authoritative `game_over` with `reason=surrender`, `actor=0`, `winner=1`.
- Player A transcript: `agent-data/matches/series-30-room-4994/player-a.jsonl`
- Confirmed gameplay bugs: none.

## Result summary

The Issue #147 clean retest passed. Giant Sandworm `ci_21` gained Hidden only after damage to that same instance. It did not gain Hidden when shield prevented the damage, it did not gain Hidden from unrelated unit damage, and each observed owner end-turn marker settlement removed one layer. A suspected AoE failure was retracted after reading the intervening end-turn settlement: the apparent `Hidden 1 -> 1` was actually `1 -> 0` at A end turn, followed by `0 -> 1` when the next enemy AoE damaged the Sandworm.

The deck hit its early Earth breakpoint and maintained a strong early physical cadence, but produced only 3 physical hero damage and never used Spatial Shift. The match turned after repeated center attackers were cleared by Lundesar plus Light Splitting/Moonlight. By A turn 21, A had only zero-attack resource bodies against B's full board, full-life hero, and repeatable removal, so concession was strategically justified rather than a time-saving shortcut.

## 1. Resource breakpoints

- First 6+ strict Earth: A turn 2, before actions.
- First 7 strict Earth: the same A turn 2.
- Sources: hero `ci_1` = 4 Earth, Squirrel `ci_11` = 1 Earth, Xinke `ci_6` = 1 Earth, free-triggered Xinke `ci_7` = 1 Earth. Total strict Earth = 7, with the two Xinke also carrying 2 Air in addition.
- First concrete 6-Earth heavy line: A turn 3, hero 4 + Squirrel 1 + Jade Guard `ci_18` 1 summoned Giant Sandworm `ci_21`.
- Concrete 7-Earth heavy line: A turn 9 summoned Rock Beast `ci_12`; another exact 7-payment line on A turn 15 equipped Autumn Maple Diamond for 4 and summoned Rock Spikeball for 3.
- Resource-stranded turns: 0. No planned action failed for lack of the required color or amount.
- Non-payment legality miss: on A turn 19, Autumn Maple Diamond and Growth Potion could not reset neutral Rapid Slayer `ci_2`; both correctly require an Earth companion. No resource was lost.
- Resource/support bodies deployed after the breakpoint without enabling an attack within one turn: 8 (`ci_15`, `ci_18`, `ci_19`, `ci_8`, `ci_9`, `ci_16`, `ci_10`, `ci_14`). Several were intentional blockers, but they still count against the registered efficiency metric.
- Scavenger temporary Earth repeatedly accumulated from enemy damage during B turns and remained available at the following A turn. It enabled the late Rock Beast summons but did not restore the lost attack cadence after those attackers were removed.

## 2. Physical attack cadence

- First physical attack: A turn 2, Xinke `ci_6` attacked and killed B's center Rapid Slayer `ci_44`.
- A turns 2-14: every turn had at least one successful physical attack.
- A turns 15-18: four consecutive blank attack turns.
  - T15: previous center Rock Beast had been removed; only newly summoned/horizontal attackers or zero-attack bodies were available.
  - T16: no attack-capable unit remained; center Squirrel was only a blocker.
  - T17: the newly summoned Rock Beast was horizontal and could not attack that turn.
  - T18: that Rock Beast had been removed on B's turn; only support/resource units remained.
- A turns 19-20: Rapid Slayers `ci_2` and `ci_3` each produced a same-turn physical attack through Rapid Assault.
- Through the last fully played turn (T20): 15 attack turns / 19 eligible turns = 78.9%.
- Including terminal concession turn T21 as an eligible blank: 15 / 20 = 75.0%.
- Total successful physical attack declarations: 17. One additional Sandworm attempt against a rear-row Prince was correctly rejected as out of range and is not counted.

## 3. Exact physical hero damage

Physical hero damage totaled 3, below the target of 4:

| A turn | Attacker | Damage | Shift-created |
| --- | --- | ---: | --- |
| 3 | Xinke `ci_6` | 1 | No |
| 4 | Xinke `ci_6` | 1 | No |
| 7 | Xinke `ci_6` | 1 | No |

First physical hero damage occurred on A turn 3, satisfying the timing target. All other changes to B hero life came from B's own healing/effects or non-physical state changes and are not credited here.

## 4. Giant Sandworm Hidden regression

Sandworm instance: `ci_21`, summoned A turn 3 at left-front `(0,0)`, base life 4, initial Hidden 0.

| Event | Life | Hidden before -> after | Interpretation |
| --- | --- | --- | --- |
| B T4 Light Blade front-row spell | 4 -> 4 | 0 -> 0 | A shield absorbed the damage; correctly no trigger. |
| B T7 Oracle Scroll single-target hit | 4 -> 3 | 0 -> 1 | Valid self-damage trigger. |
| B T7 Moon Dust | 3 | 1 -> 0 | Explicit front-row Hidden removal worked. |
| B T8 Rapid Slayer physical hit | 3 -> 2 | 0 -> 1 | Valid self-damage trigger. B later confirmed its malformed payload defaulted to `(0,0)`; no backend redirect bug. |
| A T8 end-turn marker settlement | 2 | 1 -> 0 | Normal one-layer decay. |
| B T9 Light Blade AoE collateral hit | 2 -> 1 | 0 -> 1 | Valid self-damage trigger from a non-primary AoE segment. |
| A T9 end-turn marker settlement | 1 | 1 -> 0 | Normal one-layer decay. |
| B T10 Lundesar physical hit | 1 -> destroyed | 0 at lethal | Sandworm left play; no surviving status to assess. |

- Valid surviving triggers: 3.
- Invalid triggers from unrelated or prevented damage: 0.
- Decay checks: 2, both correct.
- Explicit removal check: 1, correct.
- Direct hostile target rejection while Hidden was active was not isolated; Moon Dust removal and AoE collateral behavior were covered.
- Regression conclusion: Issue #147 remains fixed in this match.

### Event-reading correction

The initial live read incorrectly compared the B T9 post-AoE state (`Hidden 1`) to the older B T8 post-hit state (`Hidden 1`) and suspected a missed stack. The missing event was A T8's end-turn marker settlement, which had already reduced Hidden to 0. The correct causal chain is `1 -> 0 -> 1`, not `1 -> 1`. Future reviews must anchor status comparisons to the immediately preceding authoritative state after phase cleanup, not merely the previous damage observation.

## 5. Spatial Shift

- Player A Spatial Shift casts: 0.
- Shift-created or Shift-preserved A attacks: 0.
- Setup-only A Shifts: 0.
- Target result: missed.

Player A never learned or drew an actionable Spatial Shift line. B used its own Spatial Shift to move Lundesar from left-front to center-front after clearing the center, but opponent use is not credited to the registered A-deck metric.

## Deck conclusions

- The early engine was strong: 7 strict Earth by A turn 2, Sandworm on A turn 3, and uninterrupted physical attacks through A turn 14.
- The deck's physical hero conversion was weak despite good attack-turn percentage. Only the initial center Xinke converted to hero damage; later attacks were repeatedly spent clearing blockers.
- The zero-attack support density became decisive after the two Rock Beasts died. Four consecutive turns had no legal physical attack despite abundant Earth.
- Autumn Maple Diamond and Growth Potion arrived after the attack-capable Earth companions were gone. They could not reset neutral Rapid Slayers, so the reset package produced no extra attack.
- No confirmed card-text/runtime mismatch or engine bug was observed in this match.
