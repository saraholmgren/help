import csv, re, operator, functools
global list1
global list2
global list3
global list4
global list5

list1 = []
with open("results.csv","rt") as dot_txt:
    reader = csv.reader(dot_txt)

def listsandthings():
     with open("results.csv","rt",) as  dot_txt:
          files = csv.reader(dot_txt)
          #print(files)
          print("this is an unsorted list of students:")
          global list3
          list3 = []
          for row in files:
               list3.append(row)
               print(row)

listsandthings()

def sortlist():
    list3.sort()
    #print(list3)
    #sorted(list3) #python wtf?? i thought we were bros? ?? ?
    print("\nthis is a list sorted in alphabetical order")
    global list4
    list4 = []
    for row in list3:
        list4.append(row)
        print(row)
    
sortlist()

def highscores():
     print("\nsorted in order of scores:")
     list4.sort(reverse=True) #whaddya mean 'none' ok fuck u
     #print(list4)
     global list5
     list5 = []
     for row in list4:
          list5.append(row)
          print(row)
highscores()


def averagescores():
     arse = [butt[1] for butt in list4]
     (str(arse))
     arse = [int(x) for x in arse]
     sumscores = (sum(arse))
     print("\nthe average score of all students was:",sumscores/len(arse))
     
averagescores()


     


##--dump--##

     
