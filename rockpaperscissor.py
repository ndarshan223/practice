'''
set the base score of computer and user to zero
start the true  loop
    computer pick from array of rock scissor paper randomly.
    make user to give input of above options and quit options
        if quit then quit the game. 
        else 
            continue the game
            
            if userinput is rock and computer pick is scissor:
                user wins and increase score..
            elif userinput is scissor and computer pick is paper:
                user wins
            elif userinput is paper and computer pick is rock:
                user wins
            else
                computer wins.
                
    
'''
import random
computer_score,user_score=0,0
computer_options=["r","p","s"]
while True:
    random_number=random.randint(0,2)
    computer_pick=computer_options[random_number]
    print(computer_pick)
    user_pick=input("select among r,p,s,q to quit")
    if user_pick == "q":
        break
    elif user_pick not in computer_options:
        continue        
    elif user_pick=="r" and computer_pick=="s":
        print("user wins")
        user_score+=1
    elif user_pick=="s" and computer_pick=="p":
        print("user wins")
        user_score+=1  
    elif user_pick=="p" and computer_pick=="r":
        print("user wins")
        user_score+=1
    else:
        print("you loose")
        computer_score+=1
        
            