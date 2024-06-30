from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("800x800")
root.title("Notepad")
root.config(bg='lightgreen')
root.resizable(True,True)

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,con)

b1=Button(root,width='30',height='5',bg='#fff',text='save file',command=save_file).place(x=190,y=5)
b2=Button(root,width='30',height='5',bg='#fff',text='open file',command=save_file).place(x=390,y=5)

entry=Text(root,height='70',width='94',wrap=WORD)
entry.place(x=20,y=80)

root.mainloop()
