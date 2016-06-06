# -*- coding:utf-8 -*-
import random
from tkinter import *
import pyglet
import urllib.request
class B:
    def sw1(self):
        self.var=1
    def sw2(self):
        self.var=2
    def sw3(self):
        self.var=3
    def sw4(self):
        self.var=4
    def metod(self):
        """
Метод, служащий инициализатором
        :rtype: object
        """
        self.var=0
        self.root2 =Toplevel()
        self.canvas = Canvas(self.root2, bg = 'green')
        self.canvas.pack(expand = YES,fill = BOTH)

        self.image = PhotoImage(file = './mfon/fon21.png')
        self.canvas.create_image(0, 0, image = self.image, anchor = NW)
        #self.f = open('QaA1.txt', 'r')

        #self.f = urllib.request.urlopen("http://goo.gl/BYVZtV?gdriveurl")
        self.f = urllib.request.urlopen("http://goo.gl/z2RAUx?gdriveurl")
        self.massiv=[]

        #self.label1=Label(self.root2,text="Your answer :               " ,bg="medium aquamarine", fg="green",font=('Arial 14',15))
        #self.label1.place(relx=0.344, rely=0.674, anchor=CENTER)
        #self.text1=Text(self.root2,wrap=WORD,height=3.3,width=20, bg="medium aquamarine", fg="green",font='Arial 14')
        #self.text1.place(relx=0.344, rely=0.739, anchor=CENTER)


        self.q = Text(self.root2,wrap=WORD,height=4.45,width=20, bg="medium aquamarine", fg="#4B0082",font='Arial 14')
        self.q.insert(END,"Correct Answer :      ")
        self.q.config(state=DISABLED)
        self.q.place(relx=0.652, rely=0.68, anchor=CENTER)

        self.str1="s1"
        self.str2="s2"
        self.str3="Correctness  :"
        self.str4="str4"
        self.i=0

        self.b= Label(self.root2, text=""+self.str3,bg="medium sea green",fg="#4B0082",activeforeground='green',font=("Times", 35,"bold"))
        self.b.place(relx=0.5, rely=0.1, anchor=CENTER)
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

            # if(True):
            #     return True
            # else:
            #     return False
    def open_faile(self):
        """
        открытие файла с вопросами
        :rtype: object
        """
        for line in self.f:
            line=str(line)
            s=line[ 2 : -5]
            self.massiv.append(s)
    def show(self):
            """
            Метод показывает правильность ответа
            :rtype: object
            """
            self.str1=str(self.massiv[self.i+2])
            self.q = Text(self.root2,wrap=WORD,height=4.45,width=20, bg="medium aquamarine", fg="#4B0082",font='Arial 14')
            self.q.insert(END,"Correct Answer :      "+self.str1)
            self.q.config(state=DISABLED)
            self.q.place(relx=0.652, rely=0.68, anchor=CENTER)

    def check(self):
            """
            Метод проверяющий правильность ответа
            :rtype: object
            """
            self.q = Text(self.root2,wrap=WORD,height=4.45,width=20, bg="medium aquamarine", fg="#4B0082",font='Arial 14')
            self.q.insert(END,"Correct Answer :      ")
            self.q.config(state=DISABLED)
            self.q.place(relx=0.652, rely=0.68, anchor=CENTER)
            self.str3="Correctness  :"
            self.b= Label(self.root2, text=""+self.str3,bg="medium sea green",fg="#4B0082",activeforeground='green',font=("Times", 35,"bold"))
            self.b.place(relx=0.5, rely=0.1, anchor=CENTER)
            #self.str2=self.text1.get("1.0",'end-1c')
            self.str2=str(self.var)
            self.str4=str(self.massiv[self.i+2])
            print ("FF"+self.str4+"F")
            print ("FF"+self.str2+"F")
            if self.strcheck(self.str4.lower(),self.str2.lower()):
                self.music = pyglet.media.load('avacii.mp3',streaming=False)
                self.music.play()
                self.str3="Correctness  :"+"TRUE  "
            else:
                self.music = pyglet.media.load('false.mp3',streaming=False)
                self.music.play()
                self.str3="Correctness  :"+"FALSE"
            self.b= Label(self.root2, text=""+self.str3,bg="medium sea green",fg="#4B0082",activeforeground='green',font=("Times", 35,"bold"))
            self.b.place(relx=0.5, rely=0.1, anchor=CENTER)

    def next(self):
            """
            Метод вызывающий следующий вопрос
            :rtype: object
            """
            self.q = Text(self.root2,wrap=WORD,height=4.45,width=20, bg="medium aquamarine", fg="#4B0082",font='Arial 14')
            self.q.insert(END,"Correct Answer :      ")
            self.q.config(state=DISABLED)
            self.q.place(relx=0.652, rely=0.68, anchor=CENTER)
            self.open_faile()
            self.i=random.randint(0, len(self.massiv)-3)
            if(self.i%3==0):
                self.i=self.i;
            else:
                if(self.i%3==1):
                    self.i=self.i+2
                else:
                    self.i=self.i+1
            self.str1=str(self.massiv[self.i])
            self.q = Text(self.root2,wrap=WORD,height=6.3,width=40, bg="medium aquamarine", fg="#4B0082",font=("Times", 23))
            self.q.insert(END,"Question :      "+self.str1)
            self.spl=str(self.massiv[self.i+1]).split('|')
            # self.q.insert(END,'\n'+'\n'+"ANSWERS:")
            # for i in self.spl:
            #      self.q.insert(END,'\n'+"                                "+i)
            self.R1.destroy()
            self.R2.destroy()
            self.R3.destroy()
            self.R4.destroy()
            self.R1 = Radiobutton(self.root2, text='%-17s' % self.spl[1], bg='medium aquamarine',fg="#4B0082",command=self.sw1,width=15,font=("Times", 15),variable=self.var, value="1")
            self.R1.place(relx=0.35, rely=0.60, anchor=CENTER)
            self.R2 = Radiobutton(self.root2, text='%-17s' % self.spl[2],bg='medium aquamarine',fg="#4B0082", command=self.sw2,width=15,font=("Times", 15),variable=self.var, value="2")
            self.R2.place(relx=0.35, rely=0.66, anchor=CENTER)
            self.R3 = Radiobutton(self.root2, text='%-17s' % self.spl[3], bg='medium aquamarine',fg="#4B0082",command=self.sw3,width=15,font=("Times", 15),variable=self.var, value="3")
            self.R3.place(relx=0.35, rely=0.72, anchor=CENTER)
            self.R4 = Radiobutton(self.root2, text='%-17s' % self.spl[4],bg='medium aquamarine',fg="#4B0082", command=self.sw4,width=15,font=("Times", 15),variable=self.var, value="4")
            self.R4.place(relx=0.35, rely=0.78, anchor=CENTER)
            #self.q.insert(END,'\n'+'\n'+"ANSWERS:"+'\n'+"    "+str(self.massiv[self.i+1]))
            self.q.config(state=DISABLED)
            self.q.place(relx=0.5, rely=0.4, anchor=CENTER)
            #f.close()
