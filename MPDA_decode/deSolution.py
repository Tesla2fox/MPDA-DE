

import  sys
from  enum import Enum

class EventType(Enum):
    arrive = 1
    leave = 2

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
    def seq(self,_o_seq):
        if type(_o_seq) != type([]):
            raise TypeError('tuple must be LIST')
        else:
            self._seq = _o_seq
    @seq.deleter
    def seq(self):
        del self._seq
    def __eq__(self, other):
        return other._seq == self._seq

    def append(self,action_tuple):
        if type(action_tuple) != ActionTuple:
            raise TypeError('tuple must be ActionTuple')
        else:
            self._seq.append(action_tuple)

    def __getitem__(self, item):
        return self._seq[item]

    def __setitem__(self, key, value):
        self._seq[key] = value

    def __str__(self):
        res_str = str()
        for x in self._seq:
            res_str = res_str + str(x) +'\n'
        return res_str


if __name__ == '__main__':
    wtf = ActionTuple(1,2,EventType['arrive'],100)
    wtf2 = ActionTuple(1,2,EventType['arrive'],102)
    seq1 = ActionSeq()
    seq1.append(wtf)
    seq1.append(wtf2)

    seq2 = ActionSeq()
    seq2.append(wtf2)
    seq2.append(wtf)

    seq2[0] = wtf
    seq2[1] = wtf2

    print(seq1)

    if seq1 == seq2:
        print("相等")
    else:
        print("不相等")

    SolutionDe._taskNum = 2
    SolutionDe._robNum = 4
    sol_1  = SolutionDe()
    print(len(sol_1.chrom))
    SolutionDe._robNum = 5
    so_2 = SolutionDe()
    print(len(so_2.chrom))



