# Series31 Player A Review

- Game commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Room: `2835`
- Player: `official-series31-a` / `OfficialA31`
- Deck: `ROYAL-MIST-GRAVE-CLOCK-002`
- Result: loss; Player A surrendered on own T9, official `game_over` reason `surrender`, winner Player B.
- Final visible hero life: A 4, B 6.

## Result summary

002 did not solve 001's central failure. It produced one real physical attack, but no physical hero damage. The two added Arcane Bombs were useful early interaction, yet the draw sequence exposed a severe bridge problem: after the only Rapid Slayer died, the hand was dominated by explicit Dark costs, Water 5/6 costs, and zero-attack grave pieces while the hero supplied only 4 Water. Player A completed several consecutive turns without a legal clock-producing play and surrendered from an empty board against Player B's full board.

The surrender was strategic rather than time-saving: A had 4 life, no field units, no learned skills, no attack-capable playable card, and a hand whose explicit Dark or Water-6 breakpoints could not be paid by the available hero. B had three front blockers, a protected rear attacker, Water Magister, Fog Spirit, and an established skill engine.

## Exact damage ledger

### Damage dealt by Player A

1. T2 Arcane Bomb `ci_154` targeted Rapid Slayer `ci_85`. Dolphin `ci_92` was sacrificed to prevent the lethal damage; Slayer stayed at 1 life. This forced a public defensive resource but dealt no lasting unit or hero damage.
2. T3 Arcane Bomb `ci_155` targeted and killed Rapid Slayer `ci_85` (1 life to graveyard).
3. T5 Rapid Slayer `ci_150` made Player A's only physical attack and dealt exactly 1 damage to Frost Golem `ci_93` (2 to 1). A direct-hero attempt was rejected because a front unit remained in attack range.
4. Player A dealt **0 physical hero damage** and **0 total hero damage**. Player B hero remained at 6.

### Damage received by Player A

1. B T1 Rapid Slayer `ci_85` physical direct attack: A hero 6 to 5.
2. B T2 Rapid Slayer `ci_85` physical direct attack: A hero 5 to 4.
3. B T4 Six-Petal Snowflake froze Ice Wolf `ci_129`; Sophia's ultimate removed the freeze and dealt exactly 2, killing the wolf.
4. B T5 Ice Cone killed Rapid Slayer `ci_150`.
5. B T8 Ripple Slash killed Mist Dancer `ci_137`.

## Preregistered metrics

| Metric | Target | Result | Verdict |
|---|---:|---:|---|
| First physical attack | by T2 | T5 | Fail |
| First physical hero damage | by T5 | Never | Fail |
| Total physical hero damage | at least 4 | 0 | Fail |
| Attack cadence after T1 | at least 75% | 1/7 completed own turns T2-T8 = 14.3%; 1/8 if surrender turn T9 is included = 12.5% | Fail |
| Generic proactive actions before T6 | at least 2 | 2 Arcane Bombs on T2/T3 | Pass |
| Off-color stranded before T6 | 0 | 0 before T6; first explicit-Dark strand occurred T6 | Pass narrowly, structural warning |
| Bomb/Tide side-front or center-opening impact | at least 1 | Bomb 1 forced Dolphin sacrifice; Bomb 2 killed center-front Slayer | Pass via Bomb |
| Spatial Shift creates genuine attack | at least 1 | Not learned/used | Fail |
| Center replacement within one own turn | at least 1 | T5 Rapid Slayer immediately occupied center after prior blocker loss, but did not replace a same-turn cleared center lane | Fail under strict definition |
| Grave value replacing a legal attack | target 0 | 0 | Pass, but mostly because grave engine was unplayable |

## Breakpoints and resource evidence

- Generic 3: paid twice for Arcane Bomb and once for Rapid Slayer. This was the only reliable proactive breakpoint.
- Generic 4: not exercised by a relevant clock card.
- Water 5: Pirate Ship required Water 4 + Dark 1, so hero Water 4 could not bridge it. South Sea Monster at Water 5 was also one short.
- Water 6: Wendy remained stranded. Hero 4 plus Mist Dancer's Water 1 still produced only 5 Water; the Dancer's Air did not satisfy Water.
- Water 4 + Dark 1: failed exactly as written. An attempted Cannon payment using 2 Water was correctly rejected `not enough elements`, confirming explicit Dark could not be substituted.
- The first off-color hard stop was T6. It continued through T9 despite discarding Black Pine Coffin and a duplicate Pirate Ship to cycle future draws.

## Turn cadence

- T1: full mulligan had removed four non-attackers, but replacement hand still contained no attacker; reduced first-player hero supply gave only 2 Water. No attack.
- T2: Arcane Bomb forced Dolphin sacrifice. No attack-capable unit.
- T3: second Arcane Bomb killed center-front Rapid Slayer. No attack-capable unit.
- T4: summoned Ice Wolf as a blocker. No attack-capable unit.
- T5: drew, summoned, and attacked with Rapid Slayer; 1 physical damage to Frost Golem.
- T6: explicit Dark and high-Water hand stranded; no legal proactive clock.
- T7: summoned Mist Dancer and gave it Hidden 2; no attack.
- T8: no legal play; discarded duplicate Pirate Ship at cleanup.
- T9: drew South Sea Monster at Water 5, still unpayable from hero Water 4; strategically surrendered.

## 002 versus 001

Improvement:

- Physical attacks increased from 0 in the cited 001 match to 1.
- Arcane Bomb gave two meaningful, independently payable early interactions and prevented B's Rapid Slayer from continuing its direct clock.
- The added neutral Rapid Slayer was genuinely playable from hero-only resources and attacked on its summon turn.

Not improved enough:

- Physical hero damage remained 0, exactly the failure 002 was designed to repair.
- The attack density was still too low: only one of the added four neutral attackers appeared by T9, and the full mulligan replacement hand again had no attacker.
- Cutting grave-value cards by only one copy each left too many zero-attack or explicit-Dark cards together: Cannon, Hunter, Bone Knight, and Coffin/ships created hands that the Water-only hero could not deploy.
- The package had no dependable Water-only bridge at 4 or less that generated Dark while also advancing an attack lane. Mist Dancer generated Water/Air, not Dark, and therefore did not unlock Cannon, Bone Knight, Hunter, or Pirate Ship.
- Raider Tide and Spatial Shift were not reached, so the proposed side-clear/movement bridge never became operational.

## Learning and next iteration

The next revision should treat hero-only Water 4 as the baseline opening economy and require a much higher density of cards that either attack immediately for generic 3/4 or create Dark while costing no explicit Dark. The draw should not need a specific Water pirate before half the hand becomes playable. At minimum, remove more zero-attack grave pieces and reduce the Water 5/6 top end until repeated matches show a stable attacker by T2-T3. Arcane Bomb is worth retaining as interaction, but it is removal rather than a clock and must not be counted as a substitute for attack density.

No gameplay bug was identified. Rejected payments and attack targets matched the documented rules; the failure was deck construction and sequencing, not engine behavior.
