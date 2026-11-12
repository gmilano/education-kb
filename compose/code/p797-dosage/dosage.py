#!/usr/bin/env python3
"""p797 - ACTION p796-A, THIRD CARRY, BUILT. The smallest dosage instrument.

Why it exists. `T907` (the strongest RCT this base has read) found the binding constraint on an
AI tutor is not model capability but ENGAGEMENT: ~96% uptake, about a third of the intended
dosage, 0.06 SD ITT. Every regulator that now compels evidence compels evidence of this shape -
Vietnam's pre-deployment registration in the National AI Database, TEQSA's institutional
generative-AI action plan from every Australian provider, and from `2026-11-10` Brazil's
`Parecer CNE/CP 15/2026`, which gives institutions 12 months to show governance over AI use.
An LMS cannot produce it: Moodle and Canvas log *page views and submissions*, not whether a tutor
was offered, taken up, and used for long enough to matter.

Three passes scoped this and none built it, because scoping always lost the budget contest to an
action with a finding in it. So this is deliberately the SMALLEST version that is honest:

  * four metrics, named exactly as `p796-A` specified them;
  * over a tutor-agnostic EVENT LOG, not over any one tutor's schema, because PUC Chile already
    runs 194 pedagogical agents and no engagement will have one;
  * with the Canvas adapter kept to one function, so swapping `vishalsachdev/canvas-mcp` (MIT)
    for a different system of record is a 20-line change, not a rewrite;
  * and with the zeros IN. Its own first control caught it taking a median over only the students
    who practised, which flattered the result by excluding the student who was offered the tutor
    and never took a turn - the population `T907` says dominates.

What it does NOT do, stated so nobody mistakes the scope: no identity resolution, no timezone
policy beyond the caller's chosen day key (`Gap 541` applies - a day boundary is a decision), no
causal claim. It measures delivered dose. Attributing outcomes to dose is a different instrument.

Event log: one JSON object per line.
    {"student": "s1", "session": "x1", "event": "offered"|"accepted"|"turn", "ts": "2026-11-12T09:00:00"}
`offered` is the tutor being put in front of a student - the denominator nobody records.

No network. `python3 -I dosage.py EVENTS.jsonl` prints the four metrics.
"""
import json
import sys
from collections import defaultdict


def metrics(events, day_key=lambda ts: ts[:10]):
    """-> dict of the four `p796-A` metrics. `events` is an iterable of dicts."""
    offered, accepted = set(), set()
    turns = defaultdict(int)
    practice_days = defaultdict(set)
    sessions_of = defaultdict(set)
    for e in events:
        kind, sess, stu, ts = e.get('event'), e.get('session'), e.get('student'), e.get('ts', '')
        if not kind or not sess:
            continue
        sessions_of[stu].add(sess)
        if kind == 'offered':
            offered.add(sess)
        elif kind == 'accepted':
            accepted.add(sess)
        elif kind == 'turn':
            turns[sess] += 1
            if ts:
                practice_days[stu].add(day_key(ts))
    # A session with turns was accepted whether or not an `accepted` event was logged: a turn is
    # stronger evidence of acceptance than an acceptance event is. Recorded explicitly because it
    # changes the denominator, which is the whole point of the instrument.
    accepted |= set(turns)
    engaged = [turns[s] for s in accepted]
    return {
        'sessions_triggered': len(offered | accepted),
        'sessions_accepted': len(accepted),
        'acceptance_rate': (len(accepted) / len(offered | accepted)) if (offered or accepted) else None,
        'turns_total': sum(turns.values()),
        'turns_per_accepted_session': (sum(engaged) / len(engaged)) if engaged else None,
        'students': len(sessions_of),
        'practice_days_with_a_turn': {k: len(v) for k, v in sorted(practice_days.items())},
        # Over EVERY student who was offered the tutor, counting 0 for those who never took a
        # turn. Taking the median over only the students who practised was this instrument's
        # first defect, caught by its own control: it read 2.5 where the honest answer is 2,
        # because it had silently dropped the student who was offered the tutor twice and never
        # engaged - who is precisely the student `T907` says dominates the population. A dosage
        # metric that excludes the zeros measures the engaged, and the engaged were never the
        # question.
        'median_practice_days': _median(
            [len(practice_days.get(stu, ())) for stu in sessions_of]),
        'students_with_zero_turns': sum(
            1 for stu, ss in sessions_of.items() if not any(turns[s] for s in ss)),
    }


def _median(xs):
    if not xs:
        return None
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def from_canvas_mcp(rows, event_field='type', session_field='id',
                    student_field='user_id', ts_field='created_at'):
    """Adapter: Canvas-shaped rows (as `vishalsachdev/canvas-mcp` returns them) -> events.

    Kept to one function on purpose. `canvas-mcp` is MIT and its auth model was read at `p793`
    (`ACTION p792-D`); nothing here depends on a Canvas-only field name, so a different system of
    record is a change of four keyword arguments.
    """
    norm = {'tutor_offered': 'offered', 'tutor_accepted': 'accepted', 'tutor_turn': 'turn'}
    for r in rows:
        kind = norm.get(r.get(event_field), r.get(event_field))
        yield {'event': kind, 'session': r.get(session_field),
               'student': r.get(student_field), 'ts': (r.get(ts_field) or '')}


if __name__ == '__main__':
    path = sys.argv[1]
    with open(path) as fh:
        evs = [json.loads(ln) for ln in fh if ln.strip()]
    out = metrics(evs)
    for k, v in out.items():
        print('%-28s %s' % (k, v))
