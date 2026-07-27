# Player A Review — series-15 / room 3951

- Role: Player A
- Deck: WATER-PRESSURE-SCRY-001
- Opponent: FIRE-BURN-004
- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Result: Player B win
- Final state: turn 15, `game_over`, winner 1; A hero 0 life, B hero 4 life

## Match summary

A kept an opening containing 冰原狼 and 海豚伙伴 and established both on turn 1. The early turns added 寒霜傀儡, 凛冬城术士, and 唤雨师 while learning 水占术, 冰锥术, 寒冰屏障, and 冰封消解. 寒冰屏障 repeatedly protected 1-life units from 火球术, while 冰封消解 reduced several amplified fire spells to 0 power before a defense was committed.

The strongest A turn used two 寒冰爆裂卷轴 around the opposing center column. The two casts removed 火荆 and 熔岩烽蛇, damaged and heavily froze 屠魔者武士 and 梵天, and later 冰锥术 finished the warrior. 水占术 repeatedly found high-value water cards, including two 唤雨师, 冰刺堡垒, 南海海怪, and 水形之束卷轴. The two rain callers raised 寒冰屏障 to 6 power and the offensive spells by 2 power.

The late game stalled because A's six field slots were filled mostly with non-attacking resource/support units. A could defend consistently and remove one small attacker per turn, but could not pressure the opposing hero. B repeatedly defended 霜冻射线 with 烈焰反噬 plus 火球术, applying 点燃 to A's hero after each successful defense. A fell from 6 life to 0 over several own end-of-turn mark settlements. On A turn 14, the same defense package stopped 霜冻射线 and applied the final 点燃; after A discarded to hand limit, the mark reduced the 1-life hero to 0.

## Decisions that worked

- Keeping the resource-heavy opener produced a stable water economy immediately.
- Learning 寒冰屏障 early prevented multiple 火球术 hits and protected the 1-life 冰原狼 for many turns.
- Pairing 冰封消解 with 寒冰屏障 efficiently stopped high-power, piercing, or burn-enhanced attacks.
- 水占术 consistently selected useful water cards rather than the non-water potion candidate.
- Double 唤雨师 made both defense and offense substantially stronger and forced B to spend two skills to match 6 power.
- Two 寒冰爆裂卷轴 generated the largest tempo swing of the game and correctly hit the hero behind the center target via splash.

## Decisions to improve

- The board was filled too early with six support/resource units, leaving no room to deploy 南海海怪 or later defensive bodies without first losing a unit.
- A should have preserved at least one attacking unit or opened a front-row slot earlier. High spell power only determines the defense contest; most water spells still dealt 1 attack damage, so board removal was too slow.
- Several attempts to use 水占术 one turn after casting it were correctly rejected because 冷却1 prevents the next end-turn reset. Future turns should track the reset-before-mark-removal order explicitly.
- 凛冬城术士's ultimate is once per game. A second activation attempt was correctly rejected and should not be repeated.
- Repeatedly leading with 霜冻射线 let B answer with the exact 6-power 烈焰反噬 + 火球术 package and convert defense into hero burn. Once this pattern was known, A needed a different plan instead of feeding the same defense trigger each turn.
- Hand growth from 水占术 repeatedly forced end-turn discards. Some searches were still card-quality positive, but the plan needed faster deployment or fewer searches once the field was full.

## Text / behavior observations

- 冰封消解 behaved consistently with its text: reaction use changed the pending spell's main power source to 0, after which a normal defense prevented the hit.
- 寒冰屏障 received +1 power from each 唤雨师, reaching 6 with two copies in play.
- 水占术 correctly exposed only four top-card candidates, allowed selection only of water cards, and enforced 冷却1 across the following own turn.
- 寒冰爆裂卷轴 applied splash damage/freeze to the center target and hero behind it, while diagonal back-row units were not damaged.
- 烈焰反噬 consistently applied 点燃 after a successful defense; marks settled at the affected hero owner's end of turn after discard handling.
- No clear card-text/runtime mismatch or engine bug was found from Player A's observations.

## Next-match takeaways

- Water should reserve a field slot for a real attacker or late-game sea monster instead of filling all six spaces with support bodies.
- Against fire, early 冰封消解 + 寒冰屏障 is excellent, but avoiding damage is not a win condition; pair control with a concrete hero-pressure plan.
- Once the opponent shows 烈焰反噬, do not repeatedly offer exactly defendable 6-power attacks while the water hero is within burn range.
