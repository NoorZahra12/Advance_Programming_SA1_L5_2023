import random

game=['r','p','s']
print("Let's play rock paper and scissors, press q to quit")
user_choice=input("\nType 'r' for rock, 'p' for paper, or 's'for scissors: ")
#making a variable named scores which will store the user's points
score=0

while user_choice!='q':        
    if user_choice not in game:
        print('Invalid\nPlease try again')
        user_choice=input("\nType 'r' for rock, 'p' for paper, or 's'for scissors: ")
    else:
        #this will generate a random choice from the game variable every time it loops
        rps=random.choice(game)
        #displaying both choices
        print("your choice: ",user_choice ,"opponent's choice: ",rps)
        #adding new line
        print("\n")

        #draws
        if user_choice=='r' and rps=='r':
            print('draw')
        elif user_choice=='p' and rps=='p':
            print('draw')
        elif user_choice=='s' and rps=='s':
            print('draw')

        #rock
        elif user_choice=='r' and rps=='p':
            #rock loses over paper
            print('lost, 0 points')  
        elif user_choice=='r' and rps=='s':
            #rock wins over scissors
            print('won, 1 point')
            score+=1

        #scissors
        elif user_choice=='s' and rps=='r':
            #scissors loses against rock
            print('lost, 0 point')
        elif user_choice=='s' and rps=='p':
            #scissors win against paper
            print('won, 1 point')
            score+=1

        #paper
        elif user_choice=='p' and rps=='s':
            #paper loses against scissors
            print('lost, 0 point')
   
        elif user_choice=='p' and rps=='r':
            #paper wins against rock
            print('won, 1 point')
            score+=1

        user_choice=input("\nType 'r' for rock, 'p' for paper, or 's'for scissors: ")
#after the loop has ended when user presses q to quit
#it will display the user's total score
print('Your score: ',score)        