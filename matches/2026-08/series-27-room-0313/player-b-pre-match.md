# WINDLESS-BLOOD-GARDEN-002 — Series 27 controlled retest

Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`

The deck is intentionally identical to Series 26. This match changes only the driving policy so the damage sources and attack cadence can be measured independently of deck construction.

## Exact deck

```text
4611101 // 1021011 1021011 1021013 1021013 1611102 1611102 1611103 1611103 1621001 1621006 1621006 1621011 1621011 1621016 1621016 1621107 1621107 1621112 1621112 1621113 2611001 2611001 2621005 2621006 2621101 2621101 2621108 2621108 2621109 2621109 // 3021001 3021008 3621001 3621003 3621004 3621010 3621013 3621101 3621102 3621103 //
```

## Five-part deck reading

### 1. Engine

Hubert supplies four dark per normal turn and creates Blood Feast. Blood Feast converts expendable friendly companions into two dark or one life; White Bone Knight, Whisper Hunter, Blood Thorn, Death Magic Stone, Coffin, and the deathrattle package make those friendly deaths non-blank. Robert converts friendly damage/death into permanent stats.

The engine is successful once it pays for a same-turn attacker, blocker removal, or direct-deathrattle reach. Accumulating dark without changing the attack clock is not engine success.

### 2. Clock

The repeatable hero clock is physical front-row damage from Rose Reaper, Demon Slayer Warrior, Demon Slayer Killer, Nightmare, and a fully grown Robert. Whisper Hunter and Vengeful Dead are reach, not the repeatable clock.

Priority among clocks:

1. a positive attacker already able to hit this turn;
2. a hasty Killer that can take a newly opened center;
3. Rose Reaper entering an uncontested front square;
4. Robert only after six markers make its current attack at least one.

### 3. Bridge

Spatial Shift is the primary bridge. It moves an attacker into the center lane, or moves an already-used center attacker aside so a second/hasty attacker can use the same square. Blood Demon Blast and ordinary attack spells clear blockers. Disarm bridges through prevention equipment rather than through units.

The bridge is not merely “move something.” Before casting Spatial Shift, name both the unit leaving a square and the unit/action consuming the opened square.

### 4. Breakpoints

- Robert: three markers only changes printed -1 attack to 0; six markers and two attack rewards are required for 1 attack.
- Rose Reaper: six dark plus an actual front slot; rear-row Reaper is below breakpoint regardless of available dark.
- Blood Demon Blast: must already be learned/reset before the desired same-turn removal turn; learning it that turn is not a usable breakpoint because it enters horizontal.
- Death Magic Stone: five dark is the “stop farming” threshold from the prior plan, but any amount sufficient for the named same-turn bridge/clock sequence should be spent immediately.
- Lethal reach: a center-front hasty Killer is one damage; a controllable Whisper Hunter Feast death is another one damage. At opposing hero life two, those two cards plus an open center are a complete finish.

### 5. Cadence

At the start of every turn, explicitly name:

- **This turn's attacker:** the unit that will actually become horizontal from attacking the hero or the blocker that directly gates the hero.
- **Next turn's replacement:** the positive attacker held/developed for the same lane if the first attacker dies or remains out of position.

Do not fill center-front until both names are known. Side front is a staging square for Warrior/Robert; center front is for the current hit. Spatial Shift should recycle center after the current attacker has attacked whenever a hasty follow-up exists.

## Controlled damage-source prediction

Track every point of opposing hero-life loss in three exclusive buckets:

1. **Robert growth:** physical hero damage dealt by Robert after marker upgrades.
2. **Generic attackers:** physical hero damage from Rose Reaper, Demon Slayer Warrior, Demon Slayer Killer, or Nightmare.
3. **Deathrattle reach:** hero damage from Whisper Hunter or Vengeful Dead death effects.

Pre-match expected contribution to the six-life kill:

| Source | Expected damage | Confidence | Reason |
|---|---:|---|---|
| Robert growth | 0–2 | Medium | Six markers are achievable, but Robert is slow and fragile; it should not be forced if generic attackers already clock. |
| Generic attackers | 2–4 | High | The unchanged list has six native positive attackers plus two Reapers; Series 26 dealt four points this way. |
| Deathrattle reach | 1–3 | High | Two Hunters are controllable with Feast and bypassed shield in Series 26; Vengeful Dead adds conditional reach. |

Primary hypothesis: **generic attackers will again be the largest damage bucket**, while Robert contributes at most one or two points. If Robert deals the majority, Series 26's generic-attacker conclusion was draw-dependent. If deathrattle reach deals the majority, the deck should be reclassified as a reach/combo deck rather than physical beatdown.

## Driving policy for this retest

### Mulligan

Keep an opening containing either a native positive attacker or Robert plus a visible six-marker line (preferably White Bone Knight + Feast access). Reject hands made only of items, zero-attack deathrattles, and expensive Reapers without a two-turn six-dark path.

### First three turns

- Establish or stage a positive attacker by turn 2.
- Reserve center front for the first real attack, not a resource body.
- Robert may be developed off-center only when two three-marker cycles are named in advance.
- Learn Spatial Shift before a staged attacker becomes trapped; learn Blood Demon Blast one turn before it is needed.

### Transition to attack

Stop optional self-harm once any of these occurs: Robert reaches one attack; a generic attacker has a legal lane; Death Magic Stone can fund attacker plus bridge; or opposing life is within Hunter/Killer reach. Thereafter, Feast is legal only for direct reach, the exact next Robert breakpoint, or same-turn bridge payment.

### Matchup response

- First-spell prevention: cheapest legal bait first.
- Shield/prevention equipment: learn Disarm before the lock is complete.
- Repeated cheap blockers: trade with Reaper/Warrior, but keep the next attacker staged.
- Empty center: take hero damage immediately; do not develop another value permanent first.

## Experiment success criteria

The retest succeeds as evidence even if it loses, provided the review can answer:

1. exact hero damage in all three buckets;
2. whether a positive attacker was staged by turn 2;
3. whether every Spatial Shift named a concrete before/after cadence;
4. whether any self-hit occurred after the stop threshold without advancing lethal;
5. whether the unchanged deck again produces a real clock before late prevention.
