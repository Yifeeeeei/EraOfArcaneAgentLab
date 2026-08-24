# Player A pre-match hypothesis — Series 28

- Deck ID: `EARTH-MOBILE-BEATDOWN-003`
- Controlled repeat of: Series 27
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Deck change: none
- Exact deck code:

`4411101 // 1021011 1021011 1021013 1021013 1401002 1401002 1401101 1401101 1421012 1421012 1421013 1421013 1421016 1421016 1421101 1421101 1421102 1421102 1421114 1421114 2421002 2421002 2421008 2421008 2421009 2421009 2421110 2421110 2421111 2421112 // 3021001 3421003 3421004 3421101 3421103 3421104 3421107 3421108 3421109 3421110`

## Controlled-repeat purpose

This match tests whether Series 27's cadence is reproducible without treating the abnormal Giant Sandworm hidden accumulation as a legal advantage. The list is unchanged so differences should be attributed to draw, opponent interaction, and pilot decisions rather than deck construction.

If a Giant Sandworm is drawn or deployed, track its printed contributions separately from any survival, targeting failure, or extra attack enabled by hidden counters gained while that Sandworm itself took no damage. The primary strength verdict must exclude those abnormal benefits.

## Corrected driving policy

- Mulligan for a real attacker plus a payable Earth bridge: Xinke, Rapid Killer, Warrior, Sandworm Bait, or a heavy attacker supported by exact production.
- Keep center-front reserved for the current clock. Put Lizard, Squirrel, Spikeball, and Scavenger on side/rear cells unless blocking immediate lethal.
- Attack before developing resources. Before every summon, name this turn's attacker and next turn's replacement.
- Stop building the engine at six payable Earth when Sandworm is the next play; reach seven only for an actual Rock Beast line.
- Use Spatial Shift to create an attack or preserve center cadence, not as cosmetic movement. Prefer attack, shift the used attacker away, then move/deploy a ready attacker into center.
- Do not rely on hidden Sandworms to survive removal. If an attack is legal only because abnormal hidden counters prevented targeting earlier, tag that attack as contaminated and exclude it from the clean cadence result.
- Once the opponent hero is within two attacks, stop deploying resource bodies unless they directly pay for a Shift/reset lethal line.

## Pre-registered measurements

1. **First attack:** turn of the first legal physical attack by A.
2. **First hero damage:** turn and source of A's first hero damage.
3. **Six/seven Earth:** first own turn with six payable Earth and first own turn with seven payable Earth; record exact contributing sources.
4. **Physical hero damage:** total physical damage dealt to the enemy hero, with source and turn.
5. **Shift-created attacks:** number of attacks that Spatial Shift genuinely enabled in the same turn or on the immediately preserved cadence line; distinguish setup-only movement.
6. **Sandworm-clean contribution:** damage and attacks contributed by Giant Sandworms after excluding attacks/survival enabled by abnormal hidden accumulation. Report raw and clean totals separately.

Supporting cadence audit:

- own turns with any legal physical attack / total own turns;
- every lost or displaced center attacker and whether a named next-turn replacement existed;
- support/resource summons into center-front;
- fixed off-color stranded actions (target zero);
- one-turn clock blanks remaining in hand at game-over.

## Hypothesis

Even with all abnormal Sandworm hidden benefits removed, the unchanged 003 shell should reach six Earth by turn 3-4, present a legal physical attack on at least 75% of own turns after turn 1, and deal at least four physical hero damage. At least one Spatial Shift should create or preserve a real attack. Failure on those clean metrics would mean Series 27 overstated the list's strength and the next iteration should replace part of the Sandworm package with independently targetable native-Earth attackers.
