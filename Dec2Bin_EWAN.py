import math 

def Dec2BinBack(InputStr):
    InputStr = float(InputStr)
    count = 0
    BinaryStr = ""
    while (InputStr != 0 or count <= 16):
        count += 1
        InputStr = InputStr * 2
        if (InputStr >= 1):
            BinaryStr = BinaryStr + "1"
            InputStr = InputStr - 1
        else: 
            BinaryStr = BinaryStr + "0"
    return BinaryStr

def Dec2BinFront(InputStr):
    BinaryStr = ""
    while (InputStr != 0):
        if ((InputStr % 2) == 1):
            BinaryStr = "1" + BinaryStr
        else:
            BinaryStr = "0" + BinaryStr
        InputStr = math.floor(InputStr/2)
    return(BinaryStr)

def Dec2Bin(InputStr):
    InputStr = str(InputStr)
    a = InputStr.find(".")
    if (a == -1):
        BinFinal = Dec2BinFront(int(InputStr))
    else:
        BinFront = Dec2BinFront(int(InputStr[0:a]))
        BinBack = Dec2BinBack(float(InputStr[(a):]))
        BinFinal = BinFront + "." + BinBack
    return BinFinal