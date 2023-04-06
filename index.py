'''
Topic : Rock, Paper Scissor game
'''

# Main operating function for the game result 
def gameResult(Player):
    if(ComputerChoice==player):
        return None
    elif(player=='r' and ComputerChoice=='s'):
        return True
    elif(player=='p' and ComputerChoice=='r'):
        return True
    elif(player=='s' and ComputerChoice=='p'):
        return True
    else:
        return False

# package for random choice from computer
import random as ran

# Possible choices
choices = ['r', 'p', 's']

# Game start
while(True):
    #Computer and players choice
    ComputerChoice = ran.choice(choices)
    player = input("Your's turn (Choose 'r' for Rock, 'p' for for Paper and 's' for Scissor) : ")

    # Game result
    result = gameResult(player)

    # Display player and computer choices
    print(f"You choose : {player}")
    print(f"Computer choose : {ComputerChoice}")

    # Game result
    if result==None:
        print("Match tie!!!")
    elif result==True:
        print("Congratulations!, You Win.")
    else:
        print("You lose. Better luck next time!")
    
    # Condition for game continue or not
    game = input("Enter '1' to play again and enter  any key to exit game? : ")
    if game != '1':
        print("Thanks for play!!!")
        exit()