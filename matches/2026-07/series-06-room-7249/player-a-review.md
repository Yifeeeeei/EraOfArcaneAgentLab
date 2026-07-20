# Series 06 / Room 7249 — Player A Review

## Result

- Identity: Codex A, actual backend slot `0`
- Opponent: Codex B, actual backend slot `1`
- First player: A
- Test commit: `05be3b6074b2d83e8b1bb83fc3c20c204ad37d5d`
- Official result: B won on turn 9; `game_over` reported `winner: 1`,
  `reason: hero_killed`
- Final public life: A 0 / B 4
- Match time: 2026-07-19 10:39:39Z–11:14:49Z, about 35m10s
- A transcript: `raw transcript (not imported)`
- A deck: `player-a-deck.txt`
- Room log:
  `raw room log (not imported)`

The requested turn-8 finish target was not met. The game nevertheless reached
an official hero-kill result on turn 9 using only legal actions.

## Controlled experiment

The mixed Series 05 bottle experiment was fully reverted:

- `瓶中闪电` (`2321006`): 1 -> 0
- `连锁闪电卷轴` (`2321009`): 1 -> 2
- All other main-deck cards and the ten-card skill pool returned unchanged to
  WIND-RUSH-003.

The exact list passed `/api/deck/validate` with 30 main cards, 10 skills, and
no extra cards.

The one new controlled variable was the learned skill line:

- A learned `气旋波` on turn 1 as usual.
- A learned `雷击` (`3321002`) on turn 2 instead of immediately learning
  `霹雳惊雷`.
- Hypothesis: without `卡琳娜`, `雷击` attacks for 1 air instead of 2; with
  `卡琳娜`, it becomes penetrating at 2 air and retains power 3, compared with
  `霹雳惊雷` at power 2.

A eventually learned `霹雳惊雷` as a third attack spell on turn 7 because B
had expanded to three reusable defense skills. That was a response to the
match state, not a change to the pre-match deck.

## Experiment outcome

The cheap `雷击` line was not an improvement in this matchup.

- Without `卡琳娜`, A's turn-3 attempt to target the back-row hero was
  correctly rejected with `target is not in spell range`, even though B's
  center-front square was empty. Non-penetrating spells cannot simply shoot
  through an empty front square to a back-row unit.
- After summoning `卡琳娜`, `雷击` correctly became penetrating and its use
  cost rose from 1 to 2 air.
- Its power 3 was better than `霹雳惊雷`'s power 2, but B's
  `玛涅斯之杖` and later `唤雨师` raised the defensive spell powers high
  enough that every defended `雷击` still failed.
- Both penetrating skills dealt the same 1 hero damage on hit. The alternate
  line improved the defense threshold, not damage per successful attack.
- Once `卡琳娜` died to a square-area `冰雹术`, `雷击` and `气旋波` lost
  penetration and could no longer pressure the protected hero; only
  `霹雳惊雷` retained direct access.

Conclusion: keep `雷击` in the pool as an efficient removal/pressure option,
but do not treat it as a replacement for printed penetration. Against a center
blocker control deck, learning `霹雳惊雷` early remains safer unless
`卡琳娜` is already established and protected.

## Match flow

- A rejected a slow opening of two `工蜂骑士`, `雷电元素`, and
  `屠魔者武士`. The replacement hand supplied `渡鸦信使`,
  `速写卷轴`, a cheap neutral body, and future pressure.
- Turn 1 used the first-player reduced hero load to learn `气旋波`.
- Turn 2 used the hero ultimate, discarding `风息奔马` and
  `雷电元素` to move B from 6 to 5 life, then learned `雷击` and summoned
  `渡鸦信使`.
- B established the exact independent-payment shell that Series 05 suggested:
  `水栖狸猫`, `北海飞鱼`, the hero, and later the staff and
  `唤雨师`. It also learned multiple separate defensive spells.
