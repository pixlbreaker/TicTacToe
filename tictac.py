# Problem with the Player symbol
import board
import minmax

empty = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
symbols = ['O', 'X']
playersym = None

def game_start():
    '''Starts the game with either a single player option, a duos play or lets 
    the player quit.'''

    # 1 - Solo Play
    # 2 - Duos Play
    print("Hello and welcome to pretty bad tic tac toe!")
    selection = int(input("Please choose an option from the following:\n\t(1) - Solo Play\n\t(2) - Quit\n"))
    playersym = symbols[int(input("Would you rather be 'O' or 'X' (choose 0 for O and 1 for X)\n"))]
    
    master_board = board.Board(empty)

    if selection == 1:
        play(master_board, playersym)
    else:
        print("Thanks for Playing!, See you sometime... I guess")


def random_palcement(arr):
    '''This places a random spot on the board'''
    return None

def play(b, player,):
    '''The Main Play function, that asks for input from the user.'''

    if player == "X": 
        compsym = 'O'
    else:
        compsym = 'X'
    winner = False
    # Runs through the loop if the player has not won
    while winner not in symbols or b.board_is_full():

        print(b)
        try:
            # Asks the user for input
            user_input_x = input("Enter a row ")
            user_input_y = input("Enter a column ")
            
            if user_input_x == 'q' or user_input_y == 'q':
                winner = True
                break
            # Replaces the element
            if not b.board_is_full():
                b.replace_element(player, int(user_input_x), int(user_input_y))
        except ValueError:
            print('Invalid input, please retry!')
        except IndexError:
            print('Invalid index, please enter a valid one!')
        finally:
            # Print Statement
            print("\nPlaced an " + player + " at (" + str(user_input_x) + ", " + str(user_input_y) + ")")

        # if not b.board_is_full():
        #     b.random_placement(compsym)
        if not b.board_is_full():
            pos_vales = minmax.position_values(b, b.find_empty_spots(), compsym, player)
            best_location = minmax.choose_best_position(pos_vales)
            b.replace_element(compsym, best_location[0], best_location[1])
        print(b.board_is_full())
        if b.board_is_full():
            break
        winner = b.check_win()

    print(b)
    print("Congradulations to", winner)
    print('Thank you for playing!')

if __name__ == "__main__":    
    # Starts the Game
    game_start()
