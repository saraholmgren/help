## task 3
"""how about death"""

import csv, os, sys
global file
global filereq

def getcsv():
    reader_csv = csv.reader(file)
    print(reader_csv)
    list1 = []
    for lines in reader_csv:
        print(lines)
        #print(row[0]) #pos
        list1.append(lines)

##def sub_getcsv():
##    with open(filereq+".csv","r+") as file:
##        getcsv()
    

def askforclass():
    global file
    global filereq
    print("please enter a class you wish to view results for\n\n- class 1 [enter: class1]\n- class 2 [enter: class2]\n- class 3 [enter: class3]")
    filereq = input("please enter one of the options: ")
    if filereq == "class1":
        with open("class1"+".csv","r+") as file:
            getcsv()
    elif filereq == "class2":
        with open("class2"+".csv","r+") as file:
            getcsv()
    elif filereq == "class3":
        with open("class2"+".csv","r+") as file:
            getcsv()
    else:
        print("\nsorry, a file was not found for that class")
        askforclass()
askforclass()
