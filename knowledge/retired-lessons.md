# Retired Lessons

Move superseded, disproven, version-specific, or duplicate lessons here instead
of deleting their history. Entries in this file are not part of normal
pre-match context.

Each entry should include:

- the retired statement;
- why it was retired;
- Match IDs or commit that changed the conclusion;
- its replacement rule, when one exists.

## Resolved card-effect defects

Retired on commit `2d9538bab48a2e8e2be384aa0f9ae63e0c4b8f1f`
after targeted unit tests and one two-agent regression room (`1384`) passed:

- #106: 回收小精灵 now resets life, position, statuses, horizontal state, and
  other battlefield state before returning the same instance to the deck.
- #109: 冰霜之心 now prevents only the triggering spell; later enemy and
  friendly spells deal normal damage.
- #110: 连锁闪电卷轴 now exposes draw/search choices and can search the second
  physical copy.
- #111: 魔法蒲公英 draws only when summoned in the turn it was drawn.
- #112: opposing/friendly unrelated consumes no longer trigger 锻石工匠; its
  own active consume taps it and grants the selected spell +2 power.

Do not use the old broken behavior as strategic evidence. Issue #107 remains
open because it is a terminology mismatch rather than one of these mechanics.
