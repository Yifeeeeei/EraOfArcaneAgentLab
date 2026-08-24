# Series28 Player B Review

## Result and identity

- Match: `series-28-room-8508`
- Result: `contaminated_adjudicated_draw`
- Engine result: no official `game_over`; stopped at turn 38 after a provable loop.
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Deck ID: `LIGHT-GRACE-MIDRANGE-001`
- Exact deck code: `4511102 // 1021011 1021011 1021013 1021013 1511101 1511101 1521001 1521001 1521002 1521002 1521006 1521006 1521008 1521008 1521016 1521016 1521102 1521102 1521103 1521103 1521107 1521107 2521014 2521014 2521105 2521105 2521106 2521106 2521111 2521111 // 3511102 3521001 3521003 3521007 3521008 3521013 3521014 3521105 3521106 3521108 //`
- Transcript: `agent-data/matches/series-28-room-8508/player-b.jsonl`

The result is not evidence of matchup strength. Issue #147 made both Giant Sandworms gain Hidden from unrelated damage, eventually exceeding 40 and becoming permanently untargetable. Issue #146 then allowed both empty decks to continue without an automatic terminal result. At turn 38, the center Sandworm could deal one contaminated hero damage per turn while Healing Warlock's mandatory prayer healed that point back; the other Sandworm could not reach the center hero. The coordinator therefore adjudicated a contaminated draw.

## Clean versus contaminated evidence

### Clean evidence retained

- Blessing Staff repeatedly converted one activation into permanent `+1 life` on the center Warrior and two Light. Across two copies, the Warrior grew from base 4 life to 10 maximum life.
- Healing Warlock repeatedly restored the same center attacker after damage. Before the polluted endgame, this preserved a real attacker through several exchanges rather than merely padding a rear support body.
- Two Glory Scrolls cleanly killed two 3-life Rock Mountain Terrors after the Warrior helped set them up. This is the best evidence for the deck's intended `engine -> bridge -> attack body` conversion.
- Light Wave cleanly stunned and/or helped clear Xinke, Warriors, Jade Guards, Scavengers, Squirrels, and Lizards. It repeatedly created favorable blocker exchanges, although its one-turn learning delay and Jade's recurring shield reduced its damage efficiency.
- The grown Warrior, Throne Holy Wing, and Rapid Killer formed a three-attacker front. They repeatedly cleared clean blockers while supports stayed behind them.
- One clean generic physical hero hit landed on turn 12, reducing Jade from 6 to 5.
- A newly learned Light Wave was correctly horizontal and unusable in the same turn. Planning must include this setup tax.

### Contaminated evidence excluded

- Every exchange whose legality, target choice, survival, or blocking depended on a Sandworm's erroneous Hidden value.
- All Sandworm attacks, including the late raw hero hit.
- Forest Insight draws beyond the clean counterfactual draw count, and cards reached only through those extra draws.
- Any claim that Light Wave is sufficient Hidden removal: it could splash the Sandworms only while a different legal front-row target existed. Once only Hidden Sandworms remained in front, the spell had no legal anchor.
- The final turn count, endurance, and draw result.

## Hero-damage attribution

### Player B clean hero damage

| Source | Pre-registered expectation | Actual clean damage |
|---|---:|---:|
| Generic physical attackers (Warrior/Killer/Wing) | 3-5 | 1 |
| Learned Light spells | 1-3 | 0 |
| Glory Scroll | 0-3 | 0 |
| Other/trigger damage | 0 | 0 |
| **Total** | **4-11** | **1** |

The deck failed the pre-registered requirement of establishing a repeatable hero clock by turn 6. It did establish a repeatable *blocker-clearance* machine, but those are not equivalent. The only clean hero damage came from the Warrior after the front briefly opened.

## Five-layer model: prediction versus evidence

### Engine

Partly correct. Staff plus Warrior was the practical engine; Staff supplied both permanent durability and the exact Light needed for bridge spells. Healing Warlock was also excellent at preserving that investment. The pre-match emphasis on Holy Child, Defender, and broad healing redundancy was too optimistic: neither Holy Child nor Defender was necessary for the strongest observed line, and several extra healing bodies/cards remained in hand or were discarded.

Correction: identify the smallest engine first. Here it was `one durable attacker + Staff/Warlock`, not the full healing package.

### Clock

Incorrect as stated. Warrior/Wing/Killer were reliable exchange tools, but only produced one clean hero damage. The list had attack bodies without a reliable way to turn repeated clearance into repeated hero access. Flowing Light Beam never became an active clock because the deck could not reliably produce its Light+Air expense. Glory was used correctly as removal, but never as a finisher.

Correction: a card is not a clock merely because it can attack. A clock requires a reproducible path from the current board to the enemy hero on consecutive turns.

### Bridge

