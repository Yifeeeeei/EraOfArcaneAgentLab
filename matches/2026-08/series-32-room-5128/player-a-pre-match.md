# Series32 Player A Pre-Match

- Deck ID: `MONO-FIRE-FORWARD-CLOCK-001`
- Game commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Card pool: 基础包 + 王权纷争
- Hero: 掌门 龙卷火 (`4111001`), 4 Fire load and generated 万火合一术.
- Construction rule: every colored main-deck and skill cost is Fire-only. Neutral cards use generic costs that Fire can pay. There is no second colored requirement.

## Why this is a clean break

This is not another Water-Shadow patch and is not the user's Royal survival Fire list. It abandons grave value, Hidden stall, mixed-color entry costs, and the assumption that later payoff cards will repair an inert opening. It is a forward mono-Fire deck with three independent pressure types: rapid/physical units, direct item damage, and Fire spell/burn pressure.

## Engine / clock / bridge

### Engine

- Hero supplies 4 Fire every normal turn.
- Fire Spirit is free and supplies 1 Fire; Lively Furnace costs 2 and replaces itself by drawing a card.
- Lava Golem and Lava Beacon Snake turn 2/3 Fire into two-element or 2-Fire field sources.
- Fire Box converts a 2-Fire setup turn into three later bursts of 2 Fire.
- Fire Rally Horn costs 3 Fire, then supplies 1 Fire and finds two Fire companions. It is the density engine, not a second-color dependency.
- Passion of Fire draws after Fire-spell hits. Fire Flash refunds 3 Fire after a hit. Mana Enhancer A creates one free skill activation without changing color requirements.

### Clock

- Rapid Slayer is the primary T1-T2 attacker: generic 3, Rapid, one physical damage immediately when a legal lane exists.
- Slayer Warrior is the durable generic-4 replacement attacker.
- Lava Fort Chariot is a Fire-4 attacker whose physical attack also applies Burn 1.
- Volcano Valley Behemoth is the top-end Fire-6 attacker and survives ordinary one-damage removal.
- Fire Arrow sacrifices itself for unconditional 1 damage to any enemy; Burn Scroll applies Burn 1. These preserve hero pressure through blockers.
- Fireball / Incinerate / Ember / Fire Flash are primarily blocker bridges; Burn and Fire Arrow are the non-physical reach.

### Bridge

- Arcane Bomb removes a 2-life companion for generic 3 and is payable from hero Fire alone.
- Fire Meteor Scroll supplies a penetrating attack without requiring a learned skill slot.
- Burning Earth clears or softens the full front row; Fire Flash refunds resources after opening a lane.
- The cadence rule is: clear with an item/spell while preserving a vertical center attacker, then attack; do not consume the intended attacker for payment.

## Repeatable payment lines

- T1 as first player (2 Fire): learn Fireball, or deploy Furnace/Fire Box; never keep a hand whose only proactive card costs 5+.
- T1 as second player / T2 normally (4 Fire): Rapid Slayer for 3 plus a free Fire Spirit, or Slayer Warrior / Chariot for 4, or Fire Box plus Fireball learning.
- 5 Fire: hero plus one Fire Spirit/Lava source pays Chariot and Fireball use, or Slayer plus a 2-Fire bridge.
- 6 Fire: hero plus a 2-Fire source pays Behemoth exactly; no off-color conversion is involved.
- 7+ Fire: Hero + Snake/Box supports a blocker-clear spell and a separate physical attacker in the same turn.

## Mulligan

Keep any hand containing Rapid Slayer, Slayer Warrior, Chariot, Furnace, Fire Box, or Arcane Bomb plus a low-cost engine card. Full mulligan a hand consisting only of Behemoth, Rally Horn without bodies, expensive scrolls, and reactive pieces. Prefer Rapid Slayer over all value keeps.

## Turn plan

- T1: establish one low-cost source or learn Fireball. If acting second and Rapid Slayer is present, summon center-front and attack immediately.
- T2: first physical attack is mandatory if an attacker was drawn. Use Bomb/Fireball only to open its lane, not as a substitute for deploying the attacker.
- T3-T4: keep one ready center attacker and add a side resource. Fire Arrow/Burn should begin hero damage if blockers prevent physical conversion.
- T5-T8: use Fire Flash/refund, Bomb, or front-row spell to clear; rotate Warrior/Chariot/Behemoth into the open lane.
- T9-T12: finish with accumulated physical hits, Arrow, and Burn. If no deterministic or two-turn lethal line exists by T10, record the exact density/payment failure.

## Preregistered metrics

1. First legal physical attack by Player A T2; stretch goal T1 when going second.
2. First hero damage no later than Player A T5.
3. At least 4 total hero damage from all Player A sources by T8.
4. At least 3 physical attacks by T6.
5. Attack cadence at least 67% of completed own turns after T1.
6. At least one turn combines a blocker-clear bridge and a physical attack.
7. At least one independently supplied 6-Fire breakpoint by T6, or record why it was unnecessary.
8. Zero actions rejected for insufficient colored elements.
9. Zero turns with an attack-capable card stranded solely by color; generic/Fire quantity shortage is recorded separately.
10. Clear victory line by T10 and official game over by turn 12 target.
11. Exact hero-damage ledger split into physical, direct item, spell, and Burn/status damage.

## Risks

- Fire still has few low-cost printed physical attackers; the six neutral/Fire attackers below cost 5 are the critical density test.
- Spell attacks cannot normally target a hero. They are bridges, not counted as direct clock unless their text explicitly deals damage/Burn to the hero.
- Rally Horn can overfill support slots; reserve center-front for the next attacker.
- Fire Arrow enters as equipment and may not be immediately consumable if horizontal. Plan it one turn before the required point of reach.
