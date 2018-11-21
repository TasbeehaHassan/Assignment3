import time
import os
import pickle
from sys import stdout

class process :
    def __init__(self):
        self.processName=' '
        self.arrivalTime=0
        self.burstTime=0
        self.waitTime=0
        self.turnAroundTime=0
        
    def setProcessName(self,pName):
        self.processName=pName
        
    def setArrivalTime(self,arrival):
        self.arrivalTime=arrival
        
    def setBurstTime(self,burst):
        self.burstTime=burst
        
    def setwaitTime(self,wait):
        self.waitTime=wait
        
    def setTurnaroundTime(self,turnTime):
        self.turnAroundTime=turnTime
        
    def getProcessName(self):
        return self.processName

    def getArrivalTime(self):
        return self.arrivalTime

    def getBurstTime(self):
        return self.burstTime

    def getWaitTime(self):
        return self.waitTime

    def getTurnAroundTime(self):
        return self.turnAroundTime

#loading page function
stdout.write("LOADING")
def loading_page():
    for i in range(0,10):
        stdout.write("#")
        time.sleep(0.1)


def shortestJobFirst():
	averageWaitTime=0
        averageTurnAroundTime=0        

	processList=[]
        timer=0
        
        
        loading_page()
        print('\n')
        os.system("clear")
        
        count=int(input("Enter process number:"))
        processList=[process() for i in range (count)]
        QUEUE=[process() for m in range (count)]
        print(' ')
        for i in range(count):
            processName=str(input("Name of process:"))
            burstTime=int(input("Burst Time:"))
            processList[i].setProcessName(processName)
            processList[i].setBurstTime(burstTime)
    
   
        for m in range(count):
           for n in range(count):
                if (processList[m].getBurstTime() < processList[n].getBurstTime()):
                    processList[m],processList[n]=processList[n],processList[m]
                    
                    
            
        for j in range(count):
            processList[j].setwaitTime(timerProcessList[j].getArrivalTime())
            timer+=processList[j].getBurstTime()
            averageWaitTime+=processList[j].getWaitTime()
            
            
            processList[j].setTurnaroundTime(processList[j].getBurstTime()+processList[j].getWaitTime())
            averageTurnAroundTime+=processList[j].getTurnAroundTime()

        averageWaitTime=float(averageWaitTime)/count
        averageTurnAroundTime=float(averageTurnAroundTime)/count
        print("PROCESS \t B.T \t W.T \t TURN AROUND ")
        print("\n")
       
        for p in range(0,count):
             print(str(processList[p].getProcessName())+" \t\t"+str(processList[p].getBurstTime())+" \t\t"+str(processList[p].getWaitTime())+" \t\t"+str(processList[p].getTurnAroundTime()),end=' ')
             print("\n")
        print("AVERAGE W.T ="+str(averageWaitTime))
        print("AVERAGE TURN AROUND ="+str(averageTurnAroundTime))
         
           
        
def main():
     shortestJobFirst()
    
main()
