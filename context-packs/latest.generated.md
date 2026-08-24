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
- A printed special `消耗` ability can be exposed as `has_per_turn` with a
  `per_turn_label`. Use `use_ability` with `ability_type: per_turn`; ordinary
  `consume` only turns the card horizontal and takes its load. Cave Elf Pickaxe
  confirmed this distinction. Source: `series-25-room-6658`.
- On current commit `e6908601`, drawing from an empty deck has no consequence.
  It does not cause fatigue, defeat, or an automatic draw. Stable loops require
  external adjudication until Issue #146 is resolved. Source:
  `series-25-room-6658`.


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

[truncated; retrieve the source file for more]

## Recent completed matches

### series-27-room-0313

- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Result: `player_a`, turn 12
- Evidence: `matches/2026-08/series-27-room-0313`

# series-27-room-0313

- Result: Player A won on turn 12, A 2–B 0; the result is issue-contaminated.
- Duration: 1714 seconds.
- Clean evidence: Earth 003 reached six Earth on turn 3 and seven on turn 4, had a legal physical attack on 11 of 12 own turns, never stranded an off-color card, and Spatial Shift directly created two attacks including lethal.
- Controlled opponent evidence: Blood Garden 002 dealt no hero damage through Robert or generic attackers; its four damage came from deathrattles.
- Contamination: Giant Sandworms gained Hidden from unrelated damage under [Issue #147](https://github.com/Yifeeeeei/EraOfArcaneGame/issues/147). Do not use their survival or the match win as clean strength evidence.

### series-28-room-8508

- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Result: `draw`, turn 38
- Evidence: `matches/2026-08/series-28-room-8508`

# series-28-room-8508

- Result: adjudicated draw on turn 38; no official `game_over` and no matchup-strength inference.
- Duration: 3379 seconds.
- Clean Light evidence: Staff plus Healing Warlock preserved one grown attacker, and two Glory Scrolls cleanly removed priority blockers. Only one clean physical hero damage was produced, so the list built an exchange engine rather than a repeatable clock.
- The terminal state combined empty-deck nontermination [#146](https://github.com/Yifeeeeei/EraOfArcaneGame/issues/146) with Giant Sandworm Hidden corruption [#147](https://github.com/Yifeeeeei/EraOfArcaneGame/issues/147).

[truncated; retrieve the source file for more]

### series-29-room-8857

- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Result: `player_b`, turn 28
- Evidence: `matches/2026-08/series-29-room-8857`

# series-29-room-8857

- Result: Player B won officially on turn 28, A -1–B 3.
- Duration: 3818 seconds.
- Light 002 dealt its first clean physical hero damage on turn 4. Its active package improved over Light 001, and the final bridge was Moon Dust removing Hidden, Holy Wing clearing the blocker, then Lundesar attacking for lethal.
- Water-Shadow's Coffin, Elegy, Bone Knight, Hidden and spell-reset packages all generated value, but its first hero damage arrived only on turn 14 via deathrattle; it dealt zero physical hero damage in 28 turns.
- A fresh horizontal Blessing Staff reproduced the generic empty-activation defect [#149](https://github.com/Yifeeeeei/EraOfArcaneGame/issues/149).
- Log audit corrected an Agent mistake: `defense_attempt` is not `defense_success`; Ice Cone 6 correctly beat Slash 5 on turns 14 and 15.
