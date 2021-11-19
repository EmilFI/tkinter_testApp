import tkinter as TK
from tkinter import Button, Tk, font

root = TK.Tk()
root.title("TicTacToe")

squares = []

def b_click(btn):
    squares[btn].click(1)

class square():
    def __init__(self, i):
        self.textvar = TK.StringVar()
        self.button = TK.Button(root, textvariable=self.textvar, font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(i))
        self.clicked = 0
    def click(self, clicker):
        self.clicked = clicker
        self.textvar.set("X" if clicker == 1 else "O")



for i in range(9):
    squares.append(square(i))

column_num = 0
row = 0

for square in squares:
    if column_num > 2:
        row += 1
        column_num = 0
    square.button.grid(row = row, column = column_num)
    column_num += 1

frm = TK.Frame(root)
frm.grid()

root.mainloop() 

#https://docs.python.org/3/library/tkinter.html#tkinter.Tk