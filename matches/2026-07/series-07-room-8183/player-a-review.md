# Series 07 / Room 8183 — Player A Review

## Result

- Identity: CodexA, actual backend slot `0`
- Opponent: CodexB, actual backend slot `1`
- First player: A
- Deck: `WIND-RUSH-003`, unchanged from Series 06
- Test commit: `05be3b6074b2d83e8b1bb83fc3c20c204ad37d5d`
- Official result: B won on turn 6
- `game_over`: `winner=1`, `reason="hero_killed"`
- Final public life: A `-1` / B `2`
- Match time: 2026-07-19 11:20:55Z–11:38:20Z, about 17m24s
- A transcript: `raw transcript (not imported)`
- A deck: `player-a-deck.txt`
- Room log:
  `raw room log (not imported)`

The requested official finish by turn 10 was reached, but A lost the race.

## Controlled experiment

Series 07 made no deck change. The requested strategic correction was instead
tested directly:

- restore `霹雳惊雷` as the first learned attack skill;
- use its printed penetration to keep attacking the protected back-row hero;
- preserve off-color elements when wildcard or generic costs allow a choice;
- race aggressively rather than switching to the cheaper but
  penetration-dependent `雷击` line from Series 06.

The first two points worked. A learned `霹雳惊雷` on turn 1 and hit B's hero
on turns 2, 3, and 4. No ambiguous wildcard payment arose in this match, so the
off-color preservation rule was not exercised.

## Match flow

### Opening and turns 1–2

A rejected a slow initial hand. The replacement hand included
`魔法蒲公英`, `风魔`, `工蜂骑士`, and `风息奔马`.

- Turn 1 used the first-player reduced hero load to learn `霹雳惊雷`.
- Turn 2 used the hero ultimate, discarding `风魔` and `工蜂骑士`, to deal
  1 damage to B's hero.
- A then consumed the hero, summoned `魔法蒲公英`, learned `气旋波`, and
  cast `霹雳惊雷`.
- B did not defend, so the ultimate plus spell reduced B from 6 to 4.

The opening `魔法蒲公英` also drew a card when summoned even though it had
entered the hand during the mulligan and was not drawn that turn. This became
the first sign of the confirmed mismatch described below.

### Turn 3

A again consumed the hero and cast `霹雳惊雷`. B declined defense and fell
from 4 to 3.

The remaining 2 air summoned `雷傀儡` in the center front. This was a sound
defensive conversion: it survived multiple square attacks and forced B to
attack through a body rather than leaving the one-life `魔法蒲公英` as the
only screen.

B activated the hero ultimate, then used staff-enhanced `冰雹术` on the
center square. A had no useful defense payment and declined. The spell damaged
both `雷傀儡` and A's hero and applied `冻结1`.

### Turn 4

Although frozen, A's hero was still vertical and could be consumed. A used
the resulting 4 air as follows:

- `霹雳惊雷` hit B's hero from 3 to 2.
- A summoned the second `魔法蒲公英`.
- The remaining air cast `气旋波` at `海豚伙伴`.

B defended the cyclone with `冰霜利刃`, overexerting
`玛涅斯之杖` to pay. The dolphin survived.

The second dandelion was drawn on A turn 3 but summoned on A turn 4. It still
drew `连锁闪电卷轴` on entry. This is the clean cross-turn reproduction of
the card-text mismatch.

At the end of A's turn, the hero's `冻结1` prevented the already-horizontal
hero from resetting. B's next square `冰雹术` reduced A to 3 life and the
golem to 1 life.

### Turns 5–6

A turn 5 was effectively blank: the hero was still horizontal, the field had
no other resource-producing vertical card, and A had zero elements. Ending
the turn finally reset the hero.

B turn 5 used `幽影寒锋` at power 7. A could not assemble remotely enough
defense power, so its 2 attack damage reduced A from 3 to 1. B then consumed
the staff and cast `冰雹术` at the center square. A overexerted the hero to
pay for `霹雳惊雷` as a power-2 defense and survived.

