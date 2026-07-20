# Codex Deck Lab

The goal is to improve both deck construction and play. Each match should test
a stated hypothesis rather than defaulting indefinitely to the sample deck.

## Experiment format

```markdown
## Deck ID and name

- Exact deck code:
- Core plan:
- Key packages and ratios:
- Mulligan priorities:
- Expected strengths:
- Expected weaknesses:
- Matches:
- Observed result:
- Next controlled change:
```

Change one coherent package at a time when comparing versions. Keep exact deck
codes so later agents can reproduce results. A single win does not establish
that a deck is stronger; consider matchup, first player, draws, and play errors.

## SAMPLE-ARCANE-001 — Baseline sample deck

- Exact deck code: `4311003 // 1021001 1021001 1021002 1021002 1021004 1021004 1021005 1021005 1021006 1021006 1021007 1021007 1021008 1021008 1021009 1021009 1021010 1021010 1021011 1021011 1021012 1021012 1021013 1021013 1021014 1021014 1021015 1021015 1021016 1021016 // 3321002 3001001 3001002 3021001 3021002 3021003 3021004 3021005 3021006 3021007`
- Core plan: generic neutral companion curve backed by flexible arcane skills
  and `掌门 穆伶`.
- Match 2342: mirror match, CodexB won as player 1 on turn 19.
- Observed strength: stable access to bodies, resource generation, targeted
  damage, defense, and utility.
- Observed weakness: the mirror is slow and can fill the board; inefficient
  defensive overexertion creates large tempo losses.
- Next controlled change: build two distinct archetypes rather than another
  mirror. One should maximize front-row aggression and rush; the other should
  test removal/control. Record both exact codes and compare how quickly each
  creates hero-damage opportunities.

## WIND-RUSH-004 — bug-free wind pressure

- Exact deck code: `4311001 // 1321001 1321001 1321002 1321002 1321004 1321004 1321007 1321007 1321008 1321008 1321009 1321011 1321011 1321013 1321016 1321016 1021001 1021001 1021011 1021011 1021013 1021013 2021012 2021012 2021014 2021014 2321009 2321009 1311003 1311003 // 3321001 3321002 3321003 3321005 3321007 3321013 3321014 3321015 3021001 3021009`
- Core plan: printed penetration plus `速写卷轴`, with 卡琳娜 turning cheap
  wind spells into penetrating threats.
- Results: the earlier shell won on turns 15, 4, and 4; after removing the
  bugged 魔法蒲公英, this version lost on turn 7 but still dealt repeated damage.
- Next change: add independent wind resources without reintroducing #111.

## WATER-PRESSURE-003 — aggressive control benchmark

- Exact deck code: `4211003 // 1021011 1021011 1021013 1021013 1221001 1221001 1221003 1221003 1221004 1221004 1221006 1221006 1221009 1221009 1221011 1221011 1221013 1221013 1221014 1221014 1221016 1221016 2021014 2021014 2221004 2221004 2221008 2221008 2221009 2221009 // 3221001 3221002 3221003 3221004 3221005 3221008 3221009 3221011 3221012 3221014`
- Core plan: independent water sources support repeated defense while
  `幽影寒锋`, `冰雹`, scrolls, and rush attackers convert control to damage.
- Results: consecutive wins on turns 6, 7, and 6 in series 07–09.
- Strength: best confirmed balance of defense payments and fast finishing.

## FIRE-BURN-002 — fire burst prototype

- Exact deck code: archived in `series-10-room-9209/player-a-deck.txt`.
- Core plan: 梵天 load growth, direct fire damage, `速写卷轴`, independent
  sources, and neutral attackers.
- Result: won turn 6 after FIRE-BURN-001 lost turn 6; first damage turn 1.
- Warning: the archived code contains 锻石工匠, whose behavior is invalid under
  #112. Replace it before further fair testing.
