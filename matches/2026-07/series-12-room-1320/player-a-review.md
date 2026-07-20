# Series 12 — Player A review

- Room: `1320`
- Commit: `05be3b6074b2d83e8b1bb83fc3c20c204ad37d5d`
- Deck: `FIRE-BURN-003`, unchanged from Series 11
- Seat/order: slot 0, second player
- Result: A won, official `game_over` on turn 10 (`winner=0`)
- First hero damage: A turn 2
- Series score after this game: A 7–5 B

## Benchmark result

The controlled deck won again, but did not meet the requested turn-8 finish. The delay was reproducible game pressure rather than an engine failure:

1. B repeatedly restored a front row after A cleared it.
2. `寒冰屏障` protected one spell every turn from T5 onward.
3. On T9 B also had `霜冻射线`, allowing two consecutive successful defenses.
4. A therefore had to spend all three attack spells clearing the final blocker and won through `引燃` settlement on B T10.

## Match outline

- T1: A kept `火流星卷轴 / 火焰精灵 / 火云法师 / 熔岩傀儡`, summoned the free spirit, consumed the hero, learned `火球术`, and summoned `熔岩傀儡`.
- T2: A activated Brahma, generated 6 fire plus 1 earth, paid the mana enhancer wildcard with earth, and used a free `火球术`. `火流星卷轴` then pierced to B's hero for 2 damage, producing the first hero damage on T2. Brahma's load increased from 4 fire to 6 fire after the two successful fire-spell hits.
- T3–T4: A used `火球术` and `焚烧` to remove `冰原狼`, `掠夺者海盗`, and `北海飞鱼`; `引燃` softened `唤雨师`. `活泼的炉火` was paid with 1 fire plus the golem's earth as the wildcard and drew another card.
- T5: B's newly learned `寒冰屏障` stopped one spell, paid by overexerting `凛冬城术士`; A's second attack spell killed the blocker. A ignited the hero and established `屠魔者武士`.
- T6–T7: `冰刺堡垒` absorbed repeated attacks. Its damage trigger froze the warrior, then converted a repeated freeze into damage exactly as printed. A equipped and later sacrificed `火焰箭`, learned `炽热射线`, and finally removed the fortress plus the replacement front-row unit.
- T8: B added two 1-life front-row units. `寒冰屏障` stopped the first attack spell; A's remaining two attack spells cleared both blockers and applied another `引燃`, but could not deal immediate hero damage.
- T9–T10: B added another blocker and now defended twice with `寒冰屏障` and `霜冻射线`. A's third attack spell cleared it, then `引燃` marked the 1-life hero. B's T10 end-of-turn settlement dealt the final point and produced official `game_over`.

## Strategy and API findings

- A newly learned non-quick skill enters horizontal and cannot be cast that turn. The T3 attempt to cast newly learned `焚烧` correctly returned `skill is horizontal (already used)`. `引燃`, which has `速攻`, was learnable and usable immediately.
- A unit placed at `row:1` is in the back row. The T2 `屠魔者杀手` placed there correctly failed to attack with `attacker is not in front row`. This was a player-action error, not a rules bug.
- A normal unit attack can move the game to `waiting_action` when it triggers an enemy card. Actions sent before the opponent resolves that pending choice are correctly rejected with `cannot consume now` / `not in main phase`.
- `冰刺堡垒` opened a target choice after every damage event, including lethal damage. Its first freeze and subsequent repeated-freeze damage matched its printed text.
- Generic costs were paid with off-element resources whenever possible: earth paid the T2/T8 mana-enhancer wildcard and the T4 `活泼的炉火` wildcard. Strict fire was preserved for spell expenses.
- Filling all three friendly front-row slots prevented a late `屠魔者杀手` from being deployed as a new rush attacker. Against repeated chump blockers, leaving one front slot open has measurable finishing value.

## Text-versus-runtime review

No new high-confidence text/effect mismatch was observed.

- `大祭司 梵天` gained one permanent fire load per successful fire-spell hit.
- `火焰精灵` gained ignite when consumed and later died from its own end-of-turn ignite damage.
- `引燃` could not target the enemy hero while an enemy front-row unit existed, then became legal once the front row was empty.
- `寒冰屏障`, `霜冻射线`, `冰刺堡垒`, and end-of-turn ignite settlement all behaved consistently with their exposed text and the known timing rules.

## Next iteration

Keep `FIRE-BURN-003` unchanged for one more controlled sample, but tighten execution:

1. Always place rush attackers in `row:0`.
2. Keep one friendly front-row slot open when a rush attacker remains in the deck or hand.
3. Prefer early piercing or scroll access against WATER-PRESSURE, because repeated 1-life blockers plus two learned defenses can otherwise force every attack spell into board clearing.
4. Treat a T8 finish as conditional on drawing a second independent direct-damage route; the current benchmark still wins reliably, but this game shows it is not an unconditional T8 deck.
