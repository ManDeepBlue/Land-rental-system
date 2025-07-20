from datetime import date
import datetime
import rent_land
import return_land
import main

def repeat():
    repeat = input("Do you wish to continue using the application?Y/N: ")
    if repeat.upper() == "Y":
        main.main()
    elif repeat.upper() == "N":
        print("Thank you for being our valued customer. We are so grateful and hope we met your expectations.")
    else:
        print("Invalid Input!! Try Again")
        repeat()

def receipt(name, phone, kitta, returned_property, fine, price):
    print("\n\n\n\n\n")
    main.Line()
    print("\n\t\t\tTechno Property Nepal Rent Bill\n\n\n")
    print("\tPhone number:", phone, "\t\t\t\tAddress: Kamalpokhari\n")
    main.Line()
    print("\n\nName:", name, "\t\t\t\tContact Number:", phone)
    main.Line()
    print("\n Rent Details \n")
    print("S.N. \t| kitta \t| location \t| Direction \t| Annas \t| Rental Cost \t| Rented until")
    sn = 1
    totalCost = 0
    for property_info in returned_property:
        print(str(sn) + "|\t|" + property_info[0] + "\t|" + property_info[1] + "\t|" + property_info[2] + "\t\t|"
              + property_info[3] + "\t|" + property_info[4] + "\n")
        totalCost += (int(price) + fine)
        sn += 1
    print("\n\n")
    main.Line()

    print("TotalCost:", totalCost, "\t\tRented Date:", date.today())

    print("If the customer fails to pay the bills on time, a fine will be imposed.")
    main.Line()

    bill_file = open(str(name) + str(phone) + "_receipt" + ".txt", "w")
    bill_file.write("\n\n\t\t\tTechno Property Nepal Rent Receipt\n\n\n")
    bill_file.write("\tPhone number: 9841148910\t\tAddress: Kamalpokhari\n")
    bill_file.write("\n--------------------------------------------------------------------------------")
    bill_file.write("\n\n")
    bill_file.write("\n--------------------------------------------------------------------------------")
    bill_file.write("\n\nName:" + name + "\t\t\t\tContact Number: " + str(phone))

    bill_file.write("\n\nRent Details\n\n")
    bill_file.write("S.N. \t| kitta \t| location \t| Direction \t| Annas \t| Rental Cost \t| Rented until\n")

    sn = 1
    for property_info in returned_property:
        bill_file.write(str(sn) + "|\t|" + property_info[0] + "\t|" + property_info[1] + "\t|" + property_info[2] + "\t\t|" + property_info[3] + "\t|" + property_info[4] + "\n")
        sn += 1

    bill_file.write("\n\n\n--------------------------------------------------------------------------------")
    bill_file.write("\nTotal Cost: " + str(totalCost) + "\t\tRental Date: " + str(date.today()))
    bill_file.write("\n\nNote: If the customer fails to pay the bills on time, a fine will be imposed.\n")
    bill_file.write("\n\n\n--------------------------------------------------------------------------------")
    bill_file.close()
    main.Line()
    repeat()

def bill(Name, phone, bought_property, duration):
    print("\n\n\n\n\n")
    main.Line()
    print("\n\t\t\tTechno Property Nepal Rent Bill\n\n\n")
    print("\tPhone number:", phone, "\t\t\t\tAddress: Kamalpokhari\n")
    main.Line()
    print("\n\nName:", Name, "\t\t\t\tContact Number:", phone)
    main.Line()
    print("\n Rent Details \n")
    print("S.N. \t| kitta \t| location \t| Direction \t| Annas \t| Rental Cost \t| Rented until")
    sn = 1
    totalCost = 0
    for property_info in bought_property:
        print(str(sn) + "|\t|" + property_info[0] + "\t|" + property_info[1] + "\t|" + property_info[2] + "\t\t|"
              + property_info[3] + "\t|" + property_info[4] + "\n")
        totalCost += (int(property_info[4]) * duration)
        sn += 1
    print("\n\n")
    main.Line()

    print("TotalCost:", totalCost, "\t\tRented Date:", date.today())

    print("If the customer fails to pay the bills on time, a fine will be imposed.")
    main.Line()

    bill_file = open(str(Name) + str(phone) + "_bill" + ".txt", "w")
    bill_file.write("\n\n\t\t\tTechno Property Nepal Rent Bill\n\n\n")
    bill_file.write("\tPhone number: 9841148910\t\tAddress: Kamalpokhari\n")
    bill_file.write("\n--------------------------------------------------------------------------------")
    bill_file.write("\n\n")
    bill_file.write("\n--------------------------------------------------------------------------------")
    bill_file.write("\n\nName:" + Name + "\t\t\t\tContact Number: " + str(phone))

    bill_file.write("\n\nRent Details\n\n")
    bill_file.write("S.N. \t| kitta \t| location \t| Direction \t| Annas \t| Rental Cost \t| Rented until\n")

    sn = 1
    for property_info in bought_property:
        bill_file.write(str(sn) + "|\t|" + property_info[0] + "\t|" + property_info[1] + "\t|" + property_info[2] + "\t\t|" + property_info[3] + "\t|" + property_info[4] + "\n")
        sn += 1

    bill_file.write("\n\n\n--------------------------------------------------------------------------------")
    bill_file.write("\nTotal Cost: " + str(totalCost) + "\t\tRental Date: " + str(date.today()))
    bill_file.write("\n\nNote: If the customer fails to pay the bills on time, a fine will be imposed.\n")
    bill_file.write("\n\n\n--------------------------------------------------------------------------------")
    bill_file.close()
    main.Line()
    repeat()
