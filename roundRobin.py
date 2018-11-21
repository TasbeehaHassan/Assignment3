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


def roundRobin():
    processList=[]
     newQueue=[]
    timer=0
    currentTime=0
    averageWaitingTime=0
    averageTurnAroundTime=0
    loading_page()
    print('\n')
    os.system("clear")

    count=int(input(" process to enter:"))
    processList=[ process() for i in range (count)]
     newQueue=[]
    print(' ')
    for i in range(count):
            processName=str(input("Enter name of process:"))
            arrivalTime=int(input("Enter Arrival Time:"))
            burstTime=int(input("Enter Burst Time :"))
            

            processList[i].setProcessName(processName)
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
                    currentTime= currentTime + timeQuantam
                    processList[i].setRemainingBurstTime(processList[i].getRemainingBurstTime()-timeQuantam)
                    
                else:
                    currentTime= currentTime+processList[i].getRemainingBurstTime()
                    processList[i].setWaitingTime( currentTime-processList[i].getBurstTime()-processList[i].getArrivalTime())
                   
                    processList[i].setRemainingBurstTime(0)

                
                
          if(found==True):
              break
        
               
            
    for j in range(count):
                averageWaitingTime=averageWaitingTime+processList[j].getWaitingTime()
                processList[j].setTurnaroundTime(processList[j].getBurstTime()+processList[j].getWaitingTime())
                averageTurnAroundTime+=processList[j].getTurnAroundTime() 
      
    averageWaitingTime=float(averageWaitingTime)/count      
    averageTurnAroundTime=float(averageTurnAroundTime)/count
    print("Process \t A.T \t B.T \t W.T \t TURN AROUND")
    print("\n")
       
    for p in range(0,count):
       print(str(processList[p].getProcessName())+" \t \t"+str(processList[p].getArrivalTime())+" \t\t"+str(processList[p].getBurstTime())+" \t\t"+str(processList[p].getWaitingTime())+" \t\t"+str(processList[p].getTurnAroundTime()),end=' ')
       print("\n")
             
    print("AVERAGE W.T ="+str(averageWaitingTime))
    print("AVERAGE TURN AROUND ="+str(averageTurnAroundTime))
         
           
        
def main():
    os.system("cls")    
    roundRobin()
    
main()    
        
       

         
                    
                
    
    
   
       
        
