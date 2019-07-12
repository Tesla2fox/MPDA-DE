import random

def mpda_init_encode(robNum,taskNum):
    lstRes = []
    for robID in range(robNum):
        permLst = [x for x in range(taskNum)]
        random.shuffle(permLst)
        lstRes.extend(permLst)
    return lstRes

