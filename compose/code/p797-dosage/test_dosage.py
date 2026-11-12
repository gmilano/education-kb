#!/usr/bin/env python3
"""Offline controls for the p797 dosage instrument.

`p796-G`: the control set spans the KINDS this measurement actually meets in the field - a session
offered and never taken (the case `T907` says dominates), a session with turns but no `accepted`
event (a logger that only records what happened), a student with zero turns across three offers,
and multi-day practice on one session. No network.
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dosage import metrics, from_canvas_mcp   # noqa: E402

here = os.path.dirname(os.path.abspath(__file__))
evs = [json.loads(l) for l in open(os.path.join(here, 'fixture.jsonl')) if l.strip()]
m = metrics(evs)

EXPECT = {
    'sessions_triggered': 6,            # a1 a2 a3 b1 b2 c1
    'sessions_accepted': 3,             # a1 (explicit), a3 (turn only), c1
    'turns_total': 6,
    'students': 3,
    'students_with_zero_turns': 1,      # s2: offered twice, never engaged
    'median_practice_days': 2,          # s1=2 days, s3=3 days, s2 absent from the map
}
fails = 0
for k, v in EXPECT.items():
    if m[k] != v:
        print('RED %s = %r, expected %r' % (k, m[k], v))
        fails += 1
if abs(m['acceptance_rate'] - 0.5) > 1e-9:
    print('RED acceptance_rate = %r, expected 0.5' % m['acceptance_rate'])
    fails += 1
if abs(m['turns_per_accepted_session'] - 2.0) > 1e-9:
    print('RED turns_per_accepted_session = %r, expected 2.0' % m['turns_per_accepted_session'])
    fails += 1
if m['practice_days_with_a_turn'] != {'s1': 2, 's3': 3}:
    print('RED practice_days_with_a_turn = %r' % m['practice_days_with_a_turn'])
    fails += 1
# A turn implies acceptance even with no `accepted` event - the denominator rule, controlled.
only_turn = metrics([{'student': 'z', 'session': 'q', 'event': 'turn', 'ts': '2026-11-01T00:00:00'}])
if only_turn['sessions_accepted'] != 1:
    print('RED a turn without an acceptance event did not count as accepted')
    fails += 1
# An empty log must not divide by zero.
empty = metrics([])
if empty['acceptance_rate'] is not None or empty['turns_per_accepted_session'] is not None:
    print('RED empty log did not return None for the ratios')
    fails += 1
# The Canvas adapter maps its vocabulary and preserves the counts.
canvas = list(from_canvas_mcp([
    {'type': 'tutor_offered', 'id': 'k1', 'user_id': 'u1', 'created_at': '2026-11-01T00:00:00'},
    {'type': 'tutor_turn', 'id': 'k1', 'user_id': 'u1', 'created_at': '2026-11-01T00:10:00'},
]))
cm = metrics(canvas)
if cm['sessions_accepted'] != 1 or cm['turns_total'] != 1:
    print('RED canvas adapter: %r' % cm)
    fails += 1
print('-- p797-dosage controls: 11 assertions over 4 field kinds (offered-never-taken, '
      'turn-without-acceptance, zero-turn student, multi-day practice) + empty log + adapter')
if fails:
    print('RED %d control(s) failed' % fails)
    sys.exit(1)
print('   PASS')
