# -*- coding: utf-8 -*-

import config
import os

class Problem():
    'Container of problem data'
    def __init__(self, data):
        self.data = data
        #raise NotImplementedError
 
    @classmethod
    def load(cls, filename): 
        'create a problem using existing file'
        path = os.path.join(config.PROBLEMS, filename)
        with open(path, 'r') as fin:
            pass
        
    def dump(self, filename):
        path = os.path.join(config.PROBLEMS, filename)
        with open(filename, 'w') as fout:
            pass
    
    def solve(self, *args):
        pass
    
    def __call__(self, filename, *args):
        'solve and dump to file'
        self.solve(*args).dump(filename)
    
    
class Solution():
    'Cntainer of solution to problem'
    def __init__(self, problem):
        self.problem = problem
    
    @classmethod
    def load(cls, filename):
        'create a solution using existing file'
        path = os.path.join(config.SOLUTIONS, filename)
        with open(path, 'r') as fin:
            pass    
        
    def dump(self, filename):
        path = os.path.join(config.PROBLEMS, filename)
        with open(path, 'w') as fout:
            pass
    
    def verify(self):
        'Verify wheter this solution is legitimate'
        pass

    def score(self):
        'Compute the score of this solution'
        pass
     
    def improve(self, *args):
        'return a better solution and optionally a modified problem'
        pass
        
        