
# import MPDA_decode.instance
from MPDA_decode.instance import Instance
import os,sys
from scipy.optimize import differential_evolution
import  numpy as np
from MPDA_decode.robot import RobotDe,RobotState
from MPDA_decode.task import Task




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

    def decode(self,encode):
        self._encode = encode
        self._initState()
        try:
            self.decodeProcessor()
        except:
            print("some Error")
            return sys.float_info.max
        else:
            makespan = self._calMakespan()
            return makespan
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
            rob.onRoadPeriodRatio = self._encode[2*i]
            rob.onTaskPeriodRatio = self._encode[2*i+1]
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
    def decodeProcessor(self):
        self._allocateLst = []
        for robID in  range(self.robNum):
            for taskID in range(self.taskNum):
                if self._cmpltLst[taskID] == True:
                    continue
                if (robID,taskID) not in self._allocateLst:
                    onRoadPeriod = self._calRob2TaskOnRoadPeriod(robID,taskID)
                    if self._robotLst[robID].leaveTime + onRoadPeriod > self._taskLst[taskID].cmpltTime:
                        '''
                        preArriveTime > task.cmpltTime 
                        continue
                        this part still need process
                        '''
                        continue
                    preOnRoadPeriodLst.







        pass

    @staticmethod
    def
    @classmethod
    def sortOrder(self):
        for robID in range(self.robNum):


    def




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




