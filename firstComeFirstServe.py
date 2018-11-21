import time
import os
import pickle
from sys import stdout


class processes :
    def __init__(self):
        self.processName=' '
        self.arrivalTime=0
        self.burstTime=0
        self.waitTime=0
        self.turnArroundTime=0
        
    def setProcessName(self,pName):
        self.processName=pName
        
    def setArrivalTime(self,arrival):
        self.arrivalTime=arrival
        
    def setBurstTime(self,burst):
        self.burstTime=burst
        
    def setWaitTime(self,waiting):
        self.waitTime=waiting
        
    def setTurnaroundTime(self,turnTime):
        self.turnArroundTime=turnTime
        
    def getProcessName(self):
        return self.processName

    def getArrivalTime(self):
        return self.arrivalTime

    def getBurstTime(self):
        return self.burstTime

    def getWaitTime(self):
        return self.waitTime

    def get_turnArroundTime(self):
        return self.turnArroundTime

stdout.write("PAGE LOADING")
def loadingPage():
    for i in range(0,10):
        stdout.write("#")
        time.sleep(0.1)


def firstComeFirstServe():
        processList=[]
        timer=0
        averageWaitTime=0
        averageTurnArroundTime=0

        loadingPage()
        print('\n')
        os.system("clear")
        count=int(input("Processes to enter:"))
        processList=[processes() for i in range (count)]
        print(' ')
        for i in range(count):
            processName=str(input("Name of process:"))
            arrivalTime=int(input("Enter Arrival Time:"))
            burstTime=int(input("Enter burst time :"))

            processList[i].setProcessName(processName)
            processList[i].setBurstTime(burstTime)
            processList[i].setArrivalTime(arrivalTime)
            
        for m in range(count):
           for n in range(count):
                if (processList[m].getArrivalTime()< processList[n].getArrivalTime()):
                   processList[m],processList[n]=processList[n],processList[m]
               

            
        for j in range(count):
           
            processList[j].setWaitTime(timer-processList[j].getArrivalTime())
            timer+=processList[j].getBurstTime()
            averageWaitTime+=processList[j].getWaitTime()
            processList[j].setTurnaroundTime(processList[j].getBurstTime()+processList[j].getWaitTime())
            averageTurnArroundTime+=processList[j].get_turnArroundTime()

        averageWaitTime=float(averageWaitTime)/count
        averageTurnArroundTime=float(averageTurnArroundTime)/count
        print("PROCESS NAME \t A.T \t B.T\t W.T \t TURNAROUND")
        print("\n")
        # printing processes information
       
        for p in range(0,count):
             print(str(processList[p].getProcessName())+" \t \t"+str(processList[p].getArrivalTime())+" \t\t"+str(processList[p].getBurstTime())+" \t\t"+str(processList[p].getWaitTime())+" \t\t"+str(processList[p].get_turnArroundTime()),end=' ')
             print("\n")
        print("AVG W.T ="+str(averageWaitTime))
        print("AVG TURNAROUND ="+str(averageTurnArroundTime))
                 
def main():
       
      firstComeFirstServe()
    
main()    
        
       
