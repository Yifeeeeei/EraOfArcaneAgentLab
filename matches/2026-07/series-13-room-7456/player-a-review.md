# Series 13 — Player A review

- Room: `7456`
- Commit: `05be3b6074b2d83e8b1bb83fc3c20c204ad37d5d`
- Deck: `FIRE-BURN-004`
- Change from FIRE-BURN-003: `-1 火云法师`, `+1 灼烧卷轴`
- Seat/order: slot 0, second player
- Result: A won, official `game_over` on turn 7 (`winner=0`)
- Final life: A 5, B 0
- First hero damage: B turn 2 damaged A; A turn 3 damaged B
- Series score after this game: A 8–5 B

## Benchmark result

The game met both requested timing goals:

1. Both heroes took damage before turn 4.
2. The game ended on turn 7, two turns ahead of the turn-9 limit.

The one-card replacement was legal and preserved the resource/physical-plus-burn plan. `灼烧卷轴` was not drawn, so this game validates deck legality and the surrounding shell, but is not yet a direct runtime sample of the replacement card.

## Match outline

- T1: A kept `熔岩烽蛇 / 火匣子 / 屠魔者杀手 / 速写卷轴`. Brahma produced 4 fire; A learned `火球术` and equipped `火匣子`.
- B T2: `水占术` found `水形之束卷轴`; it hit Brahma for 1, giving A's first hero damage on B T2.
- A T2: Brahma's ultimate was activated. Brahma plus `火匣子` produced 6 fire. `火球术` and `速写卷轴` replaying `火球术` killed `北海飞鱼`; both hits increased Brahma's permanent load, from 4 fire to 6 fire. A also established `火焰精灵`, `凤凰之羽`, and `烈焰护体`.
- B T3: `寒冰爆裂卷轴` hit the spirit for 1 and froze it.
- A T3: `激情之火` enabled a draw on the first `火球术` hit. The drawn second `速写卷轴` replayed `火球术` to clear the last front blocker. `屠魔者杀手` then entered with rush and dealt 1 physical damage to B's hero, meeting the reciprocal pre-T4 damage goal.
- A T4: A forced `寒冰屏障` by attacking a 1-life `海豚伙伴`, then killed it with the rush unit. `引燃` marked B's hero, and `学院导师` expanded the future element mix. The burn settled on B T5.
- B T5: A preserved the rush unit by combining `火球术` and `烈焰护体` for defense 6, paying their two fire by overexerting `活泼的炉火` and `学院导师`.
- A T5: The rush unit dealt another point to the hero. A learned `焚烧`, reapplied `引燃`, and summoned `熔岩烽蛇`. The second burn settled on B T6, leaving the hero at 2.
- B T6: `烈焰护体` alone matched `冰锥术` at defense 3, paid by overexerting `活泼的炉火`, again preserving the rush attacker.
- A T6: A ignited B's new `北海飞鱼`, then cast `焚烧` strengthened by `火球术`. The printed burning-target bonus made the main spell power 6; the boost added 3, for total power 9 and attack 2. The fish died. The rush unit dealt another physical point, leaving B at 1. A equipped `火焰箭`.
- B T7: B's rush unit killed A's rush unit, but could not remove the weapon.
- A T7: `火焰箭` consumed and sacrificed itself, selected B's hero through the explicit pending action, and dealt the final direct damage. The server emitted official `game_over`.

## Strategy and API findings

- `速写卷轴` is a strong independent spell-use route. Its API is a two-step pending chain: select a learned spell (`sketch_scroll_skill`), then select its target (`sketch_scroll_target`). It correctly pays both the scroll's generic cost and the chosen spell's use cost without requiring the learned skill to be vertical.
- `激情之火` plus a reliable fire hit materially improves tempo. Here it drew the second `速写卷轴`, which converted a two-turn blocker-clear plan into same-turn clearance plus rush hero damage.
- Brahma's ultimate scales especially well with replayed spells. Two T2 fire hits permanently changed its load from 4 fire to 6 fire, supporting the later learn/cast/deploy turns without resource starvation.
- A burning target correctly modified `焚烧` before boosts: 4 base power became 6, then the `火球术` boost raised the pending spell to 9. The public `power_sources` exposed this breakdown clearly.
- Companion-paid defense worked in two configurations:
  - two defense-capable skills costing 2 fire were paid by two companions and produced defense 6;
  - one `烈焰护体` costing 1 fire was paid by one companion and produced defense 3.
  Overexertion did not trigger consume effects or grant reusable excess elements.
- Physical unit attacks to the hero resolved directly in this match; the WATER defense spells were used against spell attacks, not those physical attacks. Preserving the 1-attack rush unit therefore generated three separate hero-damage opportunities across turns.
- A second `凤凰之羽` cannot simply occupy another equipment slot because the subtype already exists. The attempted equip correctly returned `same subtype equipment must be replaced`; a replacement choice is required. This was a player-action error, not a bug.
- `火焰箭` is a reliable delayed finisher: equip on one turn, reset at that turn's end, then use `ultimate` and resolve the `fire_arrow_damage` pending target on the next turn.

## Text-versus-runtime review

No new high-confidence text/effect mismatch was observed.

- `大祭司 梵天` gained exactly one permanent fire load for each successful fire-spell hit while its ultimate was active.
- `火匣子` entered with three markers, consumed itself while producing 2 fire, and removed one marker per activation.
- `激情之火` was immediately usable because of `速攻`, drew one card on the next fire-spell hit, and entered cooldown.
- `引燃` applied one ignite mark without immediate damage; the mark damaged B's hero at the end of B's own turn.
- `焚烧` received the printed +2 power against an ignited target, and its boost calculation remained separate and visible.
- `寒冰屏障` successfully stopped a lower-power spell while paid through a companion's overexertion.
- `火焰箭` consumed and sacrificed itself before dealing 1 damage to any selected enemy, including the enemy hero.

## Bugs

No gameplay engine bug, API deadlock, illegal hidden-information exposure, or card-text/runtime mismatch was found in this game.

## Next iteration

Keep `FIRE-BURN-004` for another sample so `灼烧卷轴` itself can be drawn and exercised. Preserve these priorities:

1. Use `激情之火` before the first reliable fire hit when hand velocity can unlock a second attack route.
2. Treat `速写卷轴` as an independent activation, especially for clearing a blocker while retaining a rush unit for hero damage.
3. Preserve one physical attacker through defense when its repeated direct attacks are more valuable than the overexerted resource units.
4. Prepare delayed direct damage (`火焰箭` or the new `灼烧卷轴`) one turn before the expected lethal window.
