# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 10:12:55 2018
this is a base DECODE CLASS for the MPDA problem

@author: robot
"""
from MPDA_decode.instance import Instance
import os,sys
from scipy.optimize import differential_evolution
import  numpy as np
from MPDA_decode.robot import RobotState,Robot
from MPDA_decode.task import Task
import  random as rd
from collections import  namedtuple
import  random
import  copy
from MPDA_decode.action import ActionSeq,ActionTuple,EventType,RobTaskPair,TaskSeq,TaskStatusTuple,InvalidType
from enum import Enum


class InvalidStateException(Exception):
    '''
    Custom exception types about InvalidStateException
    '''
    def __init__(self):
        err = 'InvalidStateException'
        super(InvalidStateException, self).__init__(err)

class RobotStuckException(Exception):
    '''
    Custom exception types about RobotStuckException
    '''

    def __init__(self):
        err = 'RobotStuckException'
        super(RobotStuckException, self).__init__(err)

class CalType(Enum):
    arriveCond = 1
    leaveCond = 2
    endCond = 3
    backCond = 4
    stateInvalidCond = 5

AbsolutePath = os.path.abspath(__file__)
# 将相对路径转换成绝对路径
SuperiorCatalogue = os.path.dirname(AbsolutePath)
# 相对路径的上级路径
BaseDir = os.path.dirname(SuperiorCatalogue)


class MPDA_Decode_Discrete_Base(object):
    _ins = object
    def __init__(self):
        if type(self._ins) != Instance:
            raise TypeError("MPDA_Decode_Discrete_Base._ins must be the Instance class")
        '''
        some paras are const during calculation process
        '''
        self.robNum = MPDA_Decode_Discrete_Base._ins.robNum
        self.taskNum = MPDA_Decode_Discrete_Base._ins.taskNum
        self.threhold = MPDA_Decode_Discrete_Base._ins.threhold
        self.robAbiLst = MPDA_Decode_Discrete_Base._ins.robAbiLst
        self.robVelLst = MPDA_Decode_Discrete_Base._ins.robVelLst
        self.taskStateLst = MPDA_Decode_Discrete_Base._ins.taskStateLst
        self.taskRateLst = MPDA_Decode_Discrete_Base._ins.taskRateLst
        self.rob2taskDisMat = MPDA_Decode_Discrete_Base._ins.rob2taskDisMat
        self.taskDisMat = MPDA_Decode_Discrete_Base._ins.taskDisMat



        self.encode = np.zeros((self.robNum, self.taskNum), dtype=int)

        self.taskLst = []
        print("sdjksakdj")
        self.robotLst = []
        self.cmpltLst = []
        self.decodeTime = 0

        self.robInfoLst = []
        self.taskInfoLst = []
        self.decodeTimeLst = []

        # self._degBool = False
    '''
    generate a random encode 
    '''
    def generateRandEncode(self):
        for i in range(self.robNum):
            permLst = [x for x in range(self.taskNum)]
            random.shuffle(permLst)
            self.encode[i][:] = permLst

    def decode(self):
        '''
        ready to construct
        '''
        pass

    def initStates(self):
        '''
        initialize states of decode method
        '''
        print(self.taskDisMat)
        self.taskLst.clear()
        self.robotLst.clear()
        self.cmpltLst.clear()
        self.cmpltLst = [False] * self.taskNum
        for i in range(self.robNum):
            rob = Robot()
            rob.ability = self.robAbiLst[i]
            rob.vel = self.robVelLst[i]
            rob.encodeIndex = 0
            rob.taskID, rob.encodeIndex, stopBool = self.getRobTask(robID=i, encodeIndex=0)
            if not stopBool:
                dis = self.rob2taskDisMat[i][rob.taskID]
                dis_time = dis / rob.vel
                rob.arriveTime = dis_time
            rob.stopBool = stopBool
            rob.stateType = RobotState['onRoad']
            rob.leaveTime = 0
            self.robotLst.append(rob)

        for i in range(self.taskNum):
            task = Task()
            task.cState = self.taskStateLst[i]
            task.initState = self.taskStateLst[i]
            task.cRate = self.taskRateLst[i]
            task.initRate = self.taskRateLst[i]
            task.threhod = self.threhold
            task.cmpltTime = sys.float_info.max
            self.taskLst.append(task)

        self.decodeTime = 0
        self.validStateBool = True

    #    @profile
    def decodeProcessor(self):
        invalidFitness = False
        backBool = False
        validStateBool = True
        while not self.allTaskCmplt():
            cal_type, actionID = self.findActionID()
            if cal_type == CalType['arriveCond']:
                # =============================================================================
                # arrive event
                # =============================================================================

                rob = self.robotLst[actionID]
                arriveTime = rob.arriveTime
                encodeInd = rob.encodeIndex
                taskID = self.encode[actionID][encodeInd]
                if self.taskCmplt(taskID):
                    # =============================================================================
                    #  the task has been cmplt
                    # =============================================================================
                    self.arriveCmpltTask(actionID, encodeInd)
                else:
                    # =============================================================================
                    # the  task has not been cmplt
                    # =============================================================================
                    task = self.taskLst[taskID]
                    rob.taskID = taskID
                    validStateBool = task.calCurrentState(arriveTime)
                    if not validStateBool:
                        break
                    task.cRate = task.cRate - rob.ability
                    # can not be cmplted
                    if task.cRate >= 0:
                        leaveTime = sys.float_info.max
                    # can be completed
                    else:
                        rob.executeDur = task.calExecuteDur()
                        rob.executeBool = False
                        leaveTime = rob.arriveTime + rob.executeDur
                        coordLst = self.findCoordRobot(actionID)
                        for coordID in coordLst:
                            coordRob = self.robotLst[coordID]
                            coordRob.leaveTime = leaveTime
                            coordRob.executeDur = coordRob.leaveTime - coordRob.arriveTime
                    rob.leaveTime = leaveTime
                    rob.stateType = RobotState['onTask']
                    self.decodeTime = rob.arriveTime
            # =============================================================================
            #  begin the leave condition for
            # =============================================================================
            if cal_type == CalType['leaveCond']:
                rob = self.robotLst[actionID]
                #                print(actionID)
                taskID = rob.taskID
                #                try:
                #                    if  taskID < 0:
                #                        raise Exception('taskID < 0')
                #                except Exception as e:
                #                    print(e)
                #                print(taskID)
                task = self.taskLst[taskID]
                if self.cmpltLst[taskID] == True:
                    self.leaveCmpltTask(actionID)
                #                    print(self.cmpltLst)
                #                    validStateBool = True
                #                    while True:
                #                        print('bug',taskID)
                #                        return
                else:
                    validStateBool = task.calCurrentState(rob.leaveTime)
                    if not validStateBool:
                        break
                    if (task.isCmplt()):
                        self.cmpltLst[taskID] = True
                        try:
                            self.updateEncode(taskID)
                        except Exception as e:
                            print(e)
                        coordLst = self.findCoordRobot(actionID)
                        for coordID in coordLst:
                            self.updateRobLeaveCond(coordID)
                            self.robotLst[coordID].cmpltTaskLst.append(taskID)
                    self.updateRobLeaveCond(actionID)
                    self.robotLst[actionID].cmpltTaskLst.append(taskID)
                    self.robotLst[actionID].cmpltTaskID = taskID
                if self._degBool:
                    self.deg.write('taskID ' + str(taskID) + ' has been cmplt\n')
                    #                self.deg.write('leaveChanged\n')
                    self.saveRobotInfo()

                task.cmpltTime = rob.leaveTime
                self.decodeTime = rob.leaveTime
            #                print(taskID,' cmpltTime ', task.cmpltTime)
            if cal_type == CalType['endCond']:
                invalidFitness = True
                #                raise Exception('end-Condition-bug, robots have been stuck')
                raise RobotStuckException()
                break
            if cal_type == CalType['backCond']:
                backBool = True
                self.backRobID = actionID
                self.backTaskID = self.robotLst[actionID].taskID
                self.backArriveTime = self.robotLst[actionID].arriveTime
                self.backInfo = self.robotLst[actionID].variableInfo()
                break
            #
            #                    print(task.cRate)
            #                    print(task.cRate)
            # =============================================================================
            #  the state is too big  the decode process is wrong
            # =============================================================================
            if not validStateBool:
                break
        #            print('circleTime = ', circleTime)
        #            print('decodeTime = ', self.decodeTime)
        #            circleTime += 1
        #            if circleTime > 3000:
        #                break
        #            print(self.cmpltLst)

        if not validStateBool:
            cal_type = CalType['stateInvalidCond']
            self.validStateBool = False
            #            raise Exception('stateInvalidCond-bug, the state is too enormous')
            raise InvalidStateException()
        #        print(cal_type)
        return cal_type

    #            break

    def allTaskCmplt(self):
        if False in self.cmpltLst:
            return False
        else:
            return True

    def findActionID(self):
        cal_type = CalType['endCond']
        actionID = -1
        minTime = sys.float_info.max
        for i in range(self.robNum):
            rob = self.robotLst[i]
            if rob.stopBool != True:
                if rob.stateType == RobotState['onRoad']:
                    if rob.arriveTime < minTime:
                        minTime = rob.arriveTime
                        cal_type = CalType['arriveCond']
                        actionID = i
                if rob.stateType == RobotState['onTask']:
                    if rob.leaveTime < minTime:
                        minTime = rob.leaveTime
                        cal_type = CalType['leaveCond']
                        actionID = i

        self.saveEventInMemory()

        if minTime < self.decodeTime:
            cal_type = CalType['backCond']
        #            print(minTime)
        #            print(self.decodeTime)
        #            taskID = self.robotLst[actionI].taskID
        #        self.saveRobotInfo()
        return cal_type, actionID

    def findCoordRobot(self, robID):
        '''
        find robots which are corrdinated with the robot A
        '''
        coordLst = []
        rob = self.robotLst[robID]
        taskID = rob.taskID
        for i in range(self.robNum):
            if i == robID:
                continue
            #            crob = self.robotLst[i]
            if self.robotLst[i].stateType == RobotState['onRoad']:
                continue
            if self.robotLst[i].stopBool == True:
                continue
            if self.robotLst[i].taskID == taskID:
                coordLst.append(i)
        return coordLst

    def calRoadDur(self, taskID1, taskID2, robID):
        '''
        calculate the time fragment from the time when robID leaves the taskID1 to
        the time when rob arrives the taskID2
        '''
        dis = self.taskDisMat[taskID1][taskID2]
        rob = self.robotLst[robID]
        roadDur = dis / rob.vel
        return roadDur

    def updateEncode(self, cmpltTaskID):
        '''
        correct the encode,
        delete furture tasks which have been completed.
        '''
        for i in range(self.robNum):
            rob = self.robotLst[i]
            for j in range(rob.encodeIndex + 1, self.taskNum):
                if self.encode[i][j] == cmpltTaskID:
                    self.encode[i][j] = -1

    def updateRobLeaveCond(self, robID):
        '''
        update robot's state when the leave event has been triggered.
        '''
        rob = self.robotLst[robID]
        preTaskID = rob.taskID
        while True:
            if rob.encodeIndex == (self.taskNum - 1):
                rob.stopBool = True
                break
            rob.encodeIndex += 1
            taskID = self.encode[robID][rob.encodeIndex]
            if self.taskCmplt(taskID):
                continue
            else:
                roadDur = self.calRoadDur(preTaskID, taskID, robID)
                arriveTime = rob.leaveTime + rob.roadDur
                if arriveTime > self.taskLst[taskID].cmpltTime:
                    self.encode[robID][rob.encodeIndex] = -1
                    #                    print('optimal')
                    continue
                rob.roadDur = roadDur
                rob.taskID = taskID
                rob.arriveTime = rob.leaveTime + rob.roadDur
                rob.stateType = RobotState['onRoad']
                break

    def taskCmplt(self, taskID):
        '''
        taskID has been completed or not
        '''
        cmplt = False
        if taskID < 0:
            cmplt = True
        else:
            if self.cmpltLst[taskID]:
                cmplt = True
        return cmplt

    def getRobTask(self, robID=0, encodeIndex=0):
        '''
        get the robot next task ID
        '''
        stopBool = False
        while True:
            if encodeIndex == self.taskNum:
                stopBool = True
                break
            taskID = self.encode[robID][encodeIndex]
            if taskID < 0:
                encodeIndex += 1
                continue
            else:
                break
        return taskID, encodeIndex, stopBool

    def calMakespan(self):
        # makespan for the MPDA problem
        leaveTimeLst = [rob.leaveTime for rob in self.robotLst]
        makespan = max(leaveTimeLst)
        return makespan

    def saveEncode(self):
        '''
        save encode information into the deg2 files
        '''
        for i in range(self.robNum):
            lst = list(self.encode[i][:])
            rd.writeConf(self.deg2, str(i), lst)
        self.deg2.flush()

    def saveRobotInfo(self):
        '''
        save robot information into the deg files
        '''
        self.deg.write('\n')
        for i in range(self.robNum):
            lst = []
            lst.append(i)
            lst.append('arriveTime')
            lst.append(self.robotLst[i].arriveTime)
            lst.append('leaveTime')
            lst.append(self.robotLst[i].leaveTime)
            lst.append('state')
            lst.append(self.robotLst[i].stateType)
            lst.append('taskID')
            lst.append(self.robotLst[i].taskID)
            str_lst = [str(x) for x in lst]
            robInfo = '  '
            robInfo = robInfo.join(str_lst)
            self.deg.write(robInfo + '\n')
        self.deg.write('\n')
        self.deg.flush()

    def saveEventInMemory(self):
        pass

    def leaveCmpltTask(self, actionID):
        pass

    def arriveCmpltTask(self, actionID, encodeInd):
        pass

    def genNoBacktrackEncode(self):
        '''
        generate the no-backtrack encode
        '''
        encode = np.zeros((self.robNum, self.taskNum), dtype=int)
        for i in range(self.robNum):
            ind = 0
            for j in range(self.taskNum):
                if self.encode[i][j] != -1:
                    encode[i][ind] = self.encode[i][j]
                    ind += 1
        return encode

    def endDeg(self):
        self.deg.close()
        self.deg2.close()


class MPDA_Decode_Discrete_NB(MPDA_Decode_Discrete_Base):
    def __init__(self):
        super(MPDA_Decode_Discrete_Base,self).__init__()
        pass
    def decode(self,encode):
        self._encode = encode
        self.initStates()
        cal_type = self.decodeProcessor()
        if cal_type == CalType.stateInvalidCond:
            #            print('invalidState')
            #            invalidState = True
            makespan = sys.float_info.max
        else:
            #            print('validState')
            makespan = self.calMakespan()
        self.saveEncode()
        return makespan


if __name__ == '__main__':
    insName = '14_14_ECCENTRIC_RANDOMCLUSTERED_SVLCV_LVLCV_thre0.1MPDAins.dat'
    ins = Instance(BaseDir + '\\benchmark\\' + insName)
    MPDA_Decode_Discrete_NB._ins = ins

    mpda_dis_decode = MPDA_Decode_Discrete_NB()

    mpda_decode_base = MPDA_Decode_Discrete_Base()

    encode = np.zeros((ins.robNum, ins.taskNum), dtype=int)
    # print(encode)
    for i in range(ins.robNum):
        permLst = [x for x in range(ins.taskNum)]
        random.shuffle(permLst)
        encode[i][:] = permLst
    mpda_dis_decode.decode(encode)


    print('0-0')