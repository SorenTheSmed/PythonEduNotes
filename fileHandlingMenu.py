
handle = open("test.txt")

running = True

while running:
    print("--------------------")
    print("Awesome File Reader!")
    print("--------------------")
    print("1) Read 1 line.\n2) Read all lines.\n3) Search for specific.. (linear search)\n4) Quit.")
    userInput = input("Select function: ")

    if userInput == "1":
        print(handle.readline())
    elif userInput == "2":
        print(handle.readlines())
    elif userInput == "3":

        searchFor = input("Search for: ")
        # searchFor += "\n"
        for line in handle.readlines():
            if searchFor in line:
                print(line)
                break

    elif userInput == "4":
        running = False
    else:
        print("No such index")

    print()