Mostly correct for ordinary blockers. Glory cleanly removed two priority threats, and Light Wave generated multi-card tempo through front-row stun/clear. The missing bridge was legal Hidden interaction or position manipulation that does not require first selecting the Hidden unit. Royal/Base Light alone in this build could not force open the final lane.

Correction: bridge coverage must name what happens against ordinary bodies, shield, Hidden, and non-front supports separately. `Front-row AOE` is not a universal Hidden answer if it still needs a legal target.

### Breakpoint

Partly correct. The deck reached independent Light plus attacker, Staff growth, high-life Glory support, and three ready attackers. However, reaching those resource breakpoints did not imply a hero-damage breakpoint. After the first Warrior direct hit, the deck should have treated every additional support/heal as suspect unless it directly opened the hero.

Correction: add a hard conversion checkpoint: after two consecutive turns of only clearing blockers, stop adding healing/support and reserve resources for removal, movement, or haste.

### Cadence

The positioning discipline worked. Center-front remained the primary Warrior lane, side/rear cells held Warlock, Flower, and other support, and Rapid Killer/Wing occupied attack cells. The deck did not choke its own front with zero-attack healers. Cadence still broke whenever the opponent placed a new blocker every turn, because replacement attackers did not increase total attack above the opponent's replenishment rate.

Correction: track `attacks created minus blockers created`, not just whether one attacker is ready next turn.

## Healing-to-offense rule audit

### When healing was tempo

- Staff growth on the center Warrior was real tempo: it preserved the same attack body, raised Glory support power, and generated Light in one action.
- Warlock healing after damage preserved accumulated Staff growth and avoided paying four again for a replacement Warrior.
- Healing the right Wing in the late raw loop exactly offset one polluted Sandworm attack, proving strong sustain but not clean offensive value.

### When healing stopped being tempo

- Once the three-attacker front was established, further generic healing did not open the hero. The deck correctly discarded several redundant heal/support cards, but the list still contained too much healing density relative to bridge density.
- Repeated Warlock prayer became mandatory maintenance in the polluted terminal loop. It prolonged the state without creating a legal attack.
- Shield from Lonely Star Guardian was useful stabilization, but against Jade it often let Light Wave's one attack be absorbed without shortening the blocker clock.

Operational rule: healing is tempo only when it preserves a body that will make a legal attack or supplies the bridge in the same turn. If it does neither, stop healing and spend the card/element slot on lane access.

## Errors, anomalies, and issues

- Issue #147 contamination dominated the match: Sandworm Hidden rose on unrelated damage, multi-target damage segments, and its own attacks. Values exceeded 40 and made both copies permanently untargetable.
- Issue #146 allowed both empty decks to loop without official game over.
- The serialized dead Lightforged Titan remained in the unit grid with zero and later negative current life. It was even available as a prayer target, allowing meaningless healing selections. This is suspicious state hygiene and should be checked independently if not already tracked.
- Blessing Staff with zero markers still accepted `use_ability` and emitted `ability_used` without a target/effect. It did not alter the board, but the action should likely be rejected rather than consume the per-turn use.
- My early attack payloads incorrectly used `target_id`; the authoritative CLI expects `target_col`/`target_row`, producing `no unit at target position`. These were player-driving errors and did not mutate state.

## General deck-reading rules learned

1. Find the smallest closed engine before naming the archetype. Here Staff/Warlock plus one Warrior mattered more than the entire healing package.
2. Separate `durable attacker`, `blocker clearer`, and `hero clock`. A single card can fill two roles, but do not assume it fills all three.
3. Count whether bridge actions preserve at least one ready attack. Glory succeeded because it removed a threat cleanly; Light Wave often consumed resources only to trade shield or stun.
4. For a healing deck, pre-register the exact turn where sustain must become damage. Two consecutive blocker-only turns are a useful default stop signal.
5. Audit mixed-element learned skills against the actual production map. Flowing Light Beam looked like a finisher but lacked reliable Air production and should not be counted as live reach.
6. AOE needs a legal anchor. Against Hidden, confirm whether the spell can be cast without directly selecting the Hidden unit.

## Next iteration

- Reduce redundant pure-heal/support slots; keep the compact Staff/Warlock package that actually generated tempo.
- Add a real repeatable hero clock or a bridge that creates same-turn hero access: movement, forced displacement, legal Hidden removal, piercing/direct damage, or more haste.
- Either add stable Air production for Flowing Light Beam or replace it with a mono-Light finisher.
- Keep two Glory Scrolls: both cleanly performed as high-value priority removal.
- Keep front-row discipline and at least five true attackers; measure success by clean hero damage by turn 6, not by maximum life or board survival.
- Retest only after Issue #147 is fixed; otherwise any Hidden matchup conclusion remains invalid.
