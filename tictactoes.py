import random
board = ["-","-","-",
          "-","-","-",
          "-","-","-"]
playerX = "X"
winner = None
gameRunning = True

#gameboard
def printBoard(board):
  print(board[0] + "|" + board[1] + "|" + board[2])
  print("-------")
  print(board[3] + "|" + board[4] + "|" + board[5])
  print("-------")
  print(board[6] + "|" + board[7] + "|" + board[8])

# #take player input
# def playerInput(board):
#   inp = int(input(""))