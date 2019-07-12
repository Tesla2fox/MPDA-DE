import numpy as np

from MPDA_decode.MPDA_decode_discrete import MPDA_Decode_Discrete_NB,MPDA_Decode_Discrete_RC

IND_ROBNUM = 0
IND_TASKNUM = 0



def mpda_eval_discrete_nb(individual):
    encode =  np.zeros((IND_ROBNUM, IND_TASKNUM), dtype=int)
    i = 0
    for robID in range(IND_ROBNUM):
        for taskID in range(IND_TASKNUM):
            encode[robID][taskID] = individual[i]
            i += 1
    mpda_decode_nb = MPDA_Decode_Discrete_NB()
    # print(encode)
    ms = mpda_decode_nb.decode(encode)
    return ms,

def mpda_eval_discrete_rc(individual):
    encode =  np.zeros((IND_ROBNUM, IND_TASKNUM), dtype=int)
    i = 0
    for robID in range(IND_ROBNUM):
        for taskID in range(IND_TASKNUM):
            encode[robID][taskID] = individual[i]
            i += 1
    mpda_decode_rc = MPDA_Decode_Discrete_RC()
    # print(encode)
    ms = mpda_decode_rc.decode(encode)
    return ms,