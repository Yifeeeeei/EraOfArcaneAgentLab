# Next Match Context

Series 30–32 continued deliberate deck exploration on game commit
`92e09fba884d4f217e07440a0eafc02723807a6b`.

## Evidence

- `EARTH-MOBILE-BEATDOWN-003` passed the post-#147 Sandworm retest. It attacked
  often but converted only three hero damage before late support draws lost the
  board.
- `LIGHT-GRACE-MIDRANGE-002` won Series 30 with zero hero damage: 17 successful
  attacks all hit replacement units. Board control is not a clock.
- `ROYAL-MIST-GRAVE-CLOCK-002` is retired. A Water-only hero cannot support its
  remaining explicit Dark and Water-five/six package consistently.
- `WATER-FROZEN-CLOCK-002` fixed search access and self-obstruction. Its Monster
  plus rear Archer formed a repeat clock, but first hero damage arrived turn 11.
- `MONO-FIRE-FORWARD-CLOCK-001` proved payment closure is necessary but not
  sufficient: seven attack turns produced only one direct-item hero damage.

## General driving model

Before playing an unfamiliar list, identify:

1. Engine: what repeatedly creates resources, prevention, cards, or growth?
2. Clock: what can legally damage the hero every turn?
3. Bridge: how does the engine clear or recycle the attack lane for the clock?
4. Breakpoints: how many triggers/resources are required before the payoff is
   actually an attacker or lethal threat?
5. Cadence: name this turn's attacker and next turn's replacement before
   filling the center-front slot.

## Next experiments

- Measure `attacks created minus replacement blockers`, same-turn clear-to-hit,
  and next-turn conversion. Do not call attack cadence a clock by itself.
- Iterate Water Frozen 002 for same-turn conversion rather than more search.
- Retire the mixed Water-Shadow line unless its Dark production is rebuilt from
  the opening economy upward.
- A Fire revision needs movement, penetration, rapid replacement, or direct
  reach that functions after clearing—not more raw Fire production.
- Missing coordinate fields must be avoided until Issue #153 is fixed.

Read the relevant new deck profiles and summaries for series 30–32. Do not
preload raw transcripts.
