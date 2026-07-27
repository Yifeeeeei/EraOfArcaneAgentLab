# Player A Review — series-20 room 2976

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Deck: `FIRE-BURN-004`
- Opponent: `WATER-PRESSURE-SCRY-001`
- Actual slot: player 1
- Result: win, winner player 1, turn 10
- Transcript: `player-a.jsonl`

## Match summary

Fire kept an item-heavy opening, learned `火球术`, and used `活泼的炉火` plus the growing output of `大祭司 梵天` to establish a large resource engine. Water's opening neutral killer dealt one damage, but Fire removed it immediately. Fire then deployed its own `屠魔者杀手`, repeatedly removed both `南海海怪`, and equipped `凤凰之羽` to increase spell damage.

Water rebuilt behind `冰原狼`, `海豚伙伴`, `寒冰屏障`, and staff-enhanced defense spells. Fire forced multiple defenses with successive attacks, then used two `火焰箭` as direct-damage attempts. The first reduced the Water hero to one. The second lethal arrow was prevented by the dolphin's hidden reaction pending. Fire finally exhausted both learned defense spells, found the center wolf absent from the authoritative board after resolution, and used the neutral killer to deal the final point to the hero on turn 10.

## Decisions that worked

- Preserved the opening `凤凰之羽`; its attack increase let small Fire spells remove four-life sea monsters efficiently.
- Used `焚烧` and `火球术` in successive attacks to exhaust Water's defense resources rather than relying on one large spell.
- Removed both sea monsters before either established repeated hero attacks.
- Kept `屠魔者杀手` alive through a five-power attack. Despite later reset irregularities, it eventually delivered three hero attacks, including lethal.
- Converted the wide resource board into enough Fire to equip and activate `火焰箭` while still retaining spell pressure.
- Recognized the second arrow as a deterministic future damage source and equipped it one turn early.

## Decisions to improve

- Turn 1 batched consume, learn, and summon actions too aggressively. The furnace summon failed with `not enough elements`; actions that depend on the prior authoritative resource total should be sent sequentially.
- The first defensive investment in the one-life killer was expensive. It succeeded strategically, but only because the killer later became the primary hero-damage route.
- Several actions were resent after delayed state events. This generated harmless `not in main phase`, `not your turn`, and duplicate-action errors. Wait for the new authoritative state or inspect the transcript before retrying.
- Fire filled all eight non-hero unit positions. This prevented summoning the second killer and narrowed later tactical options.
- Some attack scrolls were aimed at back-row units before checking range; both attempts were correctly rejected.

## Reusable strategy updates

1. Against Water, use successive attacks in one turn: the first consumes the hero or a support unit, the second consumes another source, and a unit attack can finish without a defense window.
2. `凤凰之羽` materially improves low-attack Fire spells and scrolls; include its modifier when planning exact sea-monster kills.
3. `火焰箭` enters horizontal and cannot be sacrificed on the equip turn. Equip it one turn before the intended direct damage.
4. `火焰箭` activation is two-stage: use the ultimate ability, then resolve `fire_arrow_damage` with a candidate instance ID.
5. `海豚伙伴` can prevent lethal damage to the hero, not only companions. Do not count a one-point arrow as lethal while an enemy dolphin remains.
6. Preserve at least one board slot for a future attacker; a full board of resource bodies can lock a second killer out of play.

## Product / bug observations

### Opponent-only reaction pending appears as a temporary null-pending wait

When the second `火焰箭` targeted the one-life Water hero, the A client saw its own pending clear and the arrow move to the graveyard, then received `phase: waiting_action` with no visible `pending_action`. A initially interpreted this as a soft lock. The B client had an exclusive `dolphin_prevent_lethal` pending and sacrificed `海豚伙伴`; after B resolved it, A returned to main phase.

This is valid hidden decision ownership, but the machine protocol should explicitly explain that `waiting_action` with no local pending may mean the opponent has a private reaction. Agents should ask the opponent to resolve rather than retrying actions or declaring a lock.

### Killer remained horizontal across multiple owner end turns

After Water's `水形之束卷轴` targeted the Fire `屠魔者杀手`, Fire fully defended the spell at seven power. The killer nevertheless remained horizontal through several later Fire turns and repeatedly rejected attacks with `attacker is horizontal`. It eventually became vertical again later without an obvious new reset event.

The scroll's hit effect is to turn the partner horizontal, so a fully defended attack should not apply it. Even if some other effect correctly turned it horizontal, normal owner end-turn reset should restore it unless a visible freeze/cooldown state prevents reset. The transcript should be reviewed against server room logs before filing.

### First-turn failed summon and resource accounting

On turn 1, Fire consumed its four-output hero, learned `火球术`, then attempted to summon `活泼的炉火` with two Fire. The summon returned `not enough elements`, and the next state showed zero elements. Because the actions were batched, the exact ordering and whether the failed payment consumed anything was not isolated. The same furnace summon succeeded normally on turn 2 when sent after an authoritative consume state.

No confirmed printed card-text mismatch was found. The dolphin preventing hero lethal is consistent with “another friendly unit” if the hero counts as a unit, but this rule should be explicit for agents.
