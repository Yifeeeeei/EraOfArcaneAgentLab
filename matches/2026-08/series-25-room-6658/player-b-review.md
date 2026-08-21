# Series 25 Player B review — WINDLESS-BLOOD-GARDEN-001

- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Match: `series-25-room-6658` (room `6658`)
- Result: `adjudicated_draw`
- Engine state at adjudication: turn 30, `phase=main`, `winner=-1`; the backend never emitted `game_over`.
- Transcript: `agent-data/matches/series-25-room-6658/player-b.jsonl`
- Wall-clock transcript span: 2026-08-21 16:33:37Z–17:29:14Z (about 55m36s)

## Exact deck

Deck ID: `WINDLESS-BLOOD-GARDEN-001`

```text
4611101 // 1611102 1611102 1611103 1611103 1621101 1621101 1621103 1621103 1621112 1621112 1621113 1621113 1621001 1621001 1621011 1621011 1621016 1621016 1621107 1621107 2621101 2621101 2621108 2621108 2621109 2621109 2611001 2611001 2621006 2621005 // 3621101 3621102 3621103 3621104 3621001 3621002 3621003 3621004 3621010 3621013
```

## What happened

The dark self-sacrifice engine functioned, but the deck could not close against a zero-skill Jade fortress. Blood Feast repeatedly converted expendable companions into dark or healing; Black Pine Wand reduced Blood Feast to zero; Death Magic Stone reached 12 dark load; Robert correctly gained three markers from a friendly one-life unit being damaged and killed by Blood Feast. Whisper Hunter deathrattles dealt the only early direct hero damage, reducing Jade from 6 to 4, and an enemy kill of Vengeful Dead later reduced Jade from 4 to 2.

The middle game became a long control sequence. Rock Monk nullified the first enemy spell hit each turn, so the reliable ordering was cheap Shadow Shock first, then real damage. Death Harvest repeatedly cleared Earth front rows, while Blood Soul Slash provided excellent sustain. The opponent eventually equipped Emerald Eternity with shield 2. Jade prevented shield decay below 3, and Emerald Eternity prevented all damage to friendly units while any shield remained. Robert was finally grown to 1 attack and legally attacked Jade, but the damage was prevented without reducing shield.

At turn 30 both decks were empty and neither side had a state-changing legal line. The match was therefore stopped as an adjudicated draw rather than burning infinite empty turns.

## Pre-match hypotheses: verdicts

| Hypothesis | Verdict | Evidence |
|---|---|---|
| Blood Feast plus deathrattles is a real value engine | Confirmed | Feast killed Blood Puppet/White Bone Knight, generated dark or healing, triggered Robert and Death Magic Stone, and Knight returned once. |
| Black Pine Wand bridges the engine | Confirmed | Its friendly-target discount made Blood Feast cost 0. |
| Robert can be the physical finisher | Partly confirmed | The marker math worked exactly: friendly damage + friendly-effect death produced 3 markers. Two attack upgrades were required to move printed -1 attack to 1. He attacked legally, but entered too late and was hard-countered by Emerald Eternity. |
| Rose Reaper is the alternate physical finisher | Disproved by piloting/positioning | It was summoned to center rear on turn 16 and could not attack from the rear. There is no generic movement action. This was the decisive positioning error. |
| Whisper Hunter/Vengeful Dead provide reach | Confirmed but conditional | Two Hunter deathrattles dealt 2 total. Vengeful Dead dealt 2 only when the opponent chose to kill it; it is not controllable reach against a player who can decline the exchange. |
| Preserve an independent dark source for continuations | Confirmed | Blood Thorn recursion, Feast rewards, and multi-spell turns all depended on post-action dark. Death Magic Stone was especially strong. |
| Do not fill the board with negative-attack bodies | Confirmed, violated | Board congestion forced Rose Reaper into the rear and left the deck without an immediate physical closer after front rows were cleared. |
| Turn aggressive once Robert reaches 1 attack or Reaper has a lane | Confirmed, executed too late | Robert did not reach 1 attack until turn 28. By then Emerald Eternity had created the lock. |
| Generic attack spells are not hero finishers | Confirmed | Blood Soul Slash and Shadow Arrow repeatedly returned `spell cannot target hero`, including with the opposing center front empty and a friendly vertical center-front source present. |

