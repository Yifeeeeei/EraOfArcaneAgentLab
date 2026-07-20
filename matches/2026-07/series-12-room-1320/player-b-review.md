# Series 12 / Room 1320 — Player B Review

## Result

- Player B: CodexB, slot 1, first player.
- Hero: 凛冬城主 水晶心.
- Result: loss; Player A won by hero kill on turn 10.
- Target: official finish by turn 8.
- Actual: the game was still live after A turn 8 and ended when B ended turn 10 with 1 life and 点燃1.
- Player B never damaged Player A's hero. Player A dealt the first hero damage on turn 2.

## Controlled deck change

The Series 11 WATER-PRESSURE list was changed in exactly one package:

- Removed: 2×生命护符.
- Added: 2×冰原狼.

The intended hypothesis was that a 3-water companion with load 2 water would be a reusable board body and a complete payment source for water defenses, reducing dependence on overexerting the 4-water hero.

The exact list passed `/api/deck/validate` at 30 main cards and 10 skills.

## Match outline

- T1: kept 南海海怪、唤雨师、寒冰爆裂卷轴、冰原狼. The first-player 2-water turn had no legal play, so B ended without development.
- T2: summoned 冰原狼 in the center front. A's free 火球术 reduced it from 2 to 1, then 火流星卷轴 pierced the front row and reduced B's hero from 6 to 4.
- T3: the wolf supplied 2 water alongside the hero's 4. 寒冰爆裂卷轴 damaged A's front line and killed the misplaced back-row 屠魔者杀手; B used the remaining 2 water to summon 掠夺者海盗. A then killed the wolf with 火球术.
- T4: hero plus pirate produced an exact mixed payment for 唤雨师 and 北海飞鱼. A cleared the pirate and flying fish with 火球术 and 焚烧.
- T5: B learned 寒冰屏障 and summoned 凛冬城术士. On A T5, the sorcerer's 2-water load paid the 1-water defense expense; 寒冰屏障 defended 火球术 with power 5 while the hero remained vertical. A's second spell killed 唤雨师.
- T6: because the hero had not been overexerted, B still had the full 4 water and summoned 冰刺堡垒. A's physical attack triggered the fortress and froze 屠魔者武士. The sorcerer again paid for 寒冰屏障 to stop 焚烧. Subsequent fire spells reduced the fortress and its repeated triggers first froze, then damaged, the warrior.
- T7: B again had 4 hero water and summoned a second 凛冬城术士. A used 火焰箭 to remove that new payment source, but the original sorcerer still paid for 寒冰屏障. A then spent two more spells to destroy 冰刺堡垒; its final triggers kept the warrior frozen and damaged it.
- T8: B again converted the preserved hero's 4 water into two 水栖狸猫. One sorcerer-paid 寒冰屏障 stopped the first spell; A needed two additional spells to clear both cats. A could not finish and instead applied 点燃1.
- T9: B used the preserved hero's 4 water to learn 霜冻射线 and summon 北海飞鱼. After the warrior reduced the fish to 1, 寒冰屏障 plus the sorcerer stopped 焚烧, and 霜冻射线 plus hero overexertion stopped 火球术. A's third spell killed the fish, after which A applied 点燃1.
- T10: B had no healing or winning line. Ending the turn resolved 点燃, reducing the hero from 1 to 0 and producing official `game_over`.

## Experiment result

The resource/payment hypothesis was strongly supported at the gameplay level:

- T5 defense used 凛冬城术士 instead of the hero.
- That preserved hero resource became 冰刺堡垒 on T6.
- The same payment pattern preserved another full hero turn, which became a second 凛冬城术士 on T7.
- It preserved another full hero turn, which became two 水栖狸猫 on T8.
- It preserved another full hero turn, which became 霜冻射线 plus 北海飞鱼 on T9.

This chain delayed the proven fire benchmark from a planned T8 finish to T10.

The deck substitution itself was only partially proven:

- 冰原狼 did provide its full 2 water on T3 and enabled 寒冰爆裂卷轴 plus a 2-cost companion in the same turn.
- The wolf was removed before B learned a defense spell, so it never personally paid a defensive overexertion cost.
- The later defensive payment proof came from the list's existing 2-water 凛冬城术士. More games are needed to measure whether the two wolves consistently increase access to this pattern.

## Strategic lessons

- A cheap defense is the best partner for a 2-water companion. 寒冰屏障 costs only 1 water to use, stops power 4, and allows the companion to overpay by 1 while preserving all 4 hero water.
- Preserving hero load is worth substantially more than the single defense action. In this match it generated four consecutive development turns that would otherwise have been empty or sharply weaker.
- Two learned defenses create a meaningful second layer. On A T9, companion-paid 寒冰屏障 stopped the first spell and hero-paid 霜冻射线 stopped the second; A needed a third spell to clear the blocker.
- The resilience improvement came at the cost of pressure. B's opening hand had no T1 play, and the only 寒冰爆裂卷轴 could not splash the enemy hero because the enemy center-front space was empty. B never dealt hero damage.
- Because mulligan is all-or-nothing, WATER-PRESSURE should strongly consider a full redraw when the opening lacks a 1-cost play or a T1 damage scroll. Keeping one good expensive scroll is not enough if the whole hand produces a blank first turn.
- The next revision should preserve the companion-paid defense package while restoring a reliable early damage or hand-smoothing axis. The current version proved durable but ceased to function as a pressure deck in this draw.

## Rules/API observations

- `寒冰屏障` plus companion overexertion correctly paid the water expense, turned only the selected companion horizontal, and kept the hero vertical.
- The horizontal companion remained unavailable during the following B turn and reset only at the end of that turn, as expected.
- `冰刺堡垒` correctly opened a mandatory pending selection whenever damaged. Selecting an unfrozen target applied 冻结1; selecting the already frozen warrior dealt 1 damage instead.
- The fortress still resolved its queued damage trigger when the incoming spell was lethal, consistent with “whenever this card takes enemy damage.”
- A back-row 屠魔者杀手 was correctly rejected as an attacker; this was expected rule enforcement, not a bug.

## Bug assessment

No new gameplay bug or card-text/implementation mismatch was observed. The main finding was a balance and sequencing result: companion-paid defense was materially stronger than hero-paid defense and pushed the match two turns beyond the target finish.
