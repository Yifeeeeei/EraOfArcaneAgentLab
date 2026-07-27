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
