import csv
#To Do List - byaverage, byalphabetically, byscore

def sortmenu():
    print("============================")
    print("How do you wish to sort the results?")
    print("============================")
    print("Average Score [Enter 1]")
    print("Alphabetically [Enter 2]")       
    print("Highest Score [Enter 3]")
    sortchoice = input("Please enter 1, 2 or 3:")
    return sortchoice

def classmenu():
    print("========================")
    print("Choose your class!")
    print("========================")
    print("Class A [Enter A]")
    print("Class B [Enter B]")       
    print("Class C [Enter C]")
    classchoice = input("Please enter A, B or C: ")
    return classchoice

#byaverage
def byaverage():
    f = open 
#byhighest
#x:x[0]    
#byaplhabet 
def byalphabet():
    frogs = open('Classes.csv')
    csv_frogs = csv.reader(frogs)
    byalphabet = []
    for row in csv_frogs:
        byalphabet.append(row)
    for row in sorted(byalphabet, key=lambda x:x(int(x[2]), int(x[3]), int(x[4])), reverse = True): 
        print (row)


#PROGRAM START - This Is The Password System - Teacher is the password
TeacherPassword=input("Please enter the teacher password\n")
if(TeacherPassword == "Teacher"):
    classchoice = ""
    while(classchoice not in ['A', 'B', 'C']):
        classchoice = classmenu()
        if(classchoice in ['A', 'B', 'C']):
            sortchoice = ""
            while(sortchoice not in ['1', '2', '3']):
                sortchoice = sortmenu()
            if sortchoice == "1":
                byaverage()
            elif sortchoice == "2":
                byalphabet()
            elif sortchoice == "3":
                byscore()
        else:
            print("Nope, thats wrong - please enter A, B or C ")
