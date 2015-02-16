# -*- coding: utf-8 -*-

# global variables
import os
import sys

ROOT = os.path.dirname(os.path.realpath(__file__))

PROBLEMS = os.path.join(ROOT, 'problems')

SOLUTIONS = os.path.join(ROOT, 'solutions')

# python or pypy?
INTERPRETER = os.path.basename(sys.executable)