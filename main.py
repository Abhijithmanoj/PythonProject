from IPython.display import clear_output
import random

def display_board(ip_list):
    """Function to display the gaming board"""
    clear_output()
    print(ip_list[1]+'\t|\t'+ip_list[2]+'\t|\t'+ip_list[3])
    print("----|-------|------")
    print(ip_list[4] + '\t|\t'+ ip_list[5] + '\t|\t' + ip_list[6])
    print("----|-------|------")
    print(ip_list[7] + '\t|\t' + ip_list[8] + '\t|\t' + ip_list[9])


def user_choice():
    player1 = ''
    while player1 not in ['X' , 'O']:
        player1 = input("Enter Player 1 choice(X or O):")
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return((player1,player2))


def update_board(ip_list,symbol,position):
    ip_list[position]=symbol

def win_check(ip_list,symbol):
    """ checking all possible ways to win"""
    return ((ip_list[1]==ip_list[2]==ip_list[3]==symbol) or       #1st row
            (ip_list[4] == ip_list[5] == ip_list[6] == symbol) or #2nd row
            (ip_list[7]==ip_list[8]==ip_list[9]==symbol) or
            (ip_list[1]==ip_list[4]==ip_list[7]==symbol) or  #column1,2,3
            (ip_list[2]==ip_list[5]==ip_list[8]==symbol) or
            (ip_list[3]==ip_list[6]==ip_list[9]==symbol) or
            (ip_list[1]==ip_list[5]==ip_list[9]==symbol) or #diagonal1
            (ip_list[3]==ip_list[5]==ip_list[7]==symbol))   #diagonal2
def whos_first():
    x=random.randint(1,2)
    if x==1:
        return 'Player 1'
    else:
        return 'Player 2'

def free_or_not(ip_list,position): #to check whether the position is available or not
    return ip_list[position] == ''
def full_or_not(ip_list):
    for i in range(1,10):
        if free_or_not(ip_list,i):
            return False
    return True  # board is full
def choose_pos(ip_list):
    position = int(0)
    while position not in [1,2,3,4,5,6,7,8,9] or not free_or_not(ip_list,position):
        position = int(input('Enter the position(1-9)'))
    return position
def replay():
    choice = input('Play Again!(YES or NO)')
    return choice == 'YES'


print("Welcome to TIC TAC TOE!!!!!")
while True:
    ip_list = ['#', '', '', '', '', '', '', '', '', '']
    player1,player2=user_choice()
    turn=whos_first()
    print(turn + " will go first..")
    game_on=input('Ready To Play {Y or N}')
    if game_on =='Y':
        play=True
    else:
        play=False
    while play:
        if turn == 'Player 1': #player 1 chance
            display_board(ip_list) #display board
            p=choose_pos(ip_list) #choose a position
            update_board(ip_list,player1,p) #update symbol in that position
            if win_check(ip_list,player1):
                display_board(ip_list)
                print("\n YAY!!!!Player 1 has Won")
                play=False
            else:
                if full_or_not(ip_list):
                    display_board(ip_list)
                    print("\nGAME ON TIE!!!!")
                    play=False
                else:
                    turn='Player 2'

        else:# player 2 chance
            if turn == 'Player 2':  # player 2 chance
                display_board(ip_list)  # display board
                p = choose_pos(ip_list)  # choose a position
                update_board(ip_list, player2, p)  # update symbol in that position
                if win_check(ip_list, player2):
                    display_board(ip_list)
                    print("\n YAY!!!!Player 2 has Won")
                    play = False
                else:
                    if full_or_not(ip_list):
                        display_board(ip_list)
                        print("\nGAME ON TIE!!!!")
                        play = False
                    else:
                        turn = 'Player 1'


    if not replay():
        break

