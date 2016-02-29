## TODO: add validation for opening files

import random, os, sys
from random import randint #import libraries 

global scoress
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
    global class_name
    class_name = input("please enter the name of your class")
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
        print ("something went wrong! please retype your answer: ")
        continue
      else:
        break

    if usranswer == answer: #checks if the user's answer matches the computer's answer
        print("that is the right answer")
        scores += 1 #adds +1 to the variable tracking the users scoress
    else:
        print("that is the wrong answer")

    turn += 1 #adds +1 to the users turn counter
print("\nwell done,",strname,"\nyou've scoresd",scores,"point(s) out of a possible total of 10 points")

def fileap():
    global class_name
    try:
        files = open("nice.txt","a")
        files.write(str(strname+" | score: "))
        files.write(str(scores))
        files.write('\n')
    except IOError:
        print ("shit.")
    else:
        print ("\nyour results have been written to class:",class_name,"\nunder the name:",strname)
fileap()

## -- dump -- ##     \\ ur go shit here

##try:
##   f = open("testfile", "w")
##   f.write("tes")
##except IOError:
##   print ("broke")
##else:
##   print ("maybe not broke")
##   f.close()
