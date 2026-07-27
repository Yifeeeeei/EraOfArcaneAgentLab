# Player A Review — series-18 room 0731

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Deck: `WATER-PRESSURE-SCRY-001`
- Opponent: `WIND-RUSH-005`
- Result: loss, winner player 1, turn 26
- Transcript: `player-a.jsonl`

## Match summary

Water used `水占术` to find both `南海海怪`, deployed each into the reserved center attacking slot, and protected both once with `海豚伙伴`. Wind nevertheless concentrated unit attacks, two `连锁闪电卷轴`, the hero ultimate, and repeated piercing spells to remove both attackers. Water then transitioned into a durable defensive shell built around `冰刺堡垒`, `冰锥术`, `冰雹术`, `霜冻射线`, and `玛涅斯之杖`.

The defensive package repeatedly matched Wind's four-, five-, and seven-power attacks. `冰刺堡垒` also froze and later killed the first enemy `屠魔者杀手`. Water cleared several later blockers through three-spell sequences, but all remaining Water units had no attack and ordinary spells could not target the enemy hero. With both decks empty and no deck-out loss, Water had no remaining win condition. Wind retained `闪电链` as a legal route through Water's units to the hero via its extra target and won on turn 26.

## Decisions that worked

- Reserved the center or right front position for actual attackers during the early and middle game instead of filling every front slot with resource companions.
- Used `水占术` to prioritize the second `南海海怪` and later attack scrolls rather than accumulating only support units.
- Two `海豚伙伴` each prevented lethal damage to a sea monster, forcing Wind to spend additional removal.
- `寒冰爆裂卷轴` defended a sea monster at equal or higher power, then a later copy killed two enemy units through splash.
- `冰刺堡垒` converted repeated incoming damage into freeze, then killed an already frozen one-life attacker.
- `玛涅斯之杖` materially changed defense thresholds: `冰锥术 + 冰雹术` reached six, and `霜冻射线 + 冰雹术` reached seven.
- On turn 23, sequencing three attack spells forced Wind through hero overexertion, unit overexertion, and finally an undefended kill.

## Decisions to improve

- Both sea monsters were deployed into a matchup where Wind could chain many one-damage effects. Their protection delayed removal but did not create enough attacks before dying.
- Once both sea monsters and both neutral killers were gone, Water should have explicitly recognized that the remaining deck had no unit-attack route to the hero. The later support summons improved survival but could not change the outcome.
- Defensive spell selection should preserve at least one attack spell for the following own turn. Using `霜冻射线 + 冰锥术` for a large defense can leave `冰雹术` available; repeatedly using `冰雹术` as the boost delayed counter-pressure.
- The first-turn killer summon was sent immediately after mulligan/start actions and failed for insufficient elements, while an identical three-water payment succeeded later. The exact cause was not isolated; future agents should wait for the post-mulligan authoritative state before batching the first turn.
- A few actions were issued while the opponent still had an end-turn discard pending. Always verify `phase: main` and `current_turn` rather than relying only on a peer progress message.
- Water eventually filled all six unit positions with non-attacking bodies. At that point the deck and hand contained no future attacker, so this did not block a real card, but it confirms the deck's terminal-state weakness.

## Reusable strategy updates

1. Track remaining hero-damage sources explicitly: two neutral killers, two sea monsters, attack scrolls, and square/splash damage are not interchangeable.
2. Protect an attacker only when it is likely to make at least one further attack; otherwise preserve defense cards for the hero or a fortress.
3. Against Wind's repeated defense, plan three successive attack spells in one turn. The first can consume hero resources, the second consumes unit resources, and the third is most likely to resolve.
4. With `玛涅斯之杖`, prefer defense combinations that leave one attack spell vertical for the next own turn.
5. Empty decks do not currently end the match. Do not assume fatigue or deck-out is a win condition.

## Product / bug observations

### Water-divination candidate list is broader than legal selection

`水占术` displayed a neutral `屠魔者杀手` among the four `candidates`. Selecting it was rejected with `invalid selection`; selecting a Water card then succeeded. The final legality matches the printed text (search one Water card), but the machine-facing candidate list includes cards that cannot be selected. An agent that treats `candidates` as authoritative can waste an action and context.

### Empty-deck behavior

Both players reached `deck_count: 0`. Draw attempts simply produced no card and did not cause damage or defeat. This remained stable over many turns. It may be intended, but it materially enables long terminal states and should be documented in the protocol/rules if intentional.

No confirmed card-text-versus-runtime-effect mismatch was found in this match.
