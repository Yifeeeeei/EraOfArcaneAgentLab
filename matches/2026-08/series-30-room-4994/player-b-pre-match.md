# Series 30 — Player B Pre-Match

## Controlled comparison

- Player B deck: unchanged `LIGHT-GRACE-MIDRANGE-002`.
- Opponent: repaired-build `EARTH-MOBILE-BEATDOWN-003`.
- Game commit to test: `92e09fba884d4f217e07440a0eafc02723807a6b`.
- Historical deck profiles were authored against `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`; therefore old outcomes are context, not current-build truth.
- Do not intentionally reproduce old Giant Sandworm Issue #147 behavior. Judge all Hidden state from the current authoritative serialization.
- Exact Light deck code is frozen in `player-b-deck.txt`; no between-match tuning is allowed for this comparison.

## Bounded evidence loaded

- Series 27: Earth 003 reached six Earth on turn 3, seven on turn 4, and had a legal physical attack on 11 of 12 turns. Sandworm survival and the win were contaminated by #147; Spatial Shift producing two attacks is still useful clean cadence evidence.
- Series 28: Earth 003 versus Light 001 was an adjudicated contaminated draw. Light's Staff/Healing Warlock engine preserved a grown attacker, but generated only one clean physical hero damage.
- Series 29: Light 002 dealt first clean physical hero damage on turn 4 and won on turn 28. Moon Dust removed Hidden, Holy Wing cleared the blocker, and Lundesar converted the opening into lethal.

## Player B plan

1. Identify a real center-front clock before adding sustain pieces. Prefer `屠魔者杀手` for immediate pressure and retain `屠魔者武士`, `御座的圣翼`, or `大法师 伦德萨尔` as the next attacker.
2. Use `祝福之杖`, `治疗术士`, `生命之花`, `恩典`, and the hero ultimate only when they preserve or grow a body that can attack, clear, move, or pay for a bridge within one own turn.
3. Use `月霞之尘` specifically for a real Hidden obstruction; use `光辉斩裂`, `光辉波动`, scrolls, or `神谕卷轴 荣耀` to clear blockers while preserving a ready attacker.
4. Use `移形换影` as cadence infrastructure: recycle an attacker that already acted and open center-front for the next ready/rapid attacker.
5. Submit dependent actions one at a time and record success only from the next authoritative state.

## Pre-registered metrics

Turn numbers below mean the global `turn_number` in authoritative state. A
physical attack is successful only when the next authoritative event shows the
attacker horizontal and/or target life/zone changed consistently with that
attack. Rejected commands and mere attempts do not count.

### Pressure timing

- `first_physical_attack_turn`: first successful ordinary unit attack by B, whether it targets a unit or hero.
- `first_physical_hero_damage_turn`: first turn an ordinary B unit attack reduces the enemy hero's life. Exclude spells, scrolls, deathrattles, marks, and other effect damage.
- `first_hero_damage_any_source_turn`: first authoritative enemy-hero life loss caused by B, with source classified separately.
- Comparison checkpoint: test whether Light 002 repeats Series29's physical hero damage by turn 4. Record `yes/no`, not a revised threshold.

### Physical clock

- `physical_attacks_attempted`, `physical_attacks_successful`.
- `physical_hero_attacks_successful` and cumulative `physical_hero_damage`.
- `own_turns_with_ready_legal_attacker` and `own_turns_converted_to_physical_attack`.
- `clock_gaps`: consecutive B turns after first physical hero damage with no successful physical attack; record cause as blocker, horizontal/frozen/stunned, no front-row attacker, range/taunt, or resource/sequence choice.

### Clear-to-hero conversion

A `clear_opportunity` occurs when B removes, moves, disables, or strips Hidden
from the last obstruction to a legal hero attack while a B attacker can
potentially use that lane.

- Count `clear_opportunities`.
- Count `same_turn_clear_to_hero_conversions` only when a preserved ready attacker successfully damages the hero that same turn.
- Count `next_own_turn_conversions` when the first hero attack arrives on B's immediately following turn.
- For every miss, record whether the attacker was already horizontal, the slot/lane was wrong, a new blocker appeared, Hidden remained, or no attacker had been reserved.
- Explicitly record every `移形换影` use and whether it created an additional physical attack or merely rearranged support bodies.

### Hidden interaction

- `hidden_obstructions_seen`: authoritative states where Hidden prevents the intended target/attack path.
- `moon_dust_opportunities`: copies of `月霞之尘` held while a relevant Hidden obstruction exists.
- `moon_dust_uses`, `hidden_removed`, and `hidden_to_attack_conversion` (same turn / next own turn / none).
- Record the target card, source of Hidden if visible, and current-build result. Never infer Hidden from historical #147 behavior.

### Healing converted into tempo

For each heal or permanent life/load growth action, record source, target,
resource/action cost, life restored/gained, and the next authoritative use of
that target.

- `heals_attempted`, `heals_successful`, total life restored/gained.
- `heal_saved_from_lethal`: target survives damage that would otherwise have been lethal before its next reset.
- `heal_to_attack_within_one_own_turn`: healed/grown target makes a successful physical attack during the same B turn or B's next turn.
- `heal_to_bridge_within_one_own_turn`: target instead pays for or enables a successful clear, movement, defense, or resource action that directly preserves the clock.
- `nonconverting_heals`: neither conversion occurs within that window.
- Pre-registered decision rule: after two consecutive blocker-only/nonconverting heals, stop generic sustain unless the heal changes immediate lethal math or creates a quantified breakpoint.

## Hypothesis

Light 002 should reproduce early pressure if it finds an attacker by turn 4,
but the meaningful comparison is not survival time. Success means converting
clears, Hidden removal, and healing into repeated physical attacks against
Earth 003's high attack cadence. A long game with high healing and little
physical hero damage counts as failure of the bridge even if Light eventually
wins.
