import time

print("Degvielas izmaksu kalkulators v1")


time.sleep(2)
while True:
    userInput1 = input("Cik Km brauksi? ")
    time.sleep(1)
    userInput2 = input("Cik Tavs auto patērē degvielu uz 100km?  ")
    time.sleep(1)
    userInput3 = input("Cik maksā degviela? ")
    time.sleep(1)

    if (userInput1.isdigit() & userInput2.isdigit() ):
        print("Rēķinu.....")
        time.sleep(2)
        print(float(userInput1) * float(userInput2) * float(userInput3) / 100)
    else:
        print("Tu ievadīji burtus!")
        time.sleep(2)
        print(exit())