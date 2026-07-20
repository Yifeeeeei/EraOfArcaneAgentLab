# Match series-01-room-2546

- Result: CodexB / ARCANE-CONTROL-001 won on turn 23, 5 life to 0.
- Duration: approximately 96 minutes.
- Player A deck: WIND-RUSH-001 (`player-a-deck.txt`).
- Player B deck: ARCANE-CONTROL-001 (`player-b-deck.txt`).
- Key process: A used 雷术士 肃 to deal the first hero damage on turn 2, but
  could not sustain pressure; B stabilized, controlled the front row, and used
  南海海怪 for repeated direct attacks on turns 20–23.
- Confirmed bug: 冰霜之心 incorrectly left an `all_spell_attack_zero` modifier
  that affected later enemy and friendly spells.
- Issue: https://github.com/Yifeeeeei/EraOfArcaneGame/issues/109
