"""
PROJECT  Tic-Tac-Toe
This is the project for the Cisco Skills for All Python Essentials Course
Your task is to write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

the computer (i.e., your program) should play the game using 'X's;
the user (e.g., you) should play the game using 'O's;
the first move belongs to the computer − it always puts its first 
'X' in the middle of the board;
all the squares are numbered row by row starting with 1 
the user inputs their move by entering the number of the square they choose − 
the number must be valid, i.e., it must be an integer, it must be greater than 
0 and less than 10, and it cannot point to a field which is already occupied;
the program checks if the game is over − there are four possible verdicts: 
the game should continue, the game ends with a tie, you win, or the computer wins;
the computer responds with its move and the check is repeated;
don't implement any form of artificial intelligence − a random field choice 
made by the computer is good enough for the game.
"""
global board

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    first = "+-------+-------+-------+"
    middle = "|       |       |       |"
    last = "|   "
    for i in range(13):
        if i % 4 == 0 :
            print(first)
        if i % 2 != 0:
            print(middle)
        if i ==2:
            for j in range(3):
                last+=str(board[0][j])
                last+="   |   "
            print(last)
            last = "|   "
        if i ==6:
            for j in range(3):
                last+=str(board[1][j])
                last+="   |   "
            print(last)
            last = "|   "
        if i ==10:
            for j in range(3):
                last+=str(board[2][j])
                last+="   |   "
            print(last)
            last = "|   "
     
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    valid = False
    while not valid:
        move = input("Enter your move ")
        for i in range(3):
            for j in range(3):
                if move == "X" or move == "O":
                    continue
                elif move != board[j][i]:
                    continue
                else:
                    valid = True
    for i in range(3):
        for j in range(3):
            if move == board[j][i]:
                board[j][i] = "O"
    
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free_spaces
    free_spaces = []              
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" or board[i][j] == "O":
                continue
            else:
                item = (i+1,j+1)
                free_spaces.append(item)
    return free_spaces

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    winner = "none"
    #winning combinations
    won1 = board[0][0] == board[0][1]==board[0][2]
    won2 = board[1][0] == board[1][1]==board[1][2]
    won3 = board[2][0] == board[2][1]==board[2][2]
    won4 = board[0][0] == board[1][0]==board[2][0]
    won5 = board[0][1] == board[1][1]==board[2][1]
    won6 = board[0][2] == board[1][2]==board[2][2]
    won7 = board[0][0] == board[1][1]==board[2][2]
    won8 = board[0][2] == board[1][1]==board[2][0]
    
    for i in range(3):
            for j in range(3):
                if won2 or won5 or won7 or won8:
                    winner = board[1][1]
                if won1 or won4:
                    winner = board[0][0]
                if won3:
                    winner = board[2][0]
                if won6:
                    winner = board[2][2]
    if winner == sign:
        return True
    else:
        return False
    
def draw_move(board):
    # The function draws the computer's move and updates the board.
    make_list_of_free_fields(board)
    i,j = random.choice(free_spaces)
    board[i-1][j-1] = "X" 
    
#Main Game   
import random   
#initial board conditions
board = [["1","2","3"],["4","X","6"],["7","8","9"]]
#Mail Loop
looping = 0
while looping < 8:
    print(looping)
    display_board(board)
    #code for player turns
    if looping % 2 == 0:
        enter_move(board)
        if victory_for(board, "O"):
            display_board(board)
            print("You won!")
            break
    #code for computer turns    
    else:
        draw_move(board)
        if victory_for(board,"X"):
            display_board(board)
            print("Computer wins!")
            break
    looping += 1
# if loop ends without a break its a tie
else:
    display_board(board)
    print("It's a tie")
    
    
    

    
                
                