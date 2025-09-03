import math

def Bin2DecFront(InputStr):
    BinarySum = 0
    for i in range(1, (len(InputStr)+1)):
        BinarySum = BinarySum + (int(InputStr[i*-1]) * (2**(i-1)))
    return str(BinarySum)

def Bin2DecBack(InputStr):
    BinarySum = 0
    for i in range(0, (len(InputStr))):
        BinarySum = BinarySum + (int(InputStr[i]) * (1/(2**(i+1))))
    return str(BinarySum)

def Bin2Dec(InputStr):
    InputStr = str(InputStr)
    a = InputStr.find(".")
    if (a == -1):
        DecFinal = Bin2DecFront(InputStr)
    else:
        DecFront = Bin2DecFront(InputStr[0:a])
        DecBack = Bin2DecBack(InputStr[(a+1):(len(InputStr)+1)])
        DecFinal = DecFront + "." + DecBack
    return DecFinal