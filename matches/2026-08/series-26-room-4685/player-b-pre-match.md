# WINDLESS-BLOOD-GARDEN-002 — pre-match driving hypothesis

Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`

## Exact deck

```text
4611101 // 1021011 1021011 1021013 1021013 1611102 1611102 1611103 1611103 1621001 1621006 1621006 1621011 1621011 1621016 1621016 1621107 1621107 1621112 1621112 1621113 2611001 2611001 2621005 2621006 2621101 2621101 2621108 2621108 2621109 2621109 // 3021001 3021008 3621001 3621003 3621004 3621010 3621013 3621101 3621102 3621103 //
```

## Changes from WINDLESS-BLOOD-GARDEN-001

Main deck:

- Remove 2 `苦痛之魂` (`1621101`). Its load growth converted self-harm into more resources but did not shorten the clock.
- Remove 2 `鲜血傀儡` (`1621103`). The self-damage helped Robert but was a weak standalone draw and occupied the central attack lane.
- Remove 1 `冥界信鸽` (`1621001`) and 1 `谧语精灵祭司` (`1621113`). Keep one copy of each utility deathrattle but reduce the density of zero-attack bodies.
- Add 2 `屠魔者杀手` (`1021011`). They are immediate 1-attack clocks and can exploit a lane on the turn it opens.
- Add 2 `屠魔者武士` (`1021013`). They provide a durable positive-attack front body that does not require Robert markers.
- Add 2 `梦魇` (`1621006`). It starts at 1 attack and gains life from the same friendly-death engine, turning sacrifice activity into board pressure rather than only dark.

Skill deck:

- Remove `血蔷薇咒印` (`3621104`). Its one-time entry mark was too conditional for the actual control plan.
- Remove `噬血` (`3621002`). More healing is less valuable than a way to preserve the attack lane.
- Add `移形换影` (`3021001`). This is the explicit correction for the rear-row Rose Reaper failure: move a stranded attacker into an open front slot.
- Add `缴械` (`3021008`). It supplies a concrete equipment answer, especially against prevention equipment such as Emerald Eternity.

## Read the deck before playing

### Primary win condition

The primary clock is now ordinary front-row combat from Rose Reaper, Demon Slayer Warrior, Demon Slayer Killer, and Nightmare. Robert is a secondary scaling attacker, not the only way to produce positive attack. Whisper Hunter and Vengeful Dead remain reach, but they are not the plan by themselves.

The deck should win by presenting at least one positive-attack front unit while its spells/deathrattles clear the corresponding enemy lane. It must not spend ten turns proving that the resource engine works.

### Critical growth thresholds

- Robert starts at printed -1 attack. The first three markers only raise him to 0; he needs six markers and two `+1攻` choices to become a real 1-attack clock.
- The clean six-marker line is two friendly one-life Feast kills while Robert is present. White Bone Knight is best: its first death produces three markers and it returns for the second three-marker cycle.
- Nightmare already attacks for 1. Every friendly death that grows its life makes it safer to leave in the front, but no growth is required before it starts attacking.
- Rose Reaper needs no growth; its threshold is simply six dark plus an open front slot.

### Attack-square discipline

- Never summon Rose Reaper to a rear square unless `移形换影` is already learned, affordable, and there is a concrete next-action move into the front.
- Reserve the center-front square for the current or next-turn attacker. Zero-attack bodies go to side front/middle/rear squares unless their sacrifice will immediately free the center.
- Robert belongs in front only when a six-marker plan exists or when the opponent cannot remove it before the second upgrade. Do not use Robert as ordinary payment after it reaches positive attack.
- Keep one front slot open when holding Slayer Killer; its speed is valuable only if it can enter and attack immediately.
- `移形换影` is not generic convenience. Save it for rescuing a positive-attack unit from the rear or switching an attacker into the lane that exposes the enemy hero.

### Opening and first three turns

Opening priority: one independent dark source; then a positive-attack body or Robert plus White Bone Knight; then Wand/Death Magic Stone. Mulligan hands composed only of deathrattle utility and resource items.

- Turn 1: develop a cheap positive attacker if possible. Robert is acceptable only with Knight/Hunter and a near-term Feast line.
- Turn 2: bind Blood Feast or learn the spell that opens the attacker's lane. Establish Wand/Stone only if doing so does not postpone the first attacker beyond turn 3.
- Turn 3: have a front-row positive attacker or a Robert at three markers with the second three-marker sacrifice already available. If neither is true, stop adding engine pieces and play the best available attacker.

### Resource discipline

Death Magic Stone and Wand are sufficient long-game resources. Do not deploy redundant Coffin/Necklace-style value solely because dark remains. Spend accumulated dark on Reaper plus lane-clearing actions in one turn. Preserve one vertical source only when a Blood Thorn return or Feast continuation is actually pending.

### When self-harm stops

Stop sacrificing for resources and turn fully aggressive when any one condition holds:

1. Robert reaches 1 attack;
2. Rose Reaper or another positive attacker has a legal hero lane;
3. Death Magic Stone already holds at least 5 dark;
4. the opponent has four life or less and Whisper Hunter/Vengeful Dead plus one physical hit forms a two-turn clock.

After this point, a self-hit is allowed only if it immediately clears a lane, grows Robert to the next attack threshold, triggers direct damage, or pays for the same-turn finisher. “Gain two more dark” alone is not sufficient.

### Key exchange recognition

A strong sacrifice must do one of the following: produce three Robert markers, deal direct enemy-hero damage, recur White Bone Knight/Blood Thorn, or fund a same-turn Reaper/Slayer attack. A sacrifice that merely adds dark while Death Magic Stone is already loaded is a losing tempo exchange.

Against prevention equipment, learn `缴械` early and preserve a legal target/payment line. Against a rear-row attacker problem, learn `移形换影` before committing the attacker. Against first-spell prevention, bait with the cheapest spell and do not waste Blood Soul Slash as the zero-attack spell.
