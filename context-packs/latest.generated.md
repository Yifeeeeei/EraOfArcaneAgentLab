# Latest Generated Context

Generated from shared facts. Read specific reviews only when needed.

## Stable knowledge

# Core Rules for Codex Players

This file contains only stable, repeatedly confirmed rules that affect normal
decisions. Keep it below 2,000 Chinese characters or roughly 1,200 English
words. Each promoted rule should cite at least one Match ID.

- Use runtime `instance_id`, never card number, in actions.
- Decide whether action is required from `phase`, not only `current_turn`.
  `defense_window` and `waiting_action` can require acting during the
  opponent's normal turn. Source: Match `2026-07-18-room-2342`.
- Cards reset at the end of their owner's turn. A card overexerted during the
  opponent's turn remains horizontal throughout its owner's following turn and
  resets only at that turn's end. Source: Match `2026-07-18-room-2342`.
- Spell power (`威`) is not hit damage. Apply printed or implemented hit damage
  independently. Source: Match `2026-07-18-room-2342`.
- Direct attacks require a valid attack lane. A normal unit must be in the front
  row, and enemy front-row blockers can prevent attacking the hero. Source:
  Match `2026-07-18-room-2342`.
- Unspent elements do not carry between turns. Source:
  Match `2026-07-18-room-2342`.
- The latest player-specific `state_sync` is authoritative. A rejected action
  does not partially advance the game.


# Gameplay Principles

This file contains reusable play heuristics, not match narratives. Keep it
below 2,000 Chinese characters or roughly 1,200 English words. Cite Match IDs
and revise principles when later evidence contradicts them.

- Preserve a ready front-row attacker after clearing the final blocker;
  otherwise a direct-hero opening is wasted. Source:
  Match `2026-07-18-room-2342`.
- Overexert the hero on defense only when the prevented outcome is worth losing
  the following turn's high-value consume. Source:
  Match `2026-07-18-room-2342`.
- Use sorcery damage such as `奥术箭矢` to finish blockers without opening a
  normal defense window. Source: Match `2026-07-18-room-2342`.
- Include delayed status damage in end-step survival estimates. A unit that
  survives the immediate hit may still fail as a blocker. Source:
  Match `2026-07-18-room-2342`.
- Treat defense as a tempo decision. Protecting a low-value target can tap
  skills and units needed for the next offensive turn. Source:
  Match `2026-07-18-room-2342`.
- Resolve owned pending actions before attempting normal main-phase actions.
- Count defensive answers and their independent payment sources separately.
  Two learned defenses backed by one usable element source still answer only
  one threat. Sources: `series-04-room-7618`, `series-05-room-5138`.
- Against a once-per-turn defense, lead with a normal penetrating spell and use
  `速写卷轴` to create the second hit after the defense is horizontal. Sources:
  `series-02-room-0707`, `series-04-room-7618`.
- Preserve off-element resources when paying wildcard costs if a later action
  has a strict same-element expense. Source: `series-06-room-7249`.
- Spell defenses do not answer ordinary unit attacks. Maintain a front-row
  blocker whenever the opponent has a ready attacker. Source:
  `series-03-room-7736`.
- A vertical frozen unit may act once, but after becoming horizontal a long
  freeze locks it. A stunned unit cannot overexert even when serialized as
  vertical. Sources: `series-02-room-0707`, `series-05-room-5138`.
- Treat hero load as fragile when the hero must also overexert for defense or
  can be frozen. Use independent field resource sources. Sources:

[truncated; retrieve the source file for more]

## Recent completed matches

### series-11-room-1398

- Game commit: `05be3b6074b2d83e8b1bb83fc3c20c204ad37d5d`
- Result: `player_a`, turn 8
- Evidence: `matches/2026-07/series-11-room-1398`

# Series 11 — room 1398

- Result: A won turn 8, 3–0, official hero kill. Score A 6–B 5.
- Fair FIRE-BURN-003 replaced bugged 锻石工匠 with 熔岩傀儡 and produced no
  erroneous power modifiers.
- Independent fire/earth generation preserved strict fire payments; physical
  attacks plus a duplicated 火球 completed the game.
- No new defect.

### series-12-room-1320

- Game commit: `05be3b6074b2d83e8b1bb83fc3c20c204ad37d5d`
- Result: `player_a`, turn 10
- Evidence: `matches/2026-07/series-12-room-1320`

# Series 12 — room 1320

- Result: A won by burn settlement on turn 10. Score A 7–B 5.
- B's partner-based water payments preserved the four-water hero and extended
  survival by two turns, but the damage axis failed to hit A at all.
- FIRE-BURN-003 retained strict fire and applied enough repeated ignite to win
  through blockers and two learned defenses.
- No new defect.

### series-13-room-7456

- Game commit: `05be3b6074b2d83e8b1bb83fc3c20c204ad37d5d`
- Result: `player_a`, turn 7
- Evidence: `matches/2026-07/series-13-room-7456`

# Series 13 — room 7456

- Result: A won turn 7, 5–0. Score A 8–B 5.
- FIRE-BURN-004 replaced one 火云法师 with 灼烧卷轴; the new card was not
  drawn, so the change remains untested.
- 水占术 restored B's turn-2 damage by finding 水形之束 and stacking
  寒冰爆裂, but later activations did not sustain the clock.
- No new defect.
