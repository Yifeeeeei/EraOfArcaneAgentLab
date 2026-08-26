# Series 30 Player A pre-match

- Deck: `EARTH-MOBILE-BEATDOWN-003`, unchanged
- Game commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Regression boundary: Issue #147 was fixed by `20be3cd`; this is the first clean post-fix repeat.
- Prior evidence used: Series 27 and Series 28 summaries only, plus the bounded context and canonical deck profile.

## Purpose and hypothesis

This run retests the unchanged Earth 003 engine/clock/bridge package without crediting the old Giant Sandworm Hidden corruption. The expected clean line is six recurring Earth by turn 3–4, a physical attack on at least 75% of own turns after turn 1, at least four physical hero damage, and at least one attack genuinely created or preserved by Spatial Shift.

Giant Sandworm should gain exactly one Hidden layer when that Sandworm itself takes a damage event. Damage elsewhere, its own attack, spell declarations, defense events, and multi-target segments that do not damage it must not change its Hidden value. Every Sandworm trigger will be recorded with the immediately preceding damage event and authoritative status transition.

## Driving policy

- Mulligan for a real physical attacker plus payable Earth development: Xinke, Rapid Killer, Warrior, Sandworm Bait, or an exact-production heavy attacker.
- Reserve center-front for the current clock. Put resource/support bodies in side or rear cells unless they must block lethal.
- Before developing, identify this turn's attacker and the next attack-line replacement.
- Stop at six payable Earth for an actual Sandworm line; pursue seven only when it immediately enables Rock Beast or another concrete attack.
- Use Spatial Shift only when it creates an attack in the same turn or preserves the explicitly named next-turn cadence.
- Do not overexert the intended attacker unless preventing a larger clock loss.
- Once the enemy hero is within two attacks, spend only on actions that clear the lane, reset/move an attacker, or produce lethal pressure.

## Pre-registered measurements

### 1. Resource breakpoints

- First own turn with at least six payable Earth; list every vertical contributing source and total.
- First own turn with at least seven payable Earth; list every vertical contributing source and total.
- Count turns where a planned attacker or Shift line is resource-stranded, recording required versus available Earth/Arcane.
- Count resource bodies deployed after six Earth that do not enable an attack within one turn.

Targets: six Earth by turn 3–4; seven Earth by turn 4–5 only if used for a concrete line; zero off-color stranded actions.

### 2. Attack turns and cadence

- First legal physical attack turn and source.
- For each A turn after turn 1, record whether at least one legal physical attack occurred.
- Report `attack turns / eligible own turns` and percentage.
- Record every blank attack turn with cause: no attacker, horizontal/frozen, blocked lane, positioning, payment, or pilot choice.

Target: physical attack on at least 75% of eligible own turns.

### 3. Physical hero damage

- Record each physical hero hit as turn, attacker, damage, and whether Shift/reset created it.
- Sum physical hero damage separately from spells, effects, and deathrattles.

Target: at least four clean physical hero damage and first hero damage by turn 5 when the opponent's board permits it.

### 4. Giant Sandworm normal Hidden trigger

- For each Sandworm, record instance ID, position, life, Hidden before/after, and exact damage source.
- Count valid triggers where that Sandworm actually took damage.
- Count invalid triggers from unrelated events; target is zero.
- Check that Hidden decays only at the correct owner marker settlement and that targeting becomes legal again when layers reach zero.
- Separate Sandworm attacks/survival that depended on correctly earned Hidden from unrelated deck-strength measurements if any new anomaly appears.

Acceptance: `+1 Hidden` per own damage event only, no unrelated accumulation, and normal decay/target restrictions.

### 5. Spatial Shift-created attacks

- Count an attack only when Spatial Shift moves a unit into a legal attacking lane, vacates the center for a ready replacement, or preserves the immediately following turn's explicitly named attacker.
- Record turn, moved instance/positions, attacker enabled, and whether the attack actually occurred.
- Label setup-only/cosmetic Shift separately and do not count it.

Target: at least one genuine Shift-created or Shift-preserved physical attack; zero cosmetic Shift uses while an attack conversion is available.

## Result interpretation

A clean pass requires normal Sandworm Hidden behavior plus the cadence/resource measurements above. Winning alone is insufficient. If Hidden is fixed but the deck misses cadence or physical-damage targets, treat that as deck evidence rather than regression failure. If Sandworm gains Hidden without taking damage, preserve exact instance/action/state evidence and mark the match contaminated again.
