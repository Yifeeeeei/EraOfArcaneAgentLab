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
- In Kran survival Fire, preserve `烈焰反噬` as the primary defensive burn
  engine until the matchup clearly requires the Primal Flame plan. Do not exile
  it merely because `原初神炎` can grow. Sources: `series-22-room-2714`,
  `series-23-room-5788`, `series-24-room-5281`.
- Treat spell range and spell payment as separate resources. Keep a vertical
  unit in the needed lane while paying from equipment, side-lane units, or
  other independent sources; consuming Kran can otherwise strand a fully paid
  attack with no legal target. Sources: `series-22-room-2714`,
  `series-23-room-5788`.
- Wind Rush is a unit-tempo deck with spell clearing, not a spell-burn deck.
  Generic Wind attack spells clear blockers but do not replace a ready physical
  attacker for hero damage. Reducing attacker density improved resources but
  removed the finish; restoring rapid attackers produced immediate hero damage.
  Sources: `series-23-room-5788`, `series-24-room-5281`.
- Against repeated `烈焰反噬`, do not feed every low-value spell into the same
  defense. Count the resulting end-step burn clock and reserve spells for a
  turn that also converts the cleared lane into unit damage. Sources:
  `series-22-room-2714`, `series-24-room-5281`.
- Read a deck as three linked layers: engine, clock, and bridge. The engine
  creates resources or prevention; the clock repeatedly reduces hero life; the
  bridge converts the engine's advantage into that clock. A strong shield
  engine without a bridge produced only a draw. Sources:
  `series-25-room-6658`, `series-26-room-4685`.
- Convert growth text into explicit breakpoints before playing. Robert starts
  below zero attack and needed two three-marker growth events before becoming
  a one-attack clock; stopping at the first trigger overvalues the engine.
  Sources: `series-25-room-6658`, `series-26-room-4685`.
- Reserving the center-front slot is necessary but insufficient. Plan attack
  cadence: which unit attacks this turn, how it leaves or moves, and which
  ready unit occupies the lane next. Spatial Shift turned an already-used
  attacker into space for a rapid lethal attacker. Source:
  `series-26-room-4685`.
- An off-color movement or utility package needs recurring payment sources in
  the main deck. Legal cards that cannot be paid on the intended turn are not
  functional interaction. Source: `series-26-room-4685`.
- A `defense_attempt` event records that a defense was submitted; it does not
  prove success. Read the following authoritative event for `defense_success`
  or `spell_hit` before evaluating the exchange. Source:
  `series-29-room-8857` plus room-log confirmation.
- Sustain is tempo only when it preserves a body that will make a legal attack
  or supplies the bridge in the same turn. After two blocker-only turns, stop
  adding generic healing unless it changes the clock. Sources:
  `series-28-room-8508`, `series-29-room-8857`.
- Attack cadence is not a clock by itself. Track `attacks created minus enemy
  replacement fronts`, plus the rate at which a clear becomes a hero hit in the
  same turn or by the next own turn. Sources: `series-30-room-4994`,
  `series-31-room-2835`, `series-32-room-5128`.
- A rear attacker still needs its line kept clear of friendly units. Rear attack
  permission does not let it shoot through its own center-front body. Sources:
  `series-31-room-2835`, `series-32-room-5128`.
- Damage events can serialize before `OnDamaged` triggers finish. Verify marks
  and reactive state in the immediately following authoritative state rather
  than treating the event snapshot as final. Source: `series-30-room-4994`.
