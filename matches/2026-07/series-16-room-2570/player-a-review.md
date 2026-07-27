# Player A Review — series-16 room 2570

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Deck: `WIND-RUSH-005`
- Opponent: `FIRE-BURN-004`
- Result: loss, winner player 0, turn 19
- Transcript: `player-a.jsonl`

## Match summary

The wind deck controlled the early and middle board well. `雷击`, `闪电链`, copied spells, and the first `屠魔者杀手` removed nearly all of Fire's early companions. `雷术士 肃` also converted two air cards into one direct hero damage. On turns 12–14, however, the board became filled with five non-attacking resource companions plus `"风刃" 卡琳娜`. This prevented A from deploying a real attacker while attack spells could not target the opposing hero. Fire recovered behind repeated defensive spell packages, then used `火焰箭`, `火球术`, scrolls, and later速攻 units to close the game.

## Decisions that worked

- Early sequencing of consume resources into efficient removal produced a commanding board advantage.
- Using `静电屏障` plus `雷击` as a six-power defense protected important units twice.
- The hero ultimate was fired while two air cards were available and correctly dealt direct hero damage.
- On turn 16, deliberately allowing the one-life `雷电元素` to die was the right attempt to reopen a battlefield slot.
- The later速攻杀手 immediately traded into the opponent's center blocker, validating that attackers were the missing win condition.

## Decisions to improve

- Do not fill every battlefield slot with zero-attack companions. At least one front slot should remain available for `屠魔者杀手` or another actual attacker, especially after the opponent's board has been cleared.
- `"风刃" 卡琳娜` was poor in this state: she occupied the newly opened slot, had no attack, and increased targeted air-skill use costs by one. Her pierce aura mattered less than the lost deployment space and tempo.
- A spent too many spells clearing units without planning how hero damage would occur. Attack spells legally reject hero targets, so board control alone cannot end a match.
- The turn-15 attempt to cast `闪电链` on the hero was wasted information/tempo; future agents should treat `spell cannot target hero` as a firm protocol rule.
- When requesting a summon position, the engine placed the unit in the first available slot rather than the requested center slot. Future play should verify the actual synchronized position before issuing a follow-up attack.
- Defensive overexertion of the hero preserved a one-life attacker from `火球术`, but Fire could immediately follow with a piercing scroll. Against a deep Fire hand, avoid investing the last defense package in a fragile unit unless it can threaten lethal next turn.

## Reusable strategy updates

1. Reserve one front slot for an attacker; do not let resource companions occupy all six unit spaces.
2. Before removing the opponent's last unit, identify the concrete hero-damage route for the next two turns.
3. Air attack spells target units only; hero damage must come from unit attacks or explicit direct-damage effects such as the hero ultimate.
4. Evaluate Karina as a build-around rather than an automatic one-cost summon: her +1 air tax can make a five-air turn support only `闪电链` plus one cheap spell.
5. Fire's `烈焰反噬` package punishes repeated single attack spells with hero burn. Prefer forcing it early, then following with a second spell only when that second spell advances a win condition.

## Product / bug observations

- No confirmed card-text/effect mismatch was found in this match.
- The rejected hero spell target was clear and legal behavior, not a bug.
- The requested summon position appeared to be ignored in favor of the first empty slot. This is worth reproducing against the protocol documentation before filing an issue; the synchronized state was authoritative and gameplay continued correctly.
