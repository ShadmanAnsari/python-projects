import random
user_score = 0
comp_score=0
ties = 0

name = input("enter your name")
print ("""winning rules:
1. paper vs rock --> paper
2. rock vs scissor --> rock 
3. scissor vs paper --> scissor""")
while True:
    print("""choices are:
    1. rock 
    2. paper 
    3. scissor""")
    choice = int(input("enetr your choice"))
    print()
    print("choices are ")
    while choice>3 or choice<1 :
        choice  = int(input("enter valid input"))

    if choice == 1:
        user_choice = "rock"
    elif choice == 2:    
        user_choice = "paper"
    else:
        user_choice = "scissors"
        
    print("user choice is ",user_choice )
    print("now it is comps turn")

    computer = random.randint(1,3)

    if computer == 1:
        comp_choice = "rock"
    elif computer == 2:    
        comp_choice = "paper"
    else:
        comp_choice = "scissors"

    print("the compts choice is ",comp_choice)            

    if((user_choice == "paper" and comp_choice =="rock") or (user_choice == "rock" and comp_choice =="paper")):
        print ("paper wins")
        result = "paper"
    elif ((user_choice == "scissors" and comp_choice =="rock") or (user_choice == "rock" and comp_choice =="rock")):   
        print ("rock wins ")
        result =  "rock"
    elif (user_choice==comp_choice):
        print("its a tie ")
        result = "tie"    
    else:
        print("scissors wins")
        result = "scissors"    
        
    if result == "tie":
        ties+=1
    elif result==user_choice:
        user_score+=1
    else:
        comp_score+=1
        
    print("scores are ")
    print(name , "score is ", user_score)
    print("comp score is ", comp_score)
    print("ties are ",ties )        

    repeat = input("do you wants to play again ?")
    if repeat == "no" or repeat == "No":
        break

print("game over ")
print("thanks for play")   