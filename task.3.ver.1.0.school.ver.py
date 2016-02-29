## task 3
"""how about death"""

import csv, os, sys
global file

def getcsv():
    reader_csv = csv.reader(file)
    print(reader_csv)
    list1 = []
    for lines in reader_csv:
        print(lines)
        #print(row[0]) #pos
        list1.append(lines)

def options():
    global file
    filereq = input("please enter a class you wish to view results for (class1, class2, class3): ")
    while not(filereq=="class1" or filereq=="class2" or filereq=="class3"):
        print("sorry, a file was not found for that class\n")
        filereq = input("please enter the name of your class (class1, class2, or class3): ")

    if filereq == "class1":
        with open("class1"+".csv","r+") as file:
            getcsv()
    elif filereq == "class2":
        with open("class2"+".csv","r+") as file:
            getcsv()
    else:
        with open("class3"+".csv","r+") as file:
                  getcsv()
    #new elif, else validation
options()


## -- shit thats broke -- ##
##
##def importcsv():
##    import csv
##    with open("studentfile.csv", "r+",) as file:
##        reader_csv = csv.reader(file)
##        print(reader_csv)
##        list1 = []
##        for lines in reader_csv:
##            print(lines)
##            #print(row[0]) #pos
##            list1.append(lines)
###importcsv()
