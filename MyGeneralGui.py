# -*- coding:utf-8 -*-
import tkinter
from tkinter import *
from playsound import playsound
import wave
import pyglet
import About
import ClassicalQuestions
#import GameMode2.gui.game
import References
import mygui
import modeOuts
import Instra
# #
def about():
    """
    Метод вызывающий главнй метод класса About
    :rtype: object
    """
    About.mainee()
def ref():
    """
    Метод вызывающий главнй метод класса References
    :rtype: object
    """
    References.mainee()
def ins():
    """
    Метод вызывающий главнй метод класса References
    :rtype: object
    """
    Instra.mainee()
def runGame():
    """
Метод вызывающий главнй метод класса mygui
    :rtype: object
    """
    mygui.mymain()
def runGame2():
    """
Метод вызывающий главнй метод класса mygui
    :rtype: object
    """
    mygui.gui.game.main()
def outs():
    """
Метод вызывающий главнй метод класса modeOuts
    :rtype: object
    """
    modeOuts.main()
def cq():
    """
Метод вызывающий главнй метод класса ClassicalQuestions
    :rtype: object
    """
    ClassicalQuestions.mainee()
# class pop:
#         popup=0
#     #i=pop()
class MyClass:
    def metod(self):
        """
Метод, служащий инициализатором
        :rtype: object
        """
        self.i=0
        self.myroot = Tk() # окно

        self.photo = tkinter.PhotoImage(file = './mfon/fon1.png')

        self.canvas = Canvas(self.myroot, bg = 'black')
        self.canvas.pack(expand = YES,fill = BOTH)

        self.image = tkinter.PhotoImage(file = './mfon/fon1.png')
        self.canvas.create_image(0, 0, image = self.image, anchor = NW)




    # mygui.root.withdraw()
    # modeOuts.root1.withdraw()
    # ClassicalQuestions.root2.withdraw()
    # About.rootAb.withdraw()
    # References.rootAb.withdraw()

        self.menubar = Menu(self.myroot,activeforeground='black',activebackground='black')
        #
        # # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar,activeforeground='black',activebackground='black', tearoff=0)

        self.filemenu.add_command(label="Game Mode",activeforeground='#00ffBB',activebackground='gray20', command=runGame)
        #self.filemenu.add_command(label="Game Mode2",activeforeground='#00ffBB',activebackground='gray20', command=runGame2)
        self.filemenu.add_command(label="Outs Mode",activeforeground='#00ffBB',activebackground='gray20', command=outs)
        self.filemenu.add_command(label="Questions Mode",activeforeground='#00ffBB',activebackground='gray20', command=cq)

        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",activeforeground='#00ffBB',activebackground='gray20', command=self.myroot.quit)
        self.menubar.add_cascade(label="MODE",activeforeground='#00ffBB', activebackground='gray20',menu=self.filemenu)

        # # create more pulldown menus
        # editmenu = Menu(menubar, tearoff=0)
        # editmenu.add_command(label="Cut", command=runGame)
        # editmenu.add_command(label="Copy", command=runGame)
        # editmenu.add_command(label="Paste", command=runGame)
        # menubar.add_cascade(label="Edit", menu=editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)

        self.helpmenu.add_command(label="About",activeforeground='#00ffBB',activebackground='gray20', command=about)
        self.helpmenu.add_command(label="Instructions ",activeforeground='#00ffBB',activebackground='gray20', command=ins)
        self.helpmenu.add_command(label="References ",activeforeground='#00ffBB',activebackground='gray20', command=ref)
        self.menubar.add_cascade(label="Help", activeforeground='#00ffBB',activebackground='gray20',menu=self.helpmenu)

        # display the menu
        self.myroot.config(menu=self.menubar)


        self.myroot.title("POKER")
        self.myroot["bg"] = "dark orange"
        self.myroot.state("zoomed")
        self.myroot.resizable(False, False)

        self.comblpara=Label(self.myroot,text="WELCOME",bg="black",fg="white",activeforeground='red',font=("Times", 55,"bold"))
        self.comblpara.place(relx=0.2, rely=0.20, anchor=CENTER)
        self.comblpara1=Label(self.myroot,text="... to the Pocker Trainer",bg="black",fg="#00ffBB",font=("Times", 15,"bold"))
        self.comblpara1.place(relx=0.3, rely=0.270, anchor=CENTER)

    def des(self):
        """
        Метод, вызывающий звук при выходе
        :rtype: object
        """
        self.music = pyglet.media.load('exit.wav',streaming=False)
        self.music.play()

        self.i.destroy()
        self.myroot.destroy()
    def des1(self):
        """
        Метод, вызывающий звук при возврате из окна выхода
        :rtype: object
        """
        #playsound("return.wav")
        self.music = pyglet.media.load('return.wav',streaming=False)
        self.music.play()
        self.i.destroy()


    def popupmsg(self):
        """
        Метод, вызывающий окно уточнения выхода
        :rtype: object
        """
        self.i=Toplevel()
        self.i["bg"] = "OrangeRed3"
        self.i.wm_title("Quit, Do you really wish to quit?")
        label = Label(self.i, text="Quit, Do you really wish to quit?", fg="#00ffBB", bg="gray20")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(self.i, text="YES", fg="#00ffBB", bg="gray20",command=self.des )
        B1.pack(side="left",padx=30)
        B2 = Button(self.i, text="NO", fg="#00ffBB", bg="gray20",command=self.des1 )
        B2.pack(side="right",padx=30,pady=30)
        x = (self.i.winfo_screenwidth() - self.i.winfo_reqwidth()) / 2
        y = (self.i.winfo_screenheight() - self.i.winfo_reqheight()) / 2
        self.i.wm_geometry("+%d+%d" % (x, y))
        self.i.mainloop()
        print()
def maine():
        """
      Главный метод класса
        :rtype: object
        """
        a=MyClass()
        a.metod()
        a.myroot.protocol("WM_DELETE_WINDOW", a.popupmsg)
        a.myroot.mainloop()
maine()
