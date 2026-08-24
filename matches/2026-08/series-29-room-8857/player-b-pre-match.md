# Series29 Player B Pre-match

## Identity

- Deck ID: `LIGHT-GRACE-MIDRANGE-002`
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Controlled iteration from `LIGHT-GRACE-MIDRANGE-001`; no Giant Sandworm or known Issue-path card.

## Exact changes from LIGHT-GRACE-MIDRANGE-001

Main deck removals:

- `-2 光铸泰坦` (`1521002`)
- `-2 索洛城的坚守者` (`1521016`)
- `-2 神圣之子` (`1521102`)
- `-2 孤星城的守护灵` (`1521103`)

Main deck additions:

- `+2 大法师 伦德萨尔` (`1511002`): two-attack recurring clock and spell-growth value on entry/death.
- `+2 破魔之刃` (`2021102`): removes shield three so Light Wave/physical attacks convert into life loss.
- `+2 惩戒之箭卷轴` (`2521008`): penetrating bridge and potential hero reach.
- `+2 光之刃卷轴` (`2521009`): front-row bridge that does not consume the learned Light Wave cadence.
- `+2 月霞之尘` (`2521102`) is also present in the final list by replacing the two prior `沐光卷轴` (`2521106`), so the full main-deck delta is ten out / ten in.

Additional main-deck removal for that last pair:

- `-2 沐光卷轴` (`2521106`)

Skill-pool changes:

- `-治疗术` (`3521001`) `+移形换影` (`3021001`): convert setup into an extra attack or restore the center attack cell.
- `-流光之束` (`3521105`) `+光辉斩裂` (`3521006`): remove the unsupported Air requirement and add a live two-attack mono-Light finisher.

## Five-layer model

### Engine

The minimal engine is now explicit: one durable attacker (`屠魔者武士` or `御座的圣翼`) plus `祝福之杖` or `治疗术士`. Staff growth is valuable only because it preserves a real attacker and supplies two Light for a bridge. Flowers are cheap independent Light and Warlocks provide limited repeatable healing; no other card is counted as required engine infrastructure.

### Clock

Primary clock is physical: two Warriors, two Wings, two Rapid Killers, and two Archmages. A valid clock means a legal hero attack this turn and a named ready attacker next turn. Archmage's two attack should shorten both blocker and hero clocks. Secondary clock is `光辉斩裂` or a penetrating scroll; unlike the prior Flowing Beam, every cast expense is producible by the mono-Light board.

### Bridge

- `神谕卷轴 荣耀`: remove a priority blocker with the grown attacker as support.
- `光辉波动` / `光之刃卷轴`: clear or stun front rows before physical attacks.
- `惩戒之箭卷轴`: penetrate a blocker or supply reach.
- `破魔之刃`: remove shield before committing low-attack AOE or hero hits.
- `月霞之尘`: remove legal Hidden from the entire enemy front without targeting the Hidden unit.
- `移形换影`: turn a rear ready body into an additional same-turn attack and reopen center-front for the next attacker.

### Breakpoint

1. Resource breakpoint: one independent Light source plus one true attacker.
2. Staff breakpoint: a damaged or growth-worthy attacker and a bridge that can use the two generated Light this turn.
3. Attack breakpoint: at least two ready attackers or one ready attacker plus a clearing spell/scroll.
4. Conversion breakpoint: after two consecutive turns with clean blocker damage but zero clean hero damage, all optional healing/support stops; reserve resources for shield removal, displacement, haste, or direct/piercing attack.
5. Finisher breakpoint: opponent at three life or lower means `荣耀`, `惩戒之箭`, `光辉斩裂`, and Rapid Killer take priority over every heal that does not prevent immediate defeat.

### Cadence

Pre-register the attack cadence by turn:

- Turn 1: establish one attack cell/body if legal; reduced first-player resources may use Flower/Warlock only as a bridge to turn 2.
- Turn 2: center-front true attacker must exist; take a profitable unit attack or hero hit.
- Turn 3: first repeat attack; if blocked, deploy/learn the bridge while preserving a second ready attacker.
- Turn 4 onward: target at least two physical/spell attack actions per own turn. One clears the blocker; the second must threaten the hero or prepare an explicit same-turn follow-up through Shift/haste.

Before every summon, name `attacker-now`, `attacker-next`, and the square that must stay open. Center-front belongs to Warrior, Archmage, or a shifted attacker. Healer/Flower stay middle or rear. Do not summon a zero-attack support into the last open front cell.

## Healing-to-offense threshold

Healing is allowed only if at least one is true:

- it preserves an attacker that will make a legal attack this turn or next turn;
- Staff simultaneously supplies the exact Light for a clearing/finishing action;
- without the heal, the opponent has a demonstrated lethal line before the next attack.

Stop healing immediately when two ready attackers exist, when the opponent is at three life or lower, or after two consecutive blocker-only turns. At that point, even a damaged attacker is spent forward if it opens a lane; no resources go to rear supports or maximum-life growth.

## Opening priorities

Mulligan for one 3-4 cost attacker, one independent Light body, then Staff or a bridge. Keep Archmage only with a credible seven-Light line by turn 3-4. Keep Moon Dust only against visible legal Hidden/set-card evidence; do not assume a known bug matchup. Keep Breaker Blade against shield heroes, otherwise prefer an attacker.

## Pre-registered hero-damage attribution

Track clean damage only:

1. Generic physical attackers (Warrior/Killer/Wing/Archmage): expected `4-7`; primary source.
2. Learned mono-Light attacks (`光辉斩裂`, `归心`, `光辉波动`, `孤星闪耀`): expected `1-3`.
3. Attack scrolls (`荣耀`, `惩戒之箭`, `光之刃`): expected `0-3`.
4. Other/trigger damage: expected `0`.

Success requires the first clean hero damage by turn 6 and at least two separate turns with legal hero damage. If the list only clears blockers while healing, the active-finisher iteration has failed regardless of survival or board size.
