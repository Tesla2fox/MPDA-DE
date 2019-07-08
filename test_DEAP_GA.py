#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.


#    example which maximizes the sum of a list of integers
#    each of which can be 0 or 1

import random
import time
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, typecode='i', fitness=creator.FitnessMin)

toolbox = base.Toolbox()

from MPDA_decode.instance import Instance
from MPDA_decode.MPDA_decode_discrete import MPDA_Decode_Discrete_NB,MPDA_Decode_Discrete_Base,MPDA_Decode_Discrete_RC
insName = '14_14_ECCENTRIC_RANDOMCLUSTERED_SVLCV_LVLCV_thre0.1MPDAins.dat'
# insName = '11_8_RANDOMCLUSTERED_CENTRAL_SVSCV_LVSCV_thre0.1MPDAins.dat'
# insName = '20_20_CLUSTERED_RANDOM_QUADRANT_LVSCV_thre0.1MPDAins.dat'
insName = '29_29_CLUSTERED_ECCENTRIC_LVLCV_SVSCV_thre0.1MPDAins.dat'
ins = Instance('.\\benchmark\\' + insName)

IND_ROBNUM  = ins.robNum
IND_TASKNUM = ins.taskNum
MPDA_Decode_Discrete_Base._ins = ins
MPDA_Decode_Discrete_NB._ins = ins
MPDA_Decode_Discrete_RC._ins = ins
print(ins)


def mpda_init_encode(robNum,taskNum):
    lstRes = []
    for robID in range(robNum):
        permLst = [x for x in range(taskNum)]
        random.shuffle(permLst)
        lstRes.extend(permLst)
    return lstRes


import numpy as np

def mpda_eval_discrete_nb(individual):
    encode =  np.zeros((ins.robNum, ins.taskNum), dtype=int)
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
    encode =  np.zeros((ins.robNum, ins.taskNum), dtype=int)
    i = 0
    for robID in range(IND_ROBNUM):
        for taskID in range(IND_TASKNUM):
            encode[robID][taskID] = individual[i]
            i += 1
    mpda_decode_rc = MPDA_Decode_Discrete_RC()
    # print(encode)
    ms = mpda_decode_rc.decode(encode)
    return ms,



def mpda_mate(ind1,ind2):
    for i  in  range(0,len(ind1),IND_TASKNUM):
        cxInd1 = ind1[i:i+IND_TASKNUM]
        cxInd2 = ind2[i:i+IND_TASKNUM]
        # print(cxInd1)
        # print(cxInd2)
        mpda_cxPartialyMatched(cxInd1,cxInd2)

        # print('change cxInd1 = ',cxInd1)
        # print('change cxInd2 = ',cxInd2)
        ind1[i:i + IND_TASKNUM] = cxInd1
        ind2[i:i + IND_TASKNUM] = cxInd2
        # print(ind1)
        # print(ind2)

    return ind1,ind2

def mpda_cxPartialyMatched(ind1, ind2):
    """Executes a partially matched crossover (PMX) on the input individuals.
    The two individuals are modified in place. This crossover expects
    :term:`sequence` individuals of indices, the result for any other type of
    individuals is unpredictable.

    :param ind1: The first individual participating in the crossover.
    :param ind2: The second individual participating in the crossover.
    :returns: A tuple of two individuals.

    Moreover, this crossover generates two children by matching
    pairs of values in a certain range of the two parents and swapping the values
    of those indexes. For more details see [Goldberg1985]_.

    This function uses the :func:`~random.randint` function from the python base
    :mod:`random` module.

    .. [Goldberg1985] Goldberg and Lingel, "Alleles, loci, and the traveling
       salesman problem", 1985.
    """
    size = min(len(ind1), len(ind2))
    p1, p2 = [0] * size, [0] * size

    # Initialize the position of each indices in the individuals
    for i in range(size):
        p1[ind1[i]] = i
        p2[ind2[i]] = i
    # Choose crossover points
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:  # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    # Apply crossover between cx points
    for i in range(cxpoint1, cxpoint2):
        # Keep track of the selected values
        temp1 = ind1[i]
        temp2 = ind2[i]
        # Swap the matched value
        ind1[i], ind1[p1[temp2]] = temp2, temp1
        ind2[i], ind2[p2[temp1]] = temp1, temp2
        # Position bookkeeping
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

    return ind1, ind2

