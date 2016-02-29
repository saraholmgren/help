import csv,sys,os,operator,time
from collections import defaultdict
from operator import itemgetter

def sub_getcsv(): # the csv reader
    global reader_csv # makes reader_csv a global variable
    files = open(filereq+'.csv','r+')
    reader_csv = csv.reader(files)
def getclass_teacher(): # gets the file that the teacher wants to manipulate
    global filereq
    print("which class you wish to view results for?\n\n- class 1 [enter: class1]\n- class 2 [enter: class2]\n- class 3 [enter: class3]")
    filereq = input("please enter one of the options: ") # asks for user input on their class and stores the answer as a variable 'filereq'
    if filereq == "class1":
        sub_getcsv()
    elif filereq == "class2":
        sub_getcsv()
    elif filereq == "class3":
        sub_getcsv()
    else:
        print("\nsorry, a file was not found for that class.") # validation
        getclass_teacher()
getclass_teacher()
def noot_noot():
    ask_loop = input("\nwould you like to view more results? (y/n): ") # makes a loop for the program to run on
    if ask_loop == 'y':
        getclass_teacher()
        getoption()
    elif ask_loop == 'n':
        print("\nthe program will now end.")
        pass # kills the running program
    else:
        print("\nsorry, but that is not a valid option.") # validation
        noot_noot()
## --------- do stuff --------- ##
def byalphabet():
    global alphabets
    sub_getcsv() # references the csv reader
    print("\nthis is a list of students sorted in alphabetical order:")
    alphabets = []
    for row in reader_csv:
        alphabets.append(row)
    for row in sorted(alphabets, key=lambda x:(str(x[0]),int(x[1]),int(x[2])),reverse = False): # uses lambda as a temp variable
        print(row)
    ## print('debug',type(alphabets))
    noot_noot()
def byhighest_score():
    sub_getcsv()
    row_lines = []
    highest_scores = []
    for row in reader_csv:
        row_lines.append(row)
    for i in range(0,len(row_lines)):
        getlines= [row_lines[i][1],row_lines[i][2],row_lines[i][3]]
        highest_scores.append([max(getlines),row_lines[i][0]]) # max function gets the highest values
        highest_scores.sort(reverse=True) # reverses the list so that the integers are placed before the strings in names.
    print("\nthis is a list of students sorted from the highest to lowest scores:\n",highest_scores)
    noot_noot()
def byaverage_score():
    sub_getcsv()
    row_lines = []
    average_scores = []
    for row in reader_csv:
        row_lines.append(row)
    #print('debug',row_lines)
    for i in range(0,len(row_lines)):
        getlines = [row_lines[i][1],row_lines[i][2],row_lines[i][3]] 
        averages = float(getlines[0])+float(getlines[1])+float(getlines[2])
        averages/=3 # divides by the index of each list to get the average
        average_scores.append([averages,row_lines[i][0]])
    print(type(row))
    print("\nthis is a list of students sorted by their average scores:\n",average_scores)
    noot_noot()    
def getoption():
    global optionreq
    print("\nhow do you wish to view the results for this class?\n\n- alphabetically by name [enter: 1]\n- highest by score [enter: 2]\n- average by score [enter: 3]")
    optionreq = input("please enter one of the options: ") # asks the user how they want to manipulate the file
    if optionreq == "1":
        byalphabet()
    elif optionreq == "2":
        byhighest_score()
    elif optionreq == "3":
        byaverage_score()
    else:
        print("\nsorry, but that is not a valid option.") # validation
        getoption()
getoption()
