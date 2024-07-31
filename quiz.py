#Number guessing game
"""
Make the user enter the top range number via input
validate if the entered input is a number >0;
if false exit
if true go to next step
guess the number and store it in a variable
start the count 
Start the loop to ask the user to give input; keep counting the loop
validate if the input is == to guessed number
if so exit the program with scoring the number of attempts
elif input<guess make user to increase the bid
else input>guess make user to decrease the bid.
publish the count.
"""

import random

toprange=input("set the limit of guess")
if toprange.isdigit():
    toprange=int(toprange)
    if toprange<=0:
        print("enter number greater than 0")
        quit()
    
else:
    print("enter correct number next time")
    quit()
    
random_number=random.randint(0,toprange)
count=0
print(random_number)
while True:
    guessed=input("make the guess now")
    
    if guessed.isdigit():
        count+=1
        if random_number==int(guessed):
            print("correct guess")
            break
        elif random_number<int(guessed):
            print("decrease bid")
        else:
            print("increase bid")
    else:
        print("give valid input")
        
print(count)    


