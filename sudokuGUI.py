from tkinter import *
from sudokuSolver import solver

root = Tk()
root.title("Sudoku Solver")
root.geometry("400x550")


label = Label(root, text="Fill the numbers and click solve!").grid(row=0, column=1, columnspan=10)

errLabel = Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5) #error label if sudoku isnt solvable 

solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5) #solved label when sudoku successfully gets solved

cells={} #empty dictionary

#define a validation function which controls what is being entered into the cells
def validateNumber(P): #takes value of the cell as an argument
    out = (P.isdigit() or P == "") and len(P) < 2 #checks if its a digit or empty and restricts to one digit
    return out #return the boolean expression

reg = root.register(validateNumber) #register the function to the window

def draw3x3Grid(row, column, bgcolor): #takes those 3 as arguments
    for i in range(3): #indicates the rows
        for j in range(3): #indicates the columns
           e = Entry(root, width=3, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P")) 
           e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
           cells[(row+i+1, column+j+1)] = e

def draw9x9Grid():
    color = "#152238"
    for rowNo in range(1, 10, 3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo, colNo, color)
            if color == "#152238":
                color = "#253DA1"
            else:
                color = "#152238"

def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row, col)]
            cell.delete(0, "end")

def getValues():
    board = [] #declare empty list to store value of each cell in each row
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        rows = []
        for col in range(1,10):     
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)

btn = Button(root, command=getValues, text="Solve", width=10)
btn.grid(row=20, column=1, columnspan=5, pady=20)    

btn = Button(root, command=clearValues, text="Clear", width=10)
btn.grid(row=20, column=5, columnspan=5, pady=20)  

#function updates cells and displays solution
def updateValues(s): #takes sudoku matrix as arguments
    sol = solver(s) #calls solver function and pass the sudoku to it
    if sol != "no":
        for rows in range(2, 11):
            for col in range(1,10):
                cells[(rows, col)].delete(0, "end") #deletes existing values from cell
                #insert method to insert value at 0 index. Subtracting 2 and 1 because the matrix is 0 indexed
                cells[(rows, col)].insert(0, sol[rows-2][col-1]) 
        solvedLabel.config(text="Sudoku solved!")
    else:
        errLabel.config(text="No solution exists for this sudoku")

draw9x9Grid()
root.mainloop() 
