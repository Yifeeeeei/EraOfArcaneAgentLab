# Player A Review — series-17 room 4286

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Deck: `FIRE-BURN-004`
- Opponent: `WIND-RUSH-005`
- Result: win, player 0, turn 10
- Transcript: `player-a.jsonl`

## Match summary

Fire recovered from an opening hit by learning `火球术`, installing two renewable equipment engines, and keeping two real attackers on the front line. `屠魔者杀手` and `屠魔者武士` repeatedly removed blockers and later attacked the hero. `激情之火` supplied replacement cards, while `烈焰反噬` plus `火球术` protected the fragile killer from `闪电链`. On turn 10, both attackers reduced the last blocker, Fire spells removed it, and the card drawn from `激情之火` was a second `速写卷轴`. The scroll copied `火球术`, selected the one-life enemy hero, and ended the game.

## Decisions that worked

- Preserved a genuine finishing route: the center killer and right-side warrior remained attack-capable instead of filling every slot with resource units.
- Used the left column for `活泼的炉火` and `火荆`, leaving two front attackers available throughout the midgame.
- Protected the one-life killer with `烈焰反噬` plus `火球术`; its later hero attacks justified the defensive investment.
- Activated 梵天's ultimate before the longer spell sequence, increasing later fire production from successful fire-spell hits.
- Used `激情之火` before attack spells so successful hits replaced cards and eventually found the lethal second `速写卷轴`.
- Sequenced unit attacks before spells to reduce four- and three-life blockers into spell-kill range.

## Decisions to improve

- The first equipment attempt incorrectly used `use_item` on `火匣子`; equipment must use `equip`.
- Early summons incorrectly nested coordinates under `position`. The protocol requires `data.col` and `data.row`. The resulting `position already occupied` errors were operator mistakes, not engine bugs.
- On turn 6, `火焰结界` was sent with an invalid one-fire payment; its expense is two fire.
- Several direct hero attacks were attempted while any enemy front-row unit remained. The hero is protected until the entire opposing front row is clear.
- The turn-9 direct `焚烧` attempt on the hero was rejected. This was useful for diagnosis but should not be repeated unless testing the inconsistency intentionally.

## Reusable strategy updates

1. Fire should keep at least two front-row attackers when possible; resource companions belong behind them or should be limited.
2. Renewable equipment plus 梵天 provides enough fire to attack, learn, and cast in the same turn. Spend equipment markers while they convert into concrete board or card advantage.
3. `烈焰反噬` plus a three-power boost is a reliable six-defense package that can preserve a fragile lethal attacker.
4. Cast `激情之火` before likely-to-hit fire spells; the extra draw can directly produce scroll-based finishers.
5. Clear all enemy front-row units before targeting the hero with unit attacks or target-selection workflows.

## Product / bug observation

### Reproducible target-path inconsistency

With the opponent's front row empty:

- Direct `cast_spell` using `焚烧` with `target_type: hero` was rejected with `spell cannot target hero`.
- `速写卷轴` copying `焚烧` presented the enemy hero as its only legal target and successfully dealt damage.
- Later, `速写卷轴` copying `火球术` again presented the enemy hero as its only legal target and won the game.

This is not a card-text mismatch, but it is a backend legality inconsistency between normal casting and the sketch-scroll continuation path. The transcript contains both the rejected direct action and the successful copied-spell actions.

No confirmed card-text-versus-runtime-effect mismatch was found in this match.
