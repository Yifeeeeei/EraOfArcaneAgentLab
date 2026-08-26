# Series 32 Player B pre-match

## Registration

- Player: B
- Deck: **WATER-FROZEN-CLOCK-002**
- Hero: `4211102 凛冰魔巫 索菲娅`
- EraOfArcaneGame commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Construction: base set + 王权纷争, 30 main + 10 distinct skills.
- Objective: correct the Series31 clock-access and center-line failures while keeping a closed mono-water payment system.

## Exact delta from WATER-FROZEN-CLOCK-001

Removed six non-hero-facing spell consumables:

- `2221003 冰封卷轴` ×2
- `2221008 水形之束卷轴` ×2
- `2221009 寒冰爆裂卷轴` ×2

Added one coherent water-companion clock-access package:

- `1221113 凛冬城象骑兵` ×2 — durable 1-attack physical clock, Water5+Arcane1.
- `1211001 人鱼 菲尔` ×2 — mono-water companion search through Prayer when kept isolated.
- `1221012 龙王子裔` ×2 — mono-water companion search/cost reduction after Mastery2.

Unchanged:

- The ten-card skill pool.
- Two Rapid Ice Bullets as acceleration rather than damage spells.
- Two Water Arias as recurring resource engine.
- Existing physical attackers: rapid Slayer ×2, Warrior ×2, Wendi ×2, Kraken ×2, Winter Archer ×2.

Net main-deck effect: direct physical attackers rise from 10 to 12; water-attribute physical attackers rise from 6 to 8; dedicated companion-search bodies rise from 0 to 4; pure non-hero-facing spell scrolls fall from 6 to 0. The remaining two consumables are cost accelerators, not removal pretending to be a clock.

## Revised engine → clock → bridge

**Engine.** Hero4, Dolphin1, Ice Wolf2, Water Magister1, hidden Fog Spirit2, and Water Aria's repeatable +3 water remain fully mono-water. Rapid Ice Bullet compresses a summon/learn turn without introducing another color.

**Clock.** Twelve physical attackers now form the primary win condition. Water Scry can find eight water attackers rather than relying on the two neutral Slayers/four neutral bodies. Mermaid and Dragon Descendant increase effective access to the same water attacker package. Elephant/Kraken are durable 1-point clocks; Wendi is the 2-point closer; Archer supplies protected pressure only when its entire column is clear.

**Bridge.** Sophia's ultimate is explicitly registered as a **once-per-game bridge**, not an engine. Snowflake/Frost Ray/Frost Golem can establish Freeze; Sophia removes one Freeze and deals 2 to clear exactly one key blocker. All later clearing must justify preserving a physical attacker. Spells do not count as hero clock because the server correctly disallows them from targeting heroes.

## Hard positioning policy

- If a Winter Archer is or will be placed center-back, all other squares in the center column must remain empty except the hero. In particular, never place Ice Wolf, Golem, search body, or resource body at center-front.
- Default physical-clock layout: durable attacker center-front; Archer in a side-back column whose front square is empty; second attacker on the opposite front side.
- Until a true center-front attacker is available, keep center-front empty. A zero-attack blocker may occupy a side-front square only.
- Do not summon an Archer behind an occupied friendly front square. “Can attack from non-front” does not bypass friendly line obstruction.

## Payment breakpoints

- 2 water: Archer, Fog Spirit, Dragon Descendant, cheap skill use.
- 3 water: Mermaid, Ice Wolf, Water Magister, rapid Slayer via wildcard.
- 4 water: Warrior via wildcard, Water Aria.
- 5 water: Kraken.
- 6 total: Elephant (Water5+Arcane1) or Wendi (Water6).
- 7 total: attacker plus a 1-water bridge/use; target by B T4.
- 8–9 total: durable attacker plus search/skill bridge without consuming an established attacker; target by B T6.
- All exact colored requirements are water. Arcane and neutral requirements can be paid with water; no off-color converter is needed.

## Pre-registered metrics

1. First physical attack and first hero damage, target no later than B T3.
2. First repeatable hero clock, defined as a surviving attacker with a legal hero line projected across consecutive B turns; target no later than B T6.
3. Clock continuity: consecutive B turns with hero damage after clock establishment; target at least three or lethal.
4. Attacker access: natural draws, Water Scry hits, Mermaid searches, and Dragon Descendant searches; record whiffs and whether the selected card attacked within two B turns.
5. Physical attacker deployment by B T4/T6/T8; targets 1/2/3 respectively.
6. Center-line discipline: friendly zero-attack cards placed center-front (target 0); rejected attacks caused by friendly obstruction (target 0).
7. Archer value: legal non-front attacks, hero damage, and front-square occupancy for its column at each attempt.
8. Sophia bridge: freeze source, target, life before/after, exact 2 damage, blocker clearance, and hero hit by the next B turn. Maximum expected uses: one.
9. Clear-to-hit conversion: blockers removed followed by hero damage by the next B turn; target at least 50%.
10. Pure-spell burden: dead hand cards that cannot contribute to hero damage or current clearing; target no more than two at any B turn.
11. Payment closure: first 2/3/4/5/6/7/8 payable-water turns and any off-color stranding (target 0).
12. Attacker discipline: clock attackers consumed/overexerted for payment (target 0 unless preventing lethal).
13. Exact damage ledger split into physical hero, physical unit, spell unit, Sophia, and other damage.
14. Official outcome. Proactive success requires B-caused lethal; opponent surrender is a win but not a successful clock proof.

## Mulligan and pilot rules

- Keep at least one physical attacker. Prefer Archer/Slayer for speed, Warrior/Kraken for durability, or Wendi/Elephant only alongside cheap load.
- Keep at most one search body and one engine card; replace hands with multiple non-attacking resource bodies and no attacker.
- Mermaid must be placed isolated enough to preserve its Prayer condition and never in the center column reserved for clock.
- Water Scry prioritizes a water physical attacker over engine/removal unless lethal defense is required.
- Sophia's ultimate is saved for a blocker whose removal creates a legal physical hero attack by the next B turn.
