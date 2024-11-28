from board import Board
from player import Player
from randomplayer import RandomPlayer
from aiplayer import AIPlayer

def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p, b):
    """ Processes players move on the board
    """
    print(str(p) + "'s turn")
    print()
    playerNextMoveCol = p.next_move(b)
    b.add_checker(p.checker, playerNextMoveCol)
    print()
    print(b)
    print()
    if(b.is_win_for(p.checker)):
        print(p, "wins in", str(p.num_moves), "moves.")
        print("Congratulations!")
        return True
    elif(b.is_full() and not b.is_win_for(p.opponent_checker())):
        print("It's a tie!")
        return True
    else:
        return False
    
def display_menu():
    options = """
           Welcome to Connect Four by Alon Baker
              (1) Play against another Human
              (2) Play against a noob
              (3) Play against AI

              """
    print(options)

def AI():
    print("-- AI Configuration --")
    print("Difficulty: ")
    difficulty = int(input("Enter a number between 1 and 6: "))
    while True:
        if difficulty >=1 and difficulty <= 6:
            break
        difficulty = int(input("Enter a number between 1 and 6: "))
    
    print("TieBreaker MODE: ")
    TieBreaker = input("LEFT, RIGHT, or RANDOM: ").upper()
    while True:
        if TieBreaker in ["RIGHT", "LEFT", "RANDOM"]:
            break
        TieBreaker = input("LEFT, RIGHT, or RANDOM: ").upper()
    print()
    connect_four(Player('X'), AIPlayer('O', TieBreaker, difficulty))

def HUMAN():
    connect_four(Player('X'), Player('O'))

def NOOB():
    connect_four(Player('X'), RandomPlayer('O'))

def start_game():
    display_menu()
    option = int(input("Choose a game option: "))
    while True: 
        if option == 1:
            HUMAN()
            break;
        elif option == 2:
            NOOB()
            break;
        elif option == 3:
            AI()
            break;
        else:
            option = int(input("Try Again, choose a game option: "))

if __name__ == "__main__":
    start_game()

        
    
    
        
    