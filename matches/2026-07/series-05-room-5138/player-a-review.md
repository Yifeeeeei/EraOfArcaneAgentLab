# Series 05 / Room 5138 — Player A Review

## Result

- Identity: Codex A, actual backend slot `0`
- Opponent: Codex B, actual backend slot `1`
- First player: B
- Test commit: `05be3b6074b2d83e8b1bb83fc3c20c204ad37d5d`
- Official result: A won on turn 17; `game_over` reported `winner: 0`,
  `reason: hero_killed`
- Final public life: A 4 / B 0
- Match time: 2026-07-19 09:34:13Z–10:33:11Z, about 58m58s
- A transcript: `raw transcript (not imported)`
- A deck: `player-a-deck.txt`

## Controlled deck change

The WIND-RUSH-003 list was changed in exactly one controlled package:

- `连锁闪电卷轴` (`2321009`): 2 -> 1
- `瓶中闪电` (`2321006`): 0 -> 1
- The other 29 main-deck cards and all 10 skills were unchanged.

The resulting deck passed `/api/deck/validate` at 30 main cards, 10 skills,
0 extra cards, using only the base-set pool.

The hypothesis was that `瓶中闪电` could preserve pressure while reducing
dependence on drawing the exact chain-scroll payoff. The result is mixed:

- The single `瓶中闪电` was drawn only on A turn 11, so it did not preserve the
  early turn-4 pressure seen in prior WIND-RUSH-003 games.
- When drawn, its text and runtime matched: paying 1 air immediately changed
  A's air from 4 to 7, a net gain of 2, then opened the required stun choice.
- A put stun 2 on the already permanently frozen `屠魔者武士`, spending the
  drawback on a unit that was already effectively a dead board slot.
- The extra mana let A deploy `风息奔马` and still cast both learned spells.
  On the following turn, the horse helped produce an exact 8-air turn:
  `速写卷轴` copying `霹雳惊雷`, then direct `气旋波`, then direct
  `霹雳惊雷`. B stopped two threats, but the third hit.

Conclusion: the replacement did reduce reliance on a particular
`连锁闪电卷轴` draw once the game went long, but one game does not show that it
retains the deck's very early pressure. Keeping the one-for-one substitution
for another sample is reasonable; increasing the bottle count would be a
different hypothesis.

## Match flow and decisions

- Opening hand was `渡鸦信使`, `雷精灵`, `"风刃" 卡琳娜`, and `风魔`; A kept.
- Turn 1 established `卡琳娜` plus `渡鸦信使` and learned `气旋波`.
- Turn 2 used the hero ultimate to discard two air cards and deal 1 to B's
  hero, then learned `霹雳惊雷` and chained early spell pressure. B fell from
  6 to 3 life early, but did not collapse.
- B's coherent water-source revision was decisive. `水栖狸猫`,
  `北海飞鱼`, and the hero supplied independent overexertion sources, allowing
  two defense skills to be paid repeatedly. B comfortably met the target of
  surviving past turn 6.
- Two `寒冰爆裂卷轴` casts, freeze effects, and `深寒诅咒卷轴` dismantled or
  locked A's early board. In particular, permanent freeze on the central
  `屠魔者武士` consumed a board slot for many turns.
- A shifted from racing the hero to dismantling payment sources: it killed both
  `水栖狸猫` copies and the first `北海飞鱼`, eventually reducing B to a
  single water-producing hero for one turn. B later rebuilt with a second fish.
- On turn 15 A killed the first fish, then sent two spells at the hero. B saved
  its defense and took both hits, falling from 3 to 1. A used the remaining
  mana to establish `工蜂骑士`.
- B removed A's front row over turns 16–17. That opened slots for the final
  line: consume the hero, `卡琳娜`, and `渡鸦信使` for 6 air; summon
  `随风旅行者` for 1 and gain 2; summon `雷电元素` for 3 and give the new
  `北海飞鱼` stun 1; then cast both learned spells at the 1-life hero.
- The stunned fish still serialized as vertical, but the backend correctly
  rejected B's attempted overexertion with
  `card cannot be overexerted: ci_398`. B paid for the first defense with the
  hero; the second spell was therefore lethal and produced the official
  `game_over`.

## What A learned

1. Count independent payment sources, not defense cards. B's revised board
   converted the same defensive skill package from fragile to repeatable and
   extended the game from turn-4 losses to turn 17.
2. Resource denial was the correct midgame plan. Killing a 1-load water unit
   was often more valuable than adding a small amount of hero pressure.
3. `雷电元素` is a practical defense breaker. Stun prevents an otherwise
   vertical unit from being used for overexertion; the UI/state appearance
   alone is not enough to judge payment availability.
4. `随风旅行者` is a useful combo bridge. Its cost-1/gain-2 entry turned 6 air
   into the exact 7 needed for elemental plus two spells.
5. A's empty deck did not cause fatigue damage or an automatic loss. The game
   continued normally after A reached deck count 0.
6. Physical/spell target geometry needs deliberate checking. A's attempt to
   attack a back-row dolphin through an occupied front row was correctly
   rejected, and B later received the same kind of rejection when trying to
   cast a non-penetrating spell at A's back-row hero. These were player errors,
   not engine bugs.

## Bug assessment

No new high-confidence bug was found.

- `瓶中闪电` payment, resource gain, pending target selection, and stun
  resolution matched its displayed text.
- Stun correctly blocked overexertion even though the affected fish remained
  visually/serially vertical.
- The official winner and final state were consistent across `game_over` and
  the final `state_sync`.
- Existing issue #110 was not duplicated. The remaining
  `连锁闪电卷轴` was defended in this match, so its known on-hit choice problem
  was not exercised.
- Issue #109 was avoided as requested.
