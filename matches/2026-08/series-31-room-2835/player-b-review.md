# Series 31 Player B review

## Result

- Deck: **WATER-FROZEN-CLOCK-001** (`4211102 凛冰魔巫 索菲娅`)
- Commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Player B: slot 0; Player A: slot 1 / first player.
- Official result: `game_over {actor:1, reason:"surrender", winner:0}` on A's T9.
- Final heroes: B 6, A 4.
- Verdict: B won, but **did not satisfy proactive-success criteria**. B dealt only 2 hero damage and did not create a functioning repeated clock before the surrender.
- No gameplay bug observed. Illegal targets and payments were rejected consistently without corrupting state.

## Match outline

- B T1: hero supplied 4 water; rapid Slayer `ci85` entered center-front and immediately hit A hero 6→5. Dolphin entered left-middle.
- A T2: Arcane Bomb's lethal hit on Slayer was prevented by sacrificing Dolphin.
- B T2: Slayer hit A hero 5→4. Water Magister entered and Six-Petal Snowflake was learned.
- A T3: a second Arcane Bomb killed the Slayer.
- B T3: reached 5 payable water (hero 4 + Magister 1). Rapid Ice Bullet survived an illegal Cold-Explosion-to-hero rejection and then discounted Ice Cone's learning cost to zero. Frost Golem entered; Ripple Slash was learned.
- B T4: Snowflake froze A's center-front Ice Wolf; Sophia removed Freeze1 and dealt exactly 2, killing it. This was the sole clean freeze bridge. Attack spells correctly rejected direct hero targeting, so no same-turn hero hit followed.
- B T5: Ice Cone dealt 1 and killed A's rapid Slayer. B deployed a center-front Ice Wolf.
- B T6: no attacker drawn; Water Scry was learned and a second Ice Wolf filled right-front.
- B T7: Water Scry showed a neutral rapid Slayer plus three water cards; the neutral card was correctly not selectable. Fog Spirit was selected. A natural Winter Archer draw was deployed center-back.
- B T8: Winter Archer's attempted hero attack was rejected because B's own center-front Ice Wolf blocked the line. Ripple Slash dealt 2 and killed A's left-front Mist Dancer. Fog Spirit entered back-left.
- A T9: surrendered from 4 life with an empty battlefield and color-stranded hand.

## Pre-registered metrics

1. **First physical attack:** B T1, rapid Slayer `ci85`, direct hero attack for 1. Target ≤T4 met.
2. **First hero damage:** B T1, same Slayer attack, 1 damage. Target ≤T6 met.
3. **First repeatable hero clock:** not established by T10/game end. The Slayer repeated once on B T2 but died before B T3; Winter Archer was deployed on B T7 but never produced a legal attack.
4. **Water breakpoints:**
   - 2/3/4: available from hero alone on B T1.
   - 5: first explicit pre-spend state B T3, hero4 + Water Magister1.
   - 6/7: structurally available from B T5 onward (hero4 + Ice Wolf2 + Magister1 = 7), and later substantially exceeded with two Wolves/Fog Spirit, but excess resource did not convert into hero damage.
   - Sources were printed load only, except Fog Spirit's hidden +2 water from B T8 onward. No Aria activation or defensive overexertion occurred.
5. **Freeze bridge efficiency:** one Sophia ultimate. Source Snowflake; target A Ice Wolf `ci129`, life2/Freeze1 → life0/Freeze0; blocker cleared. No hero attack occurred that turn or next B turn.
6. **Clear-to-hit conversion:** three enemy blockers/attackers removed by B (Ice Wolf via Sophia, rapid Slayer via Ice Cone, Mist Dancer via Ripple). Zero were followed by hero damage by the next B turn: 0/3 = 0%.
7. **Clock continuity:** hero damage on B T1 and B T2 only (two consecutive own turns). It stopped on B T3 because the Slayer was killed. No later hero damage.
8. **Attacker discipline:** Slayer was never consumed/overexerted. Winter Archer was never consumed. Target zero met. However, a non-attacker Ice Wolf was incorrectly placed center-front and physically blocked the rear Archer's line.
9. **Rear-Archer value:** zero successful non-front attacks. One attempted hero attack on B T8 was rejected due to own center-front obstruction. Rear placement alone does not preserve the lane; the entire center column must remain clear.
10. **Spell resets:** zero Water Magister, Wave Walking, or Wendi resets. Magister was used as 1-water load instead of reset leverage.
11. **Exact B damage ledger:**
    - Hero damage: 2 total, both physical rapid-Slayer attacks (`ci85`), 1 on B T1 and 1 on B T2.
    - Physical damage to units: 0.
    - Spell damage to units: 3 total — Ice Cone 1 to rapid Slayer `ci150`; Ripple Slash 2 to Mist Dancer `ci137`.
    - Sophia ultimate: 2 to Ice Wolf `ci129`.
    - Other B damage: 0.
    - Total B damage: 7 (2 hero + 5 unit).
12. **Outcome:** official B win by opponent surrender, not B-caused lethal. Proactive success failed.

## Opponent damage received

- Second Arcane Bomb dealt 2 lethal damage to B rapid Slayer; the first identical lethal event was prevented by Dolphin sacrifice.
- A rapid Slayer dealt 1 physical damage to Frost Golem (2→1).
- B hero took no damage.

## Architecture assessment

The freeze bridge itself worked exactly as intended, but it is not repeatable: Sophia's ultimate is once per game (`ultimate_used=true` persists), so the pre-match phrase “freeze → Sophia 2 damage” overstated it as an engine. It is a one-shot bridge.

The main list also had too many non-attacking resource bodies and reactive spell cards relative to actual clock pieces. Ten nominal attackers were not enough when Water Scry cannot select the neutral Slayers/Warriors and when the pilot filled all three front squares with zero-attack units. Attack spells cannot target heroes, so spell-reset packages improve clearing but cannot substitute for physical clock density.

## Next iteration

- Treat Sophia as one-shot removal, not the repeated bridge.
- Raise searchable water attacker density: keep two Winter Archers, Krakens, and Wendis, and consider additional mono-water physical attackers rather than neutral attackers that Water Scry cannot find.
- Never place a resource body in center-front while planning a center-back Archer clock. Reserve the complete center column, not only the nominal attacker square.
- Cut at least one Ice Wolf pair or redundant attack-scroll pair for more physical attackers/search that can find them.
- Keep Rapid Ice Bullet: its rejected-action behavior was clean, and discounting Ice Cone learning from 2 to 0 was useful acceleration.
