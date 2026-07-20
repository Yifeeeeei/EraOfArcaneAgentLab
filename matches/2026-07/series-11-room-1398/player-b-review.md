# Series 11 / Room 1398 — Player B Review

## Result

- Player B: CodexB, slot 1, first player.
- Hero: 凛冬城主 水晶心.
- Deck: WATER-PRESSURE benchmark with both 屠魔者武士 replaced by two 生命护符.
- Result: loss; Player A won on turn 8 by hero kill.
- Benchmark timing: first hero damage on turn 1; official `game_over` on turn 8. Both timing goals were met.

## Match outline

- T1: kept the full opening hand because 海豚伙伴 and 水形之束卷轴 gave an independent early line. Consumed the hero for the first-player-adjusted 2 water, then 水形之束卷轴 hit the exposed enemy hero for 1.
- T2: developed 海豚伙伴 and 凛冬城术士.
- T3: activated 凛冬城术士, then 寒冰爆裂卷轴 killed both 火焰精灵, damaged the enemy hero, and stacked two freeze marks on 梵天. Added 水栖狸猫 as a front blocker.
- T4: the second 寒冰爆裂卷轴 hit 屠魔者武士 and the enemy hero. Added 北海飞鱼 as the next blocker.
- T5: used all 6 generated water to summon 唤雨师 and equip 生命护符. The amulet's pending target selection resolved on the hero, raising B from 3 life to 4.
- T6: summoned the second 唤雨师 and learned 霜冻射线. The first 唤雨师 correctly could not make a normal attack because it has no attack value.
- A T6 and A T7: 霜冻射线 plus hero overexertion successfully defended two separate 火球术 casts. With one 唤雨师 alive, defense power was 5 against power 3.
- T7 and T8: overexerting the hero during the opponent's turn left it horizontal during the following B turn. This prevented the 5-water 南海海怪 line on T7 and left both the hero and 霜冻射线 unavailable at the start of T8.
- A T8: two physical attacks reduced B from 3 to 1. B defended the first 火球术 with 霜冻射线 plus hero overexertion; after 速写卷轴 copied the already-horizontal 火球术, B had no second defense and lost 1 to 0.

## What worked

- The pressure shell met its speed target even without 屠魔者武士: T1 first damage and three total early hero hits by the end of B T4.
- The two 寒冰爆裂卷轴 produced both pressure and board control. Splash damage plus freeze delayed 梵天 and cleared the two free 火焰精灵 without relying on the excluded 锻石工匠 interaction.
- 生命护符 materially improved resilience. Its printed enter effect, payment, equipment placement, pending target selection, and +1 life result all matched the observed implementation.
- 霜冻射线 was a high-value defensive learn. It stopped three lethal or blocker-clearing fireballs across A T6, A T7, and A T8.
- The fair 熔岩傀儡 replacement behaved as an ordinary independent resource source; no unexplained bonus power or stuck pending action appeared.

## Strategic lessons

- Against repeatable 1-damage fire spells, one defensive skill is not enough when 速写卷轴 can copy a horizontal learned spell without consuming it. A second defense source or a counter-reaction is required for the same window sequence.
- Hero overexertion is powerful but creates a real next-turn tempo cost. Here it repeatedly removed 4 water from the following B turn, delaying 南海海怪 and preventing pressure from converting into a finish.
- 生命护符 bought exactly one additional life and forced A to use the copied fireball for the official kill. The resilience swap therefore worked, but it did not solve the lack of a second defensive source.
- After the two opening scrolls were spent, the deck had no reliable way to convert its board into hero damage because the utility companions had no attack. Future pressure revisions should keep the early scroll package but add a second damage axis that does not depend on drawing another scroll.
- Freeze stacking was valuable: 寒冰爆裂 plus 凛冬城术士 put 梵天 at freeze 2 and delayed its reset for multiple turns. This is a dependable tempo line worth preserving.

## Rules/API observations

- Equipment must use `equip`, not `use_item`; attempting `use_item` on 生命护符 was correctly rejected with `equipment cannot be used as a consumable item`.
- 生命护符 correctly opened a `life_amulet_buff` pending action and required `resolve_action` with the selected friendly unit instance.
- A companion with no attack value was correctly rejected as an attacker with `attacker has no attack`.
- Defensive overexertion paid the skill expense, turned the chosen hero horizontal, did not grant reusable elements, and persisted until the end of B's next turn.
- 速写卷轴 correctly selected and copied an already-horizontal learned 火球术, opened a fresh defense window, and left the original skill horizontal.

## Bug assessment

No new gameplay bug or clear card-text/implementation mismatch was observed. The two rejected actions above were expected rule enforcement, and all tested printed effects behaved consistently with their card text.
