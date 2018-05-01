import board

def position_values(master_board, locations, comp_sym, play_sym):
    '''With all possible locations calculates using the min/max algorithm
    what the value of each move is at that particular location. The possible 
    values at each location are the following:
        +10     for a winning move
        +/-0    for a non changing move
        -10     for a losing move
    With these rules the min/max algorithm is implemented.
    '''
    copy_board = board.Board(master_board.get_arr())
    lst = []

    for i in locations:
        curr_val = None
        # Adds the location
        row = i[0]
        column = i[-1]

        # Replaces with the comp_sym
        copy_board.replace_element(comp_sym, row, column)
        # Calculates Value
        #print(copy_board)
        win_val = copy_board.check_win()
        if win_val == comp_sym:
            curr_val = -10
        elif win_val == play_sym:
            curr_val = 10
        else:
            curr_val = 0
        
        #Replaces with the ply_sym
        copy_board.remove_element(row, column)
        copy_board.replace_element(play_sym, row, column)

        win_val = copy_board.check_win()
        if win_val == comp_sym:
            curr_val = 10
        elif win_val == play_sym:
            curr_val = -10
        else:
            curr_val = 0
        # Records it
        #print(win_val)
        tup = (i, curr_val)
        lst.append(tup)
        # Reverses the location change
        copy_board.remove_element(row, column)
    return lst

def choose_best_position(pos_vals):
    lst = sorted(pos_vals, key=lambda x: x[1])
    return lst[0][0]
    
