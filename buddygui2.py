#!/usr/bin/python
#Budget Buddy (GUI Version)
#A Money Management Tool


try:
    import Tkinter as tk
    import tkFileDialog
except:
    import tkinter as tk
    import tkinter.filedialog as tkFileDialog


root = tk.Tk()
root.title("Budget Buddy")
root.geometry("500x663")
root.option_add("*Font", "TkDefaultFont 9")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(0,0)


#Main Frame
mainframe = tk.Frame(root, highlightcolor="#4D4D4D",
                    highlightbackground="#4D4D4D",
                    highlightthickness=1,
                    relief='flat')
mainframe.grid(sticky='n')


#labels
lab = tk.Label(mainframe, text="Budget Buddy", font='Arial 10 bold')
lab.grid(row=0, column=0, sticky='nw', padx=12, pady=6)
lab1 = tk.Label(mainframe, text="A Money Management Tool\n")
lab1.grid(row=1, column=0, sticky='nw', padx=12, pady=4)

#month
mon = tk.Label(mainframe, text="Month: \n")
mon.grid(row=2, column=0,  sticky='nw', padx=12, pady=4)
mon = tk.Entry(mainframe, bd=1, width='11', justify='left')
mon.grid(row=2, column=0, sticky='n', padx=2, pady=4)
mon.focus_set()

lab2 = tk.Label(mainframe, text="Enter Income & Expenses", fg='#008000')
lab2.grid(row=3, column=0, sticky='nw', padx=12, pady=4)
lab3 = tk.Label(mainframe, text="Numbers Only", fg='#008000')
lab3.grid(row=3, column=1, sticky='nw', padx=6, pady=4)
stat = tk.Label(mainframe, text="If None Enter 0", fg='#008000')
stat.grid(row=3, column=2,  sticky='new', padx=6, pady=4)


#functions
def getTotal():
    res = (int(a1.get())+int(a2.get())+int(a3.get())
    +int(a4.get())+int(a5.get())+int(a6.get())
    +int(a7.get())+int(a8.get())+int(a9.get())
    +int(a10.get())+int(a11.get())+int(a12.get())
    +int(a13.get())+int(a14.get()))
    myTotal.set(res)
myTotal=tk.StringVar();


def getRemains():
    rem = int(inca.get())-int(a15.get())
    myRemains.set(rem)
myRemains=tk.StringVar();



def clear_fields(event=None):
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
	a11.delete('0', 'end')
	a12.delete('0', 'end')
	a13.delete('0', 'end')
	a14.delete('0', 'end')
	myTotal.set("")
	myRemains.set("")
	inca.focus_set()



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



def save_com(event=None):
    file = tkFileDialog.asksaveasfile(mode='w', defaultextension='.txt',
    filetypes = (("Text Files", "*.txt"),("All Files", "*.*")))
    if file:
        file.write("\n")
        file.write("\tBudget Buddy Results     " + "\n\n")

        file.write("\tMonth: " + (mon.get()) + "\n\n\n")

        file.write("\tMonthly Income:      " + (inca.get().rjust(4)) + "\n\n")
        file.write("\t  Rent/Mortgage:     " + (a1.get().rjust(4)) + "\n")
        file.write("\t  Utilities:         " + (a2.get().rjust(4)) + "\n")
        file.write("\t  Internet/TV:       " + (a3.get().rjust(4)) + "\n")
        file.write("\t  Car Insurance:     " + (a4.get().rjust(4)) + "\n")
        file.write("\t  Car Payment:       " + (a5.get().rjust(4)) + "\n")
        file.write("\t  Home Insurance:    " + (a6.get().rjust(4)) + "\n")
        file.write("\t  Health Insurance:  " + (a7.get().rjust(4)) + "\n")
        file.write("\t  Water/Sewer:       " + (a8.get().rjust(4)) + "\n")
        file.write("\t  Food/Groceries:    " + (a9.get().rjust(4)) + "\n")
        file.write("\t  Gas/Fuel:          " + (a10.get().rjust(4)) + "\n")
        file.write("\t  Phone:             " + (a11.get().rjust(4)) + "\n")
        file.write("\t  Personal Items:    " + (a12.get().rjust(4)) + "\n")
        file.write("\t  Entertainment:     " + (a13.get().rjust(4)) + "\n")
        file.write("\t  Other:             " + (a14.get().rjust(4)) + "\n\n")

        file.write("\t      Total Costs:   " + (a15.get().rjust(4)) + "\n")
        file.write("\t      Remainder:     " + (a16.get().rjust(4)) + "\n\n")
        file.close()


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


#Labels/Entry Fields
# q = question/label
# a = answer/entry

#monthly income
incq = tk.Label(mainframe, text="Monthly Income:\n")
incq.grid(row=4, column=0,  sticky='nw', padx=12, pady=4)
inca = tk.Entry(mainframe, bd=1, width='8', justify='right')
inca.grid(row=4, column=1, sticky='nw', padx=8, pady=4)

#rent/mortgage
q1 = tk.Label(mainframe, text="Rent/Mortgage:")
q1.grid(row=5, column=0,  sticky='nw', padx=28, pady=3)
a1 = tk.Entry(mainframe, bd=1, width='8', justify='right')
a1.grid(row=5, column=1, sticky='nw', padx=8, pady=3)

#utilities
q2 = tk.Label(mainframe, text="Utilities:")
q2.grid(row=6, column=0,  sticky='nw', padx=28, pady=3)
a2 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a2.grid(row=6, column=1, sticky='nw', padx=8, pady=3)

