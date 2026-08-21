# Player A pre-match hypothesis — series 26

- Deck ID: `EARTH-MOBILE-BEATDOWN-002`
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Main victory condition: maintain a real attacker in center-front, remove its blocker with physical trades/scrolls, then use Rapid Killer, Rock Beast, Warrior, Sandworm, Growth Potion, Autumn Jewel, and movement effects to convert openings into repeated hero attacks.
- Constraint retained: learn no skills unless the physical plan has irreversibly failed and a learned spell creates an immediate win.

## Exact iteration from EARTH-SHIELD-MENAGERIE-001

Removed eight cards:

- `翡翠永生` x1 — removed completely; it created a non-terminal shield lock instead of a win.
- `地穴精灵矿镐` x1 — removed pending its broken/unclear per-turn behavior; correct future activation is `use_ability`, not ordinary `consume`.
- `祝祷祭师` x2 — passive bodies occupied attack cells without advancing the win.
- `岩壁巨像` x2 — slow scaling bodies did not attack and arrived too late.
- `拜利兰森林熊` x1 — retain one shield/taunt copy, cut the second six-cost defensive draw.
- `岩壁魔怪` x1 — retain one resilient front blocker, cut the redundant passive copy.
- `翡翠永生`/Pickaxe/passive-body cuts total eight main-deck slots after counting the listed copies.

Added eight cards:

- `岩山恐兽` x2 — attack 2, life 4; the primary heavy physical finisher.
- `传送法师` x2 — moves a stranded attacker into the required front cell.
- `传送符文` x2 — reactive position correction after summon/consume.
- `生长药水` x2 — cheap immediate reset for Sandworm/Rock Beast/Xinke, turning one legal attack into two.

Net list remains 30 main cards / 10 skills.

## Read the deck before playing

### Primary win condition

This is mobile physical beatdown with a small no-spell defensive shell, not a prison deck. Actual hero-damage bodies are `屠魔者杀手`, `屠魔者武士`, `灵兽 辛柯`, `巨型沙虫`, and especially `岩山恐兽`. Scrolls clear or soften blockers; Growth Potion and Autumn Jewel produce an additional attack; Teleport Mage/Rune prevent attackers from being stranded behind supports.

### Attack cell that must remain available

- Center-front is reserved for an attacker whenever possible.
- Do not summon Monk, Monster, Guard, Bear, or Teleport Mage into center-front merely because it is empty, unless it prevents immediate lethal.
- Maintain at least one empty front cell or one ready movement effect. A rear Sandworm/Rock Beast with no legal move is not a win condition.
- Side-front Rapid Killer is acceptable only when it has a legal same-column target or a Teleport effect can reposition it.

### When to stop deploying resources

Stop adding resource/support bodies once these are simultaneously true:

1. one vertical attacker already occupies center-front;
2. enough payment exists for the next scroll/reset/movement action;
3. further deployment would occupy the last front/movement destination.

At that point, spend turns attacking and preserving the attack lane. Do not turn every open cell into nominal value. Never consume the only ready attacker to fund a support card.

### Avoiding another draw lock

- `翡翠永生` is absent. Shield is tempo, not the end state.
- Never choose a line whose only result is permanent prevention. Every two-turn plan must name the next legal hero-damage action.
- If both decks approach empty, prioritize attackers and reset/move cards over Monk/Monster/Bear.
- If the board is full and no attacker can legally hit, use movement immediately and stop summoning.
- Autumn Jewel/Growth Potion is used only after a meaningful first attack, not merely for resource value.

## Opening priority and first three turns

1. Keep one early attacker (`屠魔者杀手`, `屠魔者武士`, reactive Xinke) plus one resource/protection body.
2. Keep Teleport Mage only with an air source (normally Xinke); do not keep two movement cards without an attacker.
3. Keep one scroll if the rest of the hand can produce its cost and field an attacker.
4. Mulligan double six/seven-cost attackers without early production.

- Turn 1: resource body or Warrior; reserve center-front for a body that will attack.
- Turn 2: establish center pressure and keep a distinct payment source vertical if a scroll can clear the blocker.
- Turn 3: attack/trade first, then deploy. If Rock Beast is reachable, pay for it only into a front cell or with movement already available.

## Exchange and reset discipline

- Power is not attack: Forest Arrow/Stonehenge normally deals only 1 life damage.
- Use a scroll plus an ordinary attack to remove a 2-life blocker only when another ready/reset attack can then reach the hero.
- Growth Potion on Sandworm/Rock Beast is the cleanest finish: attack blocker or hero, reset, attack again.
- Teleport Mage requires air; plan Xinke's `地1+气1` load instead of assuming Jade's earth can pay the fixed air requirement.
- Monk prevention is globally once per turn even with two copies; expect opponents to lead with a cheap spell.
- Keep one actual attacker vertical; supports may be overexerted first.
