# -*- coding: utf-8 -*-

import config
import os
import pickle

class Problem():
    'Container of problem data'
    def __init__(self, data):
        self.data = data
        #raise NotImplementedError
 
    @classmethod
    def read(cls, filename): 
        'create a problem with text problem file'
        path = os.path.join(config.PROBLEMS, filename)
        with open(path, 'r') as fin:
            # parse input
            pass
        
    def dump(self, filename):
        path = os.path.join(config.PROBLEMS, filename)
        with open(path, 'w') as fout:
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
        'load solution (probably incomplete) from pickle file'
        path = os.path.join(config.SOLUTIONS, filename)
        with open(path, 'r') as fin:
            return pickle.load(fin)
        
    def save(self, filename):
        'save to pickle file'
        path = os.path.join(config.SOLUTIONS, filename)
        with open(path, 'r') as fin:
            pickle.dump(self, fin)
    
    @classmethod
    def read(cls, filename):
        'read a text solution file'
        path = os.path.join(config.SOLUTIONS, filename)
        with open(path, 'r') as fin:
            # parse input
            pass
    
    def dump(self, filename):
        'dump text solution file for submission'
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
        
        