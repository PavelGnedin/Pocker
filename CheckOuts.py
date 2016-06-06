# -*- coding:utf-8 -*-
__author__ = 'Павел'
from Card import Card

from checkCombOnHand import CheckComb


class CheckOuts:
    def __init__(self, game1,checkcomb1):
        """
Конструктор класса
        :rtype: object
        """
        self.game = game1
        self.checkcomb =checkcomb1
        self.outs=0

    def checkOut(self):
     """
   Метод считающий ауты
     :rtype: object
     """
     mycomb=self.checkcomb.mycombinationForOut()
     print(mycomb)
     if mycomb=="kiker":
         for i in range(0,4):
           for j in self.game.koloda[i]:
            if(j!=0):
             # self.checkkoloda=[]
             # for i1 in self.game.myCardWithTable:
             #    self.checkkoloda.append(i1)
            # self.checkkoloda.append(i)
             card=Card()
             card.__myinit__(i,j)
             self.game.myCardWithTable.append(card)

             self.CheckComb1=CheckComb(self.game.myCardWithTable)
             str=self.CheckComb1.mycombinationForOut()
             if(str=="para" or str=="strit" or str=="flesh" or str=="FH" or  str=="kare" or
                str=="SF" or
                str=="royal"  ):
                    self.outs+=1
             self.game.myCardWithTable.pop()

     elif mycomb=="para":
         for i in range(0,4):
           for j in self.game.koloda[i]:
            if(j!=0):
             # self.checkkoloda=[]
             # for i1 in self.game.myCardWithTable:
             #    self.checkkoloda.append(i1)
            # self.checkkoloda.append(i)
             card=Card()
             card.__myinit__(i,j)
             self.game.myCardWithTable.append(card)

             self.CheckComb1=CheckComb(self.game.myCardWithTable)
             str=self.CheckComb1.mycombinationForOut()
             if(str=="2para" or str=="set" or str=="strit" or str=="flesh" or str=="FH" or  str=="kare" or
                str=="SF" or
                str=="royal" ):
                    self.outs+=1
             self.game.myCardWithTable.pop()
     elif mycomb=="2para":
         for i in range(0,4):
           for j in self.game.koloda[i]:
            if(j!=0):
             # self.checkkoloda=[]
             # for i1 in self.game.myCardWithTable:
             #    self.checkkoloda.append(i1)
            # self.checkkoloda.append(i)
             card=Card()
             card.__myinit__(i,j)
             self.game.myCardWithTable.append(card)

             self.CheckComb1=CheckComb(self.game.myCardWithTable)
             str=self.CheckComb1.mycombinationForOut()
             if(str=="set" or str=="strit" or str=="flesh" or str=="FH" or  str=="kare" or
                str=="SF" or
                str=="royal" ):
                    self.outs+=1
             self.game.myCardWithTable.pop()
     elif mycomb=="set":
         for i in range(0,4):
           for j in self.game.koloda[i]:
            if(j!=0):
             # self.checkkoloda=[]
             # for i1 in self.game.myCardWithTable:
             #    self.checkkoloda.append(i1)
            # self.checkkoloda.append(i)
             card=Card()
             card.__myinit__(i,j)
             self.game.myCardWithTable.append(card)

             self.CheckComb1=CheckComb(self.game.myCardWithTable)
             str=self.CheckComb1.mycombinationForOut()
             if(str=="strit" or str=="flesh" or str=="FH" or  str=="kare" or
                str=="SF" or
                str=="royal" ):
                    self.outs+=1
             self.game.myCardWithTable.pop()
     elif mycomb=="strit":
         for i in range(0,4):
           for j in self.game.koloda[i]:
            if(j!=0):
             # self.checkkoloda=[]
             # for i1 in self.game.myCardWithTable:
             #    self.checkkoloda.append(i1)
            # self.checkkoloda.append(i)
             card=Card()
             card.__myinit__(i,j)
             self.game.myCardWithTable.append(card)

             self.CheckComb1=CheckComb(self.game.myCardWithTable)
             str=self.CheckComb1.mycombinationForOut()
             if(str=="flesh" or str=="FH" or  str=="kare" or
                str=="SF" or
                str=="royal" ):
                    self.outs+=1
             self.game.myCardWithTable.pop()
     elif mycomb=="flesh":
         for i in range(0,4):
           for j in self.game.koloda[i]:
            if(j!=0):
             # self.checkkoloda=[]
             # for i1 in self.game.myCardWithTable:
             #    self.checkkoloda.append(i1)
            # self.checkkoloda.append(i)
             card=Card()
             card.__myinit__(i,j)
             self.game.myCardWithTable.append(card)

             self.CheckComb1=CheckComb(self.game.myCardWithTable)
             str=self.CheckComb1.mycombinationForOut()
             if(str=="FH" or  str=="kare" or
                str=="SF" or
                str=="royal" ):
                    self.outs+=1
             self.game.myCardWithTable.pop()
     elif mycomb=="FH":
         for i in range(0,4):
           for j in self.game.koloda[i]:
            if(j!=0):
             # self.checkkoloda=[]
             # for i1 in self.game.myCardWithTable:
             #    self.checkkoloda.append(i1)
            # self.checkkoloda.append(i)
             card=Card()
             card.__myinit__(i,j)
             self.game.myCardWithTable.append(card)

             self.CheckComb1=CheckComb(self.game.myCardWithTable)
             str=self.CheckComb1.mycombinationForOut()
             if( str=="kare" or
                str=="SF" or
                str=="royal" ):
                    self.outs+=1
             self.game.myCardWithTable.pop()
     elif mycomb=="kare":
         for i in range(0,4):
           for j in self.game.koloda[i]:
            if(j!=0):
             # self.checkkoloda=[]
             # for i1 in self.game.myCardWithTable:
             #    self.checkkoloda.append(i1)
            # self.checkkoloda.append(i)
             card=Card()
             card.__myinit__(i,j)
             self.game.myCardWithTable.append(card)

             self.CheckComb1=CheckComb(self.game.myCardWithTable)
             str=self.CheckComb1.mycombinationForOut()
             if(
                str=="SF" or
                str=="royal" ):
                    self.outs+=1
             self.game.myCardWithTable.pop()
     elif mycomb=="SF":
         for i in range(0,4):
           for j in self.game.koloda[i]:
            if(j!=0):
             # self.checkkoloda=[]
             # for i1 in self.game.myCardWithTable:
             #    self.checkkoloda.append(i1)
            # self.checkkoloda.append(i)
             card=Card()
             card.__myinit__(i,j)
             self.game.myCardWithTable.append(card)

             self.CheckComb1=CheckComb(self.game.myCardWithTable)
             str=self.CheckComb1.mycombinationForOut()
             if(
                str=="royal" ):
                    self.outs+=1
             self.game.myCardWithTable.pop()
     elif mycomb=="royal":
         self.outs=self.outs
         # for i in self.game.koloda:
         #     self.checkkoloda=self.game.myCardWithTable.copy()
         #     self.checkkoloda.append(i)
         #     str=self.checkcomb.mycombinationForOut(self.checkkoloda)
         #     if(str=="para" or str=="2para" or str=="set" or str=="strit" or str=="flesh" or str=="FH" or  str=="kare" or
         #        str=="SF" or
         #        str=="royal" ):
         #            self.outs+=1