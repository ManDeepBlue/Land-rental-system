import operation

def main():
    print("\n")
    print("\t\t\tWelcome to The TechnoPropertyNepal \n\n\n")
    operation.Line()
    operation.Line()
    print("\n\t\tPhone:9841148910 | Address:Kamalpokhari,Kathmandu \n ")
    operation.Line()
    operation.Line()
    print("\nDiscover prime land rentals in a premier location with unbeatable deals! \n\t\tYour dream space awaits ")
    operation.Line()
    print("Choose one option to continue:")
    print("Press 1 to rent land:")
    print("Press 2 to return land:")
    print("Press 3 to exit interface:")
    operation.Line()
    try:
        a = int(input("Choose your option: "))
    except:
        print("Invalid input")
        main()
    if (a == 1):
        operation.rent()
        main()
    elif (a == 2):
        operation.returnLand()
        main()
    elif (a == 3):
        print("Thank you for being our valued customer. We are so grateful and hope we met your expectations.")
    else :
        print("Please choose a valid option as mentioned above")
        main()  
    operation.Line()

main()
