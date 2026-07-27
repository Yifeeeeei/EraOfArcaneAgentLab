# Player A Review — series-19 room 3718

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Deck: `WIND-RUSH-005`
- Opponent: `WATER-PRESSURE-SCRY-001`
- Result: loss, winner player 1, turn 12
- Transcript: `player-a.jsonl`

## Match summary

Wind removed Water's opening `屠魔者杀手` with `工蜂骑士`, used its hero ultimate for one direct damage, and later searched a second `连锁闪电卷轴`. Water established `玛涅斯之杖`, repeatedly attacked with enhanced `冰霜利刃` and `幽影寒锋`, and built a wide board containing two `南海海怪`.

Wind spent most hero output on defense to preserve low-life companions. This delayed removal but left too little proactive resource. The first `连锁闪电卷轴` killed a one-life cat, while a later `速写卷轴` copied `雷击` but produced no attack after target resolution. Water eventually cleared every Wind companion and used the center-front sea monster to attack the hero from 3 to 0 over three turns.

## Decisions that worked

- `工蜂骑士` traded into Water's opening neutral killer before it could create repeated pressure.
- The hero ultimate correctly used two otherwise low-value Air cards and dealt one direct hero damage.
- `引雷` discarded `巫师的学徒` and stunned the first sea monster, buying a full attack cycle.
- Repeated defense combinations hit exact thresholds: `雷击 + 静电脉冲` reached six, and adding `气旋波` reached seven.
- The first `连锁闪电卷轴` killed a one-life Water unit and searched the second copy, preserving a future damage source.
- A late `屠魔者杀手` blocked the center lane for a turn and damaged the center sea monster before dying.

## Decisions to improve

- Turn 1 incorrectly attached a payment to `learn_skill`, consuming more resources than intended. Fixed-color skill learning should omit `payment`.
- Too much hero output was spent protecting one- or two-life companions. Water could immediately follow one enhanced spell with another, so the saved unit often died in the same turn anyway.
- `"风刃" 卡琳娜` increased the use cost of targeted Air skills. This made defensive packages more expensive and did not generate enough offense before she died.
- The first `连锁闪电卷轴` killed a disposable cat rather than reducing a sea monster. The cat kill was efficient, but it did not weaken Water's actual hero-damage engine.
- After losing the second real attacker, Wind had no reliable path through Water's full front line. Future play should reserve resources for a second scroll or attacker instead of defending every support companion.
- Several end-turn attempts raced with discard pending actions. Verify `phase: main` and resolve `discard` before assuming the turn changed.

## Reusable strategy updates

1. Against Water spell pressure, assume two attacks in a turn; do not spend the full hero output saving a one-life unit from the first one unless that unit creates immediate lethal pressure.
2. Preserve center-front attackers and scroll resources as hero-damage routes. Support companions are expendable when defending them prevents the next proactive turn.
3. `引雷` is a useful tempo play against sea monsters, but its two-stage pending flow is discard first, enemy target second.
4. When `"风刃" 卡琳娜` is active, recalculate every targeted Air skill expense before committing to a defensive package.
5. Fixed-color `learn_skill` actions should not include explicit payment; the server handles the learning cost.

## Product / bug observations

### Sketch Scroll can silently consume a copied horizontal spell

On turn 9, Wind paid for `速写卷轴`, selected the already learned but horizontal `雷击`, then selected the only offered target, `南海海怪` `ci_55`. The `sketch_scroll_target` pending action cleared, but no defense window opened, no error was returned, and the target remained at four life. Retrying the target produced `no pending action`.

The item was spent despite producing no spell effect. If copying a horizontal learned spell is illegal, it should not be offered as a candidate or should return an error without consuming the scroll. If the scroll's printed “无需消耗该法术” is intended to allow it, the copied attack should proceed normally.

### Target behavior differed from the earlier hero-target observation

In this board state, `速写卷轴` copying `雷击` offered only the opposing right-front sea monster; the enemy hero was not a candidate. This means the prior copied-spell hero targeting behavior is at least board/range dependent rather than universally exposed.

No confirmed card-text-versus-runtime mismatch beyond the silent Sketch Scroll resolution was found in this match.
