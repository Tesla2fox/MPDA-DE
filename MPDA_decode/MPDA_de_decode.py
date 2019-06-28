
# import MPDA_decode.instance
from MPDA_decode.instance import Instance
import os,sys
from scipy.optimize import differential_evolution
import  numpy as np
from MPDA_decode.robot import RobotDe,RobotState
from MPDA_decode.task import Task
import logging
import  random as rd
from collections import  namedtuple
import  random


RobTaskPair = namedtuple('TaskRobPair',['robID','taskID'])


'''
random
'''
random.seed(1)

class MPDA_DE_decode(object):
    _ins = object
    def __init__(self):
        if type(MPDA_DE_decode._ins) != Instance:
            raise TypeError("MPDA_DE_decode._ins must be the Instance class")

        '''
        some paras are const during calculation process
        '''
        self.robNum = MPDA_DE_decode._ins.robNum
        self.taskNum = MPDA_DE_decode._ins.taskNum
        self.threhold = MPDA_DE_decode._ins.threhold
        self.robAbiLst = MPDA_DE_decode._ins.robAbiLst
        self.robVelLst = MPDA_DE_decode._ins.robVelLst
        self.taskStateLst = MPDA_DE_decode._ins.taskStateLst
        self.taskRateLst = MPDA_DE_decode._ins.taskRateLst
        self.rob2taskDisMat = MPDA_DE_decode._ins.rob2taskDisMat
        self.taskDisMat = MPDA_DE_decode._ins.taskDisMat

        self._encode = []

        '''
        some paras are changed during calculation process
        '''
        self._taskLst = []
        self._robotLst = []
        self._cmpltLst = []
        logging.basicConfig(level=logging.DEBUG)
    def decode(self,encode):
        self._encode = encode
        self._initState()
        try:
            self.decodeProcessor()
        except Exception as e:
            logging.error(e)
            print("some Error")
            return sys.float_info.max
        else:
            makespan = self._calMakespan()
            return makespan
    def decodeProcessor(self):
        self._allocateLst = []
        # raise Exception("???")
        while not self._calEndCondition():


            pairCandidate = self._selectRobTaskPair()
            self._updateSol(pairCandidate)
            break
            pass



        # for robID in  range(self.robNum):
        #     for taskID in range(self.taskNum):
        #         if self._cmpltLst[taskID] == True:
        #             continue
        #         if (robID,taskID) not in self._allocateLst:
        #             onRoadPeriod = self._calRob2TaskOnRoadPeriod(robID,taskID)
        #             if self._robotLst[robID].leaveTime + onRoadPeriod > self._taskLst[taskID].cmpltTime:
        #                 '''
        #                 preArriveTime > task.cmpltTime
        #                 continue
        #                 this part still need process
        #                 '''
        #                 continue
        #             # preOnRoadPeriodLst.


    def _updateSol(self,rob_task_pair):

        pass
    def _selectRobTaskPair(self):
        #  pre means predict
        #
        #
        #
        #

        preOnRoadPeriodLst = []
        preOnTaskPeriodLst = []
        for robID in range(self.robNum):
            for taskID in range(self.taskNum):
                if self._cmpltLst[taskID]:
                    continue
                # if RobTaskPair(robID,taskID) not in self._cmpltLst:
                rob = self._robotLst[robID]
                task = self._taskLst[taskID]
                rob_task_pair = RobTaskPair(robID,taskID)
                onRoadPeriod = self._calRob2TaskOnRoadPeriod(robID, taskID)
                if onRoadPeriod + rob.leaveTime < self._decodeTime:
                    continue
                onTaskPeriod = self._calRobOnTaskPeriod(robID, taskID)

                preOnRoadPeriodLst.append((rob_task_pair, onRoadPeriod))
                preOnTaskPeriodLst.append((rob_task_pair, onTaskPeriod))

        onRoadPeriodDic = self._sortLst(preOnRoadPeriodLst, reverseBoolean=False)
        onTaskPeriodDic = self._sortLst(preOnTaskPeriodLst, reverseBoolean=False)

        logging.debug(onRoadPeriodDic)
        logging.debug(onTaskPeriodDic)

        return RobTaskPair(robID=-1,taskID= -1)


    def _initState(self):
        self._taskLst.clear()
        self._robotLst.clear()
        self._cmpltLst.clear()
        self._cmpltLst = [False] * self.taskNum
        for i in range(self.robNum):
            rob = RobotDe()
            rob.ability = self.robAbiLst[i]
            rob.vel = self.robVelLst[i]
            rob.encodeIndex = 0
            rob.stopBool = False
            rob.stateType = RobotState['onRoad']
            rob.leaveTime = 0
            rob.onRoadPeriodRatio = self._encode[3*i]
            rob.onTaskPeriodRatio = self._encode[3*i + 1]
            rob.makespanRatio = self._encode[3*i + 2]

            self._robotLst.append(rob)

        for i in range(self.taskNum):
            task = Task()
            task.cState = self.taskStateLst[i]
            task.initState = self.taskStateLst[i]
            task.cRate = self.taskRateLst[i]
            task.initRate = self.taskRateLst[i]
            task.threhod = self.threhold
            task.cmpltTime = sys.float_info.max
            self._taskLst.append(task)
        self._decodeTime = 0
        logging.debug("init success")


    def _calEndCondition(self):
        for rob in self._robotLst:
            if rob.stopBool == False:
                return False
        return  True
        pass
    def _calMakespan(self):
        # makespan for the MPDA problem
        leaveTimeLst = [rob.leaveTime for rob in self._robotLst]
        makespan = max(leaveTimeLst)
        return makespan

    def _calRob2TaskOnRoadPeriod(self,robID,taskID):
        rob = self._robotLst[robID]
        if rob.encodeIndex == 0:
            dis = self.rob2taskDisMat[robID][taskID]
            dur = dis/self.robVelLst[robID]
        else:
            currentTaskID = rob.taskID
            dis = self.taskDisMat[currentTaskID][taskID]
            dur = dis/self.robVelLst[robID]
        return dur
    def _calRobOnTaskPeriod(self,robID,taskID):
        rob = self._robotLst[robID]
        task = self._taskLst[taskID]
        return random.random()

    def _calCurrentMakespan(self,robID,taskID):
        rob = self._robotLst[robID]
        task = self._taskLst[taskID]
        return random.random()

    def _calRobTaskEventTime(self,robID,taskID):
        rob = self._robotLst[robID]
        task = self._taskLst[taskID]
        self._calRob2TaskOnRoadPeriod(robID,taskID)
        pass



    def _sortLst(self,lst = [],keyFunc =  lambda x : x[1], reverseBoolean = False):
        lst = sorted(lst,key=keyFunc,reverse=reverseBoolean)
        val = sys.float_info.min
        # orderInd = -1
        orderInd :int
        dic = dict()
        # index: int
        for index, unit in enumerate(lst):
            if val == unit[1]:
                dic[unit[0]] = orderInd
            else:
                val = unit[1]
                orderInd = index
                dic[unit[0]] = orderInd
        return dic


if __name__ == '__main__':
    AbsolutePath = os.path.abspath(__file__)
    # 将相对路径转换成绝对路径
    SuperiorCatalogue = os.path.dirname(AbsolutePath)
    # 相对路径的上级路径
    BaseDir = os.path.dirname(SuperiorCatalogue)
    insName = '14_14_ECCENTRIC_RANDOMCLUSTERED_SVLCV_LVLCV_thre0.1MPDAins.dat'
    ins = Instance(BaseDir + '\\benchmark\\' + insName)
    MPDA_DE_decode._ins = ins

    mpda_de_decode = MPDA_DE_decode()

    encode = [rd.random() for x in range(ins.robNum * 3)]

    # print(encode)
    logging.info("encode = " + str(encode))
    mpda_de_decode.decode(encode)


    # result = differential_evolution(ackley, bounds, callback = callbackF,args = (3,3), disp = True)




