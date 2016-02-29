import random, os, sys, re
from random import randint  #import libraries

global scores
global turn

scores = 0
turn = 0


def getname():
        global strname
        while True:
            strname = input("please enter your name: ") #stores the users name as a variable
            if strname.isalpha() == True:
                break
            else:
                print("sorry, that contains unauthorised characters! only letters can be accepted\n")
getname()

while turn < 10:  #while loop for while players turns are under 10
    mathfunc = random.randint(1,3)  #assigns a random number to 'mathfunc'
    int1 = random.randint(1,10)
    int2 = random.randint(1,10)  #generates two random numbers to use in the questions

    if mathfunc == 1:    #random numbers that are generated with 'mathfunc' are assigned a mathematical fumction here
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
        usranswer = int(input())  #user's input
      except ValueError:
          
        print ("something went wrong!") #if the user enters a str rather than a int the program will force the user to re enter their answer
        continue
      else:
        break

    if usranswer == answer: #checks if the user's answer matches the computer's answer
        
        print("that is the right answer")
        scores += 1 #adds +1 to the variable tracking the users score
    else:
        print("that is the wrong answer")

    turn += 1 #adds +1 to the users turn counter
print("\nwell done,",strname,"\nyou've scored",scores,"point(s) out of a possible total of 10 points")