def mainee():
    """
Главный метод класса
    :rtype: object
    """
    b=B()
    b.metod()
    b.open_faile()
    print(len(b.massiv))
    b.i=random.randint(0, len(b.massiv)-3)
    if(b.i%3==0):
        b.i=b.i;
    else:
                if(b.i%3==1):
                    b.i=b.i+2
                else:
                    b.i=b.i+1
    b.str1=str(b.massiv[b.i])
    b.q = Text(b.root2,wrap=WORD, height=6.3,width=40,bg="medium aquamarine", fg="#4B0082",font=("Times", 23))
    b.q.insert(END,"Question :      "+b.str1)
    b.spl=str(b.massiv[b.i+1]).split('|')
    # b.q.insert(END,'\n'+'\n'+"ANSWERS:")
    # for i in b.spl:
    #              b.q.insert(END,'\n'+"                                "+i)
    b.R1 = Radiobutton(b.root2, text='%-17s' % b.spl[1], activeforeground="#4B0082",bg='medium aquamarine',fg="#4B0082",width=15,command=b.sw1,font=("Times", 15),variable=b.var, value="1")
    b.R1.place(relx=0.35, rely=0.60, anchor=CENTER)
    b.R2 = Radiobutton(b.root2, text='%-17s' % b.spl[2],bg='medium aquamarine',fg="#4B0082", width=15,command=b.sw2,font=("Times", 15),variable=b.var, value="2")
    b.R2.place(relx=0.35, rely=0.66, anchor=CENTER)
    b.R3 = Radiobutton(b.root2, text='%-17s' % b.spl[3], bg='medium aquamarine',fg="#4B0082",width=15,command=b.sw3,font=("Times", 15),variable=b.var, value="3")
    b.R3.place(relx=0.35, rely=0.72, anchor=CENTER)
    b.R4 = Radiobutton(b.root2, text='%-17s' % b.spl[4],bg='medium aquamarine',fg="#4B0082",width=15, command=b.sw4,font=("Times", 15),variable=b.var, value="4")
    b.R4.place(relx=0.35, rely=0.78, anchor=CENTER)
    #b.q.insert(END,'\n'+'\n'+"ANSWERS:"+'\n'+"    "+str(b.massiv[b.i+1]))
    b.q.config(state=DISABLED)
    b.q.place(relx=0.5, rely=0.4, anchor=CENTER)

    # text1=Text(root2,height=1,width=5,font='Arial 14',wrap=WORD)
    # text1.place(relx=0.7, rely=0.7, anchor=CENTER)

    # a = Label(root2, text="Ответ :      "+str(massiv[1]), bg="black", fg="green")
    # a.place(relx=0.7, rely=0.5, anchor=CENTER)

    #mygui.root.withdraw()
    b.root2.title("POKER")
    b.root2["bg"] = "green4"
    b.root2.state("zoomed")
    b.root2.resizable(False, False)

    b.buttonNewGame = Button(b.root2, text="Check    ",fg='#00ffBB', bg='gray20',font=("Times", 15,"bold"), command=b.check)
    b.buttonNewGame.place(relx=0.344, rely=0.9, anchor=CENTER)
    b.buttonNextGame = Button(b.root2, text="Next    ",fg='#00ffBB', bg='gray20',font=("Times", 15,"bold"), command=b.next)
    b.buttonNextGame.place(relx=0.5, rely=0.9, anchor=CENTER)
    b.buttonShowGame = Button(b.root2, text="Show      ",fg='#00ffBB', bg='gray20',font=("Times", 15,"bold"), command=b.show)
    b.buttonShowGame.place(relx=0.65, rely=0.9, anchor=CENTER)
    #f.close()
    b.root2.mainloop()