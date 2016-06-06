# -*- coding:utf-8 -*-
from tkinter import *

import About

import References
from  checkCombOnHand import CheckComb
from CheckOuts import CheckOuts
from  Game import Game
import pyglet
import urllib.request


class A:
    myout="zz"
a=A()

class my:
    def metod(self):
        """
Метод, служащий инициализатором
        :rtype: object
        """
        self.cardf4=Label()
        self.root1 =Toplevel()
        self.cardf4 = Label(self.root1)
        self.cardf4.place(relx=0.75, rely=0.225, anchor=CENTER)
        self.canvas = Canvas(self.root1, bg = 'green')
        self.canvas.pack(expand = YES,fill = BOTH)

        self.image = PhotoImage(file = './mfon/table1.png')
        self.canvas.create_image(660, 0, image = self.image, anchor = NW)
    def about(self):
        """
        Метод вызывающий главнй метод класса About
        :rtype: object
        """
        About.mainee()
    def ref(self):
        """
        Метод вызывающий главнй метод класса References
        :rtype: object
        """
        References.mainee()
    def checkcomb(self,comb):
        """
        Метод, Показывающий текущую комбинацию игрока(наилучшую)
        :param comb:
        """
        self.t = comb.mycombination(comb)
        # if t==0:
        self.comblset = Label(self.root1, text="Your Current Combination:     " + str(self.t), bg="#4B0082")
        self.comblset.place(relx=0.75, rely=0.80, anchor=CENTER)
    def party(self):
            """
            Метод, моделирующий ситуацию нахождения аутов на флопе
            """
            self.game=Game(10)
            self.comb =CheckComb(self.game.myCardWithTable)
            self.playerCard = Label(self.root1, text="Your Cards :      ",font=("Times", 15,"bold"), bg="green", fg="#4B0082")
            self.playerCard.place(relx=0.062, rely=0.13, anchor=CENTER)


            if (self.game.myPlayer.card1.card_suit == 1):
                self.flag = "б"
            elif (self.game.myPlayer.card1.card_suit == 2):
                self.flag = "ч"
            elif (self.game.myPlayer.card1.card_suit == 3):
                self.flag = "п"
            elif (self.game.myPlayer.card1.card_suit == 4):
                self.flag = "к"

            if (self.game.myPlayer.card2.card_suit == 1):
                self.flag1 = "б"
            elif (self.game.myPlayer.card2.card_suit == 2):
                self.flag1 = "ч"
            elif (self.game.myPlayer.card2.card_suit == 3):
                self.flag1 = "п"
            elif (self.game.myPlayer.card2.card_suit == 4):
                self.flag1 = "к"

            self.card1inc = str(self.flag) + str(self.game.myPlayer.card1.card_rating)
            self.card2inc = str(self.flag1) + str(self.game.myPlayer.card2.card_rating)

            print("./images/" + self.card1inc + ".gif")
            self.photoMycard1 = PhotoImage(file="./images/" + self.card1inc + ".gif")
            self.card1 = Label(self.root1, image=self.photoMycard1)
            self.card1.place(relx=0.032, rely=0.225, anchor=CENTER)

            self.photoMycard2 = PhotoImage(file="./images/" + self.card2inc + ".gif")
            self.card2 = Label(self.root1, image=self.photoMycard2)
            self.card2.place(relx=0.1, rely=0.225, anchor=CENTER)


            self.game.update_table_flopRandom()
            self.flop = self.game.tableCards
            if (self.flop[0].card_suit == 1):
                self.flag2 = "б"
            elif (self.flop[0].card_suit == 2):
                self.flag2 = "ч"
            elif (self.flop[0].card_suit == 3):
                self.flag2 = "п"
            elif (self.flop[0].card_suit == 4):
                self.flag2 = "к"

            if (self.flop[1].card_suit == 1):
                self.flag3 = "б"
            elif (self.flop[1].card_suit == 2):
                self.flag3 = "ч"
            elif (self.flop[1].card_suit == 3):
                self.flag3 = "п"
            elif (self.flop[1].card_suit == 4):
                self.flag3 = "к"

            if (self.flop[2].card_suit == 1):
                self.flag4 = "б"
            elif (self.flop[2].card_suit == 2):
                self.flag4 = "ч"
            elif (self.flop[2].card_suit == 3):
                self.flag4 = "п"
            elif (self.flop[2].card_suit == 4):
                self.flag4 = "к"

            self.card1flop = str(self.flag2) + str(self.flop[0].card_rating)
            print("VERY IMPORTANT"+self.card1flop)
            self.card2flop = str(self.flag3) + str(self.flop[1].card_rating)
            self.card3flop = str(self.flag4) + str(self.flop[2].card_rating)

            #self.flopCard = Label(root1, text="Карты стола:      ", bg="red")
            #self.flopCard.place(relx=0.75, rely=0.03, anchor=CENTER)
            self.photof1 = PhotoImage(file="./images/" + self.card1flop + ".gif")
            self.cardf1 = Label(self.root1, image=self.photof1)
            self.cardf1.place(relx=0.55, rely=0.225, anchor=CENTER)

            self.photof2 = PhotoImage(file="./images/" + self.card2flop + ".gif")
            self.cardf2 = Label(self.root1, image=self.photof2)
            self.cardf2.place(relx=0.65, rely=0.225, anchor=CENTER)

            self.photof3 = PhotoImage(file="./images/" + self.card3flop + ".gif")
            self.cardf3 = Label(self.root1, image=self.photof3)
            self.cardf3.place(relx=0.75, rely=0.225, anchor=CENTER)


            self.out = CheckOuts(self.game, CheckComb(self.game.myCardWithTable))
            self.out.checkOut()

            #self.outs=CheckOuts(self.game,self.comb)
            a.myout=str(self.out.outs)
            #self.outsss = Label(self.root1, text="Amounts of Outs :                           ", bg="black", fg="green")
            #self.outsss.place(relx=0.5, rely=0.7, anchor=CENTER)
            self.buttonNewGame = Button(self.root1, text="   NEXT   ",  bg='gray20',fg='#00ffBB',font=("Times", 12,"bold"),command=self.next)
            self.buttonNewGame.place(relx=0.7, rely=0.4, anchor=CENTER)
    def strcheck(self,str4,str2):
            """
    Проверка равенства строк
            :rtype: object
            """
            flag=True
            if (len(str2)!=len(str4)):
                return False
            for i in range(len(str2)):
                if(str4[i]==str2[i]):
                    continue
                else:
                    return False
            return True
    def check(self):
            """
            Метод проверяющий правильность ответа
            :rtype: object
            """

            self.str3="Correctness  :"
            self.str2=self.text1.get("1.0",'end-1c')
            self.str4=str(a.myout)
            if self.strcheck(self.str4.lower(),self.str2.lower()):
                self.music = pyglet.media.load('avacii.mp3',streaming=False)
                self.music.play()
                self.str3="Correctness  :"+"TRUE  "
            else:
                self.music = pyglet.media.load('false.mp3',streaming=False)
                self.music.play()
                self.str3="Correctness  :"+"FALSE"
            self.b= Label(self.separator, text=""+self.str3,bg="green",fg="#4B0082",activeforeground='green',font=("Times", 35,"bold"))
            self.b.place(relx=0.5, rely=0.2, anchor=CENTER)
    def nextT(self):
        """
        Метод,открывающий терн
        :rtype: object
        """

        self.cardf4.destroy()
        self.tern()
    def next(self):
        """
        Метод,открывающий флоп
        :rtype: object
        """
        self.cardf4.destroy()
        self.party()
    def show(self):
        """
        Метод, показывающий количество аутов
        :rtype: object
        """
        self.q = Text(self.separator,wrap=WORD,height=4.4999999999,width=20, bg="medium aquamarine", fg="#4B0082",font='Arial 14')
        #self.q.insert(END,"Correct Answer :      ")
        self.q.insert(END,"Correct Answer :"+"\n"+"Amounts of Outs :"+"\n"+a.myout)
        self.q.config(state=DISABLED)
        self.q.place(relx=0.7, rely=0.5, anchor=CENTER)
        print("happy")
    def tern(self):
            """
            Метод, моделирующий ситуацию нахождения аутов на терне
            """
            self.game=Game(10)
            self.comb = CheckComb(self.game.myCardWithTable)
            self.playerCard = Label(self.root1, text="Your Cards :      ", font=("Times", 15,"bold"),bg="green", fg="#4B0082")
            self.playerCard.place(relx=0.062, rely=0.13, anchor=CENTER)


            if (self.game.myPlayer.card1.card_suit == 1):
                self.flag = "б"
            elif (self.game.myPlayer.card1.card_suit == 2):
                self.flag = "ч"
            elif (self.game.myPlayer.card1.card_suit == 3):
                self.flag = "п"
            elif (self.game.myPlayer.card1.card_suit == 4):
                self.flag = "к"

            if (self.game.myPlayer.card2.card_suit == 1):
                self.flag1 = "б"
            elif (self.game.myPlayer.card2.card_suit == 2):
                self.flag1 = "ч"
            elif (self.game.myPlayer.card2.card_suit == 3):
                self.flag1 = "п"
            elif (self.game.myPlayer.card2.card_suit == 4):
                self.flag1 = "к"

            self.card1inc = str(self.flag) + str(self.game.myPlayer.card1.card_rating)
            self.card2inc = str(self.flag1) + str(self.game.myPlayer.card2.card_rating)

            print("./images/" + self.card1inc + ".gif")
            self.photoMycard1 = PhotoImage(file="./images/" + self.card1inc + ".gif")
            self.card1 = Label(self.root1, image=self.photoMycard1)
            self.card1.place(relx=0.032, rely=0.225, anchor=CENTER)

            self.photoMycard2 = PhotoImage(file="./images/" + self.card2inc + ".gif")
            self.card2 = Label(self.root1, image=self.photoMycard2)
            self.card2.place(relx=0.1, rely=0.225, anchor=CENTER)


            self.game.update_table_flopRandom()
            self.flop = self.game.tableCards
            if (self.flop[0].card_suit == 1):
                self.flag2 = "б"
            elif (self.flop[0].card_suit == 2):
                self.flag2 = "ч"
            elif (self.flop[0].card_suit == 3):
                self.flag2 = "п"
            elif (self.flop[0].card_suit == 4):
                self.flag2 = "к"

            if (self.flop[1].card_suit == 1):
                self.flag3 = "б"
            elif (self.flop[1].card_suit == 2):
                self.flag3 = "ч"
            elif (self.flop[1].card_suit == 3):
                self.flag3 = "п"
            elif (self.flop[1].card_suit == 4):
                self.flag3 = "к"

            if (self.flop[2].card_suit == 1):
                self.flag4 = "б"
            elif (self.flop[2].card_suit == 2):
                self.flag4 = "ч"
            elif (self.flop[2].card_suit == 3):
                self.flag4 = "п"
            elif (self.flop[2].card_suit == 4):
                self.flag4 = "к"

            self.card1flop = str(self.flag2) + str(self.flop[0].card_rating)
            print("VERY IMPORTANT"+self.card1flop)
            self.card2flop = str(self.flag3) + str(self.flop[1].card_rating)
            self.card3flop = str(self.flag4) + str(self.flop[2].card_rating)

            #self.flopCard = Label(root1, text="Карты стола:      ", bg="red")
            #self.flopCard.place(relx=0.75, rely=0.03, anchor=CENTER)
            self.photof1 = PhotoImage(file="./images/" + self.card1flop + ".gif")
            self.cardf1 = Label(self.root1, image=self.photof1)
            self.cardf1.place(relx=0.55, rely=0.225, anchor=CENTER)

            self.photof2 = PhotoImage(file="./images/" + self.card2flop + ".gif")
            self.cardf2 = Label(self.root1, image=self.photof2)
            self.cardf2.place(relx=0.65, rely=0.225, anchor=CENTER)

            self.photof3 = PhotoImage(file="./images/" + self.card3flop + ".gif")
            self.cardf3 = Label(self.root1, image=self.photof3)
            self.cardf3.place(relx=0.75, rely=0.225, anchor=CENTER)


            self.game.update_table_ternRandom()
            self.myytern = self.game.tableCards[3]
            if (self.myytern.card_suit == 1):
                self.flag5 = "б"
            elif (self.myytern.card_suit == 2):
                self.flag5 = "ч"
            elif (self.myytern.card_suit == 3):
                self.flag5 = "п"
            elif (self.myytern.card_suit == 4):
                self.flag5 = "к"
            self.card4flop = str(self.flag5) + str(self.myytern.card_rating)
            self.photof4 = PhotoImage(file="./images/" + self.card4flop + ".gif")
            self.cardf4 = Label(self.root1, image=self.photof4)
            self.cardf4.place(relx=0.85, rely=0.225, anchor=CENTER)

            self.out = CheckOuts(self.game, CheckComb(self.game.myCardWithTable))
            self.out.checkOut()

            #self.outs=CheckOuts(self.game,self.comb)
            a.myout=str(self.out.outs)
            #self.outsss = Label(self.root1, text="Amounts of Outs  :                           ", bg="black", fg="green")
            #self.outsss.place(relx=0.5, rely=0.7, anchor=CENTER)
            self.checkb = Button(self.separator, text="Check    ",fg='#00ffBB', bg='gray20',font=("Times", 15,"bold"), command=self.check)
            self.checkb.place(relx=0.3, rely=0.9, anchor=CENTER)
            self.buttonNewGame = Button(self.root1, text="   NEXT   ",  bg='gray20',fg='#00ffBB',font=("Times", 12,"bold"),command=self.nextT)
            self.buttonNewGame.place(relx=0.7, rely=0.4, anchor=CENTER)