def mpda_mutate(individual, indpb):

    size = len(individual)
    for robID in range(IND_ROBNUM):
        for i in range(IND_TASKNUM):
            if random.random() < indpb:
                swap_indx = random.randint(0, IND_TASKNUM - 2)
                if swap_indx >= i:
                    swap_indx += 1
                individual[i + robID * IND_TASKNUM], individual[swap_indx + robID * IND_TASKNUM] = \
                    individual[swap_indx+ robID * IND_TASKNUM], individual[i+ robID * IND_TASKNUM]

    return individual,




toolbox.register("mpda_attr",mpda_init_encode,IND_ROBNUM,IND_TASKNUM)
toolbox.register("individual", tools.initIterate, creator.Individual,
                 toolbox.mpda_attr)

# define the population to be a list of individuals
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


# ----------
# Operator registration
# ----------
# register the goal / fitness function
toolbox.register("evaluate",mpda_eval_discrete_nb)

# register the crossover operator
toolbox.register("mate",mpda_mate)


# register a mutation operator with a probability to
# flip each attribute/gene of 0.05
toolbox.register("mutate", mpda_mutate, indpb=0.01)
# tools.mutShuffleIndexes
# tools.mutShuffleIndexes()

# operator for selecting individuals for breeding the next
# generation: each individual of the current generation
# is replaced by the 'fittest' (best) of three individuals
# drawn randomly from the current generation.
# tools.selAutomaticEpsilonLexicase(), tournsize=3
toolbox.register("select", tools.selAutomaticEpsilonLexicase)

# tools.s

# ----------

f_data = open('.//debugData//GA_'+insName,'w')


def main():
    random.seed(64)

    # create an initial population of 300 individuals (where
    # each individual is a list of integers)
    start = time.clock()

    pop = toolbox.population(n=300)

    # CXPB  is the probability with which two individuals
    #       are crossed
    #
    # MUTPB is the probability for mutating an individual
    CXPB, MUTPB = 0.5, 0.2

    print("Start of evolution")

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print("  Evaluated %i individuals" % len(pop))

    # Extracting all the fitnesses of
    fits = [ind.fitness.values[0] for ind in pop]

    # Variable keeping track of the number of generations
    g = 0


    # Begin the evolution
    while g < 600:
        # A new generation
        g = g + 1
        print("-- Generation %i --" % g)

        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):

            # cross two individuals with probability CXPB
            if random.random() < CXPB:
                toolbox.mate(child1, child2)

                # fitness values of the children
                # must be recalculated later
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:

            # mutate an individual with probability MUTPB
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        print("  Evaluated %i individuals" % len(invalid_ind))

        # The population is entirely replaced by the offspring
        pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean ** 2) ** 0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
        f_data.write(str(g)+' '+ str(min(fits))+ ' ' + str(max(fits)) + '\n')
        f_data.flush()
    print("-- End of (successful) evolution --")
    end = time.clock()
    f_data.write('time ='+str(end-start) + '\n')
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))
    f_data.close()
# print(toolbox.select)


if __name__ == "__main__":
    # random.seed(1)
    # a = mpda_init_encode(3,4)
    # b = mpda_init_encode(3,4)
    # print('a = ',a)
    # print('b = ',b)
    #
    #
    # x,y = mpda_mate(a,b)
    # print('a = ',a)
    # print('b = ',b)
    #
    # print('x = ',x)
    # print('y = ',y)
    # a = random.sample(range(10),10)
    # b = random.sample(range(10),10)
    # print(mpda_cxPartialyMatched(a,b))
    main()
    # tools.initIterate()
    #  = [3,3,4]
    # tools.initCycle(list,toolbox.indices,3)