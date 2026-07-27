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
  `series-07-room-8183`, `series-09-room-0057`.
- Separate spell power from hit attack. Power determines the defense threshold;
  attack determines life loss. Source: `series-02-room-0707`.
- When full state output is too large, query the private transcript for phase,
  pending action, resources, hand, and board. Never inspect the opponent's
  private transcript during the match.
- Reserve a center-front slot for an actual attacker before committing the
  sixth support/resource unit. Both Water and Wind produced strong control
  boards that could not legally damage the opposing hero after their attackers
  died. Sources: `series-15-room-3951`, `series-16-room-2570`,
  `series-18-room-0731`.
- Water Scry converts control into a win only when it prioritizes a protected
  center-front finisher. The first side-lane Kraken delayed pressure; later
  center-front Krakens won after the defense engine was established. Sources:
  `series-19-room-3718`, `series-21-room-8085`.
- Submit dependent headless actions one at a time and wait for the next
  authoritative state. Batched learn/pay/summon sequences create stale-state
  mistakes that resemble engine failures. Sources: `series-20-room-2976`,
  `series-21-room-8085`.
- `waiting_action` with no local `pending_action` can mean the opponent owns a
  private reaction, such as Dolphin lethal prevention. It is not sufficient
  evidence of a soft lock. Source: `series-20-room-2976`.
