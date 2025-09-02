import ast

def charCount():
    usrString = input("Write string here to see how long it is: ")
    print("Total length: ", len(usrString))
    print("Total length, no Whitespaces: ", len(usrString.replace(" ", "")))

charCount()