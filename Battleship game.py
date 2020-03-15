# My first python game, Noob-Battleships by pneu1
#later stages to include ship length, and 2 player

from random import randint    #import the random int gen from random

board = []    #set up our board

for x in range(5):    # Fills our board with 5 lines of O's
  board.append(["O"] * 5)

def print_board(board):    # Our function to print the board
  for row in board:
    print " ".join(row)    # UI, prints a neat board rather than strings

#print_board(board)         # calls to print the board

# next two functions generate an x and y cooridnate for the ship
def random_row(board):
  return randint(1, len(board) - 1)

def random_col(board):
  return randint(1, len(board[0]) - 1)

ship_row = random_row(board)    # Assigns the random numbers to x
ship_col = random_col(board)    # Assigns the random numbers to y
# print ship_row    # prints where the ship is, so we can debug
# print ship_col    # remove this  if playing for real


print "Welcome to Noob-Battleship"
print "You will get 4 turns to try and sink my battleship"
print "Its hidden somewhere on a 5x5 grid, Good luck!"
# This loop allows us a range of turns, in this case, 4 turns
for turn in range(4):
  print "Turn", turn + 1    # its turn + 1 as turn starts at 0

  # Below 2 lines grab input from user
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  # this if loop checks for a WIN, if successful, breaks out, gg
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    board[guess_row-1][guess_col-1] = "!"
    print_board(board)
    break # Breaks out of function if we sink the battle ship

  # If we havent won already, here we check a number of posibilities
  # first if loop checks to ensure the guess was even on the board
  # then elif checks that guess has already been made
  # then else lets user know they missed and fills that loc with 'X'
  # nested and if at the end to inform user Game over if 4 turns used
  else:
    if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row - 1][guess_col - 1] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row-1][guess_col-1] = "X"
      if turn == 3:
        print "Game Over"

    turn = turn + 1          # increments turn by 1 each loop
    print_board(board)       # Calls the function
