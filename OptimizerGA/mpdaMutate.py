import  random

IND_ROBNUM = 0
IND_TASKNUM = 0


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