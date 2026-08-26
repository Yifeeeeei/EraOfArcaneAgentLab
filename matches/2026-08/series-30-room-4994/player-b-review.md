# Series 30 — Player B Review

## Result

- Commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- B: `LIGHT-GRACE-MIDRANGE-002`, slot 1, first player.
- A: `EARTH-MOBILE-BEATDOWN-003`, slot 0.
- Official result: B win on turn 21. A used the legal `surrender` action; B received `game_over` with `winner:1`, `actor:0`, `reason:surrender`.
- Final visible position: B hero 6 life with a full board; A hero 6 life. B had exhausted its deck without an automatic draw-loss. The result is a concession win, not hero lethal.

## Pre-registered metrics

### Pressure timing and physical clock

- `first_physical_attack_turn`: 2 — rapid Slayer `ci44` dealt 1 to center Xinke `ci6`.
- `first_physical_hero_damage_turn`: none.
- `first_hero_damage_any_source_turn`: none.
- Repeated the Series29 turn-4 hero-damage checkpoint: **no**.
- `physical_attacks_attempted`: 19.
- `physical_attacks_successful`: 17. The two rejected attacks were T11 right Wing attempts against an empty front square and then a mid-row Guard outside physical range.
- `physical_hero_attacks_successful`: 0.
- `physical_hero_damage`: 0.
- `own_turns_with_ready_legal_attacker`: 15 (T2 and T8–T21).
- `own_turns_converted_to_physical_attack`: 15.
- `clock_gaps`: not applicable because the first physical hero hit never occurred.

The deck maintained unit-attack cadence once it established Lundesar, but cadence was spent removing a newly supplied center blocker every turn. Winning the board and winning the game were not the same thing.

### Clear-to-hero conversion

- `clear_opportunities`: 10 meaningful center-lane clears or removals (T9, T12–T21, excluding turns where the lane remained blocked after B acted).
- `same_turn_clear_to_hero_conversions`: 0.
- `next_own_turn_conversions`: 0.
- Principal miss cause: the attacker that cleared center was already horizontal, and A placed a new center-front blocker before B's next turn.
- T15 was the cleanest planned conversion: Light Splitting killed Rock Beast and Spatial Shift moved Lundesar into center-front. A reblocked before the next B turn.
- `移形换影` uses: T6 moved Prince and enabled Lundesar deployment; T15 moved Lundesar into the cleared center lane. Neither use created an additional same-turn physical attack.

### Hidden interaction

- Giant Sandworm first took actual damage from Glory on T7: life 4→3 and authoritative Hidden 0→1.
- `moon_dust_opportunities`: 1 relevant copy while Sandworm had Hidden.
- `moon_dust_uses`: 1.
- `hidden_removed`: 1 — T7 Moon Dust resolved `remove_front_stealth`, Hidden 1→0.
- `hidden_to_attack_conversion`: none; there was no reserved ready attacker in that lane.
- Subsequent actual Sandworm damage correctly regenerated Hidden. The apparent T9 “did not stack” concern was disproved: end-of-turn settlement had already reduced Hidden to 0 before Light Blade damaged it, and the following state correctly showed Hidden 1.
- Current-build Sandworm behavior therefore produced clean positive evidence: shield-absorbed damage did not trigger Hidden; actual damage did; Moon Dust removed it; later actual damage restored it.

### Healing/growth converted into tempo

- T7 hero ultimate: paid 2 Light; Prince life 1→3 and permanent load +2. This immediately supplied the support threshold for Glory in the same turn. Count: `heal_to_bridge_within_one_own_turn = 1`.
- T8 Light Blessing on Holy Wing: +1 life/load. The grown Wing survived A's T8 physical plus two spell hits, then attacked on T9 and T10. Count: `heal_to_attack_within_one_own_turn = 1` and `heal_saved_from_lethal = yes` for the combined T8 damage sequence.
- T11 Light Blessing and T12 Life Flower grew the center Prince; T12/T13 Healing Warlock prayers repeatedly restored it. These actions delayed Rock Beast's hero attack for multiple turns but did not convert to B hero pressure.
- T14 Life Flower increased Lundesar's life; later Healing Warlock prayers restored Lundesar and allowed the repeated center-blocker clearing sequence through T21. These were defensive clock-preservation conversions, not hero-damage conversions.
- T15–T18 Healing Warlock prayer restored the hero from 2 to 6 over four turns. This changed immediate lethal math but generated no offensive conversion.
- T19 prayer healed Wing; T20 prayer healed Lundesar; T21 prayer healed a Guard. These were nonconverting sustain actions within the registered window.
- Qualitative total: 14 successful heal/growth resolutions, no rejected legal heal. The only immediate offensive bridge was the T7 ultimate→Glory line; the strongest attack conversion was T8 Blessing→Wing attacks.

## Exact B damage ledger

Physical damage:

- T2 rapid Slayer → center Xinke: 1.
- T8 rapid Slayer → Sandworm: 1.
- T9 Holy Wing → center Xinke: 1 lethal.
- T10 right Holy Wing → right Xinke: 1 lethal; center Holy Wing → Rock Beast: 1.
- T11 Lundesar → Sandworm: 2 lethal.
- T12/T13 Lundesar → newly placed ordinary Lizard: 2 lethal each turn.
- T14/T15 Lundesar → left Warrior: 2, then 2 lethal.
- T16 Lundesar → center Spike Ball: 2 lethal; right Wing → right Warrior: 1.
- T17 Lundesar → center Squirrel: 2 lethal.
- T18 Lundesar → second Rock Beast: 2.
- T19 Lundesar → center Scavenger: 2.
- T20/T21 Lundesar → rapid Slayer: lethal each turn (2 attack into 1 life).

Spell/item damage:

- T4 Light Blade: no life damage; A's shield absorbed the event.
- T7 Glory → Sandworm: 1 actual damage.
- T9 Light Blade front-row AoE: 1 to Sandworm and 1 to right Xinke.
- T14 Light Splitting: no life damage because shield 2 absorbed it; Moonlight then dealt 1 to Rock Beast.
- T15 Light Splitting → Rock Beast: 2 lethal.
- T16 Punishment Arrow → right Warrior: 1; Light Splitting then dealt 2 lethal.
- T17 Light Splitting → Emerald Guard: 2; Moonlight then dealt 1 lethal.
- T18 Light Splitting → second Rock Beast: 2 lethal.
- T19 Light Splitting → Scavenger at 1 life: lethal.
- Enemy hero damage from every B source: 0.

## Driver/API observations

- T8 I sent malformed payloads: nested `position` instead of top-level `col`/`row` for summon, then unsupported `target_id` instead of `target_col`/`target_row` for attack. Defaults placed the Slayer at left-front and attacked `(0,0)` Sandworm. This is a pilot error and an independent API-validation weakness, not an in-game redirect bug.
- Other rejected actions were legal validation outcomes: attacking a non-front unit outside range, targeting the hero with Light Splitting, targeting a right-back Guard outside spell range, using a newly learned horizontal skill, and replacing horizontal equipment.
- No unresolved soft lock or turn-flow blocker occurred. Private discard and prayer pending actions were visible and resolvable.

## Conclusion

The unchanged Light deck won the official result and showed excellent sustain, blocker removal, and current-build Hidden correctness. It failed the pressure hypothesis: no B source ever damaged the enemy hero, despite 17 successful physical attacks and repeated center clears. The strongest lesson for the next iteration is to reserve a second ready attacker for the clear turn, or add a legal hero-reaching payoff; otherwise Light's healing engine converts resources into board dominance and survival rather than a closing clock.
