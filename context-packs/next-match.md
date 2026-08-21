# Next Match Context

The next controlled run should follow up series 22–24 on game commit
`e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb` or explicitly record a newer
commit boundary.

## Current baseline

- `ROYAL-SURVIVAL-FIRE-001` beat `WIND-RUSH-005` and `WIND-RUSH-006` on turns
  13 and 15. The stable plan was Backlash defense/burn, Kran filtering, and a
  pre-equipped Fire Arrow finish.
- `ROYAL-SURVIVAL-FIRE-002` replaced one Celtic Lion with one Fire Butterfly
  and beat `WIND-RUSH-007` on turn 9. Fire Butterfly was not drawn, so its
  actual range/payment benefit is still untested.
- `WIND-RUSH-007` restored attacker density and immediately produced turn-one
  and turn-three hero attacks. The restored Warrior and Wind Demon were not
  drawn, so those exact substitutions remain untested.

## Next experiments

1. Keep `ROYAL-SURVIVAL-FIRE-002` unchanged until Fire Butterfly is actually
   deployed; record its entry turn, vertical survival turns, and whether it
   lets Kran remain vertical while paying for defense or offense.
2. Keep `WIND-RUSH-007` unchanged until Warrior or Wind Demon is drawn; measure
   whether the restored attack bodies convert a cleared lane into lethal.
3. Against Backlash, Wind should cluster spell clearing into a turn with a
   ready attacker instead of repeatedly accepting burn without hero damage.

Read only the two deck profiles and summaries for series 22–24 before the next
run. Do not preload their raw transcripts.
