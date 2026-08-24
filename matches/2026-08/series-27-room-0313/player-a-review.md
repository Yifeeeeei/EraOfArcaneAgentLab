# Player A review — Series 27

- Match: `series-27-room-0313`
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Player/deck: `official-series27-a` / `EARTH-MOBILE-BEATDOWN-003`
- Result: win, official `game_over`, winner slot 0 (A), turn 12
- Final life: Jade 2, Hubert 0
- Transcript span: 2026-08-24 01:40:21Z–02:08:55Z, about 1,714 seconds
- Transcript: `agent-data/matches/series-27-room-0313/player-a.jsonl`

## Exact deck code

`4411101 // 1021011 1021011 1021013 1021013 1401002 1401002 1401101 1401101 1421012 1421012 1421013 1421013 1421016 1421016 1421101 1421101 1421102 1421102 1421114 1421114 2421002 2421002 2421008 2421008 2421009 2421009 2421110 2421110 2421111 2421112 // 3021001 3421003 3421004 3421101 3421103 3421104 3421107 3421108 3421109 3421110`

## Decisive sequence

- Turn 1: Forest Arrow killed Whisper Hunter, whose deathrattle damaged Jade 6→5. Rapid Slayer then entered center-front and immediately attacked Hubert 6→5. The deck established both its first center attacker and first hero damage on turn 1.
- Turn 2: the Slayer damaged the opposing Warrior. Sandworm Bait found the second Sandworm and reduced its Earth entry cost by two; Spikeball entered left-middle.
- Turn 3: the opponent damaged the Slayer and Xinke entered reactively. Because reactive Xinke entered horizontal during the opponent's turn, it remained horizontal throughout A turn 3. A used the six-Earth breakpoint to deploy the discounted Sandworm and Desert Leggings.
- Turns 4–8: Xinke and the two Sandworms repeatedly traded into front blockers. Spatial Shift recycled center-front, first turning the rear Sandworm into an additional attack on turn 5, then moving used attackers out so Warrior or Sandworm could become the next center attacker.
- Turns 9–11: each Shadow blocker consumed two Earth attacks, but the third ready attacker repeatedly reached Hubert. Earth dealt two hero damage on turn 9 and one on turns 10 and 11.
- Turn 12: Xinke killed the final Hunter; its deathrattle put Jade at two life. The right Sandworm attacked Hubert 2→1. Spikeball paid for Spatial Shift, which moved the ready rear Warrior into center-front; Warrior delivered lethal.

## Nine pre-registered measurements

### 1. First center attacker and first hero damage

- First ready center-front attacker: turn 1, Rapid Slayer.
- First hero damage: turn 1, the same Rapid Slayer.
- Result: target met substantially earlier than the turn-4 deadline.

### 2. Earth production and six/seven breakpoints

Elements themselves correctly reset to zero at each turn boundary. The meaningful beginning-of-turn production capacity was:

- turn 1: 4 (Jade);
- turn 2: 4;
- turn 3: 6 (Jade 4 + Spikeball 2);
- turn 4: 7 (Jade 4 + Spikeball 2 + Desert Leggings 1);
- turn 5: 7;
- turn 6 onward: 8 after Emerald Guard added one more independent Earth.

First six-Earth turn: turn 3. First seven-Earth turn: turn 4. This corrected 002's turn-10 delayed-breakpoint failure.

### 3. Attack turns, stalled center, and physical hero damage

- Own turns with at least one legal physical attack: 11 of 12.
- The only no-attack own turn: turn 3, when reactive Xinke occupied center-front but was still horizontal under the end-of-owner-turn reset rule.
- Turns with a center-front attacker present but unable to attack: one (turn 3).
- Physical hero damage: eight total. Sources were turn 1 (1), turn 7 (1), turn 9 (2), turn 10 (1), turn 11 (1), and turn 12 (2).

The eight physical damage was necessary because Hubert healed twice during the match.

### 4. Replacement coverage

Every center-lane transition had a named successor, but one successor was not immediately attack-ready: the first Xinke entered reactively and created the turn-3 gap. Under the strict definition “next own turn has a ready attacker,” six of seven meaningful center transitions were covered (86%), above the 75% target.

The successful replacements were the second Xinke, discounted Sandworm, full-cost Sandworm, Warrior, and repeated Spatial Shift lane recycling. The failed transition is evidence that a reactive summon is not automatically cadence—it must also reset before the next own main phase or be paired with Growth Potion.

### 5. Fixed off-color stranded cards

- Count: zero.
- Spatial Shift's wildcard learn/use costs were paid entirely from Earth.
- No hand card or planned action failed for lack of Air or Shadow.

The removal of fixed-Air Mage/Rune and fixed off-color skills was fully supported.

### 6. Support summons into center-front

- Count: zero.
- Center-front was occupied only by Rapid Slayer, Xinke, Sandworm, or Warrior.
- Spikeball stayed left-middle; Guard stayed right-middle; the cheap resource cards remained in hand once the engine reached its breakpoint.

### 7. Bridge/reset actions that created attacks

- Spatial Shift created an additional same-turn attack on turn 5 by moving the ready rear Sandworm to center-front after the other two attackers had acted.
- Spatial Shift created the lethal attack on turn 12 by moving the ready rear Warrior to the empty center-front.
- Other Shift uses on turns 6, 7, 8, and 11 were cadence setup: they moved used attackers out or restored the next center configuration.
- Growth Potion, Autumn Jewel, and Regeneration Power were not drawn/used.

