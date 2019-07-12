
from enum import Enum

from MPDA_decode.MPDA_decode_discrete import MPDA_Decode_Discrete_NB, MPDA_Decode_Discrete_Base, MPDA_Decode_Discrete_RC
from MPDA_decode.instance import Instance


import OptimizerGA.mpdaMutate as _mutate
import OptimizerGA.mpdaCrossover as _crossover
import OptimizerGA.mpdaGAEval as _eval
import OptimizerGA.mpdaGAInit as _init

from deap import base
from deap import creator
from deap import tools




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


        _mutate.IND_ROBNUM = self._robNum
        _mutate.IND_TASKNUM = self._taskNum

        _crossover.IND_ROBNUM = self._robNum
        _crossover.IND_TASKNUM = self._taskNum

        _eval.IND_ROBNUM = self._robNum
        _eval.IND_TASKNUM = self._taskNum

        '''
        deap init
        '''
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, typecode='i', fitness=creator.FitnessMin)



        toolbox = base.Toolbox()
        toolbox.register("mpda_attr", _init.mpda_init_encode, self._robNum, self._taskNum)
        toolbox.register("individual", tools.initIterate, creator.Individual,
                         toolbox.mpda_attr)

        # define the population to be a list of individuals
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        # ----------
        # Operator registration
        # ----------
        # register the goal / fitness function
        if decoder_type == DecoderType.no_back:
            toolbox.register("evaluate", _eval.mpda_eval_discrete_nb)
        elif decoder_type == DecoderType.back:
            toolbox.register("evaluate", _eval.mpda_eval_discrete_rc)

        # register the crossover operator
        toolbox.register("mate", _crossover.mpda_mate)

        # register a mutation operator with a probability to
        # flip each attribute/gene of 0.05
        toolbox.register("mutate", _mutate.mpda_mutate, indpb=0.01)
        # tools.mutShuffleIndexes
        # tools.mutShuffleIndexes()
        # operator for selecting individuals for breeding the next
        # generation: each individual of the current generation
        # is replaced by the 'fittest' (best) of three individuals
        # drawn randomly from the current generation.
        # tools.selAutomaticEpsilonLexicase(), tournsize=3
        toolbox.register("select", tools.selAutomaticEpsilonLexicase)

        pass
    def run(self):

        pass


    def __str__(self):
        return 'mpda_ga_opt'

if __name__ == '__main__':


    print('main')





