# Series32 Player A Review

- Game commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Room: `5128`
- Player: `official-series32-a` / `OfficialA32`
- Deck: `MONO-FIRE-FORWARD-CLOCK-001`
- Result: loss; Player A strategically surrendered during own T12.
- Official result: `game_over`, reason `surrender`, winner Player B.
- Final hero life: A 4, B 5.

## Outcome

The mono-Fire payment redesign worked, but the clock did not. Player A never had a colored-payment failure, attacked on seven turns, and repeatedly reached six to nine usable Fire. However, only one point reached the enemy hero: Fire Arrow on T8. Player B's global front-row interception, rapid replacement blockers, two independent spell defenses, and protected rear attacker converted A's actions into blocker removal rather than a win.

The T12 surrender was strategic. A had no attacker, both Fire Boxes were exhausted, B still had a 3-life South Sea Monster in front plus a rear Archer, and B had demonstrated two refreshed defenses each A turn. A had 4 life and no credible two-turn lethal line.

## Exact hero-damage ledger

### Player A to Player B

- T8 Fire Arrow `ci_231`, sacrificed through its active ability: 1 direct item damage, B hero 6 to 5.
- Physical hero damage: 0.
- Spell hero damage: 0; ordinary attack spells could not target the hero.
- Burn/status hero damage: 0.
- **Total hero damage: 1.**

### Player B to Player A

- B T11 South Sea Monster physical attack: 1.
- B T11 protected rear Winter Archer physical attack: 1.
- A hero 6 to 4; no other hero damage before surrender.

## Physical attack ledger

1. T2 Slayer Warrior `ci_216` attacked Winter Archer `ci_190`; Dolphin prevention saved the Archer.
2. T3 the same Warrior attacked again and killed the Archer.
3. T4 Warrior attacked Wendy `ci_178`, 3 to 2.
4. T5 Fire Meteor killed the right-front blocker, Fireball reduced Wendy to 1, then Warrior killed Wendy. This was the clean bridge-plus-physical-attack turn.
5. T6 Warrior dealt 1 to Frost Elephant after Burn Scroll and Fireball.
6. T8 Lava Fort Chariot `ci_226` dealt 1 to Wendy `ci_179` and applied Burn 1; Fireball plus end-step Burn killed her.
7. T9 Rapid Slayer `ci_214` dealt 1 to the right-front Slayer Warrior after the first spell was defended and Fireball landed.

No physical attack reached the enemy hero. Player B killed each center attacker before it could exploit the next open board: Warrior on B T7, Chariot on B T9, Rapid Slayer on B T10, and the 5-life Behemoth on B T12.

## Preregistered metrics

| Metric | Target | Result | Verdict |
|---|---:|---:|---|
| First legal physical attack | by T2 | T2 | Pass |
| First hero damage | by T5 | T8, Fire Arrow | Fail |
| Total hero damage by T8 | at least 4 | 1 | Fail |
| Physical attacks by T6 | at least 3 | 5 | Pass |
| Attack cadence after T1 | at least 67% | 7/10 completed turns T2-T11 = 70%; 7/11 if surrender turn T12 is included = 63.6% | Pass on completed-turn definition; fail including T12 |
| Bridge plus physical attack in one turn | at least 1 | T5 | Pass |
| Independently supplied Fire 6 by T6 | by T6 or explain | 7 usable Fire on T3; exact Fire 6 Behemoth payment on T11 | Pass resource capability, late top-end use |
| Colored-payment rejections | 0 | 0 | Pass |
| Attack card stranded solely by color | 0 | 0 | Pass |
| Clear victory line by T10 | yes | none | Fail |
| Official game over by T12 target | win target | official surrender during A T12 | Fail |

There were three harmless protocol/pilot errors unrelated to payment: `play_item` and `use_item` were tried on an equipment before the correct `equip` action, and legacy `cast_skill` was tried before the correct `cast_spell`. No gameplay state was changed by those rejected actions.

## Payment and engine findings

- Mono-Fire solved Series31's structural color lock. Generic 3/4, Fire 1-6, Fire Box, and all learned spell expenses were repeatedly payable.
- T2 generated 6 Fire from hero plus two Fire Spirits and deployed Furnace plus both Fire Boxes after the attack.
- T3 generated 7 Fire from hero, Box, and Furnace, then paid Snake plus Rally Horn. Rally Horn found Chariot and Lava Golem.
- T11 generated 9 Fire from hero, both Boxes, and Furnace; after two spell expenses, exactly 6 remained for Volcano Valley Behemoth.
- Fire Boxes were excellent burst resources but finite. Both were exhausted by T12, while Player B's Water Aria and Water Mage formed renewable resources/reset.
- Passion of Fire was activated but did not convert enough spell hits into attackers soon enough.

## Why the victory line failed

The deck could pay actions but still had too few actions that reduce hero life through a blocker. Global front-row interception meant a blocker in any lane stopped physical hero attacks. A repeatedly spent two spells plus one attack merely removing the current front unit, after which the attacker was horizontal and Player B rebuilt before the next turn.

The clock bodies were also too sparse relative to support:

- Full mulligan replacement was two Fire Boxes and two Fire Spirits; the T1 draw found a Warrior.
- After the first Warrior died, Chariot required a setup turn and died before its second attack.
- Rapid Slayer attacked once and died.
- Behemoth was paid cleanly but entered horizontal and was killed exactly by two Ice Blades plus three physical attacks before acting.
- T10 and T12 hands again contained only support/removal, not a ready attacker.

Player B's defense package was stronger than the planned two-spell sequencing assumption. On several turns it defended All Fires Unite with a main defense plus Snowflake boost and overexertion, then either accepted Fireball or used a second independent defense. Spending five-power spells to force overexertion created tempo but no hero clock.

## Iteration conclusion

Keep the mono-color payment principle, Fire Box, Fire Arrow, Rapid Slayer, and the demonstrated T5 bridge sequencing. Cut a meaningful portion of zero-attack support and slow top-end. The next aggressive list needs either more Rapid attackers, additional direct-any-enemy damage, or effects that remove/move a front blocker without consuming the only ready attacker. Rally Horn finding support-quality Fire companions is not enough; its hits must themselves become immediate clocks.

No gameplay bug was observed. Front-row interception, spell defense, payment, Fire Arrow targeting, Burn settlement, Water Mage reset, and official surrender all matched authoritative state.
