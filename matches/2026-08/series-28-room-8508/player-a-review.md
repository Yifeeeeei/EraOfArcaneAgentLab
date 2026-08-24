# Player A review — Series 28

- Match: `series-28-room-8508`
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Deck ID: `EARTH-MOBILE-BEATDOWN-003`
- Result: `contaminated_adjudicated_draw`
- Stopped: turn 38, engine still in `main` rather than `game_over`
- Contamination: Giant Sandworm hidden-counter bug, tracked as Issue #147; the lack of an empty-deck terminal condition, tracked as Issue #146, allowed the resulting loop to continue indefinitely.

Exact deck code:

`4411101 // 1021011 1021011 1021013 1021013 1401002 1401002 1401101 1401101 1421012 1421012 1421013 1421013 1421016 1421016 1421101 1421101 1421102 1421102 1421114 1421114 2421002 2421002 2421008 2421008 2421009 2421009 2421110 2421110 2421111 2421112 // 3021001 3421003 3421004 3421101 3421103 3421104 3421107 3421108 3421109 3421110`

## Outcome and adjudication

This match is not strength evidence for Earth 003. Both Sandworms accumulated hidden counters from unrelated damage and from their own attacks while taking no damage. Their counters eventually exceeded 40, so the light deck could not select them. After both decks reached zero, A could make only one central 1-damage hero attack per turn, while the opposing Healing Mage restored exactly one life per turn. The right Sandworm could not reach the center hero. Turn 37 demonstrated the full loop: the center Sandworm dealt Eve 1, and on turn 38 Eve was back at 6. A had no remaining reset markers or second central attack. The coordinator therefore stopped the match as a contaminated adjudicated draw.

## Pre-registered measurements

1. **First legal physical attack:** A turn 2, Xinke into the opposing center Warrior.
2. **First hero damage:** A turn 10, Stonehenge Scroll area damage, not physical damage.
3. **Six/seven Earth:** both were available on A turn 4. The exact field was Jade 4 + Spikeball 2 = 6, with Xinke adding the seventh Earth.
4. **Physical hero damage:** raw total 1, from polluted Sandworm `ci_144` on turn 37. Clean total **0**.
5. **Shift-created attacks:** clean total **1**, on turn 10 when Spatial Shift moved the native Warrior into center and it attacked. Other Shift uses were setup-only or depended on a polluted Sandworm.
6. **Sandworm contribution:** the first Sandworm made two blocker attacks on turn 5 before abnormal survival changed any prior targeting decision; these are the only clean-eligible Sandworm attacks. All later Sandworm survival and attacks are excluded. Raw Sandworm actions dominated the remainder of the match and eventually produced the single raw hero damage, but clean Sandworm hero damage was **0**.

The clean hypothesis failed: the list did not deal four physical hero damage and did not sustain a 75% clean post-turn-1 physical cadence. Clean physical attacks occurred early through Xinke, Rapid Killer, Warrior, and the first pre-contamination Sandworm exchanges, but the mid/late game contained many blank turns and then a long sequence whose only attacks came from bug-protected Sandworms.

## Driving observations independent of the bug

- Reserving center-front mattered. Xinke and the native Warrior converted center access into real blocker trades; side-lane attackers repeatedly failed to reach middle or rear targets.
- Six Earth was achieved on schedule, so the resource engine itself was not the failure. Going from six to seven was also natural on turn 4 rather than requiring an off-color bridge.
- Spatial Shift created one genuine clean attack, but too many later uses merely moved the current Sandworm clock. A successful mobile-beatdown list needs a ready replacement attacker, not just an empty center cell.
- Forest Insight had a real setup tax: trying to use it on the same turn it was learned was correctly rejected because the newly learned skill was horizontal. Its three-card draws were also inflated by polluted Sandworms remaining on field; the extra cards reached through those draws cannot be credited as clean consistency.
- The native Warrior, Rapid Killer, Xinke, and blocker bodies performed according to their intended roles. However, after those attackers were removed, the clean list had no independent closing clock.
- No fixed off-color action was stranded. The problem was attacker density and attack positioning, not color payment.

## Pilot errors

- I attempted to cast newly learned Forest Insight immediately; the engine correctly rejected it. Future pilots must budget a full turn of setup for newly learned non-rush skills.
- Several side-lane attack attempts were rejected by range. Before deploying or shifting an attacker, identify the exact next target and verify that the destination preserves access to it.
- Once Sandworm pollution was established, raw play continued only to reach an engine terminal state. Those actions must not be read as evidence that the deck's cadence policy worked.

## Five-layer correction

- **Engine:** six/seven Earth is reliable, but Forest Insight counts polluted survivors and therefore overstated clean card selection here.
- **Clock:** native clean clock density remains too low; Sandworm cannot be treated as the clock until Issue #147 is fixed and retested.
- **Bridge:** Spatial Shift is valuable only when it immediately creates or preserves a legal attacker; one clean conversion in 38 turns is insufficient.
- **Breakpoint:** the deck traded blockers but did not convert the cleared center into clean hero damage before its native attackers ran out.
- **Cadence:** center reservation was correct, yet replacement cadence failed. The list needs more independently targetable native-Earth attackers or repeatable legal resets, not more resource bodies.

## Verdict

Series 28 neither confirms nor refutes the overall power of `EARTH-MOBILE-BEATDOWN-003`, because Issue #147 materially changed targeting, survival, draws, and the final loop. It does refute the narrower clean hypothesis for this game: excluding Sandworm pollution, physical hero damage was 0 and the deck lacked a late-game clock. The next controlled test should occur after Issue #147 is fixed, or should remove both Giant Sandworms and replace them with native-Earth attackers that can maintain a center attack cadence without hidden-state protection.
