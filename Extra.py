from Tkinter import *
from tkMessageBox import *
import subprocess

root = Tk()
menu = Menu(root)


def DisplayName():
    print 'po'
    try:
        subprocess.call("DisplayNames.py", shell=True)
    except:
        msguser = showinfo("warning", "error")





Button(root, text='DisplayName', command=DisplayName).grid(row=4, column=3, sticky=W, pady=5)
#Button(root, text='Desconectar', command=End_rot).grid(row=4, column=2, sticky=W, pady=5)
#Button(root, text='Carregar', command=load).grid(row=5, column=2, sticky=W, pady=5)




root.geometry("800x200")


root.title("T Back 2017")
root.resizable(width=False, height=False)
root.mainloop()
