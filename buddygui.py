#!/usr/bin/python
#Budget Buddy (GUI Version)
#A Money Management Tool
#Written by David Lawson


try:
    import Tkinter as tk
except:
    import tkinter as tk
 

root = tk.Tk()
root.title("Budget Buddy")
root.geometry("510x710")
root.option_add("*Font", "TkDefaultFont 9")
root.config(bg='silver')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


#Main Frame
mainframe = tk.Frame(root, highlightcolor="#4D4D4D", 
                    highlightbackground="#1A1A1A", 
                    highlightthickness=1, 
                    relief='flat')
mainframe.grid(sticky='n')


#labels
lab = tk.Label(mainframe, text="\nBudget Buddy", font='Arial 10 bold')
lab.grid(row=0, column=0, sticky='nw', padx=12, pady=4)
lab1 = tk.Label(mainframe, text="A Money Management Tool\n\n")
lab1.grid(row=1, column=0, sticky='nw', padx=12, pady=4)
lab2 = tk.Label(mainframe, text="Enter Income & Expenses", fg='#BA0F0F')
lab2.grid(row=2, column=0, sticky='nw', padx=12, pady=4)
lab3 = tk.Label(mainframe, text="Numbers Only", fg='#BA0F0F')
lab3.grid(row=2, column=1, sticky='nw', padx=8, pady=4)
stat = tk.Label(mainframe, text=" If None Enter 0", fg='#BA0F0F')
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


def clear():
	inca.delete('0', 'end')
	a1.delete('0', 'end')
	a2.delete('0', 'end')
	a3.delete('0', 'end')
	a4.delete('0', 'end')
	a5.delete('0', 'end')
	a6.delete('0', 'end')
	a7.delete('0', 'end')
	a8.delete('0', 'end')
	a9.delete('0', 'end')
	a10.delete('0', 'end')
	a12.delete('0', 'end')
	a14.delete('0', 'end')
	a15.delete('0', 'end')
	a16.delete('0', 'end')


def clear_fields():
    myTotal.set("")
    myRemains.set("")
    newRemains.set("")


#file menu
def exit_com(event=None):
    win = tk.Toplevel()
    win.title("Exit")
    xit = tk.Label(win, text="\n\nAre you sure you want to exit?\n")
    xit.pack()
    ex = tk.Button(win, text="Exit", width=4, command=root.destroy)
    ex.pack(side='left', padx=28, pady=4)
    ex.focus_set()
    ex.bind("<Return>", (lambda event: root.destroy()))
    can = tk.Button(win, text="Cancel", width=4, command=win.destroy)
    can.pack(side='right', padx=28, pady=4)
    win.transient(root)
    win.geometry('240x120')
    win.wait_window()
    

#help menu
def about_com(event=None):
    win = tk.Toplevel()
    win.title("About")
    bout = tk.Label(win, text="""\n\nBudget Buddy
    \nA Money Management Tool
    \nCalculates Income & Expenses
    \n\nMade in Python\n\n""")
    bout.pack()
    clo = tk.Button(win, text="Close", width=4, command=win.destroy)
    clo.pack(padx=8, pady=4)
    win.transient(root)
    win.geometry('300x220+638+298')
    win.wait_window()


def trouble_com(event=None):
    win = tk.Toplevel()
    win.title("Troubleshooting")
    trouble = tk.Label(win, justify='left', text="""\n\n
This program will give a rough estimate of 
how much you spend on a monthly basis.

All entry fields must contain a number
in order for program to work properly.

Whole Numbers Only. If none, enter zero (0)\n

Click on 'Total Costs' when you get there.
This will get the Total Costs for the month,
and the Remainder of your Monthly Income.

Fill in the next two fields (if zero, enter 0)
this will show New Remainder of income.
\n\n""")
    trouble.pack()
    cls = tk.Button(win, text="Close", command=win.destroy)
    cls.pack()
    win.transient(root)
    win.geometry('354x350+612+230')
    win.wait_window()



#income
incq = tk.Label(mainframe, text="Monthly Income:\n\n")
incq.grid(row=3, column=0,  sticky='nw', padx=12, pady=4)
inca = tk.Entry(mainframe, bd=1, width='8', justify='right')
inca.grid(row=3, column=1, sticky='nw', padx=8, pady=4)
income = inca.get()
inca.focus_set()

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
q15 = tk.Label(mainframe, text="List all additional earned income:\n\n")
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
spacer.grid(row=18, column=3,  sticky='nw', padx=12, pady=8)


#buttons (column 2)
b1 = tk.Button(mainframe, text="Total Costs ", command=lambda: [getTotal(), getRemains()])
b1.grid(row=13, column=2, sticky='nw', padx=28, pady=2)

b2 = tk.Button(mainframe, text="Remainder ", command=new_Remains)
b2.grid(row=17, column=2, sticky='nw', padx=28, pady=2)



#Menubar
menu = tk.Menu(root, bd=1, relief='flat')
root.config(menu=menu, bd=2)

#Filemenu
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File ", menu=filemenu)
filemenu.add_command(label="Clear Fields", 
                    command=lambda: [clear(), clear_fields()],
                    accelerator="".rjust(2))
filemenu.add_command(label="Exit", 
                    command=exit_com, underline=1,
                    accelerator="Ctrl+Q".rjust(2))                   


#Helpmenu
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help ", menu=helpmenu)
helpmenu.add_command(label="About", command=about_com)
helpmenu.add_command(label="Troubleshooting", command=trouble_com)

root.bind_all('<Control-q>', exit_com)


root.protocol("WM_DELETE_WINDOW")
root.mainloop()
