from datetime import date #importing real time date
import datetime
import Write
import Read

def Line():
    print("--------------------------------------------------------------------------------")


def rent():
    boughtProperty=[]
    Line()
    try:
        a=input("Please enter your name:")
        b=int(input("Please enter your phone number:"))
        Line()
        c="yes"
        while(c=="yes"):
            dicti=Read.read()

            print(" kitta \t | location \t | Direction \t | Annas \t | Rental Cost \t | Availability \t ")
            read_dict = Read.read()
            for key, value in read_dict.items():
                print(value[0],"\t","|",value[1],"\t","|",value[2],"\t","|",value[3],"\t","\t","|", value[4],"\t","|", " ", value[5],"\t","|", " ", value[6])
            try1=True
            while(try1==True):
                kitta=input("Enter the kitta number: ")           
                try:
                    if(dicti[kitta][5].replace("\t", "")==" Available"):
                        dicti[kitta][5]=" Not Available"
                        duration=int(input("Please,Enter the time you want to rent(in months):"))
                        rented_date = date.today()
                        rent_duration = int(rented_date.strftime('%m'))+duration
                        dicti[kitta][6]=rent_duration
                        Write.write(dicti)
                        boughtProperty.append(dicti[kitta])
                        sold=True
                        c=input("Do you want to continue?(yes/no):")
                        c.lower()
                        try1=False
                    else:
                        print("The land is not available")
                except KeyError:
                    print("Enter a valid kitta number")
        if(sold==True):
            bill(a, b, boughtProperty, duration)
    except ValueError:
        print("Invalid!! Try Again!")
        rent()

def returnLand():
    Line()
    returned_property = []
    try:
        name = input("Enter your name: ")
        phone = int(input("Enter your phone number: "))
        c="yes"
        while(c=="yes"):
            dicti=Read.read()

            print(" kitta \t | location \t | Direction \t | Annas \t | Rental Cost \t | Availability \t ")
            read_dict = Read.read()
            for key, value in read_dict.items():
                print(value[0],"\t","|",value[1],"\t","|",value[2],"\t","|",value[3],"\t","\t","|", value[4],"\t","|", " ", value[5],"\t","|", " ", value[6])
            kitta = input("Enter the kitta number of the land you want to return: ")
            dicti = Read.read()
            if kitta in dicti:
                if dicti[kitta][5].replace("\t", "") == " Not Available":
                    kitta = dicti[kitta][0]
                    city = dicti[kitta][1]
                    direction = dicti[kitta][2]
                    rental_cost = int(dicti[kitta][4])
                    area = dicti[kitta][3]
                    rented_till = dicti[kitta][6]
                    return_date = date.today()
                    return_date = return_date.strftime("%m")
                    fine = 0
                    if int(return_date) > int(rented_till):
                        fine = (int(return_date) - 1) * rental_cost
                    else:
                        return_date = 1
                    total_amount = rental_cost * int(return_date) + fine
                    dicti[kitta][5] = " Available"
                    dicti[kitta][6] = ""
                    Write.write(dicti)
                    print("\nLand with kitta number " + str(kitta) + " has been successfully returned.")
                    print("\n\t\t\tTechno Property Nepal Return Confirmation\n\n")
                    print("\nLand Details:\n")
                    print("Name: {}\nPhone Number: {}\nKitta Number: {}\nCity/District: {}\nDirection: {}\nArea: {} annas\nRental Cost: {}\nDuration of Rent: {} month(s)\n".format(name, phone, dicti[kitta][0], city, direction, area, rental_cost, return_date))
                    if fine > 0:
                       print("\nLate Fine: " + str(fine) + "\n")

                    print("\nTotal Amount: " + str(total_amount) + "\n")
                    print("\nReturned Date: " + str(date.today()) + "\n")
                    returned_property.append(dicti[kitta])
                    receipt(name, phone, kitta, returned_property, fine, rental_cost)
                    c=input("Do you want to continue?(yes/no):")
                    c = c.lower()
                else:
                    print("This land is not rented!")
                    returnLand()
            else:
                print("The kitta number does not exist.")
                returnLand()
    except:
        print("Invalid!! Try Again!")
        returnLand()
    Line()

def receipt(name, phone, kitta, returned_property, fine, price):
    print("\n\n\n\n\n")
    Line()
    print("\n\t\t\tTechno Property Nepal Rent Bill\n\n\n")
    print("\tPhone number:", phone, "\t\t\t\tAddress: Kamalpokhari\n")
    Line()
    print("\n\nName:", name, "\t\t\t\tContact Number:", phone)
    Line()
    print("\n Rent Details \n")
    print("S.N. \t| kitta \t| location \t| Direction \t| Annas \t| Rental Cost \t")
    sn = 1
    totalCost = 0
    for property_info in returned_property:
        print(str(sn) + "|\t|" + property_info[0] + "\t|" + property_info[1] + "\t|" + property_info[2] + "\t\t|"
              + property_info[3] + "\t|" + property_info[4] + "\n")
        totalCost += (int(price) + fine)
        sn += 1
    print("\n\n")
    Line()

    print("TotalCost:", totalCost, "\t\tRented Date:", date.today())

    print("If the customer fails to pay the bills on time, a fine will be imposed.")
    Line()
    Write.freciept(name, phone, kitta, returned_property, fine, price,totalCost)
    
    Line()

def bill(Name, phone, bought_property, duration):
    print("\n\n\n\n\n")
    Line()
    print("\n\t\t\tTechno Property Nepal Rent Bill\n\n\n")
    print("\tPhone number:", phone, "\t\t\t\tAddress: Kamalpokhari\n")
    Line()
    print("\n\nName:", Name, "\t\t\t\tContact Number:", phone)
    Line()
    print("\n Rent Details \n")
    print("S.N. \t| kitta \t| location \t| Direction \t| Annas \t \t")
    sn = 1
    totalCost = 0
    for property_info in bought_property:
        print(str(sn) + "|\t|" + property_info[0] + "\t|" + property_info[1] + "\t|" + property_info[2] + "\t\t|"
              + property_info[3] + "\t|" + property_info[4] + "\n")
        totalCost += (int(property_info[4]) * duration)
        sn += 1
    print("\n\n")
    Line()

    print("TotalCost:", totalCost, "\t\tRented Date:", date.today())

    print("If the customer fails to pay the bills on time, a fine will be imposed.")
    Line()

    Write.fbill(Name, phone, bought_property, duration,totalCost)
    Line()
 

