from Tkinter import *
from tkMessageBox import *
import subprocess

root = Tk()
menu = Menu(root)
#SPACE
w = Label(root, text="",font=(20))
w.pack()
w.grid(row=1, column=3)
sp = Label(root, text="")
sp.pack()
sp.grid(row=0, column=1)

#Methods to execute the scripts already created
def DisplayName():   
    try:
        subprocess.call("DisplayNames.py", shell=True)
    except:
        msguser = showinfo("warning", "error")
def CreateTabletbcustomeraccount(): 
    try:
        subprocess.call("CreateTable_tb_customer_account.py", shell=True)
    except:
        msguser = showinfo("warning", "error")
def InsertNrecords():
    try:
        subprocess.call("Add_values_one_at_a_time.py", shell=True)
        subprocess.call("InsertingmultipleValues.py", shell=True)
    except:
        msguser = showinfo("warning", "error")
def AvarageVlTotal():
     try:
        subprocess.call("Average.py.py", shell=True)
     except:
        msguser = showinfo("warning", "error")
    
#Help: for the scripts to work is necessary to put the database login information


Button(root, text='Display Name Used to calculate the average', command=DisplayName).grid(row=4, column=2, sticky=W, pady=5)
Button(root, text='Lets create a table in the database named tb_customer_account', command=CreateTabletbcustomeraccount).grid(row=5, column=2, sticky=W, pady=5)
Button(root, text='Insert N records into table tb_customer_account', command=InsertNrecords).grid(row=6, column=2, sticky=W, pady=5)
Button(root, text='Scroll through the objects and calculate the field average vl_total', command=AvarageVlTotal).grid(row=7, column=2, sticky=W, pady=5)     





root.geometry("400x200")


root.title("T Back 2017")
root.resizable(width=False, height=False)
root.mainloop()