- A drew `卡琳娜` with `渡鸦信使` on turn 3. From turns 3–5, the
  `卡琳娜`-enhanced `雷击` and `气旋波` repeatedly forced two successful
  defenses but dealt no hero damage.
- `魔法蒲公英` converted a turn-4 draw into another draw and helped build
  load. `雷精灵` added resources for the planned three-threat turn.
- On turn 6, A used `速写卷轴` to copy `雷击`, then cast direct
  `雷击`. B defended both. A attempted a third `气旋波`, but payment
  failed because only 1 air and 1 light remained.
- On turn 7, a rush `屠魔者杀手` attacked the 1-life raccoon. B sacrificed
  `海豚伙伴` to prevent the fatal damage, permanently removing one payment
  source. A learned `霹雳惊雷` and forced two more defenses.
- B's turn-7 `冰雹术`, enhanced by the hero ultimate, hit A's square:
  A lost `魔法蒲公英`, the hero fell from 6 to 5, and both the hero and
  `雷精灵` received freeze 1.
- On turn 8 the same rush killer attacked again and killed the raccoon. A then
  consumed the frozen-but-vertical hero and `雷精灵`, used
  `法力增强剂A型`, and presented three penetrating spell attacks. B defended
  the first two and took the third, falling from 5 to 4.
- B's pressure conversion then ended the game quickly:
  `幽影寒锋` hit the hero for 2; `冰雹术` hit the hero for 1 and cleared
  A's remaining companions; B consumed `掠夺者海盗` plus `唤雨师`,
  summoned a rush `屠魔者杀手`, and attacked the now-exposed 1-life hero
  for the official turn-9 kill.

## Important play error

On turn 6, A had 7 air and 1 light after consuming resources. The
`速写卷轴` entry cost was generic 2, but A explicitly paid 2 air. After the
copied `雷击` and direct `雷击`, only 1 air and 1 light remained. The
attempt to pay `气旋波` with `{"气":1,"光":1}` was correctly rejected as
`not enough elements`.

The correct sequencing was to spend 1 light plus 1 air on the generic scroll
cost, preserving enough air for the third spell. B had only two learned defense
skills at that point, so this mistake likely cost A a guaranteed hero hit.

This was a player payment-allocation error, not a backend defect. Light is a
real element, not a wildcard that can satisfy an air-only use cost.

## Reusable lessons

1. An empty front square does not grant line of sight to the back row.
   Penetration is still required.
2. Preserve off-color elements for generic costs. Spend constrained air on
   air-only skill costs last.
3. Count defense skills and independent payment sources separately. A
   three-spell turn is not a breakthrough once the opponent has three defense
   skills and enough sources to pay all of them.
4. Printed penetration is more robust than aura-granted penetration. Removing
   `卡琳娜` simultaneously cuts access and changes costs for multiple spells.
5. Freeze and stun have distinct payment consequences:
   - a vertical unit with freeze 1 can still consume normally;
   - if it becomes horizontal, freeze prevents its end-turn reset, then the
     freeze mark is removed;
   - the unit remains horizontal for the next turn and resets only at the end
     of that later owner turn;
   - by contrast, Series 05 confirmed that a stunned vertical unit cannot be
     overexerted.
6. A repeatable attack-2 penetrating spell materially changes the control
   deck's clock. `幽影寒锋` supplied the win condition missing from B's
   Series 05 list.

## Bug assessment

No new high-confidence bug was found.

- `雷击` range, `卡琳娜` penetration/cost modification, defense power, and
  hero damage matched the exposed card state.
- The failed mixed light/air payment was correct.
- Freeze consumption and cleanup behaved consistently with the documented
  phase order.
- Both `连锁闪电卷轴` copies were drawn late but never played, so known issue
  #110 was not exercised or duplicated.
- Issue #109 was avoided.
- The final `game_over` and final `state_sync` agreed on winner 1, turn 9,
  reason `hero_killed`, and final life A0/B4.
