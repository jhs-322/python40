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
menu.add_command(label="새파일",command=new_file)
menu.add_command(label="저장", command=save_file)
menu.add_separator()
menu.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu1)

menu2 = Menu(menu, tearoff=0)
menu.add_command(label="만든 이", command=maker)
menu.add_cascade(label="만든이", menu=menu2)

text_area = Text(window)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky= N + E + S + W)
# 각 방향으로 텍스트 영역 붙이기(확장)

window.config(menu=menu)
window.mainloop()