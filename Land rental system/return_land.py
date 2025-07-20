import invoice
from datetime import date
import datetime

def read():
    file = open("landRental.txt",'r')
    dicti = {}
    for line in file:
        line = line.replace('\n','')
        line = line.split(',')
        dicti[line[0]]=line
    file.close()
    return dicti

def write(dictionary):
    file =  open("landRental.txt","w")
    for values in dictionary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5])+","+str(values[6]))
        file.write("\n")
    file.close()

def returnLand():
    main.Line()
    returned_property = []
    try:
        name = input("Enter your name: ")
        phone = int(input("Enter your phone number: "))
        kitta = input("Enter the kitta number of the land you want to return: ")
        dicti = read()
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
                write(dicti)
                print(f"\nLand with kitta number {kitta} has been successfully returned.")
                print("\n\t\t\tTechno Property Nepal Return Confirmation\n\n")
                print(f"\nLand Details:\n")
                print(f"Name: {name}\nPhone Number: {phone}\nKitta Number: {dicti[kitta][0]}\nCity/District: {city}\nDirection: {direction}\nArea: {area} annas\nRental Cost: {rental_cost}\nDuration of Rent: {return_date} month(s)\n")
                if fine > 0:
                    print(f"\nLate Fine: {fine}\n")
                print(f"\nTotal Amount: {total_amount}\n")
                print(f"\nReturned Date: {date.today()}\n")
                returned_property.append(dicti[kitta])
                invocie.receipt(name, phone, kitta, returned_property, fine, rental_cost)
            else:
                print("This land is not rented!")
                returnLand()
        else:
            print("The kitta number does not exist.")
            returnLand()
    except:
        print("Invalid!! Try Again!")
        returnLand()
    main.Line()
