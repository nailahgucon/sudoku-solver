# import libraries
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('490x610')
messagebox.showinfo("Sudoku Solver","Welcome to Sudoku Solver!\n\n" +
                    "Instructions before use:\n1. Add numbers already present in puzzle in its respective gridbox.\n" + 
                    "(Note:  If you are unable to select grid box, click outside the GUI first (your desktop, etc), then try again)\n" +
                    "2. Click the Solve button at the bottom.\n" + 
                    "3. If you have >1 puzzle, click the Clear button at the bottom then repeat Step 1 & 2. Else, done.\n\n" +
                    "Happy Solving! :)")  
  
# Sudoku solver class
class SudokuSolver():

    def __init__(self):
        self.setZero()
        self.solve()
        
    # Set the empty cells to 0 (i.e. the cells you have not filled in)
    def setZero(self):
        for i in range(9):
            for j in range(9):
                if filledBoard[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    filledBoard[i][j].set(0)

    # backtracking algo
    def solve(self):
        # Find next empty cell
        findEmpty = self.emptyCell()
        
        if not findEmpty:
            return True   
        else:
            row, column = findEmpty
        
        for i in range(1,10):
            if self.isValid(i, (row, column)):
                filledBoard[row][column].set(i)

                if self.solve():
                    return True

                filledBoard[row][column].set(0)
        
        return False

    # Check if number can be placed in cell          
    def isValid (self, num, pos):
        # Check Row
        for i in range(9):
            if filledBoard[pos[0]][i].get() == str(num):
                return False
        # Check Column 
        for i in range(9):
            if filledBoard[i][pos[1]].get() == str(num):
                return False

        # Check Sub Grid
        row = pos[0] // 3 
        column = pos[1] // 3 

        for i in range(row * 3, (row * 3) + 3):
            for j in range(column * 3, (column * 3) + 3):
                if filledBoard[i][j].get() == str(num):
                    return False 
        return True

    # Find empty cells, defined as cells filled with a zero
    def emptyCell(self):
        for row in range(9):
            for column in range(9):
                if filledBoard[row][column].get() == '0':
                    return row,column
        return None

# GUI class
class Interface():
    def __init__(self, window):
        self.window = window
        window.title("Sudoku Solver")

        font = ('Calibri', 35)
        color = 'black'

        # Create solve and clear button and link them to Solve and Clear methods
        solve = Button(window, text = 'Solve', command = self.Solve)
        solve.grid(column=3,row=20)
        clear = Button(window, text = 'Clear', command = self.Clear)
        clear.grid(column = 5,row=20)


        self.board  = []
        for row in range(9):
            self.board += [["","","","","","","","",""]]

        for row in range(9):
            for col in range(9):
                # Change color of cells depending on position in grid
                # see better
                if (row < 3 or row > 5) and (col < 3 or col > 5):
                    color = 'white' 
                elif (row >= 3 and row < 6) and (col >=3 and col < 6):
                    color = 'white'
                else:
                    color = 'light grey'
                
                # Make each cell of grid a entry box and store each user entry into the filledBoard 2D list
                self.board[row][col] = Entry(window, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 2,
                                          highlightbackground = 'black', textvariable = filledBoard[row][col]) 
                self.board[row][col].bind('<FocusIn>', self.gridChecker) 
                self.board[row][col].bind('<Motion>', self.gridChecker)                        
                self.board[row][col].grid(row = row, column = col)

    # Function to check if user enters a value which is not an int between 1 and 9
    # If entry not valid -> clear value
    def gridChecker(self, event):
        for row in range(9):
            for col in range(9):
                if filledBoard[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
                    filledBoard[row][col].set('')

    # Call Sudoku solver class
    def Solve(self):
        SudokuSolver()

    # Function to clear board
    def Clear(self):
        for row in range(9):
            for col in range(9):
                filledBoard[row][col].set('')

filledBoard = []
for row in range(9): 
    filledBoard += [["","","","","","","","",""]]
for row in range(9):
    for col in range(9):
        filledBoard[row][col] = StringVar(root)    

Interface(root)
root.mainloop()



