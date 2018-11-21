import time
import os
import pickle
from sys import stdout

class  process :
    def __init__(self):
        self.processName=' '
        self.arrivalTime=0
        self.burstTime=0
        self.remainingBurstTime=0
        self.waitingTime=0
        self.turnAroundTime=0
        
    def setProcessName(self,pName):
        self.processName=pName
        
    def  setArrivalTime(self,arival):
        self.arrivalTime=arival
        
    def setBurstTime(self,burst):
        self.burstTime=burst     
        
    def setWaitingTime(self,wait):
        self.waitingTime=wait

    def setRemainingBurstTime(self,remaining):
        self.remainingBurstTime=remaining
        
    def setTurnaroundTime(self,turnTime):
        self.turnAroundTime=turnTime
        
    def getProcessName(self):
        return self.processName

    def getRemainingBurstTime(self):
        return self.remainingBurstTime

    def getArrivalTime(self):
        return self.arrivalTime

    def getBurstTime(self):
        return self.burstTime

    def getWaitingTime(self):
        return self.waitingTime

    def getTurnAroundTime(self):
        return self.turnAroundTime

stdout.write("LOADING")
def loading_page():
    for i in range(0,10):
        stdout.write("#")
        time.sleep(0.1)

def virtualRoundRobin():
    processList=[]
    newQueue=[]
    timer=0
     departureTime=0
    averageWaitingTime=0
     averageTurnAroundTime=0

    loading_page()
    print('\n')
    os.system("clear")
    count=int(input("Enter Number of process:"))
    
    processList=[process() for i in range (count)]
    readyQueue=[]
    print(' ')
    for i in range(count):
            processname=str(input("Name of process:"))
             arrivalTime=int(input("Arrival Time:"))
            burstTime=int(input("Burst Time:"))
            

            processList[i].setProcessName(processname)
            processList[i].setBurstTime(burstTime)
            processList[i].setArrivalTime(arrivalTime)
       
    timeQuantam=int(input("Enter Time Slice:"))
    
    for m in range(count):
           for n in range(count):
                if (processList[m].getArrivalTime()< processList[n].getArrivalTime()):
                   processList[m],processList[n]=processList[n],processList[m]
               
    for i in range(count):
        processList[i].setRemainingBurstTime(processList[i].getBurstTime())



    while(1):
        
          found=True
          for i in range (count):
            
            if(processList[i].getRemainingBurstTime()>0):
             
                found=False
                if (processList[i].getRemainingBurstTime()>timeQuantam):
                     departureTime= departureTime+timeQuantam
                    processList[i].setRemainingBurstTime(processList[i].getRemainingBurstTime()-timeQuantam)
                    
                else:
                     departureTime= departureTime+processList[i].getRemainingBurstTime()
                    processList[i].setWaitingTime( departureTime-processList[i].getBurstTime()-processList[i].getArrivalTime())
                   

                    processList[i].setRemainingBurstTime(0)

                
               
          if(found==True):
              break
        
    for j in range(count):
         #calculating turn around time
                averageWaitingTime=averageWaitingTime+processList[j].getWaitingTime()
                processList[j].setTurnaroundTime(processList[j].getBurstTime()+processList[j].getWaitingTime())
                 averageTurnAroundTime+=processList[j].getTurnAroundTime() 
   
    averageWaitingTime=float(averageWaitingTime)/count      
     averageTurnAroundTime=float( averageTurnAroundTime)/count
    print("Process \t A.T \t B.T \t W.T \t TURN AROUND")
    print("\n")
        # printing process information
       
    for p in range(0,count):
       print(str(processList[p].getProcessName())+" \t \t"+str(processList[p].getArrivalTime())+" \t\t"+str(processList[p].getBurstTime())+" \t\t"+str(processList[p].getWaitingTime())+" \t\t"+str(processList[p].getTurnAroundTime()),end=' ')
       print("\n")
             
    print("AVERAGE W.T ="+str(averageWaitingTime))
    print("AVERAGE TURN AROUND  ="+str( averageTurnAroundTime))           
        
def main():
    #os.system("cls")    
    virtualRoundRobin()
    
main()    
        
                
    
    
   
       
        
