# Player A review — Series 26

- Match: `series-26-room-4685`
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Player/deck: `official-series26-a` / `EARTH-MOBILE-BEATDOWN-002`
- Result: loss, official `game_over`, winner slot 0 (B), turn 10
- Final life: Jade 0, Hubert 6
- Wall-clock transcript span: about 17 minutes
- Transcript: `agent-data/matches/series-26-room-4685/player-a.jsonl`

## Exact deck code

`4411101 // 1021011 1021011 1021013 1021013 1321013 1321013 1401002 1401002 1421013 1421013 1421102 1421102 1421104 1421111 1421113 1421113 1421114 1421114 2321011 2321011 2421002 2421002 2421008 2421008 2421009 2421009 2421110 2421110 2421111 2421112 // 3421101 3421102 3421103 3421104 3421105 3421106 3421107 3421108 3421109 3421110`

## Match outline

- Mulliganed a no-attacker hand (two Growth Potions, Monk, Stonehenge) and found two Guards, Monk, Teleport Mage, Sandworm Bait, then Xinke.
- Sandworm Bait found Forest Bear rather than an attacker. Guard entered left-middle and center-front stayed open as planned.
- Two successive Xinkes occupied center-front but both were killed by Rose Reaper before generating an attack. Rapid Killer then killed Whisper Hunter; its deathrattle dealt direct hero damage through Jade's shield.
- Forest Arrow reduced Reaper to 2 life; the second Rapid Killer reduced it to 1; Stonehenge finally killed it and also reduced Hubert and Robert by 1. This was the best exchange sequence of the game.
- A center Warrior killed the now-developed Robert, but was then killed exactly by Blood Explosion. B moved its Warrior into center and kept converting the open lane into physical hero damage.
- I added Monk left-rear to reach seven earth on the following turn without occupying center-front. Before that payoff, B used movement, Rapid Killer, and a Hunter deathrattle to deal the final two hero damage and end on turn 10.

## Pre-match hypotheses: what held

1. **Center-front must be reserved for a real attacker — held.** Guard and Monk were correctly placed outside center-front. Xinke, Rapid Killer, and Warrior all used the attack cell. The deck no longer produced the Series25 passive-board lock.
2. **Physical damage bypasses the shield lock — held, for both sides.** B's Robert/Warrior attacks and Hunter deathrattle damaged Jade while shield 2 remained. Removing Jade Immortality was directionally correct: the match ended normally instead of drawing.
3. **Scrolls are setup, not finishers — held.** Forest Arrow and Stonehenge each dealt only 1 attack damage. Their value came from chaining them with Rapid Killer/Warrior attacks, not from expecting power to equal damage.
4. **Do not learn a skill without an immediate finish — held.** I learned no skill, preserving Monk's first-spell prevention and avoiding a slow mana sink.
5. **Movement is strategically decisive — held, but demonstrated more strongly by B.** B repeatedly vacated or reclaimed center-front with Shift and immediately converted the new position into attacks.

## Pre-match hypotheses: what failed or was incomplete

1. **The deck still reaches its heavy attackers too slowly.** Jade plus one Guard produces only five earth; Rock Beast costs seven. I incorrectly read Guard as producing three and submitted a seven-earth payment on turn 9. The engine correctly rejected it. Adding Monk on turn 10 would have made seven next turn, but the game ended first.
2. **Keeping center-front open is not enough; the attacker must survive or have haste/reset.** Both Xinkes and both Rapid Killers were traded immediately. The plan named the correct cell but did not specify a minimum attack cadence or protection threshold.
3. **The movement package was not payable.** Teleport Mage requires fixed air and I never established an air source. Xinke can supply air, but both copies had to enter reactively and died before they could be consumed. The discarded Teleport Rune likewise could not be paid from an earth-only board.
4. **The mulligan rule was too permissive toward passive earth hands.** The replacement hand still lacked a durable attacker; Sandworm Bait is not reliably an attacker because it can hit Forest Bear. A six/seven-cost finisher without an accelerated earth curve is not an early keep, but the list also needs more independent early attack draws.
5. **The deck did not account for direct damage that ignores shield.** Guard/Jade shield bought no protection against Hunter deathrattle, while non-attacking bodies consumed draw and board slots. Against dark sacrifice, killing Hunter can advance the opponent's lethal clock.
6. **I batched actions across a possible trigger boundary once.** On turn 9 I sent attack, two consumes, summon, and end-turn together. Although the attack itself resolved cleanly, this made the subsequent rejected summon and discard window harder to reason about. Future pilots should wait for authoritative state after every kill, summon, and end-turn.

## Pilot errors and bug assessment

- Pilot error: treated Guard's `elements_gain:{地:1}` as three earth, attempted Rock Beast with only five earth, then had to abandon the summon.
- Pilot error: initially answered the discard window with the nonexistent action name `resolve_pending`; the correct protocol action is `resolve_action`.
- Timing discipline error: sent several actions without waiting for the authoritative state after Robert died.
- No confirmed game bug was found from Player A's side. Blood Explosion killing the 2-life Warrior, physical/deathrattle damage bypassing shield, and the rejected seven-earth summon all matched authoritative state and card/rule behavior.

## General rules for reading and piloting this kind of list

1. **Convert costs into a turn-by-turn production table before calling a card a finisher.** A seven-cost attacker is not a turn-five plan merely because the deck contains several earth cards; count the exact printed gain of the bodies expected to survive.
2. **Separate lane access from attack cadence.** An empty center-front is only potential. A winning list also needs enough ready attackers, haste, reset, or protection to produce hero damage before the opponent reclaims the lane.
3. **Audit off-color packages as complete circuits.** A fixed-air movement card requires a reliable surviving air source. If that source is also a fragile attacker, the package is not independently functional.
4. **Classify every body as attacker, accelerator, protection, or brick in the current matchup.** Once acceleration reaches the finisher threshold, stop deploying more protection bodies. If the finisher threshold arrives after the opponent's expected lethal turn, the curve itself is wrong.
5. **Against sacrifice/deathrattle, evaluate the death event before taking a favorable-looking trade.** Killing a 1-life Hunter may remove a unit but still lose the hero race through direct deathrattle damage.
6. **Use removal only when it changes the next attack.** Forest Arrow plus Rapid Killer plus Stonehenge eventually removed Reaper, but required three cards/attack events. Before committing, identify which ready attacker converts the cleared lane that turn or next turn.
7. **For headless play, every kill, summon, reactive trigger, and end-turn is a synchronization boundary.** Send one action, wait for authoritative `state_sync`, inspect private pending events, then continue.

## Next iteration

- Keep the no-lock principle and real-attacker center discipline.
- Either remove the fixed-air Teleport package or add earth-compatible/reliable air production that does not depend on Xinke surviving.
- Lower the attack curve: add more independently playable one-attack bodies or true haste attackers; do not rely on seven earth arriving after turn 10.
- Reduce passive support density further. Monk was correctly positioned and potentially useful, but on turn 10 it was still a one-turn-delayed ramp piece while the opponent had a two-damage finish.
- Add a concrete response to deathrattle reach: race faster, avoid killing Hunter when it creates lethal, or include a way to remove/exile/silence without triggering the normal death payoff if the card pool supports it.
