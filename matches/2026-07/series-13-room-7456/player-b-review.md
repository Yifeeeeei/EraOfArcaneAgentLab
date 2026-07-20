# Series 13 / room7456 — Player B review

## Result

- CodexA (slot 0) won on turn 7.
- Final heroes: A 5 life, B 0 life.
- A sacrificed `火焰箭` for 1 direct damage to finish B.
- Both heroes took damage by turn 3, and the game ended before the turn-9 target.

## B experiment

Series 13 kept the partner-paid defense shell from Series 12 and made one controlled offensive change:

- removed `坚冰领域` (`3221014`)
- added `水占术` (`3221007`)

The hypothesis was that a turn-1 `水占术` learn could produce early damage without abandoning cheap companions that pay for `寒冰屏障` / `冰锥术` defense.

## What worked

- The opening line fit exactly: first-player hero consume, learn `水占术`, summon `北海飞鱼`.
- The first `水占术` on turn 2 found both `水形之束` and `寒冰爆裂`. B took `水形之束` for immediate pressure and put `寒冰爆裂` on top.
- `水形之束` hit A's naked hero on turn 2, reducing it from 6 to 5. This restored the early offensive clock that Series 12 lacked.
- Deck manipulation behaved coherently: the selected card entered hand, explicit `top_order` controlled the next draw, and unwanted candidates could be sent to the bottom.
- `水占术`'s cooldown cadence was correct: cast on turns 2, 4, and 6, with unavailable turns between.
- Partner-paid defense worked on turn 4: `海豚伙伴` overexerted to pay for `寒冰屏障`, stopping a fireball while leaving B's hero vertical.
- B correctly declined an impossible defense on turn 6. `寒冰屏障` plus `冰锥术` totaled only 7 against the 9-power `焚烧`; spending both would have lost the fish anyway.

## What did not work

- The pressure was not sustained. B dealt the single turn-2 hero damage and never damaged A's hero again.
- The turn-4 and turn-6 divinations found no direct damage. B used them to take cheap companions, which supported defense but did not create a lethal clock.
- A repeatedly spent defense to preserve a 1-life `屠魔者杀手`:
  - turn 5: `火球术` + `烈焰护体`, with two units overexerted, stopped `水形之束`;
  - turn 6: `烈焰护体`, with `活泼的炉火` overexerted, stopped `冰锥术`.
- Those defenses cost A tempo, but preserving the attacker was correct: it dealt hero damage on turns 5 and 6 and forced B to 1 life.
- B's cheap defense partners were temporary shields. After `海豚伙伴` paid for the turn-4 barrier, A's surviving attacker killed it physically; the turn-6 fish was then removed by the oversized burn spell.

## Rules and implementation observations

- No new backend/API bug was observed.
- No card-text/implementation mismatch was observed.
- A's attempt to equip a second `凤凰之羽` was correctly rejected because the same equipment subtype was already occupied and no replacement was selected.
- The full action, pending-action, defense, cooldown, deck-ordering, direct-damage, and game-over paths all completed normally.

## Next iteration

Keep `水占术`: it achieved the intended turn-2 damage and made the opening more deliberate. The next change should improve the density or conversion rate of follow-up damage rather than removing the companion-paid defense package. A useful target is a line that turns the cards found on the second or third divination into hero pressure, instead of defaulting to another expendable blocker.
