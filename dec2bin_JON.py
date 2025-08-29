import os
import math


def decConvert():
    decIntRaw = str(input("Input decimal string: "))

    binStrArray = []

    decimalSpot = decIntRaw.find(".")

    if decimalSpot == -1:
        decInt = int(float(decIntRaw))
        while decInt != 0:
            i = -1
            if decInt % 2 == 1:
                binStrArray.append("1")
                decInt = int(decInt / 2)
            elif decInt % 2 == 0:
                binStrArray.append("0")
                decInt = int(round(decInt / 2))
    elif decimalSpot >= 0:
        decFront = int(float(decIntRaw[0,decimalSpot]))
        decBack = int(float(decIntRaw[decimalSpot,:]))

        #while ()

    
    binStrArray.reverse()

    binStrFin = ""

    binStrFin = binStrFin.join(binStrArray)

    print(binStrFin)



decConvert()