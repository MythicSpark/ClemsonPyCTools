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
    print(ReturnStr)

def Dec2AnythingBack(InputStr, Base, NumberOfDecimals):
    InputFloat = float(InputStr)
    ReturnStr = "."
    Counter = 0
    PrevExp = 0
    while (Counter < NumberOfDecimals):
        CurrentExp = math.floor(math.log(InputFloat, Base))
        if (CurrentExp != (PrevExp - 1)):
            pass
    print()


#This fucking sucks and I can literally just use log

#Dec2AnythingFront(777, 2)
Dec2AnythingBack(.55, 2, 10)