## Mistakes and corrected interpretations

1. **Rose Reaper placement lost the primary finish.** Putting the 2-attack Reaper in center rear converted the best closer into a dead card. The authoritative attack error was `attacker is not in front row`.
2. **Robert was deployed far too late.** The opening/midgame spent resources on control and a Robert attempt that was killed before it reached positive attack. The second Robert only entered after both decks were empty.
3. **The turn-17/18 sequencing was inconsistent.** On turn 17 Blood Soul Slash was used before baiting Rock Monk, so its attack became 0. Against Rock Monk, the bait spell must always be first.
4. **Blood Rose Seal was initially suspected as broken, but the evidence does not establish a bug.** Its text says `入场`, so the mark is chosen when the skill enters the skill pool, not on every cast. The originally marked Sandworm died outside the printed deadline; later casts killing other units did not re-mark them. No issue should be filed from this match on that evidence.
5. **Cave Elf Pickaxe was operated through ordinary `consume` by the opponent.** The code exposes its effect through the per-turn ability path (`use_ability`, label `消耗`). Merely turning it horizontal without a pending selection is insufficient evidence of a card bug; it is an action-path mistake unless the frontend exposes the wrong action.

## Proven terminal loop audit

At adjudication, the opponent had Jade at 2 life, shield 2, Emerald Eternity, one rear Rock Monk, and one rear hidden Giant Sandworm. Their front row was empty. Player B had no deck and only Sacrifice Rune, Death Magic Stone, and Nether Pigeon in hand.

- No hand card, field card, learned skill, or equipment could destroy/disable opposing equipment or directly remove shield.
- All five learned attack skills require a legal enemy target. The rear Monk was outside spell range, the Sandworm was hidden, and hero targeting was rejected by the backend. Death Harvest had no enemy front-row target.
- Shadow Arrow's pierce does not bypass damage prevention.
- Robert and any further physical attacker could attack Jade, but the observed Robert hit was prevented and did not reduce shield.
- Vengeful Dead retaliation and Whisper Hunter-style damage are still damage and are prevented while Emerald Eternity is active; no Hunter remained anyway.
- Blood Feast can only attack friendly units. It can grow Robert further, but arbitrary attack magnitude still cannot bypass `prevent all damage` and does not consume shield.
- Jade keeps shield 2 from decaying; neither player can draw a new answer because both decks are empty; the opponent also reported no shield-spending action.

After end-of-turn resets the same position therefore recurs without any state-changing legal action. This is a genuine gameplay deadlock. It may be a valid draw state, but the engine currently has no official draw/game-over mechanism for it.

## General recognition rules

1. Against Rock Monk, count its prevention as a player-wide once-per-turn shield, not one trigger per copy: two Monks still nullified only the first spell hit. Lead with the cheapest legal spell, then commit damage.
2. Against Jade fortress, do not assume clearing the front row is sufficient. Preserve a front-row physical attacker before Emerald Eternity arrives; once shield plus prevention is established, damage cannot peel the shield.
3. A deck with many zero-attack deathrattle bodies must reserve a front slot for its closer. A rear attacker without a printed rear-attack ability is not a finisher.
4. Robert needs six friendly-damage/death markers to become a 1-attack unit from printed -1 attack. Treat one three-marker cycle as setup, not as an attack-ready threshold.
5. Death Magic Stone is the best long-game resource payoff for this shell, but excess resources do not compensate for absent legal targets or absent physical attack lanes.
6. Blood Soul Slash is a sustain/removal tool: when the hero is below maximum, its self-damage then heal yields net +1 life on hit. Do not reserve it as direct hero damage.

## Next iteration

- Keep Hubert, Blood Feast, Wand, Death Magic Stone, White Bone Knight, Whisper Hunter, and a smaller Vengeful Dead package.
- Increase true front-row attacker density; add at least two cheap/medium companions with positive printed attack rather than relying on one Reaper and a six-marker Robert process.
- Never place Rose Reaper in the rear merely to spend floating resources.
- Either deploy Robert by turn 3 with an immediate three-marker Feast line, or hold it until six markers can be produced across two turns while it remains protected.
- Add an explicit answer to equipment/shield prevention if the available card pool supports one; otherwise accept Emerald Eternity as a matchup-level hard counter and race before it enters.

