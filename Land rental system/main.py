import rent_land
import return_land

def Line():
    print("--------------------------------------------------------------------------------")

def main():
    print("\n")
    print("\t\t\tWelcome to The TechnoPropertyNepal \n\n\n")
    Line()
    Line()
    print("\n\t\tPhone:9841148910 | Address:Kamalpokhari,Kathmandu \n ")
    Line()
    Line()
    print("\nDiscover prime land rentals in a premier location with unbeatable deals! \n\t\tYour dream space awaits ")
    Line()
    print("Choose one option to continue:")
    print("Press 1 to rent land:")
    print("Press 2 to return land:")
    print("Press 3 to exit interface:")
    Line()
    try:
        a = int(input("Choose your option: "))
        if (a == 1):
            rent_land.rent()
        elif (a == 2):
            return_land.returnLand()
        elif (a == 3):
            print("Thank you for being our valued customer. We are so grateful and hope we met your expectations.")
        else :
            print("Please choose a valid option as mentioned above")
        Line()
        main()
    except:
        print("Invalid!! Try Again!")
        main()

main()
