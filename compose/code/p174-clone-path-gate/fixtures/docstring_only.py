#!/usr/bin/env python3
"""FIXTURE (p174). NEGATIVE CONTROL.

Path is a parameter: p120's score.py hardcoded /home/user/education-kb, which
made it unrunnable from any other clone.
"""
import pathlib
KB = pathlib.Path(__file__).resolve().parents[3]
