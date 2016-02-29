## task 3
"""how about death"""

import csv, os, sys

def getcsv():
    reader_csv = csv.reader(file)
    #print("\nhere is an unsorted list of students followed by their scores:\n")
    #print(reader_csv)
    list1 = []
    for lines in reader_csv:
        #print(lines)
        #print(row[0]) #pos
        list1.append(lines)

def sub_getcsv():
    global file
    with open(filereq+".csv","r+") as file:
        getcsv() 
    

def getclass_teacher():
    global filereq
    print("please enter a class you wish to view results for\n\n- class 1 [enter: class1]\n- class 2 [enter: class2]\n- class 3 [enter: class3]")
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
    frogs = open('class1.csv')
    csv_frogs = csv.reader(frogs)
    byalphabets = []
    for row in csv_frogs:
        byalphabets.append(row)
        #print(row[0],"this is pos 1/0")
        #print(row[1],"this is pos 2")
        #print(row[3],"this is pos 3")
    for row in sorted(byalphabets, key=lambda x:(int(x[1]), int(x[2]), int(x[3])), reverse = True):
        print (row)

def getoption():
    global optionreq
    print("just enter 1 ok")
    optionreq = input("please enter one of the options: ")
    if optionreq == "1":
        byalphabet()
getoption()
    
 
