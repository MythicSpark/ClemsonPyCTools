import sys

def main():
    systemStatus = 0
    usrEvalInput = input("Put a thing here to be super safely evaluated: ")
    while systemStatus == 0:
        evalProcessed = eval(usrEvalInput)
        print(evalProcessed)
        usrRecurrence = int(input("Evaluate again?\n1. Yes\n2. No\nUser Choice: "))
        if usrRecurrence == 1:
            main()
        elif usrRecurrence != 1:
            print("Goodbye")
            sys.exit
main()