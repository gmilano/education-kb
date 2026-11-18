"""p884: separate EDUCATION repos from MACHINE-LEARNING repos in a university-lab sweep.

Why this file exists. A naive education keyword set returns 326 "finds" from 5,741
university-lab repositories, and essentially all of them are false. The reason is
specific and structural: the vocabularies OVERLAP exactly where this KB sweeps.

  "learning"    -> machine/deep/reinforcement/transfer/federated/curriculum learning
  "curriculum"  -> *curriculum learning*, an ML training-order technique
  "grad*"       -> *gradient*
  "exam*"       -> *example*
  "study"       -> a research study
  "academic"    -> an academic paper
  "course"      -> *coarse*  (and "of course")

A university AI lab is the worst possible population for these collisions, which is
why the defect appears here and not in a vendor sweep.
"""
import re

# TIER A - terms with no machine-learning sense. A hit here is education or an edge case.
TIER_A = re.compile(r"""(
  educat | tutor(?!ial\s+on\s+(deep|machine)) | pedagog | classroom | syllab
| moodle | open\s?edx | \bedx\b | \blms\b | canvas-?lms | blackboard | sakai | moocs?
| gradebook | auto-?grad(er|ing)\b | \bgrading\b | rubric | homework | coursework
| schoolteacher | \bteacher | teaching\s+(assistant|material|operating|os)
|学生 | 教育 | 教学 | 课程 | 作业 | 教师
| student-?(facing|centred|centered) | k-?12 | kindergarten
| examination\s+(board|paper|system) | \bquiz | flashcard | spaced\s+repetition
| intelligent\s+tutoring | knowledge\s+tracing | learner\s+model
| school\s+management | student\s+information\s+system | \bsis\b
)""", re.I | re.X)

# ML collocations that POISON the ambiguous terms. Checked before TIER B is believed.
ML_NOISE = re.compile(r"""(
  (machine|deep|reinforcement|transfer|federated|representation|contrastive|metric
   |active|curriculum|in-?context|few-?shot|zero-?shot|one-?shot|multi-?task|meta
   |self-?supervised|un?supervised|semi-?supervised|continual|incremental|imitation
   |ensemble|manifold|dictionary|kernel|adversarial|multimodal|preference|residual
   |statistical|bayesian|online|offline|distributed|graph|structured|dense|sparse
   |prompt|instruction|policy|reward|latent|visual|federated|transferable
   |similarity|quasi-?dense|contextual|lifelong|multi-?agent|robot)
  [\s-]+learning
| learning\s+(rate|curve|to\s+(act|drive|hash|rank|optimi[sz]e|generate|reason|navigate|play))
| gradient | \bexample | coarse | state-?of-?the-?art
)""", re.I | re.X)

# TIER B - ambiguous terms, believed ONLY when ML_NOISE is absent.
TIER_B = re.compile(r"\b(course|learning|student|school|exam|academic|study|curriculum|lecture)", re.I)


def tier(name, desc):
    """Return 'A', 'B' or None. 'A' is publishable as an education candidate;
    'B' needs a human read; None is not an education repo."""
    text = (name or "") + " " + (desc or "")
    if TIER_A.search(text):
        return "A"
    if TIER_B.search(text) and not ML_NOISE.search(text):
        return "B"
    return None
