# Series29 Player B Review

## Result

- Match: `series-29-room-8857`
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Deck: `LIGHT-GRACE-MIDRANGE-002`
- Result: Player B win, official `game_over`, turn 28, winner `1`.
- Final heroes: Eve 3; Bailey -1.
- Exact deck code: `4511102 // 1021011 1021011 1021013 1021013 1511002 1511002 1511101 1511101 1521001 1521001 1521006 1521006 1521008 1521008 1521107 1521107 2021102 2021102 2521008 2521008 2521009 2521009 2521014 2521014 2521102 2521102 2521105 2521105 2521111 2521111 // 3021001 3511102 3521003 3521006 3521007 3521008 3521013 3521014 3521106 3521108 //`

## Pre-match model versus play

- Engine: partly correct. Warlock prayer plus Blessing Staff kept Wing/Warrior alive and converted damage into repeated attacks. The second Staff also exposed a bug, but its legitimate last marker later grew the Warrior. Flowers and Holy Defenders were correctly treated as expendable and discarded once the conversion breakpoint was reached.
- Clock: improved over 001, but still draw-sensitive. First clean hero damage arrived on B turn 4, meeting the turn-6 threshold. Wing hit Bailey on turns 4 and 5. The clock then stalled behind Hidden and repeated center blockers until the turn-22 double physical burst and turn-28 lethal.
- Bridge: Glory was excellent on turn 4: it killed the center blocker and preserved Wing for a same-turn hero hit. Moon Dust was decisive on turn 28 by legally stripping Hidden from the sole front blocker. Shift repeatedly restored the center attack cell and created relevant future attacks. Slash was a strong defense/clear card, but one copy cannot defend in the opponent turn and then attack in the immediately following own turn.
- Breakpoint: the stop-healing rule was directionally right. Prayer remained mandatory, but optional resources went to attackers, movement and clearing; both Life Flowers and a Holy Defender were discarded late. Some defensive Slash uses were still necessary to avoid losing the current clock.
- Cadence: the planned two-action cadence was achieved intermittently, not continuously. Turns 4-5 produced bridge plus hero attack. Turns 12-22 mostly produced blocker damage/replacement attackers. Turns 22 and 28 were the decisive conversion turns.

## Hero damage attribution

- Generic physical attackers: 7 total, all clean.
  - Wing: turn 4 for 1, turn 5 for 1, turn 22 for 1.
  - Archmage Lunde: turn 22 for 2, turn 28 lethal for 2 (Bailey 1 to -1).
- Learned Light attacks: 0 hero damage.
- Attack scrolls: 0 hero damage. Punishment Arrow correctly rejected hero targeting.
- Other/trigger: 0.

The pre-registered expectation that physical attackers would be primary was correct. The expected spell/scroll reach did not materialize; these cards were blocker bridges, not hero finishers in this match.

## Important play evidence

- Turn 4 Glory Scroll cleared the center Wolf and Wing immediately hit Bailey. This is the cleanest evidence that clearing is valuable only when it preserves a same-turn attacker.
- Moon Dust removed legal Hidden from Mist Dancer earlier and removed Hidden from the last Cannon on turn 28. The latter directly enabled Wing to clear the blocker and Lunde to deal lethal.
- Shift was strongest when it moved a durable attacker from rear to center or opened center for a Rapid Killer. It was setup-only when no ready follow-up existed.
- Archmage supplied a real 2-attack clock, but both entry/death buffs landed on utility or already-sufficient spells; buffing Shift's attack was functionally wasted.
- Blessing Staff/Prayer growth made Warrior a recurring blocker-clearer, but healing itself never dealt hero damage. It was tempo-positive only when it preserved the next attack.
- Defensive Slash created a structural cadence cost: after being used during A's turn, it stayed horizontal throughout B's immediately following turn. A single copy therefore cannot be both the defense and the own-turn bridge in the same round.

## Errors and suspected bugs

1. **Blessing Staff illegal empty use.** On B turn 6, fresh Staff `ci_232` entered horizontal with three markers. `use_ability(per_turn)` was accepted, emitted `ability_used`, and incremented use state, but produced no target/effect and consumed no marker. A horizontal source should not pay a printed consume/tap cost. Transcript time around `2026-08-24T03:28:02Z` contains the exact event sequence.
2. **Corrected event-reading error at turn 14.** Ice Cone `ci_200` had power 6 and Slash `ci_243` had power 5. Authority emitted `defense_attempt(6,5)`, then `spell_hit(1)` and damage, exactly like turn 15. `defense_attempt` records a submitted attempt, not success; success must be confirmed by a later `defense_success` event.
3. **Corrected life-tracking error.** Wing was at 3 life before Ice Cone, fell to 2 from its one damage, and then Undertow's two damage destroyed it. The authoritative arithmetic closes without a defect.
4. User-level targeting lesson, not a bug: side-front physical attackers could not reach middle/rear targets; direct hero attacks required coordinates `(1,1)`. Punishment Arrow rejected hero targeting by rule.

## LIGHT-GRACE-MIDRANGE-002 verdict

The active-offense iteration succeeded narrowly: it won officially, dealt first hero damage by turn 4, and dealt hero damage on four separate turns (4, 5, 22, 28). Compared with 001, Archmage, Shift, Glory and Moon Dust supplied genuine finishing structure instead of a pure healing loop.

It is still too slow and blocker-sensitive. The match lasted 28 turns and both decks emptied. Only 7 hero damage was dealt, all physical. Breaker Blades were dead because the opponent had no shield, zero-attack support accumulated in hand, and Slash's defensive timing repeatedly removed the own-turn clearing option.

## Next iteration

- Keep both Archmages, both Rapid Killers, Shift, Glory and Moon Dust.
- Keep healing only at the minimum density needed to preserve one attacker; cut at least two more zero-attack support slots.
- Reduce Breaker Blade to a sideboard/metagame slot or one copy unless shields are common.
- Add another independent clearing spell/scroll so defense does not consume the only own-turn bridge.
- Prefer attack bodies with two attack or haste over more one-load support.
- Treat Glory as live only after explicitly verifying `current life + current load > 5`; Staff growth did not make the turn-18 Warrior a legal support despite intuitive expectations.
- General read rule: identify whether the list has (a) a ready attacker, (b) a different card that clears the front, and (c) a replacement attacker. Healing is tempo only when it preserves one of those three roles. Once the opponent is at 3 or less, Hidden removal and front clearing outrank all optional healing.
