while True:
    print("Please select your choice ('1','2','3'):")
    print("    1. Evaluate Expression")
    print("    2. Sort Expression")
    print("    3. Exit")
    userChoice = (input("Enter Choice: "))
    if userChoice.isnumeric()==False:
        print("Seems like what u entered is not a number. The choice u enter must be a number between 1-4!. Please try again!\n")
        input("Press Enter, to continue...")
    else:
        userChoice=int(userChoice)
        if userChoice is 1:
            expression  = ((input("Please enter the expression you want to evaluate: ")))
            ## the rest of the code
            input("Press any key, to continue...")
        elif userChoice is 2:
            inputFile = str(input("Please enter input file: "))
            outputFile = str(input("Please enter output: "))
            input("Press any key , to continue...")

        elif userChoice is 3:
            print("Bye, thanks for using ST1507 DSAA CA2 Assignment")
            quit()
        else:
            print("This number {} doesn't exist. Please make sure u type a number between 1-3. Try again!".format(userChoice))