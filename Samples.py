import yaml
from tkinter import *
from tkinter.ttk import Combobox

rows = []
root = Tk()
root.title('Samples Creator')
for i in range(5):
       cols = []
       for j in range(4):
           e = Entry(relief=RIDGE)
           e.grid(row=i, column=j, sticky=NSEW)
           e.insert(END, '%d.%d' % (i, j))
           cols.append(e)
       rows.append(cols)

def onPress():
       for row in rows:
           for col in row:
               print (col.get()),
           print

Button(text='Create', command=onPress).grid()
root.mainloop()
