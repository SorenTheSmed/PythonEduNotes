from functions import *


theList = [11, 41, 345, 6554, 23, 54, "ayy", "sdf"]


running = True

while running:
    showMenu()
    userInput = input("Select Menu: ")
    print()

    if userInput == "1":
        sayHi()

    elif userInput == "2":
        helloTenTimes()

    elif userInput == "3":
        printList(theList)

    elif userInput == "4":
        running = False

    else:
        print("Undefined menu chosen.")

    print("\n\n\n\n\n")
