# Pre-registration, pass 589 — written and committed BEFORE any measurement
## Closing 584-E (Trend 39's mechanism has a mechanism and only two data points)

Trend 39: agent-shaped supply appears where the layer has NO published spec
(0.19% on lti/xapi/qti) and collapses to libraries where one exists (7.9% on
school operations). 584-E: "predict the agent share from whether the layer has a
published spec, THEN measure - one specified axis (topic:scorm) and one
unspecified (topic:iep, topic:truancy)."

### Predictions (p589, before measurement)
- topic:scorm      SPECIFIED (SCORM 1.2 / 2004, ADL)  -> predict agent share <= 1%
- topic:truancy    UNSPECIFIED (operational judgement) -> predict agent share >= 5%

### Calibration controls, measured in the SAME pass with the SAME matcher
- topic:lti        published at 0.19% band by p583
- topic:gradebook  published inside the 7.9% band by p583
Needed because p589 CANNOT execute this base's classifier (environment denies
ingest/*.py), so the matcher below is a declared REPLICA, not the same code.

### Matcher, fixed before the run
agent-shaped := name or description matches, case-insensitive,
  agent|multi-agent|llm|gpt|copilot|chatbot|assistant|mcp|autonomous|ai-tutor
Denominator := total_count from gh api search/repositories -f q='topic:X'
Sample      := up to 100 items/page, all pages up to the API's 1000-item cap.

### Falsified if
scorm > 2% agent-shaped, OR truancy < 2% agent-shaped, OR a control lands
outside the band p583 published for it (which would condemn the replica, not
the trend).
