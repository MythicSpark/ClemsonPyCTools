import os
import math
import sys
import enum
import ast

# Classhole

class baseNumber:

    def __init__(self, stringValueArray, baseValue):
        self._stringValueArray = stringValueArray
        self._baseValue = baseValue

    def __str__(self):
        return f"DIAGNOSTIC:\nConstant Array: {self.stringValueArray}\nBase Number: {self.baseValue}"

    @property
    def stringValueArray(self):
        return self._stringValueArray
    
    @stringValueArray.setter
    def stringValueArray(self, value):
        self._stringValueArray = value
    
    @property
    def baseValue(self):
        return self._baseValue
    
    @baseValue.setter
    def baseValue(self, value):
        if (type(value) != int):
            print("Fractional number systems not supported")
        elif (value <= 0):
            print("Zero or negative system values not supported")

# Drivers

def anyBNumVals():
    pass

def any2dec():
    pass

def main():
    usrArrayInput = list(input("Input constant string: "))
    usrBaseInput = int(input("Input constant base system: "))
    anyBNum = baseNumber(usrArrayInput,usrBaseInput)
    print("--------------------\n", anyBNum)

    decimalBNum = 0
    anyBNumStrLen = int(len(anyBNum.stringValueArray)) # Integer length of the constant array
    for i in range(0, anyBNumStrLen, 1):
        decimalBNum += (int(anyBNum.stringValueArray[i]) * (anyBNum.baseValue ** (anyBNumStrLen - 1 - i)))

    print(f"--------------------\nDecimal Output: {decimalBNum}")       


main()