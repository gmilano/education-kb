"""POSITIVE control for `T271`: a test that imports the module beside it.
Under `python3 -I` this raises ModuleNotFoundError and classifies as `crash`.
Under plain `python3` it exits 0. The suite asserts BOTH, which is the only way
to show the sweep is measuring the flag and not the suite."""
import sibling_module  # noqa: F401

print("imported the sibling")
