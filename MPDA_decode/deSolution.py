

import  sys

class SolutionDe(object):
    _taskNum = 0
    _robNum = 0
    def __init__(self):
        self.chrom = [0] * SolutionDe._robNum

from collections import namedtuple


ActionTuple = namedtuple('ActionTuple',['robID','taskID','eventType','eventTime'])

class ActionSeq(object):
    def __init__(self):
        self._seq = []
    @property
    def seq(self):
        return self._seq
    @seq.setter
    def seq(self,action_tuple):
        if type(action_tuple) != ActionTuple:
            raise TypeError('tuple must be ActionTuple')
        else:
            self._seq.append(action_tuple)
    @seq.deleter
    def seq(self):
        del self._seq




if __name__ == '__main__':
    wtf = ActionTuple()




    SolutionDe._taskNum = 2
    SolutionDe._robNum = 4
    sol_1  = SolutionDe()
    print(len(sol_1.chrom))
    SolutionDe._robNum = 5
    so_2 = SolutionDe()
    print(len(so_2.chrom))



