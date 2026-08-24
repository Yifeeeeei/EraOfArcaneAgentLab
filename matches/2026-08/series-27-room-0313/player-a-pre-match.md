# Player A pre-match hypothesis — Series 27

- Deck ID: `EARTH-MOBILE-BEATDOWN-003`
- Parent: `EARTH-MOBILE-BEATDOWN-002`
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Exact deck code:

`4411101 // 1021011 1021011 1021013 1021013 1401002 1401002 1401101 1401101 1421012 1421012 1421013 1421013 1421016 1421016 1421101 1421101 1421102 1421102 1421114 1421114 2421002 2421002 2421008 2421008 2421009 2421009 2421110 2421110 2421111 2421112 // 3021001 3421003 3421004 3421101 3421103 3421104 3421107 3421108 3421109 3421110`

## Complete iteration from 002

Removed from the main deck (eight cards):

- `传送法师` x2 (`1321013`): fixed Air entry cost was not reliably payable.
- `传送符文` x2 (`2321011`): fixed Air trigger payment made the bridge nonfunctional.
- `拜利兰森林熊` x1 (`1421104`): six-cost prevention did not advance the clock.
- `岩壁魔怪` x1 (`1421111`): passive blocker occupied draws without accelerating a real attacker.
- `岩壁修道士` x2 (`1421113`): its no-skill prevention delayed the seven-Earth breakpoint and conflicted with the new payable movement skill.

Added to the main deck (eight cards):

- `普通蜥蜴` x2 (`1401101`): one-cost native-Earth source; converts Jade's turn into five Earth immediately and is cheap to place outside center-front.
- `林地飞鼠` x2 (`1421012`): one-cost native-Earth source with two life; its temporary-Air ability is incidental, not required by the list.
- `岩壁刺球` x2 (`1421101`): three-cost native-Earth source producing two Earth, a cleaner bridge to six/seven-cost attackers.
- `食腐者` x2 (`1421016`): two-cost, three-life native-Earth bridge that can create two Earth after another friendly unit takes enemy damage.

Skill-deck changes:

- Removed `苍岚之刃` (`3421102`), `苍老之触` (`3421105`), and `腐朽侵蚀` (`3421106`) because each required fixed Air or Shadow payment.
- Added `移形换影` (`3021001`) as an Earth-payable one-cost lane bridge.
- Added `裂地重击` (`3421003`) as a lower-cost Earth-only attack spell.
- Added `再生之力` (`3421004`) as an Earth-only reset bridge for a physical attacker.

## Five-part deck reading

### 1. Engine

Jade produces four Earth. Lizard and Squirrel each cost one and later produce one; Spikeball costs three and produces two; Scavenger can add two temporary Earth when friendly units are damaged. The engine's job is narrow: reach six Earth for Sandworm or seven for Rock Beast without filling center-front with support bodies.

Resource placement discipline:

- Lizard/Squirrel/Spikeball go to side-middle or rear cells.
- Scavenger may occupy a side-front cell as a damage trigger/blocker, but never center-front unless it prevents immediate lethal.
- Stop adding resource bodies once the board produces at least six Earth and a finisher is in hand.

### 2. Clock

The repeated legal hero-damage cards are:

- early: Xinke, Rapid Killer, Warrior;
- late: two Sandworms and two Rock Beasts;
- extra attack: Growth Potion, Autumn Jewel, or learned Regeneration Power after a meaningful first attack.

The deck must present a center-front attacker no later than turn 4. A defensive board without a named attacker this turn is not progress.

### 3. Bridge

- Forest Arrow and Stonehenge soften or clear blockers.
- Spatial Shift is now the only movement bridge and costs one wildcard, so any Earth source can pay it. It should move an already-used attacker out of center-front and move/place the next ready attacker into the lane.
- Growth Potion and Autumn Jewel reset native-Earth attackers.
- Sandworm Bait searches a six-plus-cost Earth body and discounts Sandworm, shortening the real breakpoint.
- Learning Spatial Shift disables no-skill synergies, but those bodies were removed; this is an intentional architecture change.

### 4. Breakpoints

- Jade alone: four Earth, enough for Warrior but not a heavy Earth attacker.
- Jade + one Lizard/Squirrel: five Earth.
- Jade + one Spikeball: six Earth, enough for Sandworm.
- Jade + two one-Earth sources: six Earth, enough for Sandworm.
- Jade + Spikeball + one one-Earth source: seven Earth, enough for Rock Beast.
- A Sandworm found by Sandworm Bait costs four, so Jade alone can deploy it on the following legal summon turn.

Do not again submit a seven-Earth payment merely because multiple Earth cards are present; inspect exact current loads in authoritative state.

### 5. Cadence

Before every summon, name both attackers:

- **this turn:** the unit that attacks from center-front now;
- **next turn:** the ready replacement, reset line, or Shift destination.

Preferred sequence: attack with center unit, Shift it to a side/rear cell, summon or move a ready attacker into center, then attack if it has Rapid or has been reset. If no replacement exists, do not consume the only attacker for support value. Side-front attackers are acceptable only when their own column is open or Shift is already learned and payable.

## Opening and first three turns

Mulligan priority:

1. Keep Rapid Killer, Warrior, Xinke, or Sandworm Bait plus at least one one/three-cost Earth source.
2. Keep Rock Beast only with a credible seven-Earth production table; keep Sandworm with Spikeball or two cheap Earth sources.
3. Do not keep multiple resets/movement cards without an attacker.
4. A hand of Guard/support bodies without an attacker is a full mulligan even if it has excellent nominal resource value.

Turn plan:

- Turn 1: establish one cheap side resource or an immediate attacker; never place support center-front.
- Turn 2: put the first real attacker in center-front or use Sandworm Bait while preserving the next-turn six-Earth line.
- Turn 3: attack first. Only then deploy support. If the opponent clears center, the next ready attacker must already be in hand or on a side cell with Shift payable.

## First-match measurement metrics

Record these precisely in the review:

1. Turn when the first center-front attacker became ready and turn of first hero damage.
2. Earth production available at the start of each own turn; first turn reaching six and seven payable Earth.
3. Number of own turns with a legal physical attack, number with a center-front attacker but no legal attack, and total physical hero damage.
4. For every center attacker that leaves/dies, whether a named next-turn replacement existed; target replacement coverage at least 75%.
5. Number of cards/actions stranded by fixed off-color payment; target zero.
6. Number of support/resource summons into center-front; target zero except to prevent immediate lethal.
7. Whether Spatial Shift, Growth Potion, Autumn Jewel, or Regeneration Power actually created an additional attack rather than merely moving/resetting for value.
8. Sandworm/Rock Beast deployment turn and whether each attacked before dying or the game ended.
9. Cards remaining in hand at game-over that could not affect the clock within one turn.

## Experimental hypothesis

Replacing the unsupported Air bridge and slow passive shell with eight cheap native-Earth sources should move the six-Earth breakpoint before the opponent's turn-10 clock while keeping all ten physical attackers. A payable Spatial Shift plus Earth resets should then convert that earlier deployment into at least one additional physical attack and avoid both the Series25 lock and the Series26 delayed-finisher failure.
