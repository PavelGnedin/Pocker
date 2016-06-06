# -*- coding:utf-8 -*-

from tkinter import *

# canvas = Canvas(rootAb, bg = 'black')
# canvas.pack(expand = YES,fill = BOTH)
#
# image = PhotoImage(file = './mfon/fon21.png')
# canvas.create_image(0, 0, image = image, anchor = NW)
f = open('Operator', 'r')
massiv = []




def open_faile():
    """
    Открытие файла с текстом
    :rtype:
    """
    for line in f:
        massiv.append(line)


def mainee():
    """
    Метод, cоздающий окно с ссылками
    :rtype: object
    """
    rootAb = Toplevel()
    open_faile()
    frame = Frame(rootAb, bd=2, bg='gray20', relief=SUNKEN)
    scrollbar = Scrollbar(frame, bg='green4', activebackground='green4', highlightbackgroun='green',
                          highlightcolor='green', troughcolor='green')
    scrollbar.configure(bg='green')
    scrollbar.pack(side=RIGHT, fill=Y)
    l = Label(rootAb, text="Instructions :", bg="green4", fg="#4B0082", activeforeground='red',
              font=("Times", 35, "bold"))
    l.place(relx=0.5, rely=0.20, anchor=CENTER)
    q = Text(frame, wrap=WORD, yscrollcommand=scrollbar.set, height=15.3, width=80, bg="green4", fg="#4B0082",
             font=("Times", 23))
    for element in massiv:
        q.insert(END, "" + element)
    q.config(state=DISABLED)
    q.pack()
    frame.place(relx=0.5, rely=0.6, anchor=CENTER)
    scrollbar.config(command=q.yview)
    # mygui.root.withdraw()
    rootAb.title("POKER")
    rootAb["bg"] = "green4"
    rootAb.state("zoomed")
    rootAb.resizable(False, False)
    rootAb.mainloop()
