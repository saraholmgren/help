## task 3
"""how about death"""

import csv, sys, os, operator
from operator import itemgetter

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
    dicks = open('class1.csv',"r")
    csv_dicks = csv.reader(dicks)
    alphabets = []

    for row in csv_dicks:
        alphabets.append(row)
    for row in sorted(alphabets, key=lambda x:(str(x[0]), int(x[1]), int(x[2])), reverse = False):
        print(row)

def read_in():
    dick = open("score_results_output.csv","r")
    csv_dick = csv.reader(dick)
    idk = []
    for row in csv_dick:
        idk.append(row) #idk is an empty list apparently ok??
    print(csv_dick)
    print(idk)
    

def highestscore():
    with  open("class1.csv","r") as r, open("score_results_output.csv","w", newline="") as f:
        csv_w = csv.writer(f)
        csv_r = csv.reader(r)
        csv_w.writerows(sorted((((name, max(scores,key=int))
            for name,*scores in csv_r)), key=itemgetter(1), reverse=True))
        read_in()
        
def getoption():
    global optionreq
    print("\nhow do you wish to view the results for this class?\n\n- alphabetically by name [enter: 1]\n- highest by score [enter: 2]\n- average by score [enter: 3]")
    optionreq = input("please enter one of the options: ")
    if optionreq == "1":
        byalphabet()
    elif optionreq == "2":
        highestscore() #pass
    elif optionreq == "3":
        pass
    else:
        ("nah m8")
getoption()
