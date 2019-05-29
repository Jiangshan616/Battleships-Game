# Battleships Games.py
# Author: Jiangshan Li
# Last updated: May 1, 2019
# Purpose: A program that gives the user guesses to sink a battleship
#          whose position is randomly chosen by the computer in a 8 by 8 ocean
# Program uses module random, the python built-in funcions of range(),
#          randint(), a 8x8 two-dimensional ocean of "O" and the
#          Boolean operators "and" & "or" or “or”
#



#Game Rules:
#1. The ocean is 8*8
#2. There are two battle ship in the ocean(1*3,3*1)
#3. Guess number:4 times


print('---BATTLESHIPS GAME---')
print("\n***How to play this game?***")
print ("----------------")
print("There are two battleships on the ocean.(1*3 & 3*1)")
print('Enter the coordinate you want to sink the ship!')
print('You can input the times to play the game. ')
print ("----------------")







guess_num = 0#inital guess number

#game running
running = True
while running:

#0.This step is to check the input times
    guess_num_input_running = True
    while guess_num_input_running:
        guess_num_input = input('\nHow many times do you want to play：')
        if guess_num_input.isdigit() == False:
            print("Please enter a integer number and bigger than 0!")

        elif float(str(guess_num_input)) == 0:
            print("Please enter an integer number and bigger than 0!")
        elif guess_num_input.isdigit():

            guess_num_input = int(guess_num_input)
            guess_num_input_running = False

    #greate a buffer to store the coordinate
    guess_row_buffer = []
    guess_col_buffer = []

#1.This step is to create two ships in different coordinate

    random_num = [0,1,2,3,4]#if the coordinate bigger than 4, the battleship will not in the ocean


    import random

    ship1_coordinate_1 = random.sample(random_num, 2)  # random 4 no repeat numbers

    # 1. First battleship coordinate
    ship1_row1 = ship1_coordinate_1[0]
    ship1_col1 = ship1_coordinate_1[1]

    ship1_row2 = ship1_row1 + 1
    ship1_row3 = ship1_row1 + 2
    # the other two coordinate of ship1
    ship1_coordinate_2 = [ship1_row2, ship1_col1]
    ship1_coordinate_3 = [ship1_row3, ship1_col1]

    differ_num = True#if the differ_num is True, the coordinate will random in a circle
    while differ_num:
        ship2_coordinate_1 = random.sample(random_num, 2)
        # 2. Second battleship coordinate
        ship2_row1 = ship2_coordinate_1[0]
        ship2_col1 = ship2_coordinate_1[1]

        ship2_col2 = ship2_col1 + 1
        ship2_col3 = ship2_col1 + 2
        # the other two coordinate of ship2
        ship2_coordinate_2 = [ship2_row1, ship2_col2]
        ship2_coordinate_3 = [ship2_row1, ship2_col3]

        #check ships are not on the same position
        if ship1_coordinate_1 != ship2_coordinate_1 and ship1_coordinate_1 != ship2_coordinate_2 and \
                ship1_coordinate_1 != ship2_coordinate_3 and ship1_coordinate_2 != ship2_coordinate_1 and \
                ship1_coordinate_2 != ship2_coordinate_2 and ship1_coordinate_2 != ship2_coordinate_3 and \
                ship1_coordinate_3 != ship2_coordinate_1 and ship1_coordinate_3 != ship2_coordinate_2 and \
                ship1_coordinate_3 != ship2_coordinate_3:
            differ_num = False

#2.This step is to create an ocean(8*8)

    from random import randint

    board = []

    # Create a list whose elements are lists of five zeros
    for x in range(0, 8):
        board.append(["O"] * 8)


    # Convert lists into strings of zeros to represent the ocean
    def print_board(board):
        """ Creates a 8x8 grid of "O" """
        for row in board:
            print (" ".join(row))  # Convert list to string


    # Print the ocean
    print ("----------------")
    print ("The Ocean")
    print ("----------------")
    print_board(board)
    print ("----------------")

    #other two coordinate of battleship1(1*3)

    board [ship1_row1] [ship1_col1] = "B"
    board [ship1_row2] [ship1_col1] = "B"
    board [ship1_row3] [ship1_col1] = "B"

    #other two coordinate of battleship2(3*1)
    ship2_col2 = ship2_col1 + 1
    ship2_col3 = ship2_col1 + 2
    board [ship2_row1] [ship2_col1] = "B"
    board [ship2_row1] [ship2_col2] = "B"
    board [ship2_row1] [ship2_col3] = "B"


