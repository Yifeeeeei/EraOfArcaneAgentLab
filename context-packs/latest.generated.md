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

### series-30-room-4994

- Game commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Result: `player_b`, turn 21
- Evidence: `matches/2026-08/series-30-room-4994`

# series-30-room-4994

- Result: Player B won by legal surrender on turn 21; both heroes remained at 6.
- Duration: 2323 seconds.
- Giant Sandworm Issue #147 passed: three real damage events produced three correct Hidden gains, unrelated/prevented damage produced none, and decay plus Moon Dust removal were correct.
- Earth attacked on 75% of measured turns but dealt only three physical hero damage. Light made 17 successful physical attacks and dealt zero hero damage; every attack was spent on units.
- A malformed coordinate payload exposed strict-input gap [#153](https://github.com/Yifeeeeei/EraOfArcaneGame/issues/153). It was not a targeting or Sandworm defect.

### series-31-room-2835

- Game commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Result: `player_b`, turn 9
- Evidence: `matches/2026-08/series-31-room-2835`

# series-31-room-2835

- Result: Player B won by legal surrender on turn 9, A 4–B 6.
- Duration: 874 seconds.
- Water-Shadow 002 used two Arcane Bombs effectively but attacked only once in seven eligible turns and dealt zero hero damage. Explicit Dark and Water-five/six costs remained stranded behind a four-Water hero.
- Frozen Clock 001 dealt hero damage on turns 1 and 2 with one Rapid Slayer. Sophia's one-use freeze bridge correctly killed a blocker, but zero of three clears converted into a later hero hit.
- A rear Archer was blocked by its owner's center-front unit. Rear attack permission does not bypass a friendly unit in the same line.

### series-32-room-5128

- Game commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Result: `player_b`, turn 12
- Evidence: `matches/2026-08/series-32-room-5128`

# series-32-room-5128

- Result: Player B won by legal surrender on turn 12, A 4–B 5.
- Duration: 1920 seconds.
- Mono-Fire had zero colored-payment failures, first attacked on turn 2, and attacked on seven completed turns. It still dealt only one hero damage, from Fire Arrow on turn 8; all physical attacks were absorbed by replacement fronts.
- Frozen Clock 002 searched four Water companions with Mermaid plus one with Water Scry and made zero friendly-obstruction mistakes. Sophia remained a one-use bridge.
- One of three clear sequences converted into a next-turn hit. South Sea Monster plus an unobstructed rear Archer dealt the first two hero damage on turn 11.
