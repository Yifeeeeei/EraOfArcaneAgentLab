# Series 29 Player A Review

## Result

- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Match: `series-29-room-8857`, room `8857`
- Player: `official-series29-a` / `OfficialA29` / slot 0 / first player
- Deck: `ROYAL-MIST-GRAVE-CLOCK-001`
- Result: loss, official `game_over`, winner slot 1, `hero_killed`, turn 28
- Final heroes: Bailey `-1` (from 1), Eve `3`
- Terminal sequence: B used Moon Dust `ci_234` with `remove_front_stealth`, removed Hidden from the sole center-front Cannon `ci_185`; Wing `ci_223` killed the Cannon; Lunde `ci_215` then attacked Bailey for 2.

## Exact deck code

`4211101 // 1221001 1221001 1221003 1221003 1221007 1221007 1221009 1221009 1221101 1221101 1221103 1221103 1221105 1221105 1221109 1221109 1221111 1221111 1211103 1621001 1621001 1621011 1621011 1621016 1621016 1621112 1621112 2621108 2621109 2621109 // 3021001 3221002 3221009 3221011 3221103 3221104 3221105 3221106 3221108 3221109`

## Registered measurements

- First physical attack: turn 9, Wendy `ci_187` attacked the center Wing.
- First hero damage: turn 14, Hunter `ci_195` deathrattle hit Eve for 1.
- Physical hero damage by A: 0.
- Deathrattle hero damage by A: 3 total (Hunter 1 on turn 14; Vengeful Dead 2 on turn 26).
- Spell hero damage by A: 0.
- Shift-created attacks: 1. On turn 21 Shift moved Ship `ci_177` from right-front to center-front; it immediately attacked the center Warrior.
- Graveyard-value conversions:
  - Bone Knight `ci_190` returned once and became a stable Dark source.
  - Coffin `ci_196` discarded Raven `ci_188`, immediately resolved its draw deathrattle.
  - Elegy `ci_198` used an existing Dark companion in grave to discount and summon Raven `ci_189`.
  - A late second Elegy `ci_197` correctly failed when no searchable deathrattle shadow companion remained.
- Deck exhaustion: both decks reached 0, but live attackers and finite blockers kept the game progressing; this was not a stable loop.

## Pre-match hypothesis comparison

### Engine: Hidden / deathrattle / graveyard value

Partly correct. Hidden repeatedly bought attack windows for Wendy, Ships, and Kraken, while Coffin, Elegy, Raven, Bone Knight, Hunter, and Vengeful Dead all produced observable value. The grave package was functional rather than decorative.

The missing step was conversion. Most grave value became cards, elements, or extra blockers; only Hunter and Vengeful Dead damaged the enemy hero. The package did not create enough positive-attack bodies.

### Clock: real attackers

Incorrect in density and timing. The first attack was delayed until turn 9. Wendy attacked once before dying; the first Ship was removed before attacking; the second Ship and two Krakens spent nearly all their attacks clearing replacement blockers. A produced zero physical hero damage in 28 turns.

The deck's actual clock was `one 1-attack center body + Ice Cone + Undertow`. That line repeatedly reduced a blocker but normally left the opponent's permanently enhanced Slash available to defend Undertow. It was a clearing cadence, not a hero-kill cadence.

### Bridge: movement / removal

Shift was genuinely useful but underrepresented. It created one immediate attack, repaired center occupancy, and later stretched survival by moving rear resources into front slots. One copy/use cadence was insufficient to overcome three-column global hero blocking.

Ice Cone's permanent power 6 reliably beat Slash power 5, but still dealt only 1 damage. Undertow dealt 2 but was usually the second spell and was repeatedly defended by Slash. The ordering should sometimes be reversed only when another defense breaker exists; with this list, the opponent could preserve Slash for the 2-damage spell.

### Breakpoint and stop-resource rule

The pre-match rule to stop adding support once a clock existed was directionally right, but the list itself contained too many zero-attack resource bodies. Late turns demonstrated the cost: the board could be refilled with blockers for many turns, yet could not threaten Eve. Resource density should be judged by whether it creates another attack, not merely whether all costs remain payable.

## Key tactical lessons

1. Read the opponent's defense pair as a cadence lock: a defense spell with power 5 plus a repeatable 2-Light payment means `Ice 6 / attack 1` gets through while `Undertow 4 / attack 2` is saved against. Add a third attack spell, reaction, pierce, or defense denial; otherwise the 3-damage turn is actually only 1.
2. Global front-row protection means clearing only center is insufficient. Side-front companions prevented direct center hero attacks even when the center lane was empty.
3. Hidden is tempo, not a win condition. The terminal Moon Dust cleanly removed Hidden from the last Cannon and exposed the hero. A Hidden blocker must buy time for a clock already in place.
4. Wendy's trigger resets a low-expense spell after it hits; it does not reset Wendy. The private continuation appears before opponent defense resolution and must be handled immediately.
5. Bone Knight rebirth is a two-step private continuation: choose the card, then choose `pos:col:row`.
6. The best clean graveyard conversion was Vengeful Dead: forcing the enemy attacker to kill it translated board defense into 2 hero damage. Increase this kind of reach rather than generic draw-only deathrattles.

## Deck iteration recommendation

- Cut at least four zero-attack or redundant resource slots (one Cannon, one Ghost, one Elegy, and one low-impact resource companion are the first candidates).
- Add four native positive-attack bodies, including at least two affordable center attackers and one fast attacker.
- Add a second movement/position bridge or a way to clear side-front blockers.
- Add one independent finisher that can damage the hero after fronts are cleared; do not rely on Hidden survival.
- Keep one Coffin, one Elegy, both Vengeful Dead, and at least one Hunter: these were the grave package pieces that produced meaningful conversion.

## Corrected event-reading evidence

Turn 14 initially looked inconsistent, but room-log review showed correct resolution:

- A cast Ice Cone `ci_200`; A state serialized `effective_attack_power=6` and `power=6`.
- B submitted enhanced Light Slash `ci_243`, power 5, with Warlock `ci_218` overexert payment. Authority emitted `defense_attempt(6,5)`, then `spell_hit(1)` and damage; there was no `defense_success`.
- Wing fell from 3 to 2 life, then Undertow `ci_206` dealt 2 and destroyed it. The life arithmetic is complete.
- Turn 15 repeated the same correct sequence. The lesson is that `defense_attempt` means only that a defense was submitted; inspect the following event for `defense_success` or `spell_hit`.

This was an Agent event-reading error, not a game defect, and no Issue should be filed.

Separately, B preserved evidence that a newly equipped horizontal Blessing Staff accepted `use_ability` and emitted `ability_used` while consuming no marker, producing no elements, and applying no effect. Treat that as B-side evidence for coordinator review.

## General recognition rule

When reading a Water/Dark Hidden-grave list, count three things before calling it a clock deck: affordable positive-attack bodies, repeatable ways to put one in center, and damage that survives the opponent's best defense. Hidden, draw, rebirth, and resource recursion are only an engine. If those three counts are low, pilot the list as attrition and deliberately draft deathrattle reach; otherwise it can survive to deck exhaustion while still being unable to win.
