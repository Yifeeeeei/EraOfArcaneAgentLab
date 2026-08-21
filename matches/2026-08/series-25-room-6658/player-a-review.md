# Player A review — series-25-room-6658

- Result: `adjudicated_draw` (engine never emitted `game_over`)
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Deck ID: `EARTH-SHIELD-MENAGERIE-001`
- Deck code: `4411101 // 1021011 1021011 1021013 1021013 1401002 1401002 1421002 1421002 1421102 1421102 1421104 1421104 1421110 1421110 1421111 1421111 1421113 1421113 1421114 1421114 2411101 2421008 2421008 2421009 2421009 2421109 2421110 2421110 2421111 2421112 // 3421101 3421102 3421103 3421104 3421105 3421106 3421107 3421108 3421109 3421110`
- Transcript: `agent-data/matches/series-25-room-6658/player-a.jsonl`

## Outcome and key sequence

The no-learned-spell wall survived a long dark spell chain, but its physical clock was too weak. Two Warriors, two Xinke, two Sandworms, two Bears, two Jade Guards, Rock Wall Monster, Rock Wall Colossus, and two Monks all produced useful defensive evidence. The opponent repeatedly used a low-value spell to consume the Monk prevention, followed with multi-spell removal, and eventually removed every front attacker.

At turn 25 A equipped `翡翠永生` with exactly 2 shield. Jade Baron's aura prevented shield below 3 from decaying. `翡翠永生` prevented all friendly-unit damage while shield existed; an opposing physical hero attack dealt zero and did not reduce shield. Both decks were empty, but empty decks caused neither fatigue nor game-over. At turn 28–29 the players reached a provable cycle and stopped by coordinator adjudication.

## Provable-loop audit at adjudication

A had empty hand, empty deck, no learned skills, 2 hero life, and 2 shield. Field: Jade Baron, Rock Wall Monk left-rear, Giant Sandworm right-rear. Equipment: `地穴精灵矿镐`, used `沙漠护腿`, `秋枫宝钻`, `翡翠永生`.

- No hand card existed to replace/destroy `翡翠永生` or spend shield.
- No engine action exists to discard or destroy one's own equipment voluntarily.
- Pickaxe had no deck target; in addition, its consume effect had already failed to produce any search three times.
- Autumn Jewel only resets an earth companion; all surviving earth companions were vertical and neither rear unit had a legal attack.
- Consuming Jade/Monk/Sandworm only makes unusable resources and cannot remove shield.
- A had no skill and no legal hero-damage line.
- B's physical attacker could legally attack Jade, but `翡翠永生` prevented the damage before shield loss. B's tested dark attack skills rejected hero targets. No exposed A unit was a reachable way to remove shield.
- Empty decks did not terminate the match, and there was no turn cap observed through turn 29.

Therefore repeating end-turns cannot change any resource, zone, life, shield, or legal action relevant to victory. This is an adjudicated draw, not an official engine result.

## Pre-match hypothesis review

### Confirmed

- Never learning a skill is a real archetype enabler. Rock Wall Monk repeatedly set the first enemy spell's attack to zero, and Rock Wall Monster capped each damage event at 1.
- Jade's 1–2 shield retention is strategically structural. Bears and Jade Guards converted it into several extra turns.
- `翡翠永生` plus persistent low shield is much stronger than ordinary prevention and can create an absolute lock.
- Rapid Killer gives immediate tempo. It attacked on entry, and Desert Leggings once preserved it from a 2-attack spell.
- Preserve distinct payment sources: Hero + Monk exactly enabled six-cost Bear/Sandworm turns; scroll + boost defense using Hero overexertion successfully stopped a full-front attack.

### Wrong or incomplete

- “A scroll removes the final blocker” was false for 2-life bodies. Forest Arrow/Stonehenge had power 4 but only attack 1; a Warrior still had to spend its attack finishing the blocker.
- Sandworm was not a sustained finisher when placed behind another unit or when the opponent maintained a center blocker. Hidden stacks protected it but did not solve range or positioning.
- Autumn Jewel never created a second attack because the surviving earth attacker became stranded right-rear. The deck lacked movement, sacrifice, or self-clear tools.
- The opening kept expensive Sandworm/Bear cards and relied on exact Hero+Monk production; it stabilized but clogged the hand and slowed pressure.
- Two Monks do not each prevent one spell. The prevention is globally once per turn: spell one became attack 0, spell two dealt damage.
- The planned emergency “learn a spell” pivot never became practical: learning and casting costs were too slow, and the deck had no established skill slots/resources while under repeated pressure.

### Missing from the hypothesis

- Shield absorbs spell attack globally before unit life. A 2-attack front-row spell against shield 3 reduced shield to 1 and left every unit untouched.
- `沙漠护腿` is a once-per-game ultimate. It reduced one 2-damage hit to zero, then remained `ultimate_used=true`; later damage relied on Monster's cap instead.
- Direct physical attack range is narrow: side attackers could not cross to the hero, and a front unit could not target a rear enemy in its column in the observed states.
- Back-row attackers can become permanently stranded without a movement/sacrifice plan. Reserving center-front alone is insufficient; every intended finisher needs a verified route to front.
- Deck exhaustion has no terminal rule in the tested engine, so a prison deck needs a proactive win condition or the game can loop forever.

## General recognition rules

When seeing a no-learned-spell earth list:

1. Verify attack and power separately. Power wins defense checks; attack changes life/shield.
2. Treat Monk as one global spell tax per turn, not one shield per copy. Lead with the cheapest spell, then use the meaningful attack.
3. Count shield as a shared damage buffer. Against Jade, shield 1–2 does not decay; remove it before the endgame.
4. Identify actual front-capable attackers, not merely high-life companions. Rear Sandworm plus passive supports is not a clock.
5. Do not fill all nine cells without a move/sacrifice plan. A full board can lock one's own attackers out of relevant rows.
6. Before equipping `翡翠永生`, verify that either player retains a legal shield-removal or game-ending line; otherwise flag loop risk.
7. Against this shell, remove Monk with physical damage when possible, bait its global prevention with the cheapest spell, then chain 1-attack and 2-attack spells to sequence around shield, Leggings, and Monster cap.

## Bugs / rule anomalies observed

- `地穴精灵矿镐` was operated incorrectly. Its special printed `消耗` is exposed as `use_ability` with `ability_type: per_turn`; ordinary `consume` only turns it horizontal and takes its printed load. The three identical outcomes are protocol evidence, not a card bug.
- `血蔷薇咒印` also resolved correctly. It marks once when learned; the marked Giant Sandworm died after the printed deadline, and later casts do not create a new mark.
- With both decks at zero, no draw-loss/fatigue/game-over occurred. Combined with Jade + `翡翠永生`, this produced a provable non-terminal loop. Tracked as https://github.com/Yifeeeeei/EraOfArcaneGame/issues/146.

## Next deck iteration

Keep Jade, Monk, Monster, Guards, and a smaller shield package, but reduce passive six-cost bodies. Add a verified movement/sacrifice route or more front-capable Rapid attackers, and include a proactive win condition that does not require learning late. Do not use `翡翠永生` as an unconditional endgame lock until the rules define draws/deck exhaustion. If Pickaxe remains, invoke its special consume through `use_ability/per_turn`.
