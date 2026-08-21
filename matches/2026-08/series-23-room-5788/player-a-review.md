# Player A review — series-23-room-5788

- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Player: `OfficialA23` / `official-series23-a` / slot 0
- Result: win, official `game_over`, turn 15, final life 2–0
- Wall-clock transcript span: 2026-08-21 05:19:20Z–05:54:57Z (about 35m38s, including coordination waits)
- Transcript: `agent-data/matches/series-23-room-5788/player-a.jsonl`

## Exact deck code

```text
4111102 // 1021001 1021001 1021007 1111002 1121004 1121004 1121005 1121005 1121006 1121006 1121012 1121014 1121014 1121103 1121103 2021002 2021002 2111002 2111102 2121002 2121002 2121003 2121004 2121004 2121009 2121009 2121013 2121107 2121107 2121110 // 3111102 3121001 3121006 3121007 3121012 3121013 3121101 3121102 3121103 3121108
```

## Controlled-repeat hypothesis

The list was intentionally unchanged from Game 1. The test changed only pilot policy: do not exile `烈焰反噬` early, maintain a vertical central mana-range source, preserve independent payment sources, and keep `火焰箭` for the closing race.

## Strategy execution

- Learned `烈焰反噬` immediately and equipped `火焰箭` early, but kept both for the long game rather than converting them prematurely.
- `烽火台守卫` twice bought time and shield; `回收小精灵` put `火荆` back on top, proving the deck can recycle a relevant defensive/deathrattle body instead of only raw value.
- Repeated successful Rebound defenses against `霹雳惊雷` stacked ignite on 肃 while Kran converted those defenses into hand filtering.
- `神火集结号` supplied both bodies and an independent one-fire payment source. In the late game it paid for `火球术` while Kran stayed vertical, which preserved legal mana range.
- `火焰符文` punished an opponent consume: it was revealed by overexerting `火焰洞察者` to pay its arcane-one reveal cost, putting another ignite on 肃.
- At 2 life, `熔岩魔甲 业炎` was equipped, then sacrificed after a spell hit for shield 2. The shield and a late `火荆` let A survive until opponent-end ignite produced official game over.

## Pilot errors and corrected assumptions

1. First Rebound defense attempt used `巫师的学徒` plus `火荆` for a strict fire-two payment and correctly failed: neutral load cannot satisfy strict fire. Retried with fire-producing units successfully.
2. On turn 11, Kran was consumed before attempting `火球术`; although enough fire existed, consuming the only vertical central source removed legal mana range. This wasted a lethal-pressure window. The correct order is to pay with `神火集结号`/other sources while leaving Kran vertical.
3. `火球术` could not target the enemy hero while a unit occupied the enemy central front. The spell correctly had to clear `渡鸦信使` first.
4. `火焰箭`'s ultimate opens a private `fire_arrow_damage` selection; target fields on the initial `use_ability` do not finish the effect. Resolve the follow-up explicitly.
5. A revealed `火焰符文` needs its arcane-one payment in the resolve payload. The first reveal attempt without payment correctly failed; `overexert_ids` plus an explicit `{火:1}` payment succeeded.
6. One defense submission raced a stale coordination notice and returned `not in defense window`. Refreshing until the new authoritative `pending_spell=气旋波` appeared avoided acting on the already-resolved copied Thunder segment.

## Bugs or suspicious behavior

No confirmed gameplay bug in this match. Every apparent stall or rejection was explained by a private continuation, strict-element payment, mana-range legality, target blocking, or stale timing. The failed actions above are pilot/protocol lessons, not issue candidates.

## Game 3 iteration recommendation

Keep the exact deck for one more controlled run, but tighten the policy further:

- Before every offensive spell, reserve one vertical unit in the required lane/range; never consume or overexert the last range source before targeting.
- Treat `神火集结号` as premium independent spell payment after its entry trigger, rather than automatically consuming Kran.
- When the enemy central front is occupied, explicitly plan a two-turn clear-then-face sequence; do not assume hero targeting is available.
- Preserve one cheap vertical fire body specifically for opponent-turn Rebound payment. Do not count neutral load toward strict fire.
- Poll authoritative state after every copied spell or private continuation before responding; match on `pending_spell.skill.instance_id` and target, not only a coordination message.
- Continue holding `火焰箭` for life 1 when possible. In this game it was used at life 3 because range was temporarily lost; that was acceptable but not ideal.

For a meaningful Game 3 deck change rather than another policy-only repeat, the best small experiment is replacing one high-cost `凯尔特雄狮` with another cheap fire-producing companion. The observed bottleneck was independent vertical fire sources, not late-game spell power.