Thus the new payable movement bridge was not merely nominal value; it directly created two attacks, including lethal.

### 8. Sandworm/Rock Beast deployment and conversion

- Discounted Sandworm `ci_20`: deployed turn 3 for four Earth at right-front; first attacked turn 4; survived to game-over and repeatedly damaged blockers/heroes.
- Full-cost Sandworm `ci_21`: deployed turn 4 at center-rear; first attacked turn 5 after Spatial Shift; survived to game-over and repeatedly cleared center blockers.
- Rock Beast: neither copy was drawn/deployed.

Both deployed heavy attackers attacked before the next full turn elapsed and remained part of the clock, a decisive improvement over 002.

### 9. Non-clock hand at game-over

Six cards remained: one Squirrel, two ordinary Lizards, two Scavengers, and one Spikeball. None could create hero damage within one turn from the final state. This did not prevent the win, but it shows the list still contains more engine bodies than it needs after reaching eight recurring Earth.

## Five-layer model: evidence and correction

### Engine

**Supported.** Spikeball plus Desert Leggings moved the list to six Earth on turn 3 and seven on turn 4. Guard later raised production to eight. Cheap native-Earth pieces fixed the previous payoff delay.

**Correction:** the deck does not need to deploy every cheap source. Once six/seven recurring Earth exists, additional Lizard/Squirrel/Scavenger draws become blanks. Future versions should retain enough early sources for consistency but convert some late engine density into clock or reset cards.

### Clock

**Supported.** Ten physical attackers were enough to attack on 11 of 12 turns and deal eight hero damage. The clock began on turn 1 rather than waiting for a seven-cost finisher.

**Correction:** Xinke has two different clock modes. A normally ready Xinke is an attacker; an Xinke reactively summoned during the opponent's turn is a horizontal future resource/blocker until the end of its owner's following turn. Do not count the latter as next-turn cadence without a reset.

### Bridge

**Strongly supported.** Forest Arrow plus a physical attack cleared early blockers. Sandworm Bait transformed Jade's four Earth into a turn-3 Sandworm. Spatial Shift was payable from Earth and created both an extra turn-5 attack and the turn-12 lethal attack.

**Correction:** one Shift moves one unit; it cannot simultaneously vacate center and pull a rear attacker forward. The pilot must create an empty center on the prior turn when planning a rear-unit lethal.

### Breakpoints

**Supported.** The explicitly calculated breakpoints matched runtime payment: six Earth on turn 3 deployed the four-cost discounted Sandworm plus Leggings; seven on turn 4 learned Shift and deployed the full-cost Sandworm; eight thereafter sustained the bridge.

**Correction:** Sandworm Bait's successful discount is a separate four-Earth breakpoint and should be treated as a primary line, not incidental upside. The undiscounted Sandworm remains six.

### Cadence

**Supported with one identified gap.** The deck continually named this turn's attacker and the replacement. Moving already-used attackers away from center was often more valuable than adding another support body.

**Correction:** cadence should be recorded as a three-state sequence: `ready now`, `ready after own end-step`, or `requires bridge`. The earlier binary “attacker/replacement” label hid the turn-3 reactive-Xinke timing failure.

## Confirmed pilot errors

- None of the Series26 payment/off-color errors repeated.
- On turn 3 I initially described the reactive Xinke as the next attacker before applying the end-of-owner-turn reset rule; authoritative state corrected the plan before an illegal attack was sent.
- The match stayed synchronized action-by-action across kills, deathrattles, Shift selections, and discard cleanup.

## Candidate defect evidence (exclude from strategy until audited)

Both Sandworms accumulated `隐蔽` when other cards dealt or received damage while both Sandworms remained at four life. Printed text says each Sandworm should gain hidden when **that card** takes damage.

Representative authoritative observations:

- Around `2026-08-24T01:52:02Z`, Xinke dealt lethal damage to the opponent's central Warrior. Neither Sandworm lost life, but `ci_21` changed from hidden 1 to 3 and `ci_20` from hidden 3 to 5.
- At `2026-08-24T01:52:22Z`, `ci_20` attacked the opponent's right Warrior while both Sandworms remained at four life. `ci_21` advanced 3→4 and `ci_20` 5→6.
- The counters continued rising with later unrelated damage and reached abnormally high values (over 20) by game-over.

This likely made both Sandworms much harder to target than printed. It materially affected survivability, so the win proves the curve/bridge can function but does **not** fairly measure normal Sandworm interaction. The room log, implementation, and existing issues must be checked before filing a new issue or promoting conclusions about Sandworm durability.

A second audit note: B reported Blood Explosion selecting left Xinke on turn 10, but A's following authoritative turn-10 state still showed `ci_7` at two life. Do not label this a defect until the room log determines whether shield/prevention or another legal rule prevented the damage.

## Next iteration

- Keep the Earth-only payment architecture, both Sandworm Baits, Spatial Shift, and the 10-attacker baseline.
- Reduce two to four late engine-only bodies, especially redundant Squirrel/Lizard/Scavenger copies, for additional reset/removal/clock cards that remain Earth-payable.
- Preserve at least six Earth by turn 3 and seven by turn 4 in the revised production table.
- Add `ready now / after own end-step / bridge required` to the cadence checklist.
- Re-test only after the Sandworm hidden trigger is audited/fixed; otherwise attacker-survival measurements are contaminated.
