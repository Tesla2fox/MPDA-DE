# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:47:56 2019
@author: robot
"""
# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
#import sys
#sys.path.append('../')
# End of fix


import NiaPy
# import MyNiaPy


print(NiaPy.__all__)
print(MyNiaPy.__all__)
# import numpy
#
#
#
# print(numpy.__all__)
# #numpy.wtf
#
# #import NiaPy
# #
# #

from NiaPy.algorithms.basic import  DifferentialEvolution
from MyNiaPy.algorithms.basic import DifferentialEvolution
from MyNiaPy.task.task import StoppingTask, OptimizationType
from MyNiaPy.benchmarks import Sphere
#
# we will run Differential Evolution for 5 independent runs
for i in range(5):
    task = StoppingTask(D=10, nFES=5000, optType=OptimizationType.MINIMIZATION, benchmark=Sphere())
    algo = DifferentialEvolution(NP=50, F=0.5, CR=0.9)
    best = algo.run(task=task)
    print('%s -> %s' % (best[0].x, best[1]))


