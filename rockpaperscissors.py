import random
N_GAMES =3


def main():
    print_welcome()
    ai_score=0
    human_score=0
    
    
    # 1.get the moves
    for i in range(N_GAMES):
        if(i==0):
            ai_score=0
            human_score=0
        else:
            ai_score=score[0]
            human_score=score[1]
        print("AI=>",ai_score)
        print("Human=>",human_score)
        ai_move =get_ai_move()
    
        human_move=get_human_move()
    

        winner=get_winner(ai_move,human_move)
        score=get_score(winner,ai_score,human_score)
        
        print("ai move was",ai_move) 
        print("Winner is",winner)
        
    print("Score:",score)

def get_ai_move():
    l=["rock","paper","scissor"]
    res=random.choice(l)
    return str(res)
def get_human_move():
  # get a valid move from human either rock or paper or scissor
    while True: 
         human_move=input("Enter ur Move:  ")
         if is_valid_move(human_move):
               return human_move
         else:
               print("Invalid move")
def is_valid_move(move):
    """ parameter move:string representing what a user  entered
    return:boolean which is True if the move is valid
    >>> is valid_move('rock')
    True
    >>> is valid_move('unicorn')
    False
    >>> is valid_move('rock')
    """
    if move =="rock":
        return(True)
    if move=="paper" :
        return(True)
    if move=="scissor" :
        return(True) 
    else:
        return(False)
def get_score(winner,ai_score,human_score):
    if(winner=="AI"):
         ai_score+=1
         

        
    elif(winner=="HUMAN"):
        
        human_score+=1
        
        
    else:
        ai_score+=0
        human_score-=0
    return [ai_score,human_score]

    
def get_winner(ai_move,human_move):
    """return ai or human or tie"""
    if((ai_move)==human_move):
        
        return"tie"
    else:
    
                if(ai_move =="rock"):
                            if(human_move=="scissor"):
                                return"AI"
                            elif(human_move=="paper"):
                                return"HUMAN"
                            else:
                                return"tie"
                elif(ai_move=="paper"):
                            if(human_move=="rock"):
                                return"AI"
                            elif(human_move=="scissor"):
                                return"HUMAN"
                            elif(human_move=="paper"):
                                return"tie"
                else:
                            if(human_move=="rock"):
                                return"HUMAN"
                            elif(human_move=="paper"):
                                return"AI"
                            else:
                                return"tie"
                




def print_welcome():
    print("Welcome to Rock paper Scissors")
    print("You will play 'str(N_GAMES)+'game against the AI")
    print("Rock beats scissors")
    print("scissors beats paper")
    print("paper beats rock")
    print("--------------------------------------------")

main()