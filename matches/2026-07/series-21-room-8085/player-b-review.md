# Player B Review — series-21-room-8085

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Player B: slot 1, `FIRE-BURN-004`
- Player A: slot 0, `WATER-PRESSURE-SCRY-001`
- Result: A won on turn 20 (`winner: 0`), B 0 life to A 4 life.

## What worked

- Phoenix Feather plus Fireball/Burn created repeated two- and three-spell pressure turns. Fire Arrow also provided reliable hero damage through its equipment sacrifice ability.
- Firebox enabled late multi-spell turns while the hero was horizontal. Combining it with Mana Enhancer and Sketch Scroll produced three attacks in one turn.
- Once actions were submitted one at a time and authoritative state was checked after each response, summons, equipment, attacks, and pending choices were substantially more reliable.

## Strategic problems

- Fire could not efficiently remove the one-life second South Sea Kraken because Water had four independent defensive layers: Ice Barrier, Frost Ray, Ice Blade, and overexertable units. Three consecutive attack spells were all defended on turns 18 and 19.
- Several early board-development actions were sent in batches. Dependent actions raced against state updates: learned skills, summons, attacks, and follow-up plays sometimes did not land even though later assumptions treated them as successful. This cost Fire its early tempo and left the board much weaker than intended.
- `屠魔者武士` was mistaken for a rapid attacker. Unlike `屠魔者杀手`, it entered horizontal and could not attack immediately.
- Fire spent too many resources preserving disposable units with two-skill defenses. This repeatedly left the hero horizontal on the next own turn and prevented normal resource generation.

## Suspicious behavior / bugs

- Multiple rejected actions still reduced available elements. Examples included attempting to cast Fireball outside spell range and attempting unaffordable summons/equipment. This matches the opponent's independent observations and warrants a focused payment rollback issue.
- Units sometimes remained horizontal across owner end turns without a visible status. The first South Sea Kraken and earlier rapid units showed this repeatedly. In other cases they eventually reset, so the trigger conditions need replay-level reproduction.
- A center-front `屠魔者武士` received `target is not in attack range` when targeting the exposed center hero. A taunting `冰刺堡垒` existed in the opponent's left-front lane; if global taunt intentionally blocked the attack, the rejection should identify the taunt source. Otherwise the attack-range check may be wrong.
- `火焰箭` must be activated as `use_ability` with `ability_type: ultimate`; `per_turn` and hand-item paths correctly rejected it. The protocol should call this out explicitly.
- End-turn discard pending actions are private to the active player. The opponent repeatedly saw `waiting_action` or stale turn state until B resolved the discard. This is expected perspective filtering but needs agent coordination guidance.

## Next-match guidance

- Submit one state-changing action at a time and verify authoritative state before sending dependent actions.
- Against Water, prioritize direct hero damage and removal that cannot be spread across many separately defendable spells. Do not assume three ordinary spells are enough once Water has a full defensive skill suite.
- Track printed versus effective attack and power separately; Phoenix Feather changes damage, while defensive calculations still depend on effective power.
