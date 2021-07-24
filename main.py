import sys, os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from core import analysis

def button1_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    load_path.insert(0,filepath)
    
def button2_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.asksaveasfilename(filetypes = fTyp,initialdir = iDir)
    save_path.delete(0)
    save_path.insert(0,filepath)
    

def clicked():
    load = load_path.get()
    save = save_path.get()
    analysis(load, save)
    result.configure(text='analysis is done')

root = Tk()

root.title("Task analysis")
root.geometry('450x200')

save_lbl = Label(root, text="enter LOAD csv path")
save_lbl.grid(row=0, column=0)

load_path = Entry(root,width=50)
load_path.grid(row=1, column=0)

button1 = ttk.Button(root, text='Browse', command=button1_clicked)
button1.grid(row=1, column=3)
    
load_lbl = Label(root, text="enter SAVE path")
load_lbl.grid(row=2, column=0)

save_path = Entry(root,width=50)
save_path.grid(row=3, column=0)

button1 = ttk.Button(root, text='Browse', command=button2_clicked)
button1.grid(row=3, column=3)

btn = Button(root, text="ANALYSIS", command=clicked)
btn.grid(row=4, column=0)

result = Message(root, text='Preparetion analysis', width = 150)
result.grid(row=5, column=0)

root.mainloop()