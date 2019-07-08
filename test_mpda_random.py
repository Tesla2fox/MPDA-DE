from MPDA_decode.instance import Instance
from MPDA_decode.MPDA_decode_discrete import MPDA_Decode_Discrete_NB,MPDA_Decode_Discrete_Base,MPDA_Decode_Discrete_RC
import numpy as np
import random
import copy
import sys

insNameLst = ['14_14_ECCENTRIC_RANDOMCLUSTERED_SVLCV_LVLCV_thre0.1MPDAins.dat',
              '11_8_RANDOMCLUSTERED_CENTRAL_SVSCV_LVSCV_thre0.1MPDAins.dat',
              '20_20_CLUSTERED_RANDOM_QUADRANT_LVSCV_thre0.1MPDAins.dat']

insName = insNameLst[2]


# for insName in insNameLst:
ins = Instance('.\\benchmark\\' + insName)
IND_ROBNUM  = ins.robNum
IND_TASKNUM = ins.taskNum
MPDA_Decode_Discrete_Base._ins = ins
MPDA_Decode_Discrete_NB._ins = ins
MPDA_Decode_Discrete_RC._ins = ins

# print(mpda_dis_decode)
mpda_decode_base = MPDA_Decode_Discrete_Base()
encode = np.zeros((ins.robNum, ins.taskNum), dtype=int)
# random.seed(3)
NFE = 20000

# makespan1Lst = []
# makespan2Lst = []
min_makespan1 = sys.float_info.max
min_makespan2 = sys.float_info.max

f_data = open('.//debugData//RD_'+insName,'w')
for NFE_i in range(NFE):
    for i in range(ins.robNum):
        permLst = [x for x in range(ins.taskNum)]
        random.shuffle(permLst)
        encode[i][:] = permLst
    # print('encode =  ',encode)
    print('NFE_i = ',NFE_i)
    mpda_dis_decode_nb = MPDA_Decode_Discrete_NB()
    encode1 = copy.deepcopy(encode)
    makespan1 = mpda_dis_decode_nb.decode(encode1)
    if makespan1 < min_makespan1:
        min_makespan1  = makespan1
        f_data.write('min_makespan1 = ' + str(min_makespan1) + '\n')
    # makespan1Lst.append(makespan1)
    # print("makespan1 = ",makespan1)
    # print('encode1 =  ',encode1)

    mpda_dis_decode_rc = MPDA_Decode_Discrete_RC()
    encode2 = copy.deepcopy(encode)
    makespan2 = mpda_dis_decode_rc.decode(encode2)
    if makespan2 < min_makespan2:
        min_makespan2  = makespan2
        f_data.write('min_makespan2 = ' + str(min_makespan2) + '\n')

    # print("makespan2 = ",makespan2)
    # makespan2Lst.append(makespan2)
    # print('encode2 =  ',encode2)
    # f_data.write(str(NFE_i) + ' ' +str(makespan1) + ' ' +str(makespan2) + '\n')
    f_data.flush()
f_data.write('last_min_makespan1 = ' + str(min_makespan1) + '\n')
f_data.write('last_min_makespan2 = ' + str(min_makespan2) + '\n')
# f_data.write('min '+'')
f_data.close()


