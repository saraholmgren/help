## TODO: add append so it actually works
"""os.path does nothing. burn it."""

import random, os, sys
import os.path
from random import randint #import libraries 

global scores
global turn
scores = 0
turn = 0

def getname():
    global strname
    while True:
        strname = input("please enter your name: ") #stores user's name as a variable
        if strname.isalpha() == True:
            break
        else:
            print("sorry, that contains unauthorised characters! only letters can be accepted.\n")
getname()

def getclass():
    global classname
    classname = input("please enter the name of your class (class1, class2, or class3): ")
    while not(classname=="class1" or classname=="class2" or classname=="class3"):
        print("sorry that is not a valid class\n")
        classname = input("please enter the name of your class (class1, class2, or class3): ")
getclass()
  
print("\nlet the games begin")

while turn < 10: #while loop for while players turns are under 10
    mathfunc = random.randint(1,3) #assigns random number to 'mathfunc'
    int1 = random.randint(1,10)
    int2 = random.randint(1,10) #generates two random numbers to use in the questions

    if mathfunc == 1: #random numbers that are generated with 'mathfunc' are assigned a mathematical function here
        print("\nquestion:", int1, "+",int2,"= ?")
        answer = int1 + int2
    elif mathfunc == 2:
        print("\nquestion: ",int1,"*",int2,"= ?")
        answer = int1 * int2
    else:
        print("\nquestion: ",int1,"-",int2,"= ?")
        answer = int1 - int2

    while True:
      try:
        usranswer = int(input()) #user input
      except ValueError: 
        print ("something went wrong! please retype your answer ")
        continue
      else:
        break

    if usranswer == answer: #checks if the user's answer matches the computer's answer
        print("that is the right answer")
        scores += 1 #adds +1 to the variable tracking the users scoress
    else:
        print("that is the wrong answer")

    turn += 1 #adds +1 to the users turn counter
print("\nwell done,",strname,"\nyou've scored",scores,"point(s) out of a possible total of 10 points")

def fileap(): #a function that contains the code to append the data to a file
    global classname #makes the variable 'classname' a global
    files = open(classname+".txt","a") #adds '.txt' (file type) to the end of the file name, and the mode 'a' meaning to append to the file
    #print("successfully found file")
    files.write(str(strname+" | score: ")) #some formatting to make the data exported into the file clearer
    files.write(str(scores)) #writes the data to the files
    files.write('\n')
    print("\nyour results have been written to:",classname,"\nunder the name:",strname) #summarises the data exported to the user
    files.close()
fileap()

def getclassesinfile():
    global classname_file
    classname_file = input("which class would you like to view the results for? (class1, class2, or class3): ")
    while not(classname_file=="class1" or classname_file=="class2" or classname_file=="class3"):
        print("sorry the file for that class was not found\n")
        classname_file = input("please enter the name of your class (class1, class2, or class3): ")
getclassesinfile()

files = open(classname_file+".txt","r")
lis1 = []
list1 = files.readlines()
files.close()
list2 = []
for i in list1:
    list2.append(i.rstrip(" | score: "))
    print(list2)

##def open_as_list():
##    files = open("class1.txt","r")
##    lis1 = []
##    list1 = files.readlines()
##    files.close()
##    list2 = []
##    for i in list1:
##        list2.append(i.rstrip(" | score: "))
##
##open_as_list()


## -- dump -- ##
    
#listname[listname.len()-3]

