import tkinter as TK

root = TK.Tk()
frm = TK.Frame(root)
frm.grid()
TK.Label(frm, text="Hello world!").grid(column=1, row=0)
btn = TK.Button(frm, text="Quit!", command=root.destroy).grid(column=2, row=1)
print(btn.configure().keys())
root.mainloop() 

https://docs.python.org/3/library/tkinter.html#tkinter.Tk