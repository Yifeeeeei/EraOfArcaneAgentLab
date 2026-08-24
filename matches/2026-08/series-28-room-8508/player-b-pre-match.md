# Series28 Player B Pre-match

## Identity

- Deck ID: `LIGHT-GRACE-MIDRANGE-001`
- Game commit: `e6908601d0ffd7f538d6eae22d9bd7c18d5c8ecb`
- Constraint: new Base + Royal Conflict Light healing/shield midrange; no copied deck code.

## Five-layer model

### Engine

The repeatable core is `祝福之杖` plus `神圣之子` / `索洛城的坚守者`: the Staff turns one activation into +1 life and two temporary Light, Holy Child doubles a life/load gain through its ultimate, and Defender converts otherwise-wasted full-life healing into permanent life. `治疗术士`, `生命之花`, `孤星城的守护灵`, `恩典`, `治疗术`, and `沐光卷轴` provide redundant healing triggers. `末路的王子` and `孤星守护者` add shield without consuming the healing package; `光铸泰坦` replaces cards.

### Clock

The default recurring physical clock is `御座的圣翼` (one attack, four life) and the two neutral `屠魔者武士`, with `屠魔者杀手` converting a cleared lane immediately. Healing is meant to preserve these attackers, not replace them. The spell clock/finisher is `流光之束`, while `神谕卷轴 荣耀` converts a high life+load partner into a high-power penetrating bridge with three hit damage.

### Bridge

`光辉波动` clears or stuns a whole front row, `归心` attacks a square, `绝境之光 孤星闪耀` supplies penetrating splash while behind on unit count, and `神谕卷轴 荣耀` removes a priority blocker. The bridge succeeds only if a ready physical attacker remains after the final blocker is cleared.

### Breakpoints

1. First stable breakpoint: one independent Light source plus one front attacker.
2. Healing breakpoint: Staff or healer plus a worthwhile injured/growth target. Do not cast healing merely because it is available.
3. Holy Child breakpoint: one gain can become an extra life/load; two such triggers make it a durable resource body, but it still is not the clock by itself.
4. Glory breakpoint: select a partner whose current life + load is above five, preferably seven or more, while preserving enough Light to keep an attacker ready.
5. Attack breakpoint: once a ready attacker and one clearing action coexist, stop adding support units and convert the turn into lane clearance plus hero damage.

### Cadence

Before each summon, name the current and next attacker. Center-front belongs first to Warrior/Wing/Killer. Healers and growth supports go middle/rear or side columns. If this turn's attacker survives, heal it after combat and keep the next attacker out of its square; if it dies, the next summon takes center-front. Never fill all front cells with zero-attack healing bodies.

## When healing is tempo

Healing is a tempo gain when it:

- preserves a ready attacker for another hero attack;
- moves a unit out of the opponent's known one-hit removal range;
- activates Defender at full life for permanent growth;
- triggers Holy Child's extra life/load and crosses the Glory threshold;
- creates enough Light through Staff/Grace to cast the clearing bridge in the same turn.

Healing is not tempo when it only increases a rear support body that cannot attack, when the target will still die to the same next hit, or when spending the healer/resource prevents clearing the front lane. Stop healing and turn to offense as soon as a ready attacker plus a legal bridge can produce hero damage; at opponent life 3 or lower, prioritize direct three-damage Glory or repeated physical hits over further stabilization.

## Opening priorities and first three turns

Mulligan priority: one 2–4 cost attacker (`武士`, `御座圣翼`, or emergency `杀手`), one independent Light body, then Staff/Prince. Keep Holy Child only with a near-term gain effect. Do not keep multiple mass-heal/Glory cards without bodies.

- Turn 1: branch on reduced first-player load; deploy a one/two-cost Light body or Killer fallback, never assume four Light.
- Turn 2: establish center-front attacker and a side/rear Light source.
- Turn 3: add Staff or shield, take the first profitable trade/hero hit, and preserve a replacement attacker rather than a third passive support.

## Pre-registered hero-damage attribution

Track exact damage in these buckets:

1. Generic physical attackers (Warrior/Killer/Wing): expected 3–5, primary source.
2. Repeated learned Light spells (`流光之束`, `归心`, `绝境之光`, `光辉波动`): expected 1–3, mostly after lanes stabilize.
3. `神谕卷轴 荣耀`: expected 0–3, intended finisher/priority clear.
4. Other/trigger damage: expected 0.

Success requires at least one source to become a repeatable legal hero clock by turn 6; high life, shield, and healing without that clock count as experiment failure even if the game lasts long.
