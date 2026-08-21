# Player B Review — series-24-room-5281

- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Deck ID: `WIND-RUSH-007`
- Result: Player A win, official `game_over` on turn 9; final hero life A 2, B 0.
- Transcript: `agent-data/matches/series-24-room-5281/player-b.jsonl`

## Exact deck code

`4311001 // 1321001 1321001 1321002 1321002 1321003 1321003 1321004 1321004 1321008 1321008 1321009 1321011 1321011 1321013 1321016 1321016 1021001 1021001 1021011 1021011 1021013 1021013 2021012 2021012 2021014 2021014 2321009 2321009 1311003 1311003 // 3321001 3321002 3321003 3321005 3321007 3321013 3321014 3321015 3021001 3021009`

## Changes from WIND-RUSH-006

- Removed `工蜂骑士` (`1321007`) x2.
- Removed one `传送法师` (`1321013`).
- Added `屠魔者武士` (`1021013`) x2.
- Added `风魔` (`1321009`) x1 as a high-resource 2-attack finisher.

The two restored warriors and Wind Demon were not drawn. Nevertheless, the higher practical attack density was immediately visible because the opening hand contained both `屠魔者杀手` copies.

## Strategy execution

B kept `速写卷轴`, two `屠魔者杀手`, and `魔法蒲公英` as second player. Turn 1 used the full four gas to summon Dandelion plus a rush killer; the killer immediately hit Kran from 6 to 5. On turn 3, the first killer killed `火荆`, the second killer entered in the newly available front slot and immediately hit Kran from 5 to 4. This was exactly the intended “clear, deploy attacker, convert immediately” pattern and happened far earlier than in WIND-RUSH-006.

The opponent then used one-life/two-life front units and `烽火台守卫` shield to tax attacks. B repeatedly split work correctly: the surviving killer removed `巫师的学徒`, `烽火台守卫`, `熔岩傀儡`, and another apprentice, while `霹雳惊雷`, `气旋波`, and `速写卷轴` pressured or removed the remaining blocker. On turn 7, B executed a true three-wave sequence against `熔岩烽蛇`: `霹雳惊雷` forced `烈焰反噬`, `气旋波` dealt one, then Sketch Scroll copied Thunder and killed the final one life after A exhausted strict-fire payment.

The cost of those defended spells was repeated ignite on Su. Kran's first-turn `烈焰反噬` was online before B's first spell and generated enough tempo plus ignite to win the race. On turn 8, with Su at one life and ignite one, B converted all remaining direct damage: the surviving killer hit Kran from 4 to 3, then Su discarded `传送法师` and `风息奔马` to use the ultimate on Kran from 3 to 2. No surviving companion other than the killer had attack, and generic attack spells could not target the hero. End-turn ignite produced official game over.

## What the attack-density change proved

- The concept is correct. A rush attacker on turn 1 and a second rush attacker on turn 3 forced immediate life loss while also clearing several blockers.
- Attack bodies turn spell clearing into real pressure. WIND-RUSH-006 often cleared a board and then passed; WIND-RUSH-007 repeatedly cleared and threatened a direct hit next turn.
- Two `屠魔者杀手` were substantially more useful than two `工蜂骑士`. They dealt three total hero damage across the game and killed multiple blockers despite shield and ignite.
- The remaining weakness is draw access to the *other* attackers. Neither `屠魔者武士` nor `风魔` appeared before turn 9, so the experiment supports their inclusion but does not directly validate their battlefield performance.
- Wind Demon is still theoretically attractive as a resource sink, but a seven-cost card does nothing if it is not drawn before the burn clock ends. More selection/draw may be preferable to simply adding another expensive finisher.

## Good decisions

- Kept the ideal aggressive opening rather than redrawing for a more conventional resource hand.
- Used the first killer to trade into Firethorn, then immediately filled a different front square with the second rush killer and attacked Kran in the same turn.
- Used normal attacks against one-life blockers before spending spells, preserving spell chains for the two-life targets and defense exhaustion.
- Learned `气旋波` before the midgame chain, giving a cheap second wave after `霹雳惊雷` forced Reflection.
- Used `气旋波` on the friendly `随风旅行者` after the opponent board was cleared, triggering the death draw and replacing a zero-attack body with `雷精灵` for better future resources.
- In the final turn, correctly used both available unavoidable damage sources before accepting the ignite loss.

## Mistakes and constraints

- Two direct attacks were submitted close together on turn 4 rather than waiting for the first authoritative state. Both happened to be legal and processed, but this violates the safest one-action/one-state discipline and should not be repeated.
- The deck still placed too many zero-attack companions on a full board. They produced resources but could not finish once the sole killer had attacked.
- `烈焰反噬` punished every repeated spell wave with ignite. Against Kran, forcing defense three times can be strategically losing even when the board is eventually cleared.
- B never drew the restored `屠魔者武士` or `风魔`, so the final result remains partially draw-dependent.
- Shield absorbs damage aimed at companions, making one-power attacks and `气旋波` particularly inefficient against `烽火台守卫` starts.

## Bugs or suspicious behavior

No confirmed bug was observed. Rejected or pending actions behaved consistently, and all card effects in the decisive sequence matched the current authoritative state.

## Three-game cumulative learning

Across WIND-RUSH-005/006/007, B lost all three games to the Kran burn shell, but the deck's execution improved materially:

1. **WIND-RUSH-005:** poor initial Horse placement and a slow resource/skill setup produced almost no reliable finishing pressure; A won turn 13 with 6 life.
2. **WIND-RUSH-006:** Dandelion and better placement enabled large multi-spell turns and full front-line clears, but generic spells could not hit heroes and zero-attack bodies failed to convert; A won turn 15 with 2 life.
3. **WIND-RUSH-007:** early rush attackers converted immediately and repeatedly, shortening the game to turn 9 and again leaving A at 2. The game was lost to the ignite clock, not inability to contest the board.

The durable lesson is that this archetype should be treated as **unit-tempo with spell removal**, not spell burn. Its attack spells clear companions; actual victory comes from attack companions plus Su's ultimate. Resource generation beyond the amount needed for one clear-and-attack turn has sharply diminishing value.

## Recommended next iteration

- Keep both `屠魔者杀手`, both `屠魔者武士`, both scrolls, and the cheap Dandelion/Traveler draw shell.
- Keep only enough zero-attack resources to fund one two/three-wave clear. Cut at least one additional zero-attack mid-cost body for another attack companion or card-selection effect.
- Against Kran specifically, do not automatically fire three attack spells into a ready `烈焰反噬`. Prefer normal attacks/trades, or wait until one spell plus a unit attack can clear the blocker without giving multiple ignite triggers.
- Mulligan priority: one rush killer, one cheap resource/draw body, and either a second attacker or one removal spell. Two removal tools without an attacker should be sent back.
- Treat Su's ultimate as the final point only when it changes the clock; discarding two gas cards earlier removes future attacker/resource options.
