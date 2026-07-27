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
- Rejected normal actions do not deduct submitted payment. Apparent losses in
  batched play came from reading a stale state after an earlier accepted
  action. Wait for the next authoritative state before sending a dependent
  action. Sources: `series-20-room-2976`, `series-21-room-8085` room-log audit.
- Accepting `end_turn` does not finish cleanup when the active player still has
  a private discard pending action. Card reset and turn ownership change only
  after that pending action resolves. Source: `series-21-room-8085` room-log
  audit.


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

[truncated; retrieve the source file for more]

## Recent completed matches

### series-19-room-3718

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Result: `player_b`, turn 12
- Evidence: `matches/2026-07/series-19-room-3718`

# series-19-room-3718

- Result: Player B won on turn 12, A 0–B 4.
- Duration: 1204 seconds.
- Water Scry found two Krakens and the second center-front Kraken supplied the turn-12 finish; a copied horizontal Lightning Strike disappeared without resolving.
- Confirmed issue: https://github.com/Yifeeeeei/EraOfArcaneGame/issues/125

### series-20-room-2976

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Result: `player_a`, turn 10
- Evidence: `matches/2026-07/series-20-room-2976`

# series-20-room-2976

- Result: Player A won on turn 10, A 5–B 0.
- Duration: 1045 seconds.
- Fire removed both Krakens, exhausted Water defenses with consecutive spells, and finished through a surviving rapid attacker.
- No newly confirmed defect in this match.

### series-21-room-8085

- Game commit: `261247af08dd681f738c8ea0ccb2f01cba5abfad`
- Result: `player_a`, turn 20
- Evidence: `matches/2026-07/series-21-room-8085`

# series-21-room-8085

- Result: Player A won on turn 20, A 4–B 0.
- Duration: 2647 seconds.
- Water protected a one-life center-front Kraken with three independent defenses and attacked the Fire hero once per turn to win.
- No newly confirmed defect in this match.
