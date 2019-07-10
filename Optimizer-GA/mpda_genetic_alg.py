
from  enum import Enum
from MPDA_decode.instance import Instance
from MPDA_decode.MPDA_decode_discrete import MPDA_Decode_Discrete_NB,MPDA_Decode_Discrete_Base,MPDA_Decode_Discrete_RC


class DecoderType(Enum):
    no_back = 1
    back = 2


class MPDA_Genetic_Alg(object):
    def __init__(self,ins_name,decoder_type):
        ins = Instance(ins_name)
        self._robNum = ins.robNum
        self._taskNum = ins.taskNum
        MPDA_Decode_Discrete_Base._ins = ins
        MPDA_Decode_Discrete_NB._ins = ins
        MPDA_Decode_Discrete_RC._ins = ins
        print(ins)
        pass
    def run(self):
        pass