#3.This step is to enter the coordinate and check the answer


    guess_running=True
    while guess_num < guess_num_input:

        #check the input is a number or not
        guess_row_running = True
        while guess_row_running:
            guess_row = input('Guess Row(1~8): ')
            if int(str(guess_row))==0:
                print("Please enter an integer number!(1~8)")
            elif guess_row.isdigit():
                guess_row = int(guess_row) - 1
                guess_row_running = False


            else:
                print("Please enter an integer number!(1~8)")

        # check the input is a number or not
        guess_col_running = True
        while guess_col_running:
            guess_col = input('Guess Col(1~8): ')
            if int(str(guess_col))==0:
                print("Please enter an integer number!(1~8)")
            elif guess_col.isdigit():
                guess_col = int(guess_col) - 1
                guess_col_running = False

            else:
                print("Please enter an integer number!(1~8)")

        #(1)if the coordinate is not in the ocean
        if guess_row > 7 or guess_col > 7:
            print ("Oops, that's not even in the ocean.")
            print("Number of guesses so far: ", guess_num + 1, "\n")


        #(2)if the coordinate is already guessed
        if guess_row == guess_row_buffer and guess_col == guess_col_buffer:#check the coordinate
            print("You guessed that one already.")


        #(3)if the coordinate is in the ocean
        if guess_row>=0 and guess_row<=7 and guess_col>=0 and guess_col<=7:
            board [guess_row] [guess_col] = "G"

        #check the coordinate

            #(1)if the coordinate is right
            if ((guess_row == ship1_row1 and guess_col == ship1_col1) or
                (guess_row == ship1_row2 and guess_col == ship1_col1)or
                (guess_row == ship1_row3 and guess_col == ship1_col1)or
                (guess_row == ship2_row1 and guess_col == ship2_col1)or
                (guess_row == ship2_row1 and guess_col == ship2_col2)or
                (guess_row == ship2_row1 and guess_col == ship2_col3)):
                #compare the coordinate

                board[guess_row][guess_col] = "X"#the right coordinate is X


                print ("Congratulations! You sunk the battleship!")

                print ("----------------")
                print_board(board) #print the result of the game
                print("\nB-Battleship\nG-Guess coordinate\nX-Hit coordinate")
                print("\n*** Game Over ***")
                print("\nYour guesses number are:" + str(guess_num+1))
                print ("----------------")
                break
                guess_running=False#stop game running


            #(2)if the coordinate is wrong
            else:

                print("---------")
                print ("You missed the battleship!")
                guess_row_buffer = guess_row #renew the coordinate
                guess_col_buffer = guess_col


                print("Number of guesses so far: ", guess_num + 1, "\n")

                playagain_running = False#stop play again running,or the proj will go to next step

        guess_num+=1#renew the guess number

    #if the guess number > 4, game over
    else:
        print ("----------------")
        print_board(board)
        print("\nB-Battleship\nG-Guess coordinate")
        print("\n*** Game Over ***")
        print("\nYour guesses number are:" + str(guess_num))#the guess number already +1 in the front,no need +1 again
        print ("----------------")

#4.This step is to play again the game

    playagain_running = True
    while playagain_running:
        run_again = input("\nDo you want to play again (Y/N):")
        #(1)when input is "N" or "n"
        if run_again.upper() == "N":
            print("***Thanks for playing!***")
            #kill each running
            playagain_running = False
            running = False
            
            exit()# exit the program

        #(2)when input is "Y" or "y"
        elif run_again.upper() == "Y":
            guess_num = 0#renew the guess number
            playagain_running = False#stop playagain_runnning

        #(3)when input is neither "Y/y" or "N/n"
        else:
            print("You have entered an incorrect character! ")
            #playagain_running still running