That emergency defense left both the hero and `霹雳惊雷` horizontal for A
turn 6. A again had no elements and no legal pressure, so it ended the turn.
B consumed the hero and cast `幽影寒锋` a second time. A declined the
impossible power-7 defense, and the backend produced the official
`game_over`.

## Strategic conclusions

Restoring early `霹雳惊雷` was correct. It produced three consecutive hero
hits and moved B from 6 to 2 by turn 4 when combined with the hero ultimate.
Unlike the Series 06 `雷击` plan, it did not depend on drawing or protecting
`卡琳娜` to reach the back row.

The loss came from resource-source fragility rather than failure to find
damage:

- Almost all early actions depended on consuming the hero for 4 air.
- B's turn-3 freeze converted one successful `冰雹术` into a completely
  blank A turn 5.
- The emergency defense on B turn 5 required overexerting the hero, producing
  another completely blank A turn 6.
- B could therefore survive at 2 life and take two consecutive effective
  turns while A could not cast its penetrating finisher.

A turn 4 had a meaningful alternative: summon `雷精灵` for 2 air instead of
the dandelion-plus-cyclone line. The chosen line forced one defense payment
and tested the dandelion text, but `雷精灵` would have survived the next
one-damage square hit and provided an independent air/light resource source.
It still would not by itself have paid the 2-air `霹雳惊雷`, so this is a
possible improvement rather than a proven reversal of the result.

The control matchup lesson is that printed penetration is necessary but not
sufficient. WIND-RUSH also needs at least one early non-hero source that
survives square damage; otherwise freeze or defensive overexertion can turn
off the entire attack engine.

## Confirmed text/runtime mismatch: 魔法蒲公英 always draws on entry

Printed text:

> 诱发:当你抽到此卡时,将其展示.入场:如果你在本回合抽到此卡,抽1张牌

The intended condition is explicit: the entry draw should happen only if that
specific instance was drawn during the current turn.

Series 07 produced two contrary observations:

1. `ci_510` was drawn during the mulligan at `11:20:55Z`, then summoned on
   A turn 2 at `11:23:10Z`. It immediately drew `雷傀儡 ci_520`.
2. `ci_509` was naturally drawn on A turn 3 at `11:25:25Z`, then summoned on
   A turn 4 at `11:32:00Z`. It immediately drew
   `连锁闪电卷轴 ci_533`.

The second case removes any possible ambiguity about whether a mulligan
replacement counts as a draw: the card was demonstrably held across a full
turn boundary and still received the conditional entry reward.

Code inspection confirms the runtime cause in
`server/game/card_1321003_magic_dandelion.go`. `OnEnter` unconditionally calls
`DrawCards(1)`, with a comment stating that per-instance draw-turn tracking is
not implemented.

This is a high-confidence text/effect mismatch found through normal agent
play, exactly the class of problem the agent-player framework is intended to
surface. It changes hand advantage and should be tracked as a Card Effect bug.

## Agent/API mistakes that were not game bugs

- A initially sent the enemy-hero spell target as `target_type:"hero"`.
  The protocol labels that form as a friendly-hero target; enemy heroes are
  board units and require `target_type:"unit"` plus owner and coordinates.
  The backend correctly rejected the first request, and the corrected action
  succeeded.
- On turn 4 A once sent `skill_instance_id` instead of the documented
  `instance_id` for `cast_spell`. The backend correctly returned
  `skill not found in skill area or bound skills`; resending the documented
  shape succeeded without state mutation.

These errors should remain in the private transcript as agent-learning
examples, not be filed as gameplay bugs.

## Next-match recommendation

Keep `霹雳惊雷` as the first learned attack skill against a protected back-row
hero. If making the single allowed deck experiment, replace one low-impact
non-resource attacker with a cheap, durable air-producing companion rather
than changing the spell package. The next test should ask whether A can retain
at least 2 air of independent production after the hero is frozen or
overexerted.
