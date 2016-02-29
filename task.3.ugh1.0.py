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
    spaaace = open('class1.csv',"r")
    csv_spaaace = csv.reader(spaaace)
    alphabets = []

    for row in csv_spaaace:
        alphabets.append(row)
    #for row in sorted(alphabets, key=lambda x:(str(x[0]), int(x[1]), int(x[2])), reverse = False):
        print(row)


def highestscore():
    noot = open("class1.csv","r+")
    noot_noot = []
    csv_noot = csv.reader(noot)
    noot_noot_noot = []
    for row in csv_noot:
        noot_noot_noot.append(row)
        #print(row)
    ugh = (sorted((((name, max(scores,key=int))for name,*scores in noot_noot_noot)), key=itemgetter(1), reverse=False)) # this is a tuple
    print('here are the scores from highest to lowest:\n',ugh)
    for x in ugh:
        x[1] = int(x[1])
    print(ugh)     
    dict(ugh)
    #print(dict(ugh))
    #shit = [ugh(x) for x in ugh]
    #for index, line in enumerate(ugh):
        #ugh[index] = line.split(',')
        
def getoption():
    global optionreq
    print("\nhow do you wish to view the results for this class?\n\n- alphabetically by name [enter: 1]\n- highest by score [enter: 2]\n- average by score [enter: 3]")
    optionreq = input("please enter one of the options: ")
    if optionreq == "1":
        byalphabet() #pass
    elif optionreq == "2":
        highestscore() #pass
    elif optionreq == "3":
        pass
    else:
        ("nah m8")
getoption()



## ---- ##

##def read_in():
##    spaaace = open("scores_output.txt","r")
##    csv_spaaace = csv.reader(spaaace)
##    idk = []
##    for row in csv_spaaace:
##        idk.append(row) #idk is an empty list apparently liek ok??
##    print(csv_spaaace)
##    print(idk)
##    
##
##def highestscore():
##    with  open("class1.csv","r") as read, open("scores_output.txt","w", newline="") as file:
##        files_w = csv.writer(file)
##        files_r = csv.reader(read)
##        files_w.writerows(sorted((((name, max(scores,key=int))
##            for name,*scores in files_r)), key=itemgetter(1), reverse=True))
##        read_in()
