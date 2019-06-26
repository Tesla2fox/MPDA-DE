
# import MPDA_decode.instance
from MPDA_decode.instance import Instance
import os,sys

from scipy.optimize import differential_evolution




class MPDA_DE_decode(object):
    _ins = object
    def __init__(self):
        self._robNum = MPDA_DE_decode._ins.robNum

        pass


if __name__ == '__main__':
    AbsolutePath = os.path.abspath(__file__)
    # 将相对路径转换成绝对路径
    SuperiorCatalogue = os.path.dirname(AbsolutePath)
    # 相对路径的上级路径
    BaseDir = os.path.dirname(SuperiorCatalogue)
    insName = '14_14_ECCENTRIC_RANDOMCLUSTERED_SVLCV_LVLCV_thre0.1MPDAins.dat'
    ins = Instance(BaseDir + '\\benchmark\\' + insName)
    MPDA_DE_decode._ins = ins

    result = differential_evolution(ackley, bounds, callback = callbackF,args = (3,3), disp = True)