def main():
    """
    Главный метод класса
    :rtype: object
    """

    myyyyy=my()
    myyyyy.metod()
    myyyyy.separator = Frame(myyyyy.root1,bg="green",height=350,width=700, bd=1, relief=SUNKEN)
    myyyyy.separator.place(relx=0.5, rely=0.75, anchor=CENTER)
    myyyyy.text1=Text(myyyyy.separator,wrap=WORD,height=3.3,width=20, bg="medium aquamarine", fg="#4B0082",font='Arial 14')
    myyyyy.text1.place(relx=0.3, rely=0.55, anchor=CENTER)
    myyyyy.label1=Label(myyyyy.separator,text="Your answer :               " ,bg="medium aquamarine", fg="#4B0082",font=('Arial 14',15))
    myyyyy.label1.place(relx=0.3, rely=0.41, anchor=CENTER)

    myyyyy.q = Text(myyyyy.separator,wrap=WORD,height=4.4999999999,width=20, bg="medium aquamarine", fg="#4B0082",font='Arial 14')
    myyyyy.q.insert(END,"Correct Answer :      ")
    myyyyy.q.config(state=DISABLED)
    myyyyy.q.place(relx=0.7, rely=0.5, anchor=CENTER)
    myyyyy.str3="Correctness  :"
    #mygui.root.withdraw()
    myyyyy.root1.title("POKER")
    myyyyy.root1["bg"] = "green4"
    myyyyy.root1.state("zoomed")
    myyyyy.root1.resizable(False, False)
    myyyyy.b= Label(myyyyy.separator, text=""+myyyyy.str3,bg="green",fg="#4B0082",activeforeground='green',font=("Times", 35,"bold"))
    myyyyy.b.place(relx=0.5, rely=0.2, anchor=CENTER)
    #myyyyy.b1= Label(myyyyy.root1, text="OUTS MODE",bg="green",fg="#4B0082",activeforeground='#4B0082',font=("Times", 35,"bold"))
   # myyyyy.b1.place(relx=0.2, rely=0.05, anchor=CENTER)
    myyyyy.b2= Label(myyyyy.root1, text="OUTS MODE:Count the number of outs",bg="green",fg="#00ffBB ",activeforeground='#4B0082',font=("Times", 25,"bold"))
    myyyyy.b2.place(relx=0.3, rely=0.05, anchor=CENTER)
    myyyyy.buttonNewGame = Button(myyyyy.separator, text="   SHOW   ",  bg='gray20',fg='#00ffBB',font=("Times", 12,"bold"),command=myyyyy.show)
    myyyyy.buttonNewGame.place(relx=0.7, rely=0.9, anchor=CENTER)
    #myyyyy.party()
    #myyyyy.root1.protocol('WM_DELETE_WINDOW', myyyyy.root1.destroy)
    myyyyy.checkb = Button(myyyyy.separator, text="Check    ",fg='#00ffBB', bg='gray20',font=("Times", 15,"bold"), command=myyyyy.check)
    myyyyy.checkb.place(relx=0.3, rely=0.9, anchor=CENTER)

    myyyyy.menubar = Menu(myyyyy.root1)
    # create a pulldown menu, and add it to the menu bar
    myyyyy.filemenu = Menu(myyyyy.menubar, tearoff=0)
    myyyyy.filemenu.add_command(label="Flop Mode", activeforeground='#00ffBB',activebackground='gray20',command=myyyyy.next)
    myyyyy.filemenu.add_command(label="Tern Mode", activeforeground='#00ffBB',activebackground='gray20',command=myyyyy.nextT)
    #myyyyy.filemenu.add_separator()
    myyyyy.filemenu.add_command(label="Exit", activeforeground='#00ffBB',activebackground='gray20',command=myyyyy.root1.destroy)
    myyyyy.menubar.add_cascade(label="MODE", menu=myyyyy.filemenu)


    myyyyy.helpmenu = Menu(myyyyy.menubar, tearoff=0)
    myyyyy.helpmenu.add_command(label="About",activeforeground='#00ffBB',activebackground='gray20', command=myyyyy.about)
    myyyyy.helpmenu.add_command(label="References ",activeforeground='#00ffBB',activebackground='gray20', command=myyyyy.ref)
    myyyyy.menubar.add_cascade(label="Help", activeforeground='#00ffBB',activebackground='gray20',menu=myyyyy.helpmenu)
    myyyyy.root1.config(menu=myyyyy.menubar)
    #myyyyy.root1.protocol('WM_DELETE_WINDOW', myyyyy.root1.destroy)
    myyyyy.party()
    myyyyy.root1.mainloop()
