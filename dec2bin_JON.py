import os
import math
import sys
import ast


def dec2binConvert():
    usrSelReturn = 0
    while usrSelReturn == 0:
        inputModeTEMP = input("Choose number input:\n1. Simple (Only text, no complex symbols besides decimal points)\n2. Complex (Can put resolved equations in here)\nUser Choice: ")
        if len(inputModeTEMP) == 1:
            inputMode = int(inputModeTEMP)
            if inputMode == 1:
                decIntRaw = input("----------------------------------\nInput simple decimal string: ")
                usrSelReturn = 1
            elif inputMode == 2:
                decIntRawTemp = input("----------------------------------\nInput math equation: ")
            
                # "oh but jon evals are DAAAAANGEROOOOUS" yeah mang i dont give a fuck if someone's hacking into government servers with a python calculator, i think bigger problems would exist if that were possible
                # ast module saves the day (no it didnt)

                decIntRaw = str(eval(decIntRawTemp))
                usrSelReturn = 1
            else:
                print("----------------------------------\nMaybe learn to read before doing math")
                sys.exit()
        else:
            print("----------------------------------\nMaybe learn to read before doing math")
            sys.exit()

    decimalSpot = int(decIntRaw.find("."))

    doesInputExist = False

    if len(decIntRaw) != 0:
        doesInputExist = True

    print("Diagnostic - Location of decimal:", decimalSpot)

    # This is after the stripped down version and might not work yet

    binStrFin = ""

    if decimalSpot == -1 and doesInputExist == True: # Decimal not detected
        binStrArray = []
        decInt = int(float(decIntRaw))
        while decInt != 0:
            if decInt % 2 == 1:
                binStrArray.append("1")
                decInt = int(round(decInt / 2))
            elif decInt % 2 == 0:
                binStrArray.append("0")
                decInt = int(round(decInt / 2))
        binStrArray.reverse()
        binStrFin = binStrFin.join(binStrArray)
    elif decimalSpot >= 0 and doesInputExist == True: # Decimal detected
        if decIntRaw[0] != ".":
            decFrontTemp = int(float(decIntRaw[0:decimalSpot]))
            decFront = decFrontTemp
            print("DECFRONT: ", decFront)
            binFrontArray = []
            doesFrontArrayExist = True
        else:
            binFrontArray = "DNE"
            doesFrontArrayExist = False
        if decIntRaw[-1] != ".":
            decBackTemp = float(decIntRaw[decimalSpot:])
            decBack = decBackTemp
            print("DECBACK: ", decBack)
            binBackArray = []
            doesBackArrayExist = True
        else:
            binBackArray = "DNE"
            doesBackArrayExist = False

        # had to declare decimal spot as an integer outside of loop first; same procedure for decimal regions

        print("----------------------------------\nFeature not complete\n----------------------------------")

        finishStatus = 0
        while finishStatus < 2:
            if doesFrontArrayExist == True:
                while (decFront != 0):
                #segment for decFront
                    if decFront % 2 == 1:
                        binFrontArray.append("1")
                        decFront = int(decFront / 2)
                    elif decFront % 2 == 0:
                        binFrontArray.append("0")
                        decFront = int(decFront / 2)
            finishStatus = finishStatus + 1
            print("DIAGNOSTIC: Finished processing decFront\nCurrent finishStatus Value: ", finishStatus, "\n----------------------------------")
            
            if doesBackArrayExist == True:
                while (decBack != 0):
                #segment for decBack
                    decBack = decBack * 2
                    if decBack < 1.0:
                        binBackArray.append("0")
                    elif decBack >= 1.0:
                        binBackArray.append("1")
                        decBack = decBack - 1.0
            finishStatus = finishStatus + 1
            print("DIAGNOSTIC: Finished processing decBack\nCurrent finishStatus Value: ", finishStatus, "\n----------------------------------")
            pass

        #current issue is that after so many decimal places, the fractional binary just shits out and doesnt exist anymore
        #(THIS LINE FIXED) aaaand this is a problem because the length and therefore accuracy is chained to one or the other end
        #BIG PROBLEM: this shit may take forever lmao, enjoy the memory leak
        #POSSIBLE FIX: I forgot to add the decBack mult in lmao
        #POSSIBLE REASON: SO i may or may not have put finishStatus in the wrong spot earlier, sequence breaking the loop and making a memory hog 

        #prep for final

        if doesBackArrayExist == True and doesFrontArrayExist == True:
            binFrontArray.reverse()
            binFrontArray.append(".")
            binMeld = binFrontArray + binBackArray
        elif doesFrontArrayExist == True and doesBackArrayExist == False:
            binFrontArray.reverse()
            binFrontArray.append(".")
            binMeld = binFrontArray
        elif doesBackArrayExist == True and doesFrontArrayExist == False:
            binMeld = binBackArray
            binMeld.insert(0, ".")
        else: 
            print("No input detected. Exiting...")
            sys.exit()

        print("DIAGNOSTIC:\nFRONT ARRAY: ", binFrontArray, "\nBACK ARRAY: ", binBackArray)


        print("DIAGNOSTIC for BINMELD: ", binMeld)

        binStrFin = binStrFin.join(binMeld)
    elif doesInputExist == False:
        print("Incompatible input detected. Exiting...")
        sys.exit() 

    else:
        print("What the fuck have you done")
        sys.exit()

    print("----------------------------------\nBinary String Output: ", binStrFin)



dec2binConvert()