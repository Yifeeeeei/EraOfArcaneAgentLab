# Player B Review — series-15 / room 3951

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Player: B (`codex-b-series15`)
- Deck: `FIRE-BURN-004`
- Opponent public archetype: water pressure/control
- Result: win; player 1, game over at turn 15. B hero had 4 life; A hero died from burn at the end of A turn 14.
- Transcript: `player-b.jsonl`

## Deck code

`4111003 // 1121001 1121001 1121002 1121002 1121005 1121006 1121006 1121014 1121014 1121015 2121003 2121001 2121001 2121004 2121004 2121006 2121011 2121011 2121014 2121014 2021012 2021012 2021014 2021014 1021002 1021002 1021011 1021011 1021013 1021013 // 3121001 3121002 3121003 3121007 3121008 3121011 3121012 3121013 3121014 3121015`

## Match summary

- Developed Firethorn and Lava Beacon Snake early, then learned Fireball.
- Water repeatedly defended Fireball with Ice Barrier and later combined Ice Dispel plus Ice Barrier against enhanced spells.
- Established independent resources through Flame Mask, Phoenix Feather, two Academy Tutors, Hearth, Lava Golem, and fire units. This kept B functional through repeated hero freeze and defensive overexertion.
- Learned Passionate Fire and Flame Ward for offensive pressure, then Flame Backlash for the decisive defensive burn plan.
- Used Flame Backlash plus Fireball as a 6-power defense four times. Each successful defense preserved a unit and applied burn 1 to the opposing hero. Repeated end-turn burn reduced the water hero from 6 to 0 despite almost every offensive spell being defended.
- At 1 opposing life, equipped Fire Arrow as a next-turn direct-damage threat. The final Flame Backlash burn ended the game first.

## What worked

- Independent resource bodies were the main reason the deck survived long freeze chains. The hero was often horizontal, but tutors, mask, hearth, golem, and snake continued paying costs.
- Flame Backlash plus Fireball exactly matched the water deck's common power-6 attacks after two Raincaller auras. The burn rider converted defense into the actual win condition.
- Zero-cost Mana Enhancer turns let B spend resources on board or equipment while still forcing a spell defense.
- Fire Arrow's direct-damage threat forced a lethal clock even though it entered horizontal and could not be used immediately.
- Fast Slayer removed a 1-life Ice Wolf after the copied/offensive spell line was defended.

## What to improve

- Preserve fire payment when planning mixed/wildcard costs. Automatic payment for Slayer Warrior consumed the remaining fire on turn 14, leaving air but preventing Burn Wind.
- Equip actions use `equip`, not `use_item`; avoid losing tempo to local protocol mistakes.
- Fire Arrow's activated effect creates a target-selection pending action. Do not include `target_id` and then continue submitting main-phase actions before resolving it.
- Newly summoned Fire Spirit could not be consumed immediately because it was horizontal; an older vertical Fire Spirit was consumable and gained burn as printed.
- Against double Raincaller, unenhanced Fireball is mainly a tax on Ice Barrier, not a realistic damage source. Prioritize the defensive burn loop earlier.

## Bugs / suspicious behavior

- No confirmed gameplay bug from B's authoritative state stream.
- Zero-valued status keys continued to remain serialized after settlement, but their mechanics were consistent.
