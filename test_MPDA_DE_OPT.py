import MPDA_decode as md
import os,sys
import numpy as np
import  random
from scipy.optimize import differential_evolution




def mpda_decode(x,*args):
    arg1 = -0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2))
    arg2 = 0.5 * (np.cos(2. * np.pi * x[0]) + np.cos(2. * np.pi * x[1]))
#    print(x)
#    print('ssss = ',*args)
    return random.random()




if __name__ == '__main__':
    insName = '14_14_ECCENTRIC_RANDOMCLUSTERED_SVLCV_LVLCV_thre0.1MPDAins.dat'
    ins = md.Instance('.\\benchmark\\' + insName)
    # md.Instance()

    bounds = [(0,2)] * ins.robNum *3
    print(bounds)
    # decode = MPDA_DE_decode()
    md.MPDA_DE_decode._ins = ins
    # MPDA_DE_decode


    result = differential_evolution(mpda_decode, bounds, args = ins, disp = True)



