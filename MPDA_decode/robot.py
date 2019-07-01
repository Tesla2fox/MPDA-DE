# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 14:50:30 2018

@author: robot
"""

import numpy as np
import math
from enum import Enum

class RobotState(Enum):
    onRoad = 1
    onTask = 2


class Robot():
    def __init__(self):
        self.arriveTime = 0
        self.leaveTime = 0
        self.executeDur = 0
        self.roadDur = 0
        self.encodeIndex = 0
        self.taskID = -1
        self.stateType =  RobotState['onRoad']  
        self.stopBool = False
        self.executeBool = False        
        self.ability = 0
        self.vel = 0
        self.cmpltTaskID = 0
        self.cmpltTaskLst = []
    def variableInfo(self):
        return self.arriveTime,self.leaveTime,self.executeDur,self.roadDur,self.encodeIndex,self.taskID,self.stateType,self.stopBool,self.executeBool,self.cmpltTaskID,self.cmpltTaskLst
    def display(self):
        print(' arriveTime ',self.arriveTime,' leaveTime ',self.leaveTime,
        ' executeDur', self.executeDur,' roadDur',self.roadDur,
        ' encodeIndex ',self.encodeIndex, ' taskID ',self.taskID,
        ' stateType ', self.stateType, ' stopBool ',self.stopBool,
        ' excuteBool ',self.executeBool,' ability ',self.ability,
        'vel',self.vel)
    def recover(self,arriveTime,leaveTime,executeDur,roadDur,encodeIndex,taskID,stateType,stopBool,executeBool,cmpltTaskID,cmpltTaskLst):
        self.arriveTime = arriveTime
        self.leaveTime = leaveTime
        self.executeDur = executeDur
        self.roadDur = roadDur
        self.encodeIndex = encodeIndex
        self.taskID = taskID
        self.stateType =  stateType
        self.stopBool = stopBool
        self.executeBool = executeBool
        self.cmpltTaskID = cmpltTaskID
        self.cmpltTaskLst = cmpltTaskLst
    def __str__(self):
        return  ' arriveTime ' + str(self.arriveTime) + ' leaveTime '+ str(self.leaveTime) +\
        ' executeDur'+ str( self.executeDur) +' roadDur'+ str(self.roadDur) +\
        ' encodeIndex '+ str(self.encodeIndex) + ' taskID '+ str(self.taskID) +\
        ' stateType '+ str( self.stateType) + ' stopBool '+ str(self.stopBool) +\
        ' excuteBool '+ str(self.executeBool) +' ability '+ str(self.ability) +\
        'vel'+ str(self.vel)
        

class RobotDe(Robot):
    def __init__(self):
        super(Robot,self).__init__()
        self.onRoadPeriodRatio = -1
        self.onTaskPeriodRatio = -1
        self.makespanRatio = -1



if __name__ == '__main__':
    rob = Robot()
    print(rob)
#    rob.display()
    variable = rob.variableInfo()
#    variable[0] = 1
    print(variable)
    rob.recover(*variable)