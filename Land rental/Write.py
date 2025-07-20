from datetime import date
def write(dictionary):
    file =  open("landRental.txt","w")
    for values in dictionary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5])+","+str(values[6]))
        file.write("\n")
    file.close()

def freciept(name, phone, kitta, returned_property, fine, price,totalCost):
    bill_file = open(str(name) + str(phone) + "_receipt" + ".txt", "w")
    bill_file.write("\n\n\t\t\tTechno Property Nepal Rent Receipt\n\n\n")
    bill_file.write("\tPhone number: 9841148910\t\tAddress: Kamalpokhari\n")
    bill_file.write("\n--------------------------------------------------------------------------------")
    bill_file.write("\n\n")
    bill_file.write("\n--------------------------------------------------------------------------------")
    bill_file.write("\n\nName:" + name + "\t\t\t\tContact Number: " + str(phone))

    bill_file.write("\n\nRent Details\n\n")
    bill_file.write("S.N. \t| kitta \t| location \t| Direction \t| Annas \t \n")

    sn = 1
    for property_info in returned_property:
        bill_file.write(str(sn) + "|\t|" + property_info[0] + "\t|" + property_info[1] + "\t|" + property_info[2] + "\t\t|" + property_info[3] + "\t|" + property_info[4] + "\n")
        sn += 1

    bill_file.write("\n\n\n--------------------------------------------------------------------------------")
    bill_file.write("\nTotal Cost: " + str(totalCost) + "\t\tRental Date: " + str(date.today()))
    bill_file.write("\n\nNote: If the customer fails to pay the bills on time, a fine will be imposed.\n")
    bill_file.write("\n\n\n--------------------------------------------------------------------------------")
    bill_file.close()

def fbill(Name, phone, bought_property, duration,totalCost):
    bill_file = open(str(Name) + str(phone) + "_bill" + ".txt", "w")
    bill_file.write("\n\n\t\t\tTechno Property Nepal Rent Bill\n\n\n")
    bill_file.write("\tPhone number: 9841148910\t\tAddress: Kamalpokhari\n")
    bill_file.write("\n--------------------------------------------------------------------------------")
    bill_file.write("\n\n")
    bill_file.write("\n--------------------------------------------------------------------------------")
    bill_file.write("\n\nName:" + Name + "\t\t\t\tContact Number: " + str(phone))

    bill_file.write("\n\nRent Details\n\n")
    bill_file.write("S.N. \t| kitta \t| location \t| Direction \t| Annas \n")

    sn = 1
    for property_info in bought_property:
        bill_file.write(str(sn) + "|\t|" + property_info[0] + "\t|" + property_info[1] + "\t|" + property_info[2] + "\t\t|" + property_info[3] + "\t|" + property_info[4] + "\n")
        sn += 1

    bill_file.write("\n\n\n--------------------------------------------------------------------------------")
    bill_file.write("\nTotal Cost: " + str(totalCost) + "\t\tRental Date: " + str(date.today()))
    bill_file.write("\n\nNote: If the customer fails to pay the bills on time, a fine will be imposed.\n")
    bill_file.write("\n\n\n--------------------------------------------------------------------------------")
    bill_file.close()
