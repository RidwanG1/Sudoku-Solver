from tkinter import *

root = Tk()
root.title("Sudoku Solver")
root.geometry("324x550")

label = Label(root, text="Fill the numbers anc click solve").grid(row=0, column=1, columnspan=10)

errLabel = Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5) #error label if sudoku isnt solvable 

solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5) #solved label when sudoku successfully gets solved

cells={} #empty dictionary

#define a validation function which controls what is being entered into the cells
def validateNumber(P): #takes value of the cell as an argument
    out = (P.isdigit() or P == "") and len(P) < 2 #checks if its a digit or empty and restricts to one digit
    return out #return the boolean expression

