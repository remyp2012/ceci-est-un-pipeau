# -*- coding: utf-8 -*-
"""
Numpy patch for pypy.

Usage:

from numpy_patch import numpy
"""

import numpy
import config

def pypy_patch():
    'do some numpy patch for pypy'
    def unravel_index(ind, (a,b)):
        'ad-hoc unravel_index, works only for 1 index, 2 dims and row-major.'
        r = ind / b
        c = ind % b
        return r, c
        
    numpy.unravel_index = unravel_index
    


interpreter = config.INTERPRETER

if interpreter == 'python':
    pass
elif interpreter == 'pypy':
    pypy_patch()
    