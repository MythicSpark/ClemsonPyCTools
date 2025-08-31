import os
import math
import enum
import sys
import ast

class convOperation:
    placeHolder = 1

# Conversion functions

def bin2dec():
    print("Input binary string: ")
    binStrInit = input() #Seeing if prompt text is screwing with the answer 
    binStr = binStrInit.replace(" ", "")
    binSum = 0
    for i in range(-1, -(len(binStr))-1, -1):
        if binStr[(i)] == "1":
            binSum = binSum + (2 ** (-i - 1))
    
    print("--------------------\nDiagnostic: ", type(binStr), "\nDiagnostic 2: ", isinstance(binStr, str), "\nBit Length: ", len(binStr), "\nCleaned Input:", binStr)
    print("--------------------\nResult: ", binSum)

def dec2bin():
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
                # ast module saves the day 

                decIntRaw = str(ast.literal_eval(decIntRawTemp))
                usrSelReturn = 1
            else:
                print("----------------------------------\nMaybe learn to read before doing math")
                sys.exit()
        else:
            print("----------------------------------\nMaybe learn to read before doing math")
            sys.exit()

    decimalSpot = int(decIntRaw.find("."))

    print("Diagnostic - Location of decimal:", decimalSpot)

    # This is after the stripped down version and might not work yet

    binStrFin = ""

    if decimalSpot == -1:
        binStrArray = []
        decInt = int(float(decIntRaw))
        while decInt != 0:
            if decInt % 2 == 1:
                binStrArray.append("1")
                decInt = int(decInt / 2)
            elif decInt % 2 == 0:
                binStrArray.append("0")
                decInt = int(round(decInt / 2))
        binStrArray.reverse()
        binStrFin = binStrFin.join(binStrArray)
    elif decimalSpot >= 0:
        decFrontTemp = int(float(decIntRaw[0:decimalSpot]))
        decFront = decFrontTemp
        binFrontArray = []
        decBackTemp = float(decIntRaw[decimalSpot:])
        decBack = decBackTemp
        binBackArray = []

        # had to declare decimal spot as an integer outside of loop first; same procedure for decimal regions

        print("----------------------------------\nFeature not complete\n----------------------------------")

        finishStatus = 0
        while finishStatus < 2:
            while (decFront != 0):
            #segment for decFront
                if decFront % 2 == 1:
                    binFrontArray.append("1")
                    decFront = int(round(decFront / 2))
                elif decFront % 2 == 0:
                    binFrontArray.append("0")
                    decFront = int(round(decFront / 2))
            finishStatus = finishStatus + 1
            print("DIAGNOSTIC: Finished processing decFront\nCurrent finishStatus Value: ", finishStatus, "\n----------------------------------")
            decBack = decBack * 2
            while (decBack != 0):
            #segment for decBack
                if decBack < 1.0:
                    binBackArray.append("0")
                    decBack = decBack * 2
                elif decBack >= 1.0:
                    binBackArray.append("1")
                    decBack = decBack - 1.0
                finishStatus = finishStatus + 1
            finishStatus = finishStatus + 1
            print("----------------------------------\nDIAGNOSTIC: Finished processing decFront\n----------------------------------")
            pass

        #current issue is that after so many decimal places, the fractional binary just shits out and doesnt exist anymore
        #(THIS LINE FIXED) aaaand this is a problem because the length and therefore accuracy is chained to one or the other end
        #BIG PROBLEM: this shit may take forever lmao, enjoy the memory leak
        #POSSIBLE FIX: I forgot to add the decBack mult in lmao

        #prep for final

        binFrontArray.reverse()
        binFrontArray.append(".")
        print("DIAGNOSTIC:\nFRONT ARRAY: ", binFrontArray, "\nBACK ARRAY: ", binBackArray)

        #finalized - put this fucking garbage together goddammit

        binMeld = binFrontArray + binBackArray

        print("DIAGNOSTIC for BINMELD: ", binMeld, "\n----------------------------------")

        binStrFin = binStrFin.join(binMeld)

    else:
        print("What the fuck have you done")
        sys.exit()

    print(binStrFin)

# Dialogue tree data

def convertFromDiaTree():
    usrConvInitSel = int(input("Please choose a base system to convert from:\n1. Decimal\n2. Binary\n3. Octal\n4. Hexadecimal\n5. Custom Bases (WIP)\n6. Nevermind\nUser Choice: "))
    if usrConvInitSel in range(6):
        dialogueTrees.get(usrConvInitSel) # fully expecting this fucker to trip me up and have me re-define the number outside of nesting here
    else:
        print("Incompatible selection. Try again or exit with LCtrl + C.")
        dialogueTrees.get("init")
    pass

def terminationDiaTree():
    sys.exit()

# Integumentary data

dialogueTrees = {
    "init": convertFromDiaTree(),
    "end": terminationDiaTree(),        # yeah the dictionary approach doesnt work, fuck this im going to sleep
    1:bin2dec()
}

# Nothing besides THE MAIN FUNCTION should go below this comment

def dec2allMain():
    dialogueTrees = {
    "init": convertFromDiaTree(),
    "end": terminationDiaTree(),
    1:bin2dec()
}
    usrInitSel = 0
    usrInitReturn = 0
    while usrInitSel == 0:
        usrInitReturn = int(input("Welcome to All2Dec2All, a poly-base numeric conversion app. Please choose an option: \n1. Convert \n2. Quit \nSelection: "))
        if usrInitReturn == 1:
            usrInitSel = usrInitReturn
            dialogueTrees.get("init")
        elif usrInitReturn != 1:
            dialogueTrees.get("end")

dec2allMain()