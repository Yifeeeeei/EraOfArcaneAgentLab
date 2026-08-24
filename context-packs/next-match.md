# Next Match Context

Series 27–29 continued deliberate deck exploration on game commit
`e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`.

## Evidence

- `EARTH-MOBILE-BEATDOWN-003` hit six Earth on turn 3, seven on turn 4, and
  attacked on 11 of 12 turns in Series 27. Its Sandworm survival and victory
  are not clean evidence because of Issue #147.
- `LIGHT-GRACE-MIDRANGE-001` proved that Staff/Warlock is the smallest useful
  sustain engine, but produced only one clean hero damage before a contaminated
  loop in Series 28.
- `LIGHT-GRACE-MIDRANGE-002` replaced pure sustain with attack and bridge cards,
  dealt first hero damage on turn 4, and won Series 29 on turn 28. Moon Dust was
  the decisive Hidden bridge.
- `ROYAL-MIST-GRAVE-CLOCK-001` generated graveyard and reset value but dealt
  zero physical hero damage in 28 turns. Its clock body and side-lane clearing
  density were insufficient.

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

- Do not retest Sandworm-dependent Earth strength until Issue #147 is fixed.
- Iterate Water-Shadow by adding independently payable physical attackers and
  side-lane removal; keep only grave pieces that convert into clock or cards.
- Keep Light 002 stable once, measuring whether turn-4 pressure repeats and
  whether its 28-turn finish can be shortened.
- Treat `defense_attempt` as an attempted defense, not a success event. Read the
  next authoritative event before drawing a conclusion.
- Do not intentionally reproduce Issues #146–#149.

Read the relevant new deck profiles and summaries for series 27–29. Do not
preload raw transcripts.
