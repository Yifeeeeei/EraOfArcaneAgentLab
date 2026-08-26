# Series 31 Player A pre-match

- Deck ID: `ROYAL-MIST-GRAVE-CLOCK-002`
- Parent: `ROYAL-MIST-GRAVE-CLOCK-001`
- Game commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Card pool: base set + Royal Conflict only
- Construction: 30-card main deck + 10-card skill deck

Exact deck code:

`4211101 // 1221001 1221003 1221003 1221007 1221009 1221009 1221101 1221101 1221103 1221103 1221105 1221105 1221109 1221111 1211103 1621001 1621011 1621011 1621016 1621016 1621112 1621112 2621108 2621109 1021011 1021011 1021013 1021013 2021116 2021116 // 3021001 3221002 3221009 3221011 3221103 3221104 3221105 3221106 3221109 3221110`

## Iteration thesis

001 proved that Coffin, Elegy, Bone Knight, deathrattles, Hidden and spell reset all produce value. It still dealt zero physical hero damage in 28 turns because too much of that value became cards, resources and blockers rather than independently payable attackers. 002 keeps the smallest grave engine that converted meaningfully and replaces six passive/redundant slots with one coherent generic-cost clock-and-clear package.

This is not the Royal survival-Fire shell. It remains Water/Dark Hidden tempo, but now generic Water load can directly pay for Rapid Slayers, Warriors and Arcane Bombs without first assembling mixed Water/Dark production.

## Exact delta from 001

Main-deck removals, one copy each:

- `1221001` Sea Dolphin: cut the second prevention-only body.
- `1221007` Icefield Wolf: cut one pure two-Water resource body.
- `1221109` Mist Wraith: cut the second Hidden resource body.
- `1221111` Raider Gunner: cut the second zero-attack discard-value body.
- `1621001` Netherworld Raven: cut one draw-only deathrattle.
- `2621109` Elegy Scroll: cut the redundant second grave search.

Main-deck additions:

- `1021011` Rapid Slayer x2: generic cost 3, immediate physical attack and center conversion.
- `1021013` Slayer Warrior x2: generic cost 4, independent durable one-attack replacement.
- `2021116` Arcane Bomb x2: generic cost 3, two damage to a companion for clearing side-front or center blockers without consuming the physical attacker.

Skill change:

- Remove `3221108` Six-petal Snowflake: zero-damage freeze did not convert the lane into hero pressure.
- Add `3221110` Raider Tide: one-attack front-row spell that can clear multiple side-front blockers while replacing cards on hit. It is the explicit three-column bridge.

Kept grave core: one Coffin, one Elegy, two Bone Knights, two Vengeful Dead, two Whisper Hunters and one Raven. Every retained grave card either returns a body, converts death into reach, or supplies one compact card-value line.

## Five-layer plan

### Engine

- Bailey supplies the initial four Water.
- Raider Pirates and Ships supply the Dark bridge while remaining part of the Water plan.
- One Mist Wraith, one Cannon, one Raven, one Coffin and one Elegy are the reduced value package.
- Bone Knight is retained because rebirth produces both a blocker and recurring Dark; Vengeful Dead and Hunter are retained because death converts into hero reach.

### Clock

- Tier 1: Rapid Slayer. It is payable from any three load and attacks on entry.
- Tier 2: Winter Archer and Slayer Warrior. Archer attacks outside front row; Warrior is a durable generic-cost replacement.
- Tier 3: Kraken, Pirate Ship and Wendy. These are the stable center clocks once five or six Water is online.
- Deathrattle damage is reach, not the primary clock. A successful run must include physical hero damage.

### Bridge

- Arcane Bomb removes a two-life blocker in any payable lane before the physical attack.
- Raider Tide attacks the whole front-row problem instead of repeatedly clearing only center.
- Undertow, Ice Cone, Frost Blade and Corrosive Flow remain single-lane clearing tools.
- Spatial Shift must either move a ready attacker into center, vacate center for a Rapid Slayer, or preserve the named following-turn attacker.
- Hidden and Water Escape preserve an attacker only after a real clock exists.

### Breakpoints

- Generic 3: any three Water/other load pays Rapid Slayer or Arcane Bomb. This is the first proactive breakpoint and must be valued above a third passive resource body.
- Generic 4: Slayer Warrior is independently payable from Bailey alone on a normal full-load turn.
- Water 4 + Dark 1: Pirate Ship and Raider Tide learn line.
- Water 5: Kraken.
- Water 6: Wendy.
- Stop adding passive resource bodies once generic 4 plus one ready attacker exists, or once six Water supports Wendy/Kraken and a replacement attacker is named.

### Cadence

Before each development action, name:

1. the attacker this turn;
2. the blocker that prevents hero conversion;
3. the bridge used on that blocker;
4. the attacker already reserved for the following turn.

Reserve center-front for Kraken, Ship, Wendy, Warrior or a Rapid Slayer. Put Archer outside front whenever possible. Do not occupy center with Dolphin, Wraith, Cannon, Raven or Bone Knight unless it prevents immediate lethal and no clock can be deployed.

## Mulligan

Keep at least one independently payable physical attacker:

1. Rapid Slayer;
2. Winter Archer;
3. Slayer Warrior;
4. Kraken/Ship only with a credible payment curve.

Keep one cheap Water source alongside the attacker. Arcane Bomb is a keep only when the hand already has an attacker. Coffin or Elegy is never a keep without a functional clock hand. Full-mulligan hands containing only passive resources, Hidden and grave value.

## Pre-registered metrics

1. First legal physical attack: target turn 2 or earlier; record attacker and target.
2. First physical hero damage: target by turn 5; record exact attacker and damage.
3. Total physical hero damage: target at least 4 and strictly greater than 001's zero.
4. Attack cadence: at least one legal physical attack on 75% of own turns after turn 1. Record every blank and its cause.
5. Independent payment: record each Rapid Slayer, Warrior and Arcane Bomb payment and whether it required Dark setup. Target at least two proactive generic-cost actions before turn 6 and zero off-color stranded actions.
6. Side-lane bridge: at least one Arcane Bomb or Raider Tide action must remove/damage a side-front blocker or create a same-turn center hero opening. Setup-only casts are separate.
7. Spatial Shift: target at least one immediate or next-turn-preserved physical attack; cosmetic uses count zero.
8. Center replacement: after every center-clock loss, record whether a named ready/recruitable replacement existed. Target replacement within one own turn.
9. Grave efficiency: count Coffin, Elegy, Raven, Bone Knight, Vengeful Dead and Hunter copies that create cards, bodies or hero reach. Also count turns where grave value replaces a legal physical attack; target zero.
10. Resource breakpoints: first own turn with generic 3, generic 4, Water 5, Water 6, and Water 4 + Dark 1, listing sources.

## Falsifiable hypothesis

002 should attack by turn 2, deal physical hero damage by turn 5, and finish with at least four physical hero damage. At least two generic-cost proactive actions should occur before turn 6, and at least one side-front blocker must be affected by Bomb or Raider Tide. If the list again reaches deck exhaustion with physical hero damage below four, the reduced grave core is still too large or the Water/Dark shell lacks a sufficient bridge even after generic attackers.
