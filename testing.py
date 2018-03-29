
# Testing for calculations of ai
def calculate_position(arr):
    '''Calculates the best position to put a symbol'''
    cal_arr = [[],[],[]]
    for item in arr:
        if item in symbols:
            pass
        else:
            pass


def check_win(arr)->str:
    '''Checks if there is a win!'''
    # Checks for a horizontal win
    if arr[0][0] == arr[0][1] == arr[0][2] != '.' or \
        arr[1][0] == arr[1][1] == arr[1][2] != '.' or \
        arr[2][0] == arr[2][1] == arr[2][2] != '.' or \
        arr[0][0] == arr[1][0] == arr[2][0] != '.' or \
        arr[0][1] == arr[1][1] == arr[2][1] != '.' or \
        arr[0][2] == arr[1][2] == arr[2][2] != '.' or \
        arr[0][0] == arr[1][1] == arr[2][2] != '.' or \
        arr[0][2] == arr[1][1] == arr[2][0] != '.':
            return True
    else:
        return False        
    

print(check_win([["X", ".", "."], [".", "X", "."], [".", ".", "X"]]))