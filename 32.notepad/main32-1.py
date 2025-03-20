from tkinter import *
from tkinter.filedialog import *

def new_file():
    pass

def save_file():
    pass

def maker():
    pass

window = Tk()
window.title("메모장")
window.geometry("400x400+800+300")
window.resizable(False,False)

menu = Menu(window)
menu1 = Menu(menu, tearoff=0)
menu.add_command(label="새파일", command=new_file)
menu.add_separator()
menu.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu1)

menu2 = Menu(menu, tearoff=0)
menu.add_command(label="만든이", command= maker)
menu.add_cascade(label="만든이",menu=menu2)

window.config(menu=menu)
window.mainloop()