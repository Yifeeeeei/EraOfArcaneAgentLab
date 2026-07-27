# Player B Review — series-20-room-2976

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Player B: slot 0, `WATER-PRESSURE-SCRY-001`
- Player A: slot 1, `FIRE-BURN-004`
- Result: A won on turn 10 (`winner: 1`), B 0 life to A 5 life.

## Findings

- Reserving center-front was strategically correct, but both South Sea Krakens were removed by repeated Fireball/Burn sequences before they could attack. Water needs a learned defense spell before committing a five-cost finisher against Fire.
- Water Scry consistently found pressure cards, including both Krakens, but early resource investment into Scry and Staff delayed defensive coverage.
- The second Kraken appeared to survive Burn plus Fireball by printed attack values, but Phoenix Feather raised the actual damage and killed it. Decisions must use effective attack values from authoritative state, not printed values.
- A center-front Ice Wolf plus Ice Fortress successfully restored a blocker late, but the line was too slow after B fell to one life.
- Dolphin Companion correctly created a private `dolphin_prevent_lethal` pending action when Fire Arrow targeted the one-life hero. A saw `waiting_action` with no pending, while B saw the optional sacrifice. Selecting the Dolphin prevented that lethal; this was information asymmetry, not a soft lock.

## Suspicious behavior

- A's rapid Slayer remained horizontal across multiple owner end turns after Water Shape Scroll was fully defended. The scroll should not have consumed the target when defended, but the persistent horizontal state needs replay review.
- On the final turn B submitted Ice Blade defense at effective power 4 against Burn power 4, yet the authoritative match ended with B at 0. Review the final defense transcript to determine whether payment/defense was rejected, Phoenix Feather changed effective power after the reported value, or another damage event resolved.
- A reported an earlier failed summon consuming resources. This should be checked independently in the server room log.

## Next adjustment

- Against Fire, learn Ice Barrier or another defense spell before the first Kraken, then place the attacker center-front with Dolphin protection available.
- Keep using the center-front finisher slot, but do not treat occupying it as sufficient; the deck needs two layers of protection against consecutive attack spells.
