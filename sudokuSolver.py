N = 9 #declares variable that holds number of rows and columnsg

#function that checks if its fine to assign a number to a given row and column
def isSafe(sudoku, row, col, num): #takes these as arguments
    for i in range(9): #checks if same number exists in same row
        if sudoku[row][i] == num:
            return False 

    for i in range(9): #checks if same number exists in same column
        if sudoku[i][col] == num:
            return False
    #checks if number exists in specific 3x3 grid
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[startRow + i][startCol + j] == num:
                return False
    return True

#function which will assign values to all non-assigned locations
def solveSudoku(sudoku, row, col): #takes these as arguments
    if row == N-1 and col == N: #this condition will act as base condition because i will use recursion
        return True 
    #moves to next row when last column is reached
    if col == N: 
        row += 1
        col = 0

    #checks if a number is asssigned to current position
    if sudoku[row][col] > 0:
        return solveSudoku(sudoku, row, col+1)

    for num in range(1, N + 1): #checks for each number from 1 to 9
        #check if its ok to assign this number at given row & col using prev func i wrote
        if isSafe(sudoku, row, col, num): 
            sudoku[row][col] = num #assigns to sudoku it if its fine

            #assuming the num assinged is correct, it then checks possiblity in next column
            if solveSudoku(sudoku, row,col + 1): 
                return True
        #in the for loop code block it reassigns 0 at given position since the assumption was wrong & checks for next value
        sudoku[row][col] = 0
    return False


#function that returns solved sudoku if its solvable
def solver(sudoku):
    if solveSudoku(sudoku, 0, 0):
        return sudoku
    else:
        return "no"