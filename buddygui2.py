#!/usr/bin/env python3
#Budget Buddy 2 (GUI Version)
#A Money Management Tool

import tkinter as tk
import tkinter.filedialog as tkFileDialog


root = tk.Tk()
root.title("Budget Buddy")
root.geometry("500x663")
root.option_add("*Font", "TkDefaultFont 9")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#root.resizable(0,0)


#Main Frame
mainframe = tk.Frame(root, highlightcolor="#4D4D4D",
                    highlightbackground="#4D4D4D",
                    highlightthickness=1,
                    relief='flat')
mainframe.grid(sticky='n')


#labels
lab = tk.Label(mainframe, text="Budget Buddy", font='Arial 10 bold')
lab.grid(column=0, row=0, padx=12, pady=6, sticky='nw')
lab1 = tk.Label(mainframe, text="A Money Management Tool\n")
lab1.grid(column=0, row=1, padx=12, pady=4, sticky='nw')

#month
mon = tk.Label(mainframe, text="Month: \n")
mon.grid(column=0, row=2, padx=12, pady=4, sticky='nw')
mon = tk.Entry(mainframe, bd=1, width='11', justify='left')
mon.grid(column=0, row=2, padx=2, pady=4, sticky='n')
mon.focus_set()

lab2 = tk.Label(mainframe, text="Enter Income & Expenses", fg='#008000')
lab2.grid(column=0, row=3, padx=12, pady=4, sticky='nw')
lab3 = tk.Label(mainframe, text="Numbers Only", fg='#008000')
lab3.grid(column=1, row=3, padx=6, pady=4, sticky='nw')
stat = tk.Label(mainframe, text="If None Enter 0", fg='#008000')
stat.grid(column=2, row=3, padx=6, pady=4, sticky='new')


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
incq.grid( column=0, row=4, padx=12, pady=4, sticky='nw')
inca = tk.Entry(mainframe, bd=1, width='8', justify='right')
inca.grid(column=1, row=4, padx=8, pady=4, sticky='nw')

#rent/mortgage
q1 = tk.Label(mainframe, text="Rent/Mortgage:")
q1.grid(column=0, row=5, padx=28, pady=3, sticky='nw')
a1 = tk.Entry(mainframe, bd=1, width='8', justify='right')
a1.grid(column=1, row=5, padx=8, pady=3, sticky='nw')

#utilities
q2 = tk.Label(mainframe, text="Utilities:")
q2.grid(column=0, row=6, padx=28, pady=3, sticky='nw')
a2 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a2.grid(column=1, row=6, padx=8, pady=3, sticky='nw')

#internet/tv
q3 = tk.Label(mainframe, text="Internet/TV:")
q3.grid(column=0, row=7, padx=28, pady=3, sticky='nw')
a3 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a3.grid(column=1, row=7, padx=8, pady=3, sticky='nw')

#car ins
q4 = tk.Label(mainframe, text="Car Insurance:")
q4.grid(column=0, row=8, padx=28, pady=3, sticky='nw')
a4 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a4.grid(column=1, row=8, padx=8, pady=3, sticky='nw')

#car payment
q5 = tk.Label(mainframe, text="Car Payment:")
q5.grid(column=0, row=9, padx=28, pady=3, sticky='nw')
a5 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a5.grid(column=1, row=9, padx=8, pady=3, sticky='nw')

#home ins
q6 = tk.Label(mainframe, text="Home Insurance:")
q6.grid(column=0, row=10, padx=28, pady=3, sticky='nw')
a6 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a6.grid(column=1, row=10, padx=8, pady=3, sticky='nw')

#health ins
q7 = tk.Label(mainframe, text="Health Insurance:")
q7.grid(column=0, row=11, padx=28, pady=3, sticky='nw')
a7 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a7.grid(column=1, row=11, padx=8, pady=3, sticky='nw')

#water/sewer
q8 = tk.Label(mainframe, text="Water/Sewer:")
q8.grid(column=0, row=12, padx=28, pady=3, sticky='nw')
a8 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a8.grid(column=1, row=12, padx=8, pady=3, sticky='nw')

#food/groceries
q9 = tk.Label(mainframe, text="Food/Groceries:")
q9.grid(column=0, row=13, padx=28, pady=3, sticky='nw')
a9 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a9.grid(column=1, row=13, padx=8, pady=3, sticky='nw')

#gas/fuel
q10 = tk.Label(mainframe, text="Gas/Fuel:")
q10.grid(column=0, row=14, padx=28, pady=3, sticky='nw')
a10 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a10.grid(column=1, row=14, padx=8, pady=3, sticky='nw')

#phone
q11 = tk.Label(mainframe, text="Phone:")
q11.grid(column=0, row=15, padx=28, pady=3, sticky='nw')
a11 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a11.grid(column=1, row=15, padx=8, pady=3, sticky='nw')

#personal
q12 = tk.Label(mainframe, text="Personal Items:")
q12.grid(column=0, row=16, padx=28, pady=3, sticky='nw')
a12 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a12.grid(column=1, row=16, padx=8, pady=3, sticky='nw')

#entertainment
q13 = tk.Label(mainframe, text="Entertainment:")
q13.grid(column=0, row=17, padx=28, pady=3, sticky='nw')
a13 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a13.grid(column=1, row=17, padx=8, pady=3, sticky='nw')
person = a13.get()

#other
q14 = tk.Label(mainframe, text="Other:\n")
q14.grid(column=0, row=18, padx=28, pady=3, sticky='nw')
a14 = tk.Entry(mainframe, bd=1,  width='8', justify='right')
a14.grid(column=1, row=18, padx=8, pady=3, sticky='nw')


#total costs
q15 = tk.Label(mainframe, text="\t\tTotal Costs:")
q15.grid(column=0, row=19, padx=8, pady=4, sticky='nw')
a15 = tk.Entry(mainframe, bd=1, width='8', justify='right', 
				textvariable=myTotal)
a15.grid(column=1, row=19, padx=8, pady=4, sticky='nw')
a15.config(state='readonly')

#remainder
q16 = tk.Label(mainframe, text="\t\tRemainder:\n")
q16.grid(column=0, row=20, padx=8, pady=4, sticky='nw')
a16 = tk.Entry(mainframe, bd=1, width='8', justify='right', 
				textvariable=myRemains)
a16.grid(column=1, row=20, padx=8, pady=4, sticky='nw')
a16.config(state='readonly')



#buttons (column 2)
b1 = tk.Button(mainframe, text="Total Costs ", 
				command=lambda: [getTotal(), getRemains()])
b1.grid(column=2, row=19, padx=26, pady=0, sticky='nw')

b2 = tk.Button(mainframe, text="Clear Fields", command=clear_fields)
b2.grid(column=2, row=5, padx=26, pady=0, sticky='nw')


#empty space at bottom
spacer = tk.Label(mainframe)
spacer.grid(column=3, row=21, padx=12, pady=8, sticky='nw')



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
