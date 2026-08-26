# Series 31 Player B pre-match

## Registration

- Player: B
- Deck name: **WATER-FROZEN-CLOCK-001**
- Hero: `4211102 凛冰魔巫 索菲娅`
- EraOfArcaneGame commit: `92e09fba884d4f217e07440a0eafc02723807a6b`
- Construction: 30-card main deck + 10 distinct skills, base set + 王权纷争 legality checked locally.
- Comparison intent: a new proactive water list, distinct from LIGHT-GRACE-MIDRANGE-002 and from the user's defensive royal-fire list.

## Engine → clock → bridge

**Engine.** The cheap load curve is mono-water: 海豚伙伴 (1), 寒霜傀儡 (1), 冰原狼 (2), 雾霭幽魂 while hidden (2), plus 水之咏叹's repeatable 3-water activations and two 0-cost 速射冰弹 discounts. 水魔导师 and 踏浪术 convert a single learned low-expense attack spell into extra casts rather than asking for a second color. No card requires off-color payment.

**Clock.** The repeatable hero clock is physical first: 屠魔者杀手 gives an immediate 1-point attack, 屠魔者武士/南海海怪 are durable front attackers, and 凛冬城射手 can keep attacking from a protected rear square. 海上巾帼 珊瑚 雯迪 is the top-end 2-attack closer and can reset a sub-3-expense water spell. The positioning rule is to reserve center-front for a ready attacker and keep one second attacker on a side or in the rear; resource bodies should not occupy the future center lane unless blocking is mandatory.

**Bridge.** 寒霜傀儡、冰封卷轴、寒冰爆裂卷轴、六瓣雪花、霜冻射线 create freeze. 索菲娅 then removes one freeze marker to deal 2 damage to that unit. This turns control into blocker removal instead of merely delaying combat. 水形之束 and the low-expense learned attacks supply the remaining point, while 速射冰弹 compresses the bridge into the same turn. This is the intended conversion: freeze blocker → Sophia 2 damage → cheap spell/physical cleanup → preserved attacker hits the hero.

## Turn-10 plan and payment breakpoints

- T1–T2: establish at least 2 payable water (hero plus one cheap load body), or deploy a rapid Slayer if the center lane is open.
- T3–T4: reach repeatable 4–5 water, learn one 1–2 expense attack skill, and establish the first durable attacker. A hidden 雾霭幽魂 plus hero alone represents 6 water before other bodies; 水之咏叹 represents three future 3-water bursts.
- T5–T7: maintain one ready center attacker and one backup attacker; use freeze plus Sophia's 2 damage only when it clears or materially shortens a blocker. Avoid consuming the planned attacker for mana.
- T8–T10: establish a repeated hero clock of at least 1 damage per own turn. Preferred closer is Wendi (2 physical) or two separate 1-attack bodies; spell resets are the bridge when a blocker appears.
- Color test: 100% of colored main-deck and skill requirements are water. Neutral costs may be paid from water; no conversion card is required.
- Key payable thresholds: 2 water (most setup/cheap attacks), 3 water (water-magister/low spell chain), 5 water (Kraken), 6 water (Wendi), and 6–7 total water for summon-plus-bridge turns.

## Pre-registered metrics

1. First physical attack turn and source; target is no later than T4.
2. First hero damage turn, source, and exact amount; target is no later than T6.
3. First turn with a repeatable hero clock, defined as a surviving ready attacker or repeatable spell line projected to deal hero damage on consecutive own turns; target no later than T10.
4. Water breakpoint timing: first turns with 2, 3, 5, 6, and 7 payable water before spending; distinguish printed load, hidden bonus, Aria activation, and overexertion.
5. Freeze bridge efficiency: for every Sophia ultimate, record freeze source, target life before/after, whether 2 damage cleared a blocker, and whether a hero attack occurred in the same turn or next own turn.
6. Clear-to-hit conversion: number of blockers removed, number followed by hero damage by the next own turn, and conversion rate.
7. Clock continuity: consecutive own turns with hero damage after the clock begins; record each interruption and whether caused by blocker, defense, resource failure, or positioning.
8. Attacker discipline: number of turns a planned attacker was consumed/overexerted for payment; target zero unless it prevents lethal.
9. Rear-archer value: attacks made from non-front positions and whether rear placement preserved the center lane.
10. Spell-reset value: successful 水魔导师、踏浪术、Wendi resets; extra attacks produced; water paid per extra damage.
11. Exact damage ledger split by physical attacks, spell attacks, Sophia ultimate, and other effects.
12. Outcome and official game-over reason; proactive success requires B to cause lethal rather than relying on opponent surrender, timeout, or deck exhaustion.

## Mulligan and pilot rules

- Keep one cheap water load card (海豚、寒霜傀儡、冰原狼、雾霭幽魂), one clock body (Slayer/Archer/Warrior), and at most one engine/bridge card.
- Mulligan duplicate expensive attackers and hands with both Wendies or both Krakens and no cheap load.
- Do not spend freeze merely because a target exists. Prefer a blocker whose removal exposes center or preserves an already-ready attacker.
- Do not reveal hidden information from the opponent client; act only from Player B's authoritative state.
