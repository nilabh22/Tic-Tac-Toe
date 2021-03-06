theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

# I created a board here manually

# I will noe define a function to printed the visual of the board
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

printBoard(theBoard)

# The game starts
def game():
    playerX = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + playerX + ".Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = playerX
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

# Now i have checked if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # It will check across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +playerX + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # It will check across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +playerX + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # It will check across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +playerX + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +playerX + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # It will check down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +playerX + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # It will check down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +playerX + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # It will check diagonal 1
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +playerX + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # It will check diagonal 2
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +playerX + " won. ****")
                break

        # If neither X nor O wins and the board is full, i've declared the result as 'tie'
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Code to change the player after every move
        if playerX =='X':
            playerX = 'O'
        else:
            playerX = 'X'

### We ask player if he wants to play again or not ###

board_keys = []

for key in theBoard:
    board_keys.append(key)

restart = input("Do want to play Again?(y/n)")

if restart == "y" or restart == "Y":
    for key in board_keys:
        theBoard[key] = " "

    game()
