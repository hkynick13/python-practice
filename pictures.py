



def house():
    print()
    print("     ^")
    print("    ^^^")
    print("   ^^^^^")
    print("  ^^^^^^^")
    print(" ^^^^^^^^^")
    print("^^^^^^^^^^^")
    print("|---------|")
    print("|---------|")
    print("|---------|")




def plumbbob():
    print()
    print("     !")
    print("    !!!")
    print("   !!!!!")
    print("  !!!!!!!")
    print(" !!!!!!!!!")
    print("!!!!!!!!!!!")
    print("|---------|")
    print("|---------|")
    print("|---------|")
    print("|---------|")
    print("!!!!!!!!!!!")
    print(" !!!!!!!!!")
    print("  !!!!!!!")
    print("   !!!!!")
    print("    !!!")
    print("     !")


def hourglass():
    print()
    print("|---------|")
    print("***********")
    print(" *********")
    print("  *******")
    print("   *****")
    print("    ***")
    print("     *")
    print("     *")
    print("    ***")
    print("   *****")
    print("  *******")
    print(" *********")
    print("***********")
    print("|---------|")

def main():
    loopflag = True
    while loopflag == True:
        userInput = input("Enter shape to display\n")
        if userInput == "hourglass":
            hourglass()
            loopflag = False
        elif userInput == "house":
            house()
            loopflag = False
        elif userInput == "plumbbob":
            plumbbob()
            loopflag = False
        else:
            print("Try again")


main()





