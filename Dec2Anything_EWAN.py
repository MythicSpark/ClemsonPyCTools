#from bs4 import BeautifulSoup
#import requests
import math

def Dec2AnythingFront(InputStr, Base):
    InputInt = int(InputStr)
    MaxExponent = math.floor(math.log(InputInt, Base))
    ReturnStr = ""
    Counter = 0
    while InputInt != 0:
        CurrentExp = (MaxExponent - Counter)
        AmountThatFitsIn = InputInt // (Base ** CurrentExp)
        ReturnStr = ReturnStr + str(AmountThatFitsIn)
        InputInt = InputInt - ((Base ** CurrentExp) * AmountThatFitsIn)
        Counter += 1
    return(ReturnStr)

def Dec2AnythingBack(InputStr, Base, NumberOfNonZeros):
    InputFloat = float(InputStr)
    ReturnStr = "."
    Counter = 0
    PrevExp = 0
    while (Counter < NumberOfNonZeros and InputFloat != 0.0):
        CurrentExp = math.floor(math.log(InputFloat, Base))
        if (CurrentExp != (PrevExp - 1)): #There was a negative exponent passed
            ReturnStr = ReturnStr + "0" * ((PrevExp - 1) - CurrentExp)
        
        AmountThatFitsIn = InputFloat // (Base ** CurrentExp)
        ReturnStr = ReturnStr + str(int(AmountThatFitsIn))
        InputFloat = InputFloat - ((Base ** CurrentExp) * AmountThatFitsIn)
        
        PrevExp = CurrentExp
        Counter += 1
    return(ReturnStr)

def Dec2Anything(InputStr, Base, NumberOfNonZeros=8):
    InputStr = str(InputStr)
    DecimalLoc = InputStr.find(".")
    if (DecimalLoc == -1):
        TotalStr = Dec2AnythingFront(InputStr, Base)
    else:
        Front = InputStr[:DecimalLoc]
        Back = InputStr[DecimalLoc:]
        if ((Front == "") or (int(Front) == 0)):
            TotalStr = Dec2AnythingBack(Back, Base, NumberOfNonZeros)
        else:
            FrontStr = Dec2AnythingFront(Front, Base)
            BackStr = Dec2AnythingBack(Back, Base, NumberOfNonZeros)
            TotalStr = FrontStr + BackStr
    return(TotalStr)

def Anything2DecFront(InputStr, Base):
    StrLength = len(InputStr)
    ReturnInt = 0
    for i in range(StrLength):
        ReturnInt += ((Base ** i) * int(InputStr[StrLength-(i+1)]))
    print(ReturnInt)

def Anything2DecBack(InputStr, Base):
    StrLength = len(InputStr)
    ReturnFloat = 0.0
    for i in range(StrLength):
        ReturnFloat += (Base**(-1*(i+1))) * float(InputStr[i])
    print(ReturnFloat)

def Anything2Dec(InputStr, Base):
    InputStr = str(InputStr)
    DecimalLoc = InputStr.find(".")
    if (DecimalLoc == -1):
        TotalStr = str(Anything2DecFront(InputStr, Base))
    else:
        Front = InputStr[:DecimalLoc]
        Back = InputStr[(DecimalLoc+1):]
        if ((Front == "") or (int(Front) == 0)):
            TotalStr = Anything2DecBack(Back, Base)
        else:
            Front = str(Anything2DecFront(Front, Base))
            Back = str(Anything2DecBack(Back, Base))
            
#Anything2Dec("0111001", 3)
#Anything2DecBack("1101001", 2)
print(Dec2Anything("0.8203125", 2))