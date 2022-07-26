# import tkinter as tk
# from tkinter import ttk

# app = tk.Tk()

# a = tk.IntVar()
# e = ttk.Entry(app, width=7, textvariable=a)
# e.grid(column=0, row=0)
# def f():
#     eg = a.get()
#     print(eg)
#     print(type(eg))
    
#     if eg in [1,2,3,4,5,6,7,8,9,0]:
#         print('성공')
# b = ttk.Button(app,  width=10, text='a', command=f)
# b.grid(column=1, row=0)


# app.mainloop()
import tkinter as tk
from tkinter import ttk

app = tk.Tk()

at = tk.StringVar()
a = ttk.Entry(app, width = 10, textvariable=at)
a.grid(column=0, row=0)

def b_function():
    atg = at.get()
    print(atg, type(atg))
    atg = tuple(atg)
    print(atg, type(atg))

b = ttk.Button(app, text="button", command=b_function)
b.grid(column=1, row=0)

app.mainloop()