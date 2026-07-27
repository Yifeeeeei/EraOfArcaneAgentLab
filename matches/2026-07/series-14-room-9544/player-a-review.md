# Player A Review — series-14 / room 9544

- Role: Player A
- Deck: FIRE-BURN-004
- Opponent: Water pressure/scry
- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Result: Player A win
- Final state: turn 11, `game_over`, winner 0; A hero 6 life, B hero 0 life

## Match summary

The opening hand was mulliganed in full. The replacement hand produced an early resource curve with 活泼的炉火 and 熔岩烽蛇, followed by learning 火球术. On turn 3, 梵天's ultimate plus two 火球术 casts (one copied by 速写卷轴) removed 冰原狼 and permanently raised 梵天's fire load twice. A fast 屠魔者杀手 then began contesting the front row.

The middle game was won through repeated board clearing and resource expansion. 火球术 removed several 1-life water units, while direct attacks cleared the remaining front row. Fire later learned 火焰结界, 激情之火, 烈焰反噬, and 烈焰重燃. 火焰结界 made a 火球术 apply 点燃 to 冰刺堡垒; the fortress died at the end of its owner's turn. 激情之火 had to be cast before its later fire-spell hits drew cards, and 烈焰重燃 restored enough fire to continue developing.

The finishing sequence used two 火焰箭 activations for direct hero damage, 火流星卷轴 and 火球术 to clear blockers, and two direct attacks after the opponent's front row was empty. The opponent stabilized at 1 life behind 南海海怪, but on B turn 10 A defended 幽影寒锋 with 火球术 + 烈焰反噬 (7 defense power, paid by overexerting 梵天). The successful defense applied 点燃1 to the opposing hero, which dealt the final damage at end of turn.

## Decisions that worked

- Mulliganing the weak first hand produced two independent fire sources and a viable early skill curve.
- Using 梵天's ultimate before the double-fireball turn converted both spell hits into permanent fire load, accelerating every later turn.
- Saving 速写卷轴 until after the first defense window let the copied 火球术 finish 冰原狼.
- Learning 烈焰反噬 created both a defensive answer to 幽影寒锋 and the eventual win condition against a 1-life hero.
- Casting 激情之火 before 烈焰重燃 correctly activated the draw engine; the later spell hit drew a card.
- Clearing every opposing front-row unit enabled direct attacks on the hero. A hero cannot be attacked while any opposing front-row blocker remains, even if the attacker's column is open.

## Decisions to improve

- I initially attempted to attack the opposing hero while another front-row enemy remained and received `target is not in attack range`. Future play should treat any enemy front-row unit as global protection for the hero.
- I attempted to activate a newly equipped 火焰箭 on the same turn and received `火焰箭需要竖置才能献祭`. Newly equipped cards enter horizontal, so the activation must wait until a later turn.
- Several turns floated fire because all six unit spaces were occupied. A tighter curve would avoid filling back-row slots with low-impact bodies when the hand contains higher-value resource units.
- 火焰结界 and 激情之火 with 冷却1 remain horizontal through the next own turn; planning should account for the end-turn reset-before-mark-removal order.

## Text / behavior observations

- 火焰结界 behaved consistently with its text: after being cast, 火球术 displayed increased power and applied 点燃1 on hit.
- 激情之火 did not draw from a fire spell cast before 激情之火 itself was used; after activation, a later fire-spell hit drew a card. This matched the observed runtime status `异能持续`.
- 烈焰反噬 behaved consistently with its text: a successful defense applied 点燃1 to the enemy hero, and the mark dealt damage at that hero owner's end of turn.
- 火焰箭 correctly required a vertical source, sacrificed itself, and offered all enemy units including the hero as candidates.
- No clear card-text/runtime mismatch or engine bug was found in this match.

## Next-match takeaways

- Against water, prioritize independent fire producers so defensive overexertion of 梵天 does not shut down the next turn completely.
- Preserve 烈焰反噬 when the opponent has a high-power attack spell; combining it with 火球术 exactly matched 幽影寒锋's 7 power twice.
- When the opponent is low, remove the entire front row first; direct attackers can then reach the hero regardless of column.
