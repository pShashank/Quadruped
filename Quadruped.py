# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import vrep
import sys
import math
import random

class Quadruped:
    
    genome = []
    best_genome = []
    cur_fitness = 0
    best_fitness = 0
    iteration = 0
    genome = 0
    x = 0
    y = 0
    z = 0
    
    clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
    
    def __init__(self):
        global clientID
        vrep.simxFinish(-1)
         # Connect to V-REP
        if clientID!=-1:
            print ('Connected to remote API server')
        else: 
            print('not')
            sys.exit('not connect')
        return 0
    
    def initgenome(self):
        gen = []
        for i in range(0,8):
#            speed
        			gen.append(random.randint(1,9))       
        for i in range(8,16):
#            angle
        			gen.append(random.randint(0,9))	
        return gen

    def mutate(self,gen):
    	 index = math.floor(random.randint(0,16))
    	 if (index == 32) :
    			index = 31
    	 if (index < 16) :
    			gen[index] = (random.randint(1,9))
     	 else :
    			gen[index] = (random.randint(0,9))
         return gen
    
    def setGenome(self,gen):      
        global genome 	
        genome = gen 
        return 0

    def Getgenome(self):
        global genome
        return genome

    def Getbest_genome(self):
        global best_genome
        return best_genome

    def Getfitness(self):
        global cur_fitness
        return cur_fitness

    def Getbest_fitness(self):
        global best_fitness
        return best_fitness

    def fitness(self,x,y,z):
        return math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2))
   
    def evaluate(self):
#        global a
        global x,y,z
        global generation
        global genome
        global best_genome
        cur_fitness = self.fitness(x,y,z);
        generation += 1;
        if  not best_genome :
            self.add_best_indivisual()
        elif cur_fitness > best_fitness and genome !=best_genome:
            self.add_best_indivisual()
            genome = best_genome[0]
        else:
            genome != best_genome
            genome = self.mutate()
        return genome
    
    
genome = Quadruped.initgenome()
print genome
A=Quadruped.evaluate()
        
#b = Quadruped()

    
#    
#    errorcode,hexajoint1handle=vrep.simxGetObjectHandle(clientID,'hexa_joint1',vrep.simx_opmode_blocking)
#    errorcode,hexajoint2handle=vrep.simxGetObjectHandle(clientID,'hexa_joint1#1',vrep.simx_opmode_blocking)
#    errorcode,hexajoint3handle=vrep.simxGetObjectHandle(clientID,'hexa_joint1#2',vrep.simx_opmode_blocking)
#    errorcode,hexajoint4handle=vrep.simxGetObjectHandle(clientID,'hexa_joint1#4',vrep.simx_opmode_blocking)
#    
#    errorcode,hexajoint12handle=vrep.simxGetObjectHandle(clientID,'hexa_joint1#2',vrep.simx_opmode_blocking)
#    errorcode,hexajoint32handle=vrep.simxGetObjectHandle(clientID,'hexa_joint3#2',vrep.simx_opmode_blocking)
#    errorcode,hexa=vrep.simxGetObjectHandle(clientID,'hexa_body',vrep.simx_opmode_blocking)
#    k=0
#    v=-0.5
#    j1=-0.6
#    j3=0.6
#    returnCode,Data=vrep.simxGetObjectPosition(clientID,hexa,-1,vrep.simx_opmode_streaming)
#    
#    while k == 0:
#        returnCode,Data=vrep.simxGetObjectPosition(clientID,hexa,-1,vrep.simx_opmode_streaming)
#        time.sleep(1)
#        vrep.simxSetJointTargetVelocity(clientID,hexajoint1handle,v,vrep.simx_opmode_streaming)
#        vrep.simxSetJointTargetPosition(clientID,hexajoint1handle,j1,vrep.simx_opmode_streaming)    
#        vrep.simxSetJointTargetVelocity(clientID,hexajoint3handle,v,vrep.simx_opmode_streaming)
#        vrep.simxSetJointTargetPosition(clientID,hexajoint3handle,j1,vrep.simx_opmode_streaming)
#        vrep.simxSetJointTargetVelocity(clientID,hexajoint2handle,v,vrep.simx_opmode_streaming)
#        vrep.simxSetJointTargetPosition(clientID,hexajoint2handle,j3,vrep.simx_opmode_streaming)    
#        vrep.simxSetJointTargetVelocity(clientID,hexajoint4handle,v,vrep.simx_opmode_streaming)
#        vrep.simxSetJointTargetPosition(clientID,hexajoint4handle,j3,vrep.simx_opmode_streaming)
#        #    vrep.simxSetJointTargetVelocity(clientID,hexajoint32handle,v,vrep.simx_opmode_streaming)
#        #    vrep.simxSetJointTargetPosition(clientID,hexajoint32handle,j3,vrep.simx_opmode_streaming)
#        if j1==0.6:
#            j1=-0.6
#            v=0.5
#            j3=1
#        else:
#            j1=0.6
#            v=-0.5
#            j3=2
    #    vrep.simxSetJointTargetVelocity(clientID,hexajoint12handle,v,vrep.simx_opmode_streaming)
    #    vrep.simxSetJointTargetPosition(clientID,hexajoint12handle,j1,vrep.simx_opmode_streaming)
    
