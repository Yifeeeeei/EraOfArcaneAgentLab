# Player A pre-match hypothesis — Series 29

- Deck ID: `ROYAL-MIST-GRAVE-CLOCK-001`
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- New archetype: Royal water/dark hidden-graveyard tempo
- Explicit exclusions: no Giant Sandworm, no known Issue path, no copied smoke/WATER-PRESSURE list

Exact deck code:

`4211101 // 1221001 1221001 1221003 1221003 1221007 1221007 1221009 1221009 1221101 1221101 1221103 1221103 1221105 1221105 1221109 1221109 1221111 1221111 1211103 1621001 1621001 1621011 1621011 1621016 1621016 1621112 1621112 2621108 2621109 2621109 // 3021001 3221002 3221009 3221011 3221103 3221104 3221105 3221106 3221108 3221109`

## Five-layer model

- **Engine — hidden / deathrattle / grave value:** Coral Bailey supplies the initial four Water. Raider Pirates bridge into Dark while still producing Water. Mist Wraith is a two-cost hidden Water source; Dancer can hide a clock body. Raven, Bone Knight, Vengeful Dead and Whisper Hunter turn deaths into cards, repeated bodies, retaliation and direct reach. Elegy finds a deathrattle body with a grave discount; Blackpine Coffin converts an otherwise slow deathrattle hand into immediate value.
- **Clock — real attackers:** Winter Archer is the cheap clock and can attack outside the front row; South Sea Monster and Raider Pirate Ship are durable one-attack bodies; Coral Wendy is the two-attack finisher with a legal reset line. These physical attackers, not hidden counters or spell-to-hero assumptions, must deliver the final hero damage.
- **Bridge — movement / blocker removal:** Spatial Shift preserves the center attack cell. Ice Cone, Frost Blade, Corrosive Flow, Undertow and Ripple Slash clear or freeze blockers. Water Escape protects a valuable attacker or resource source; Six-petal Snowflake freezes a blocker but is not counted as hero reach.
- **Breakpoint:** Bailey's first attack spell receives permanent +3 power, so the first cheap attack spell should be saved for a meaningful blocker. Elegy/Coffin should create enough grave value to avoid spending attacker turns rebuilding resources. The key breakpoint is a cleared center with either Wendy ready or a center/remote Archer still able to attack.
- **Cadence:** name the current attacker and next replacement before every summon. Keep center-front for Ship, Monster or Wendy; place Archer in a rear/side cell because it may attack from non-front. Stop adding resource companions once six payable Water or a Wendy/Ship line is secured.

## Mulligan and opening priorities

Priority keep:

1. At least one real attacker: Winter Archer first, then South Sea Monster or Pirate Ship if the hand also pays it.
2. A one/two-cost Water engine piece: Dolphin, Raider Pirate, Mist Wraith, Water Wolf.
3. Elegy only with an otherwise functional opener; it is value, not the clock.
4. Keep one deathrattle body when Coffin is present, but never keep Coffin plus several passive deathrattles without an attacker.

Full-mulligan hands with no real attacker and no Water engine. Do not keep Wendy alone merely because the hero can eventually reach six Water.

## First three turns

- **Turn 1:** deploy a side/rear Water source or a center Archer. Preserve center-front when the hand already contains a turn-2/3 durable attacker.
- **Turn 2:** establish the first legal physical attack if Archer was drawn; otherwise reach four-to-five payable Water and name the next-turn Ship/Monster. A Raider Pirate is preferred when Dark deathrattles or Ship are in hand.
- **Turn 3:** present or preserve a real center clock. Use Bailey's first-spell +3 power only if it clears the blocker protecting the enemy hero. Deploy deathrattle value after the attack, not instead of it.

## Position and resource discipline

- Center-front is an attack cell, not a generic resource slot.
- Archer goes rear/side whenever possible because its printed rule allows attacks outside front row.
- Mist Wraith is an engine source only while hidden; do not expose it for a low-value block if another body can block.
- Pirate/Dark production is a bridge, not a goal. Stop adding Dark sources once current Dark deathrattles and Ship costs are payable.
- Do not spend Spatial Shift cosmetically. It must create an immediate attack, save the next-turn clock, or open center for a ready attacker.

## Stop-engine / turn-attack rule

Stop laying resource bodies and turn fully aggressive when any one is true:

- six payable Water is already present and Wendy is in hand/field;
- a center attacker plus one replacement exists and the opponent has at most two blockers protecting the hero;
- the enemy hero is within two physical attacks plus one printed Whisper Hunter deathrattle.

At that point, spend resources on blocker removal, Shift and attacker replacement. Do not use Hunter reach as the only win condition; it is a bridge to the final physical attack.

## Pre-registered damage and cadence measurements

1. First legal A physical attack: turn, attacker and target.
2. First A hero damage: turn, source, physical/spell/deathrattle bucket.
3. First own turns reaching four Water, six Water and one Dark plus four Water.
4. Hero damage by source: Archer, Monster, Ship, Wendy, other physical, spell, Vengeful Dead, Whisper Hunter.
5. Number of Spatial Shift uses that create an attack in the same turn; setup-only uses separate.
6. Number of deathrattle cards that yield actual value versus die with no meaningful conversion.
7. Turns after turn 2 with a legal physical attack / total own turns after turn 2.
8. Every center-clock loss and whether a named replacement was already available.
9. Final hero damage must be clean: identify the exact legal physical attacker. If the engine ends the game via deathrattle instead, mark the clean-finisher hypothesis failed even if the match is won.

## Falsifiable hypothesis

The new shell should make its first legal physical attack by turn 3, reach six payable Water by turn 4-5, and deliver at least three clean physical hero damage. At least one blocker must be removed by Bailey's empowered first attack spell, and either Shift or Archer's non-front rule must preserve one additional attack cadence. A win whose only hero reach is deathrattle does not validate the clock design.
