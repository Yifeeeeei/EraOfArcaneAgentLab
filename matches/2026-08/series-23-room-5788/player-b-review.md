# Player B Review — series-23-room-5788

- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Deck ID: `WIND-RUSH-006`
- Result: Player A win, official `game_over` on turn 15; final hero life A 2, B 0.
- Transcript: `agent-data/matches/series-23-room-5788/player-b.jsonl`

## Exact deck code

`4311001 // 1321001 1321001 1321002 1321002 1321003 1321003 1321004 1321004 1321007 1321007 1321008 1321008 1321011 1321011 1321013 1321013 1321016 1321016 1021001 1021001 1021011 1021011 2021012 2021012 2021014 2021014 2321009 2321009 1311003 1311003 // 3321001 3321002 3321003 3321005 3321007 3321013 3321014 3321015 3021001 3021009`

## Experimental hypothesis and execution

WIND-RUSH-006 reduced the prior curve and added two `魔法蒲公英` plus a second `传送法师`, aiming to establish independent gas sources and produce earlier double/triple spell turns. The resource part worked: by turn 3 the board had `雷精灵`, `卡琳娜`, `魔法蒲公英`, and a centrally adjacent `风息奔马`, enabling seven or more gas-equivalent resources in later turns. The first planned turn-2 double cast was only partially valid: newly learned `气旋波` entered horizontal, while rush `霹雳惊雷` was ready, so a same-turn pair cannot be formed from those two skills.

Turn 4 was the clearest successful execution. After the opponent filled all three front squares, B chained `气旋波`, `霹雳惊雷`, and two `连锁闪电卷轴`. The first two pressured defense; the scroll chain killed `巫师的学徒`, `火荆`, and `烽火台守卫`, leaving only Kran. The first scroll searched the second; when no further copy remained, the second automatically drew a card. This was the deck's best breakthrough turn.

The direct-damage finish did not exist. Generic attack skills `气旋波` and `霹雳惊雷` rejected `target_type:"hero"` even with no opposing companions. This was reproduced through ordinary cast payloads and through `速写卷轴`. The latter's authoritative `sketch_scroll_target` candidates explicitly contained enemy companions only, not the enemy hero. Code inspection after the game confirms `validateSpellTargetWithPierce` rejects hero targets for generic spells, so this is current target policy rather than a malformed CLI payload; it should not be filed as a bug without a rule/text decision from the designer.

B instead dealt hero damage via `屠魔者杀手` and Su's ultimate. The killer attacked Kran repeatedly while spells and scrolls cleared front blockers; Su discarded two `工蜂骑士` to deal one direct damage. This brought Kran to 2. The opponent then repeatedly supplied one-life front blockers, accumulated ignite through successful `烈焰反噬` defenses, and survived behind shield from `烽火台守卫`/`熔岩魔甲 业炎`. B died to ignite during turn-15 cleanup.

## Decisions that worked

- Central-front placement for the first `风息奔马` fixed the prior adjacency mistake and enabled a large resource turn.
- The two-scroll line correctly selected search first, then received an automatic draw after the second copy was exhausted.
- Preserving `屠魔者杀手` rather than spending it into every blocker created repeated direct hero damage and forced A to keep rebuilding the front.
- Su's ultimate converted two stranded three-cost `工蜂骑士` into direct damage, which was more valuable than trying to find board space for them.
- At low life, B discovered a legitimate digging line: cast `霹雳惊雷` on its own `随风旅行者`, triggering the traveler's death draw. This worked twice and is strategically useful when the board is clogged with zero-attack resource units.
- `霹雳惊雷` plus `气旋波` defended a power-3 `火球术`; with Karina active, overexerting Su and explicitly paying four gas was accepted.

## Mistakes and rule-learning

- The initial experiment assumed both newly learned skills could cast on turn 2. `气旋波` was horizontal after learning; only rush `霹雳惊雷` was ready.
- Several early hero-target attempts spent no resources but consumed tempo and showed a wrong strategic assumption: generic attack spells in this implementation target units, not heroes. Pierce did not change that.
- A direct attack at Kran on turn 8 was rejected because a newly summoned front blocker existed; the subsequent legal attack killed the blocker without cost from the rejected action.
- `速写卷轴` is a pending-action workflow: choose the learned spell, then resolve `sketch_scroll_target`; issuing a normal `cast_spell` while this target pending exists is rejected as `not in main phase`.
- The deck generated more resources than it could convert once only the enemy hero remained. Its two learned attack skills were unit removal, while most surviving companions had zero attack.
- Two `工蜂骑士` were again stranded by board congestion and were ultimately only ultimate fuel. Their three-cost 1-attack profile remains too slow for the intended finish.

## Bugs or suspicious behavior

No issue should be filed from this review without further rule confirmation.

- Hero-target rejection was highly visible but is explicitly enforced by current generic spell-target code and reproduced by the candidate list. It may be a design mismatch if the intended tabletop rule allows these spells to hit heroes, but current metadata/text does not settle that question.
- Karina correctly increased non-piercing gas spell cost. A serialized pending `气旋波` still showed base `has_pierce:false`; successful defenses are not evidence of a bug because pierce does not mean “cannot be defended.” No incorrect outcome was demonstrated.
- Rejected actions (`spell cannot target hero`, `not in main phase`, `cannot consume now`, `target is not in attack range`) caused no observed resource/card mutation.

## Concrete game-3 iteration

Deck goal: keep the low-cost gas engine and scroll chain, but add reliable attackers/direct finishing rather than more zero-attack resource bodies.

Recommended changes from WIND-RUSH-006:

- Remove both `工蜂骑士` (`1321007` x2). They were stranded and became discard fuel.
- Remove one `传送法师` (`1321013` x1). Movement was not used because the important issue was attack conversion, not positioning.
- Add back both `屠魔者武士` (`1021013` x2) if legal in the current pool, plus one additional rush/attack companion already in the list or one copy of a direct-damage item. Validate exact substitutions before game 3.
- Keep both `连锁闪电卷轴`, both `屠魔者杀手`, both `魔法蒲公英`, and both Karina copies.

Game-3 experiment: mulligan for one early resource companion plus `屠魔者杀手` or another attack body. Learn one reusable removal spell early, but do not over-invest in a second removal-only skill until an attacker is established. Use spell/scroll chains to clear the front immediately before one or more direct unit attacks. Treat Su's ultimate as the final unavoidable point and preserve two gas cards for it only when the opponent reaches 1 life.
