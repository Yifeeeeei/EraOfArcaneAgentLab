# Player A Review — series-22-room-2714

- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Player: `OfficialA22` / slot 0 / 后手
- Result: win, official `game_over`, turn 13, life 6–0
- Deck ID: `ROYAL-SURVIVAL-FIRE-001`
- Exact deck code: `4111102 // 1021001 1021001 1021007 1111002 1121004 1121004 1121005 1121005 1121006 1121006 1121012 1121014 1121014 1121103 1121103 2021002 2021002 2111002 2111102 2121002 2121002 2121003 2121004 2121004 2121009 2121009 2121013 2121107 2121107 2121110 // 3111102 3121001 3121006 3121007 3121012 3121013 3121101 3121102 3121103 3121108`

## Strategy execution

The opening established `烈焰反噬` on turn 1 and used `熔岩烽蛇` as both a center blocker and a defense-payment source. Two early successful defenses placed repeated `点燃1` on the opposing hero, while `大将军 克兰` converted each defense into a fire-card filter. This reduced the opponent from 6 to 4 without exposing our hero.

At 4 life I pivoted to `原初神炎 洛普修斯`. Exiling `烈焰反噬` correctly increased it from 2 attack / 6 power to 3 attack / 8 power. It then removed two successive center-front blockers. The opponent continuously rebuilt the center lane, so direct spell access to the hero remained constrained.

The actual finishing package was attrition plus deterministic item damage: two `火焰符文` triggers punished opposing hero consumes and reduced the opponent to 1; repeated successful defenses let Kran dig until the second `火焰箭` appeared. It was equipped on turn 12, reset at end of turn, and dealt the final point on turn 13.

`祈祷之焰` also completed a full two-cast cycle: add three markers, then remove them to summon `熔岩傀儡` for free. That stabilized the resource board but was slower than the fire-rune/arrow route.

## Decisions that worked

- Paid early `烈焰反噬` defenses by overexerting the spell target itself. This preserved the unit, triggered Kran, and avoided tapping the hero.
- Declined a self-triggered `火焰符文` window after consuming Kran, then saved the trap for the opponent's hero consume.
- Paid the second rune reveal with `熔岩傀儡`, preserving the center-front source and keeping the hero available for later range.
- Used low-power `火球术` to draw out `静电屏障`; even though the center blocker survived, Kran's successful-defense trigger found the finishing Fire Arrow.
- Did not spend expensive defense on expendable 1-life units when the next turn's resource plan mattered more.

## Mistakes and corrected rules understanding

- I exiled `烈焰反噬` too early. At opponent life 4, I assumed a grown Original Divine Flame could attack the hero immediately. The server rejected `target_type:"hero"` while the center lane/range condition was not met. Against a spell-heavy opponent, retaining Rebound for another burn cycle would have shortened the game.
- I twice consumed Kran before attempting a hero-targeting spell, leaving no vertical center source in spell range. A vertical center unit must be preserved before spending the hero's load; independent equipment load is particularly valuable for this reason.
- I attempted to activate a newly equipped `火焰箭`. It enters horizontal and cannot pay its consume/sacrifice cost until it resets at end of its owner's turn.
- I initially overlooked private counter windows because the CLI emitted no new concise line while the opponent was waiting. For future play, inspect the latest private state after every publicly observed opponent consume.

These were legal-action/sequence errors, not evidenced engine defects. `原初神炎` exile and permanent growth behaved correctly on this commit. No new bug is claimed from this match.

## Next-match iteration

Keep the main deck unchanged for one controlled repeat, but change the pilot policy:

1. Do not exile `烈焰反噬` until either the opponent stops presenting spells or a grown Original Divine Flame has a concrete center-lane attack sequence.
2. Treat a vertical center-range source and a separate fire payment source as a paired lethal prerequisite.
3. Set `火焰符文` only when its reveal can be paid by a non-center resource; decline self-consume triggers.
4. Equip Fire Arrow one full turn before projected lethal.
5. Prefer using `激情之火` or `祈祷之焰` as Original Divine Flame fodder; keep Rebound when the opposing deck repeatedly casts attack spells.

If a deck change is required after the controlled repeat, the first candidate is replacing one high-cost `凯尔特雄狮` with a cheap independent fire/earth resource. Both lions repeatedly clogged the hand because the deck could not reliably produce the required earth while keeping Kran vertical.
