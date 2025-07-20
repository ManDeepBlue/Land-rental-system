from invoice import bill
from datetime import date

def Line():
    print("--------------------------------------------------------------------------------")

def read():
    file = open("landRental.txt", 'r')
    dicti = {}
    for line in file:
        line = line.replace('\n', '')
        line = line.split(',')
        dicti[line[0]] = line
    file.close()
    return dicti

def write(dictionary):
    file = open("landRental.txt", "w")
    for values in dictionary.values():
        file.write(",".join(map(str, values)) + "\n")
    file.close()

def rent():
    boughtProperty = []
    Line()
    try:
        a = input("Please enter your name:")
        b = int(input("Please enter your phone number:"))
        Line()
        c = "yes"
        while c == "yes":
            dicti = read()
            print(" kitta \t | location \t | Direction \t | Annas \t | Rental Cost \t | Availability \t | Rented until")
            read_dict = read()
            for key, value in read_dict.items():
                print(value[0], "\t", "|", value[1], "\t", "|", value[2], "\t", "|", value[3], "\t", "\t", "|",
                      value[4], "\t", "|", " ", value[5], "\t", "|", " ", value[6])
            kitta = input("Enter the kitta number: ")
            if dicti[kitta][5].replace("\t", "") == " Available":
                print(dicti[kitta], "=========")
                dicti[kitta][5] = " Not Available"
                duration = int(input("Please,Enter the time you want to rent(in months):"))
                rented_date = date.today()
                rent_duration = int(rented_date.strftime('%m')) + duration
                dicti[kitta][6] = rent_duration
                write(dicti)
                boughtProperty.append(dicti[kitta])
                sold = True
                c = input("Do you want to continue?(yes/no):").lower()
            else:
                print("The land is not available")
        if sold == True:
            bill(a, b, boughtProperty, duration)
    except ValueError:
        print("Invalid!! Try Again!")
        rent()
