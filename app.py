import tkinter as TK
from tkinter import font

root = TK.Tk()
root.title("TicTacToe")

def b_click(btn):
    global clicked, count

clicked = True
count = 0


#Buttons
b1 = TK.Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
b2 = TK.Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
b3 = TK.Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
b4 = TK.Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = TK.Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = TK.Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
b7 = TK.Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = TK.Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = TK.Button(root, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)



frm = TK.Frame(root)
frm.grid()

root.mainloop() 

#https://docs.python.org/3/library/tkinter.html#tkinter.Tk