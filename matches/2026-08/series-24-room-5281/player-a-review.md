# Player A review — series-24-room-5281

- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Deck: `ROYAL-SURVIVAL-FIRE-002`
- Player: `OfficialA24` / `official-series24-a` / slot 1
- Result: win, official `game_over`, turn 9, final life 2–0
- Transcript span: 2026-08-21 05:57:49Z–06:14:10Z (about 16m21s)
- Transcript: `agent-data/matches/series-24-room-5281/player-a.jsonl`

## Exact deck code

```text
4111102 // 1021001 1021001 1021007 1111002 1121004 1121005 1121005 1121006 1121006 1121012 1121014 1121014 1121103 1121103 1121108 2021002 2021002 2111002 2111102 2121002 2121002 2121003 2121004 2121004 2121009 2121009 2121013 2121107 2121107 2121110 // 3111102 3121001 3121006 3121007 3121012 3121013 3121101 3121102 3121103 3121108
```

Change from `ROYAL-SURVIVAL-FIRE-001`: remove one `1121004 凯尔特雄狮`; add one `1121108 火蝴蝶`.

## Match summary

- Mulliganed an unusably expensive opening hand. The replacement produced `火荆`, `巫师的学徒`, `火焰箭`, and a defense scroll.
- As first player, Kran's first consume produced only two fire; those two learned `烈焰反噬`. Two subsequent summon attempts correctly failed for lack of elements and changed no state.
- Turn 2 established central `火荆`, a side apprentice, and an early equipped `火焰箭`.
- Rebound repeatedly defended Thunder by using strict-fire sources. Kran filtered away `供奉之炬`, `熔岩魔甲`, and the expensive `狄斯托德` while finding `熔岩傀儡`, `神火集结号`, and a second arrow.
- `烽火台守卫` plus `熔岩傀儡` created shield and two independent fire sources. They paid for one Rebound without tapping Kran, directly validating the refined range/payment policy.
- After that board was removed, `神火集结号` fetched `狄斯托德` and `熔岩烽蛇`. A later `熔岩烽蛇` plus apprentice rebuilt the board.
- A set `火焰符文` was revealed on the opponent's Kran consume by overexerting `熔岩烽蛇` and explicitly paying arcane one with fire. The next successful Rebound stacked a second ignite.
- At opponent life 2 with ignite 1 remaining, the stored `火焰箭` dealt the final direct point; opponent-end ignite produced official game over.

## Fire Butterfly experiment

`火蝴蝶` was not drawn, fetched, or played, so this match does **not** directly validate its battlefield value. The changed list nevertheless remained legal and won without missing the removed second Lion. The result supports only the weak claim that the one-card substitution did not disrupt the deck's core plan in this sample.

The intended hypothesis remains sound: a one-fire, two-life companion that produces fire is a much earlier independent strict-fire source than the second `凯尔特雄狮`. More games are required before promoting that from theory to learned knowledge.

## Errors and questions

- The first-player turn-one resource reduction was not accounted for before two summon attempts. The server correctly returned `not enough elements`; no state corruption occurred. Future pilots should inspect the authoritative pool after consume, especially on turn one.
- No confirmed card or engine bug occurred.
- All private windows (Kran, Firethorn, Fire Rune, Fire Arrow) resolved normally when the current authoritative state was checked first.

## Three-game cumulative lessons

1. `烈焰反噬` is the primary clock, not disposable fuel. Across the series, repeated successful defenses generated the decisive ignite totals.
2. Range and payment are separate resources. The largest pilot mistakes came from consuming/overexerting the only vertical range source before casting. `神火集结号` and cheap fire companions are valuable because they let Kran remain vertical.
3. Strict fire cannot be paid by neutral load. Build defense payments from explicit fire-producing units; preserve at least one such body for the opponent turn.
4. Central-front blockers must be cleared before targeting the hero with ordinary ranged spells. `火焰箭` is exceptional because its follow-up can select any enemy.
5. `火焰箭` is strongest as a stored final point after ignite has reduced the hero to 1–2 life.
6. Kran's optional filtering is excellent for converting situational high-cost cards into relevant bodies, counters, armor, or arrows. Skip it when hand quality is already sufficient or the game is ending.
7. Private continuations are normal flow, not soft locks. Poll authoritative state after every spell segment, copied spell, deathrattle, counter trigger, and Kran defense.

## Recommendation

Keep `ROYAL-SURVIVAL-FIRE-002` for several additional matches specifically until `火蝴蝶` is drawn and used. Track three observations: turn played, number of turns it stays vertical/alive, and whether its fire load enables a Rebound or offensive spell while Kran remains vertical. Only then decide whether it is better than the second Lion.
