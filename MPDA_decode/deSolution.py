

import  sys

class SolutionDe(object):
    _taskNum = 0
    _robNum = 0
    def __init__(self):
        self.chrom = [0] * SolutionDe._robNum




if __name__ == '__main__':
    SolutionDe._taskNum = 2
    SolutionDe._robNum = 4
    sol_1  = SolutionDe()
    print(len(sol_1.chrom))
    SolutionDe._robNum = 5
    so_2 = SolutionDe()
    print(len(so_2.chrom))



