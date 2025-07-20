def read():
    file = open("landRental.txt",'r')
    dicti = {}
    for line in file:
        line = line.replace('\n','')
        line = line.split(',')
        dicti[line[0]]=line
    file.close()
    return dicti
