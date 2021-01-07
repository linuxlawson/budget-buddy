#!/usr/bin/python
# Budget Buddy (GUI Version)
# Income/Expenses Program
# Written by David Lawson


try:
    import Tkinter as tk
except:
    import tkinter as tk
 

root = tk.Tk()
root.title("Budget Buddy")
root.geometry("508x714")
root.option_add("*Font", "TkDefaultFont 9")
root.config(bg='silver')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



#Main Frame
mainframe = tk.Frame(root, bd=0, highlightbackground="black", 
                    highlightcolor="black", 
                    highlightthickness=2, relief='flat')
mainframe.grid(sticky='n')


#labels
lab = tk.Label(mainframe, text="\nBudget Buddy")
lab.grid(row=0, column=0, sticky='nw', padx=12, pady=4)
lab1 = tk.Label(mainframe, text="Income and Expenses Program\n\n")
lab1.grid(row=1, column=0, sticky='nw', padx=12, pady=4)
lab2 = tk.Label(mainframe, text="Enter Income & Expenses", fg='#BA0F0F')
lab2.grid(row=2, column=0, sticky='nw', padx=12, pady=4)
lab3 = tk.Label(mainframe, text="Numbers Only", fg='#BA0F0F')
lab3.grid(row=2, column=1, sticky='nw', padx=8, pady=4)
stat = tk.Label(mainframe, text=" If None Enter 0\n", fg='#BA0F0F')
stat.grid(row=2, column=2,  sticky='new', padx=8, pady=4)


def getTotal():
    res = int(a1.get())+int(a2.get())+int(a3.get())+int(a4.get())+int(a5.get())+int(a6.get())+int(a7.get())+int(a8.get())+int(a9.get())
    myTotal.set(res)
myTotal=tk.StringVar();


def getRemains():
    rem = int(inca.get())-int(a10.get())
    myRemains.set(rem)
myRemains=tk.StringVar();


def new_Remains():
    new = int(a12.get())-int(a14.get())+int(a15.get())
    newRemains.set(new)
newRemains=tk.StringVar();


def banked():
    ban = tk.Label(mainframe, text="", fg="#B3B3B3")
    ban.grid(row=15, column=2, sticky='nw', padx=0, pady=4)
    ban = a14.get()


#income
incq = tk.Label(mainframe, text="Monthly Income:\n\n")
incq.grid(row=3, column=0,  sticky='nw', padx=12, pady=4)
inca = tk.Entry(mainframe, bd=1, width='8', justify='right', bg="#FFFF00")
inca.grid(row=3, column=1, sticky='nw', padx=8, pady=4)
income = inca.get()

#rent
q1 = tk.Label(mainframe, text="Rent:")
q1.grid(row=4, column=0,  sticky='nw', padx=28, pady=4)
a1 = tk.Entry(mainframe, bd=1, width='8', justify='right')
a1.grid(row=4, column=1, sticky='nw', padx=8, pady=4)
rent = a1.get()

#consumers
q2 = tk.Label(mainframe, text="Consumers:")
q2.grid(row=5, column=0,  sticky='nw', padx=28, pady=4)
a2 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a2.grid(row=5, column=1, sticky='nw', padx=8, pady=4)
con = a2.get()

#internet/tv
q3 = tk.Label(mainframe, text="Internet/TV:")
q3.grid(row=6, column=0,  sticky='nw', padx=28, pady=4)
a3 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a3.grid(row=6, column=1, sticky='nw', padx=8, pady=4)
cable = a3.get()

#car ins
q4 = tk.Label(mainframe, text="Car Insurance:")
q4.grid(row=7, column=0,  sticky='nw', padx=28, pady=4)
a4 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a4.grid(row=7, column=1, sticky='nw', padx=8, pady=4)
carins = a4.get()

#food
q5 = tk.Label(mainframe, text="Food/Groceries:")
q5.grid(row=8, column=0,  sticky='nw', padx=28, pady=4)
a5 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a5.grid(row=8, column=1, sticky='nw', padx=8, pady=4)
food = a5.get()

#gas
q6 = tk.Label(mainframe, text="Gas:")
q6.grid(row=9, column=0,  sticky='nw', padx=28, pady=4)
a6 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a6.grid(row=9, column=1, sticky='nw', padx=8, pady=4)
gas = a6.get()

#personal
q7 = tk.Label(mainframe, text="Personal Items:")
q7.grid(row=10, column=0,  sticky='nw', padx=28, pady=4)
a7 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a7.grid(row=10, column=1, sticky='nw', padx=8, pady=4)
person = a7.get()

#cell
q8 = tk.Label(mainframe, text="Cell Phone:")
q8.grid(row=11, column=0,  sticky='nw', padx=28, pady=4)
a8 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a8.grid(row=11, column=1, sticky='nw', padx=8, pady=4)
cell = a8.get()

#other
q9 = tk.Label(mainframe, text="Other expenses:\n\n")
q9.grid(row=12, column=0,  sticky='nw', padx=28, pady=4)
a9 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a9.grid(row=12, column=1, sticky='nw', padx=8, pady=4)
other = a9.get()


#total costs
q10 = tk.Label(mainframe, text="\t\tTotal Costs:")
q10.grid(row=13, column=0,  sticky='nw', padx=8, pady=4)
a10 = tk.Entry(mainframe, bd=1, width='8', justify='right', textvariable=myTotal)
a10.grid(row=13, column=1, sticky='nw', padx=8, pady=4)
a10.config(state='readonly')
total = a10.get()

#remains
q12 = tk.Label(mainframe, text="\t\tRemainder:\n\n")
q12.grid(row=14, column=0,  sticky='nw', padx=8, pady=4)
a12 = tk.Entry(mainframe, bd=1, width='8', justify='right', textvariable=myRemains)
a12.grid(row=14, column=1, sticky='nw', padx=8, pady=4)
a12.config(state='readonly')
remains = a12.get()


#intosavings
q14 = tk.Label(mainframe, text="How much into savings account?")
q14.grid(row=15, column=0,  sticky='nw', padx=12, pady=4)
a14 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a14.grid(row=15, column=1, sticky='nw', padx=8, pady=4)
savings = a14.get()

#additional
q15 = tk.Label(mainframe, text="List all additional earned income\n\n")
q15.grid(row=16, column=0,  sticky='nw', padx=12, pady=4)
a15 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a15.grid(row=16, column=1, sticky='nw', padx=8, pady=4)
addit = a15.get()


#new remainder
q16 = tk.Label(mainframe, text="\t\tNew Remainder:\n\n")
q16.grid(row=17, column=0,  sticky='nw', padx=8, pady=4)
a16 = tk.Entry(mainframe, bd=1, width='8', justify='right', textvariable=newRemains)
a16.grid(row=17, column=1, sticky='nw', padx=8, pady=4)
a16.config(state='readonly', bg='yellow')
newremains = a16.get()

spacer = tk.Label(mainframe, text="")
spacer.grid(row=18, column=0,  sticky='nw', padx=12, pady=4)


#buttons (column 2)
b1 = tk.Button(mainframe, text="Total Costs ", command=lambda: [getTotal(), getRemains()])
b1.grid(row=13, column=2, sticky='nw', padx=28, pady=2)

b2 = tk.Button(mainframe, text="Remainder ", command=lambda: [new_Remains(), banked()])
b2.grid(row=17, column=2, sticky='nw', padx=28, pady=2)




root.protocol("WM_DELETE_WINDOW")
root.mainloop()
