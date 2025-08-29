import math
import os

#!/usr/bin/env python

def binaryConvert():
    print("Input binary string: ")
    binStrInit = input() #Seeing if prompt text is screwing with the answer 
    binStr = binStrInit.replace(" ", "")
    binSum = 0
    for i in range(-1, -(len(binStr))-1, -1):
        if binStr[(i)] == "1":
            binSum = binSum + (2 ** (-i - 1))
    
    print("--------------------\nDiagnostic: ", type(binStr), "\nDiagnostic 2: ", isinstance(binStr, str), "\nBit Length: ", len(binStr), "\nCleaned Input:", binStr)
    print("--------------------\nResult: ", binSum)

binaryConvert()