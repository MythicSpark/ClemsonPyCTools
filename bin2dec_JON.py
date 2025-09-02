import math
import os

#!/usr/bin/env python

def binaryConvert():
    print("Input binary string: ")
    binStrInit = input() #Seeing if prompt text is screwing with the answer 
    binStr = binStrInit.replace(" ", "")
    binSum = 0

    decimalSpot = int(binStr.find("."))

    if decimalSpot == -1:
        for i in range(-1, -(len(binStr))-1, -1):
            if binStr[(i)] == "1":
                binSum = binSum + (2 ** (-i - 1))
    elif decimalSpot != -1:
        usrBinFront = binStr[0:decimalSpot]
        BinFrontSum = 0
        usrBinBack = binStr[decimalSpot+1:]
        BinBackSum = 0
        for i in range(-1, -(len(usrBinFront))-1, -1):
            if usrBinFront[(i)] == "1":
                BinFrontSum = BinFrontSum + (2 ** (-i - 1))
        for i in range(0, len(usrBinBack), 1):
            if usrBinBack[(i)] == "1":
                BinBackSum = BinBackSum + (2 ** (-i - 1))
        binSum = BinFrontSum + BinBackSum
        
    
    print("--------------------\nDiagnostic: ", type(binStr), "\nDiagnostic 2: ", isinstance(binStr, str), "\nBit Length: ", len(binStr), "\nCleaned Input:", binStr)
    print("--------------------\nResult: ", binSum)

binaryConvert()