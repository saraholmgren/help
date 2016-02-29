## task 3
"""how about death"""

import csv, os, sys

def getcsv(): # does csv-y stuff
    reader_csv = csv.reader(file)

def sub_getcsv():
    global file
    with open(filereq+".csv","r+") as file:
        getcsv() 
    

def getclass_teacher(): # gets the file that the teacher wants to manipulate
    global filereq
    print("which class you wish to view results for?\n\n- class 1 [enter: class1]\n- class 2 [enter: class2]\n- class 3 [enter: class3]")
    filereq = input("please enter one of the options: ")
    if filereq == "class1":
        sub_getcsv()
    elif filereq == "class2":
        sub_getcsv()
    elif filereq == "class3":
        sub_getcsv()
    else:
        print("\nsorry, a file was not found for that class")
        getclass_teacher()
getclass_teacher()


## ---------------------------- do stuff ---------------------------- ##

def byalphabet():
    dicks = open('class1.csv')
    csv_dicks = csv.reader(dicks)
    alphabets = []
    for row in csv_dicks:
        alphabets.append(row)
    for row in sorted(alphabets,key=lambda x:(str(x[0]),int(x[1]),int(x[2])),reverse=False):
        print(row)

def getoption():
    global optionreq
    print("\nhow do you wish to view the results for this class?\n\n- alphabetically by name [enter: 1]\n- average by score [enter: 2]\n- by highest by score [enter: 3]")
    optionreq = input("please enter one of the options: ")
    if optionreq == "1":
        byalphabet()
    elif optionreq == "2":
        pass
    elif optionreq == "3":
        pass
    else:
        ("nah m8")
getoption()

## -- dump -- ##

##for row in sorted(alphabets, key=lambda x:(str(x[0]), int(x[1]), int(x[2])), reverse = False):


