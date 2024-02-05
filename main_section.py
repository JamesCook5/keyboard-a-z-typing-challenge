import time
import msvcrt
alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha = []
for i in alphabet:
    alpha += i
compare = []
running  = True
running_total = 0
print("this is an alphabetic typing game where you must type out the alphabet in order!\n")
time.sleep(2)
print("\nyoull begin once <GO!> is outputted, okay?")
time.sleep(3)
print("ready.")
time.sleep(1)
print("set..")
time.sleep(1)
print("GO!")
import side_code
from side_code import *


start_time = time.time()
while running == True:
    x = msvcrt.getch().decode('utf-8').lower()  # Get a single key press and decode it to a string
    print(x, end='', flush=True)
   
   
    #x = str(input()).lower()
    compare.append(x)
    running_total += 1

    if running_total>25:
        running = False
        end_time = time.time()
        print("\nTime for calculations to see if you did it correctly.")
        time.sleep(1)
        for i in range(1):
            time.sleep(1)
            print("calculating.")
            time.sleep(1)
            print("calculating..")
            time.sleep(1)
            print("calculating...")

correct_answers = [i == compare[num] for num, i in enumerate(alpha)]

if all(correct_answers):
    print("\nCongratulations, you did it ape!")
else:
    print("\nYou lose you monkey...")




if all(correct_answers):
    elapsed_time = end_time - start_time
    elapsed_time = round(elapsed_time,2)
    print("it took you a whole",elapsed_time,"seconds")
    side_code.database(elapsed_time)
    
else:
    print("\nbetter luck next time.")
time.sleep(2)

question = int(input("\ndo you want to see the current record?\n\nIf yes input <1>\n\nIf no input <2>\n\nenter: "))

if question == 1:
    
    filetxt = open("record.txt","r")
    search = []
    search = filetxt.readline()
    #make it so the list is split into different attempts at the challenge
    
    
    new_search = ""
    for i in search:
        if i.isdigit() or i == ".":
            new_search += i
    
    from textwrap import wrap
    new_search = wrap(new_search, 4)
    score = 100
    for i in new_search:
        i = float(i)
        if i < score:
            score = i
    print(score,"seconds is the current record.")
    filetxt.close()
time.sleep(2)
question2 = int(input("\ndo you wish to see the record that stores all the past typing times?\n\nIf you do wish to enter <1>\n\nIf not enter <2>\n\nenter:"))
if question2 == 1:
    filetxt = open("record.txt","r")
    search = []
    search = filetxt.readline()
    filetxt.close()
    print(search)