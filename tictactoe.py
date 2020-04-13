from os import system
import random

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

playersign=''
compsign=''

def printboard():
    system('clear')
    print("\n{} is  {} and Computer is {}\n".format(player, playersign, compsign))
    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("----------")
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("----------")
    print("{} | {} | {}".format(board[6], board[7], board[8]))

def computerplay():
    if remainingchoice:
        computerchoice = int(random.choice(remainingchoice))
        print("Computer choice {}".format(computerchoice))
        board[computerchoice-1] = compsign
        remainingchoice.remove(computerchoice)
        printboard()

def rowwin():
    if (board[0] == board[1] == board [2] != ' '):
        return True
    elif (board[3] == board[4] == board [5] != ' '):
        return True
    elif (board[6] == board[7] == board [8] != ' '):
        return True
    else:
        return False

def columnwins():
    if (board[0] == board[3] == board [6] != ' '):
        return True
    elif (board[1] == board[4] == board [7] != ' '):
        return True
    elif (board[2] == board[5] == board [8] != ' '):
        return True
    else:
        return False

def diagonalwins():
    if (board[0] == board[4] == board [8] != ' '):
        return True
    elif (board[2] == board[4] == board [6] != ' '):
        return True
    else:
        return False


def checkwin():
    return (rowwin() or columnwins() or diagonalwins())


player=input("Enter your name : ")
system('clear')
print("Hello {}, Pls carefully see the placeholder for each cell. The 1-9 numbers will be your next choices.".format(player))
print("1  | 2 |  3 ")
print("-----------")
print("4  | 5 |  6 ")
print("-----------")
print("7  | 8 |  9 ")

print("Let the computer start or Would you like to start this {}? Y=Yes".format(player))
choice=input()
print("Choice - {}".format(choice))
if choice.upper() == 'Y':
    print("Would you like to use X or O")
    playersign=input()
    playersign = playersign.upper()
else:
    print("{} dont want to start, so Computer is starting ".format(player))
    playersign='X'

if playersign == 'X':
    compsign='O'
else:
    compsign='X'

remainingchoice=[1,2,3,4,5,6,7,8,9]
while remainingchoice :
    print("The Valid Choices are : {}".format(remainingchoice))
    playerchoice = int(input("Enter the position you choose {} : ".format(player)))
    while playerchoice not in remainingchoice:
        playerchoice = int(input("Invalid Choice. Enter the position you choose {} : ".format(player)))
    board[playerchoice-1]=playersign
    remainingchoice.remove(playerchoice)
    printboard()
    if (checkwin()):
        print("Brilliant Move!! You won {}".format(player))
        exit()
    computerplay()
    if (checkwin()):
        print("The house alwasy wins! Sorry {}".format(player))
        exit()

print("That was a good game {} but it is a Tie".format(player))