#internet/tv
q3 = tk.Label(mainframe, text="Internet/TV:")
q3.grid(row=7, column=0,  sticky='nw', padx=28, pady=3)
a3 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a3.grid(row=7, column=1, sticky='nw', padx=8, pady=3)

#car ins
q4 = tk.Label(mainframe, text="Car Insurance:")
q4.grid(row=8, column=0,  sticky='nw', padx=28, pady=3)
a4 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a4.grid(row=8, column=1, sticky='nw', padx=8, pady=3)

#car payment
q5 = tk.Label(mainframe, text="Car Payment:")
q5.grid(row=9, column=0,  sticky='nw', padx=28, pady=3)
a5 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a5.grid(row=9, column=1, sticky='nw', padx=8, pady=3)

#home ins
q6 = tk.Label(mainframe, text="Home Insurance:")
q6.grid(row=10, column=0,  sticky='nw', padx=28, pady=3)
a6 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a6.grid(row=10, column=1, sticky='nw', padx=8, pady=3)

#health ins
q7 = tk.Label(mainframe, text="Health Insurance:")
q7.grid(row=11, column=0,  sticky='nw', padx=28, pady=3)
a7 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a7.grid(row=11, column=1, sticky='nw', padx=8, pady=3)

#water/sewer
q8 = tk.Label(mainframe, text="Water/Sewer:")
q8.grid(row=12, column=0,  sticky='nw', padx=28, pady=3)
a8 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a8.grid(row=12, column=1, sticky='nw', padx=8, pady=3)

#food/groceries
q9 = tk.Label(mainframe, text="Food/Groceries:")
q9.grid(row=13, column=0,  sticky='nw', padx=28, pady=3)
a9 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a9.grid(row=13, column=1, sticky='nw', padx=8, pady=3)

#gas/fuel
q10 = tk.Label(mainframe, text="Gas/Fuel:")
q10.grid(row=14, column=0,  sticky='nw', padx=28, pady=3)
a10 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a10.grid(row=14, column=1, sticky='nw', padx=8, pady=3)

#phone
q11 = tk.Label(mainframe, text="Phone:")
q11.grid(row=15, column=0,  sticky='nw', padx=28, pady=3)
a11 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a11.grid(row=15, column=1, sticky='nw', padx=8, pady=3)

#personal
q12 = tk.Label(mainframe, text="Personal Items:")
q12.grid(row=16, column=0,  sticky='nw', padx=28, pady=3)
a12 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a12.grid(row=16, column=1, sticky='nw', padx=8, pady=3)

#entertainment
q13 = tk.Label(mainframe, text="Entertainment:")
q13.grid(row=17, column=0,  sticky='nw', padx=28, pady=3)
a13 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a13.grid(row=17, column=1, sticky='nw', padx=8, pady=3)
person = a13.get()

#other
q14 = tk.Label(mainframe, text="Other:\n")
q14.grid(row=18, column=0,  sticky='nw', padx=28, pady=3)
a14 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a14.grid(row=18, column=1, sticky='nw', padx=8, pady=3)


#total costs
q15 = tk.Label(mainframe, text="\t\tTotal Costs:")
q15.grid(row=19, column=0,  sticky='nw', padx=8, pady=4)
a15 = tk.Entry(mainframe, bd=1, width='8', justify='right', 
				textvariable=myTotal)
a15.grid(row=19, column=1, sticky='nw', padx=8, pady=4)
a15.config(state='readonly')

#remainder
q16 = tk.Label(mainframe, text="\t\tRemainder:\n")
q16.grid(row=20, column=0,  sticky='nw', padx=8, pady=4)
a16 = tk.Entry(mainframe, bd=1, width='8', justify='right', 
				textvariable=myRemains)
a16.grid(row=20, column=1, sticky='nw', padx=8, pady=4)
a16.config(state='readonly')



#buttons (column 2)
b1 = tk.Button(mainframe, text="Total Costs ", 
				command=lambda: [getTotal(), getRemains()])
b1.grid(row=19, column=2, sticky='nw', padx=26, pady=0)

b2 = tk.Button(mainframe, text="Clear Fields", command=clear_fields)
b2.grid(row=5, column=2, sticky='nw', padx=26, pady=0)


#empty space at bottom
spacer = tk.Label(mainframe)
spacer.grid(row=21, column=3,  sticky='nw', padx=12, pady=8)



#Menubar
menu = tk.Menu(root, bd=1, relief='flat')
root.config(menu=menu, bd=2)

#Filemenu
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File ", menu=filemenu)
filemenu.add_command(label="Clear Fields",
                    command=clear_fields,
                    accelerator="Ctrl+C ".rjust(8))
filemenu.add_command(label="Save As",
                    command=save_com,
                    accelerator="Ctrl+S ".rjust(8))
filemenu.add_command(label="Exit",
                    command=exit_com, underline=1,
                    accelerator="Ctrl+Q ".rjust(8))

#Helpmenu
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help ", menu=helpmenu)
helpmenu.add_command(label="About", command=about_com)
helpmenu.add_command(label="Troubleshooting", command=trouble_com)


#bindings
root.bind_all('<Control-c>', clear_fields)
root.bind_all('<Control-s>', save_com)
root.bind_all('<Control-q>', exit_com)

root.protocol("WM_DELETE_WINDOW")
root.mainloop()
