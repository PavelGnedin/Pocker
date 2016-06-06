# -*- coding:utf-8 -*-
__author__ = 'Павел'


class CheckComb:
 def __init__(self,myCardWithTable):
         self.myCardWithTable=myCardWithTable
         self.myRatingCardWithTable=[]
         for i in myCardWithTable:
             self.myRatingCardWithTable.append(i.card_rating)
 def checkWinner(self,checkComb,players,tablecards):
        points=[]
        for i in players:
            mas=[]
            mas.append(i.card1)
            mas.append(i.card2)
            for j in tablecards:
             mas.append(j)

            chcomb=CheckComb(mas)
            str1=chcomb.mycombinationForOut()
            if i.active :
                if (str1=="kiker"):
                    points.append(0)
                elif (str1=="para"):
                    points.append(1)
                elif (str1=="2para"):
                    points.append(2)
                elif (str1=="set"):
                    points.append(3)
                elif (str1=="strit"):
                    points.append(4)
                elif (str1=="flesh"):
                    points.append(5)
                elif (str1=="FH"):
                    points.append(6)
                elif (str1=="kare"):
                    points.append(7)
                elif (str1=="SF"):
                    points.append(8)
                elif (str1=="royal"):
                    points.append(9)
            else:
                points.append(-1)
        k=points.index(max(points))

        if(max(points)==0):
            max1=0
            i=0
            for t in players:
                if t.card1.card_rating>max1:
                    max1=t.card1.card_rating
                elif t.card2.card_rating>max1:
                    max1=t.card2.card_rating
                i=i+1
            if(i!=0):
                return str("WINNER GAMER NOMER : "+str(i)+" COMBINATION : kiker  with "+str(max1))
            else:
                print ("YOU: "+str(i)+" COMBINATION : kiker  with "+str(max1))
                return str("YOU ARE WINNER : "+" COMBINATION : kiker  with "+str(max1))


        else:
                mas1=[]
                mas1.append(players[k].card1)
                mas1.append(players[k].card2)
                for j in tablecards:
                     mas1.append(j)
                z=CheckComb(mas1)

                if(k!=0):
                    return str("WINNER GAMER NOMER : "+str(k)+" COMBINATION : "+z.mycombination(z))
                else:
                     print ("YOU! : "+str(k)+" COMBINATION : "+z.mycombination(z))
                     return str("YOU ARE WINNER : "+" COMBINATION : "+z.mycombination(z))




 def checkWinner1(self,checkComb,players,tablecards):
        """

         :param checkComb:
         :param players:
         :param tablecards:
         :return:
        """
        points=[]
        for i in players:
            mas=[]
            mas.append(i.card1)
            mas.append(i.card2)
            for j in tablecards:
             mas.append(j)

            chcomb=CheckComb(mas)
            str1=chcomb.mycombinationForOut()
            if i.active :
                if (str1=="kiker"):
                    points.append(0)
                elif (str1=="para"):
                    points.append(1)
                elif (str1=="2para"):
                    points.append(2)
                elif (str1=="set"):
                    points.append(3)
                elif (str1=="strit"):
                    points.append(4)
                elif (str1=="flesh"):
                    points.append(5)
                elif (str1=="FH"):
                    points.append(6)
                elif (str1=="kare"):
                    points.append(7)
                elif (str1=="SF"):
                    points.append(8)
                elif (str1=="royal"):
                    points.append(9)
            else :
                points.append(-1)
        k=points.index(max(points))

        if(max(points)==0):
            max1=0
            i=0
            for t in players:
                if t.card1.card_rating>max1:
                    max1=t.card1.card_rating
                elif t.card2.card_rating>max1:
                    max1=t.card2.card_rating
                i=i+1
            if(i!=0):
                return i
            else:
                return 0

        else:
                mas1=[]
                mas1.append(players[k].card1)
                mas1.append(players[k].card2)
                for j in tablecards:
                     mas1.append(j)
                z=CheckComb(mas1)

                if(i!=0):
                    return k
                else:
                     return 0

 def check_flesh(self):
     chervi=0
     bubi=0
     piki=0
     kresti=0
     for i in self.myCardWithTable:
         if i.card_suit==1 :
             bubi=bubi+1
         elif i.card_suit==2:
             chervi=chervi+1
         elif i.card_suit==3:
             piki=piki+1
         elif i.card_suit==4:
             kresti=kresti+1
     if chervi>=5:
         return 2
     elif bubi>=5:
         return 1
     elif piki>=5:
         return 3
     elif kresti>=5:
         return 4
     else:
         return 0

 def check_kare(self):
     for i in range(2,15):
         j=self.myRatingCardWithTable.count(i)
         if j==4:
             return i
             break
     return 0


 def mySort(self,mycard):
     return mycard.card_rating


 def mycheck_strit(self):
     k=0
     mas=self.myCardWithTable.copy()
     mas.sort(key=self.mySort)
     if (len(self.myCardWithTable)==5):
         for i in range(4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 return []
         return mas

     elif (len(self.myCardWithTable)==6):
         flag=1
         for i in range(1,5):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(1,6):
                 mas1.append(mas[i])
             return mas1
         else :
             return []

         flag=1
         for i in range(0,4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(0,5):
                 mas1.append(mas[i])
             return mas1
         else :
             return []
     elif (len(self.myCardWithTable)==7):

         flag=1
         for i in range(2,6):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(2,7):
                 mas1.append(mas[i])
             return mas1
         else :
             return []

         flag=1
         for i in range(1,5):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(1,6):
                 mas1.append(mas[i])
             return mas1
         else :
             return []

         flag=1
         for i in range(0,4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(0,5):
                 mas1.append(mas[i])
             return mas1
         else :
             return []
     else:
         return []



 def check_strit(self):
     k=0
     s=[]
     flag=0
     for i in self.myCardWithTable:
         for j in s:
           if(j.card_rating==i.card_rating):
             flag=1
         if(flag==0):
             s.append(i)
         flag=0
     #print (len(s))
     #s=sorted(s)
     mas=self.myCardWithTable.copy()
     mas.sort(key=self.mySort)

     if (len(self.myCardWithTable)==5):
         for i in range(4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 return []
         return mas

     elif (len(self.myCardWithTable)==6):
        if len(s)==6:
         flag=1
         for i in range(1,5):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(1,6):
                 mas1.append(mas[i])
             return mas1


         flag=1
         for i in range(0,4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(0,5):
                 mas1.append(mas[i])
             return mas1
         else :
             return []

        elif(len(s)==5):
            s.sort(key=self.mySort)
            for i in range(4):
                if (s[i].card_rating)!=(s[i+1].card_rating-1):
                 return []
            return s
        else:
            return[]
     elif (len(self.myCardWithTable)==7):
       if len(s)==7:
         flag=1
         for i in range(2,6):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(2,7):
                 mas1.append(mas[i])
             return mas1


         flag=1
         for i in range(1,5):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(1,6):
                 mas1.append(mas[i])
             return mas1


         flag=1
         for i in range(0,4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(0,5):
                 mas1.append(mas[i])
             return mas1
         else :
             return []
       elif(len(s)==6):
         s.sort(key=self.mySort)
         flag=1
         for i in range(1,5):
             if s[i].card_rating!=s[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(1,6):
                 mas1.append(s[i])
             return mas1


         flag=1
         for i in range(0,4):
             if s[i].card_rating!=s[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(0,5):
                 mas1.append(s[i])
             return mas1
         else :
             return []
       elif(len(s)==5):
           s.sort(key=self.mySort)
           for i in range(4):
                if (s[i].card_rating)!=(s[i+1].card_rating-1):
                 return []
           return s
       else:
           return []
     else:
         return []


 def check_set_trips(self):
     flag=0
     for i in range(2,15):
         j=self.myRatingCardWithTable.count(i)
         if j==3:
             flag=i
     return flag
 def check_para(self):
     flag=0
     for i in range(2,15):
         j=self.myRatingCardWithTable.count(i)
         if j==2:
             flag=i
     return flag
 def check_2para(self):
     para=[]
     for i in range(2,15):
         j=self.myRatingCardWithTable.count(i)
         if j==2:
             para.append(i)
     if(len(para)==2):
             return para
     elif(len(para)==3):
             mas1=[]
             mas1.append(para[1])
             mas1.append(para[2])
             return mas1
     else :
             return []

 def check_fullHouse(self):
     flag=[]
     for i in range(2,15):
         j=self.myRatingCardWithTable.count(i)
         if j==3:
             flag.append(j)
     if (len(flag) == 1):
         para = []
         for i in range(2, 15):
             j = self.myRatingCardWithTable.count(i)
             if j == 2:
                 para.append(j)
         if (len(para) == 1):
             if(para[0]!=flag[0]):
                 return 1
         elif (len(para) == 2):
                 return 1
         elif (len(para) == 3):
                 return 1
         else:
                return 0
     else:
         return 0


 def check_fleshForSTRFL(self, mas):
     chervi=0
     bubi=0
     piki=0
     kresti=0
     for i in mas:
         if i.card_suit==1 :
             bubi=bubi+1
         elif i.card_suit==2:
             chervi=chervi+1
         elif i.card_suit==3:
             piki=piki+1
         elif i.card_suit==4:
             kresti=kresti+1
     if chervi>=5:
         return 2
     elif bubi>=5:
         return 1
     elif piki>=5:
         return 3
     elif kresti>=5:
         return 4
     else:
         return 0

 def suitestack(self,cards):
     s=self.check_fleshForSTRFL(cards)
     mas=[]
     for i in cards:
         if i.card_suit==s:
             mas.append(i)
     return mas
#не работает
 def check_stritFlush(self):
   k=0
   s=[]
   flag=0
   check=self.suitestack(self.myCardWithTable)

   if(len(check)<5):
       return []
   else:
     for i in check:
         for j in s:
           if(j.card_rating==i.card_rating):
             flag=1
         if(flag==0):
             s.append(i)
         flag=0

     #s=sorted(s)
     mas=check.copy()
     mas.sort(key=self.mySort)

     if (len(check)==5):
         for i in range(4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 return []
         if (self.check_fleshForSTRFL(mas)!=0):
            return mas
         else:
             return []

     elif (len(check)==6):
        if len(s)==6:
         flag=1
         for i in range(1,5):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(1,6):
                 mas1.append(mas[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    return mas1
             else:
                     return []
         else :
             return []

         flag=1
         for i in range(0,4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(0,5):
                 mas1.append(mas[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    return mas1
             else:
                     return []
         else :
             return []
        elif(len(s)==5):
            s.sort(key=self.mySort)
            for i in range(4):
                if (s[i].card_rating)!=(s[i+1].card_rating-1):
                 return []
            if (self.check_fleshForSTRFL(s)!=0):
                    return s
            else:
                     return []
        else:
            return[]
     elif (len(check)==7):
       if len(s)==7:
         flag=1
         for i in range(2,6):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(2,7):
                 mas1.append(mas[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    return mas1
             else:
                     return []
         else :
             return []

         flag=1
         for i in range(1,5):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(1,6):
                 mas1.append(mas[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    return mas1
             else:
                     return []
         else :
             return []

         flag=1
         for i in range(0,4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(0,5):
                 mas1.append(mas[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    return mas1
             else:
                     return []
         else :
             return []
       elif(len(s)==6):
         s.sort(key=self.mySort)
         flag=1
         for i in range(1,5):
             if s[i].card_rating!=s[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(1,6):
                 mas1.append(s[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    return mas1
             else:
                     return []
         else :
             return []

         flag=1
         for i in range(0,4):
             if s[i].card_rating!=s[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(0,5):
                 mas1.append(s[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    return mas1
             else:
                     return []
         else :
             return []
       elif(len(s)==5):
           s.sort(key=self.mySort)
           for i in range(4):
                if (s[i].card_rating)!=(s[i+1].card_rating-1):
                 return []
           if (self.check_fleshForSTRFL(s)!=0):
                    return s
           else:
                     return []
       else:
           return []


 def sortForRoyal(self,mycard):
    return mycard.card_suit
#не работает
 def fleshRoyal(self):
   k=0
   s=[]
   flag=0
   check=self.suitestack(self.myCardWithTable)

   if(len(check)<5):
       return []
   else:
     for i in check:
         for j in s:
           if(j.card_rating==i.card_rating):
             flag=1
         if(flag==0):
             s.append(i)
         flag=0

     #s=sorted(s)
     mas=check.copy()
     mas.sort(key=self.mySort)

     if (len(check)==5):
         for i in range(4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 return []
         if (self.check_fleshForSTRFL(mas)!=0):
            if(mas[len(mas)-1].card_rating==14):
                return mas
            else: return[]
         else:
             return []

     elif (len(check)==6):
        if len(s)==6:
         flag=1
         for i in range(1,5):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(1,6):
                 mas1.append(mas[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    if(mas1[len(mas1)-1].card_rating==14):
                        return mas1
                    else: return[]
             else:
                     return []
         else :
             return []

         flag=1
         for i in range(0,4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(0,5):
                 mas1.append(mas[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    if(mas1[len(mas1)-1].card_rating==14):
                        return mas1
                    else: return[]
             else:
                     return []
         else :
             return []
        elif(len(s)==5):
            s.sort(key=self.mySort)
            for i in range(4):
                if (s[i].card_rating)!=(s[i+1].card_rating-1):
                 return []
            if (self.check_fleshForSTRFL(s)!=0):
                    if(s[len(s)-1].card_rating==14):
                        return s
                    else: return[]
            else:
                     return []
        else:
            return[]
     elif (len(check)==7):
       if len(s)==7:
         flag=1
         for i in range(2,6):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(2,7):
                 mas1.append(mas[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    if(mas1[len(mas1)-1].card_rating==14):
                        return mas1
                    else: return[]
             else:
                     return []
         else :
             return []

         flag=1
         for i in range(1,5):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(1,6):
                 mas1.append(mas[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    if(mas1[len(mas1)-1].card_rating==14):
                        return mas1
                    else: return[]
             else:
                     return []
         else :
             return []

         flag=1
         for i in range(0,4):
             if mas[i].card_rating!=mas[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(0,5):
                 mas1.append(mas[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    if(mas1[len(mas1)-1].card_rating==14):
                        return mas1
                    else: return[]
             else:
                     return []
         else :
             return []
       elif(len(s)==6):
         s.sort(key=self.mySort)
         flag=1
         for i in range(1,5):
             if s[i].card_rating!=s[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(1,6):
                 mas1.append(s[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    if(mas1[len(mas1)-1].card_rating==14):
                        return mas1
                    else: return[]
             else:
                     return []
         else :
             return []

         flag=1
         for i in range(0,4):
             if s[i].card_rating!=s[i+1].card_rating-1:
                 flag=0
         if (flag==1):
             mas1=[]
             for i in range(0,5):
                 mas1.append(s[i])
             if (self.check_fleshForSTRFL(mas1)!=0):
                    if(mas1[len(mas1)-1].card_rating==14):
                        return mas1
                    else: return[]
             else:
                     return []
         else :
             return []
       elif(len(s)==5):
           s.sort(key=self.mySort)
           for i in range(4):
                if (s[i].card_rating)!=(s[i+1].card_rating-1):
                 return []
           if (self.check_fleshForSTRFL(s)!=0):
                    if(s[len(s)-1].card_rating==14):
                        return s
                    else: return[]
           else:
                     return []
       else:
           return []
 def kiker(self):
     mas1=self.myRatingCardWithTable.copy()
     mas1.sort()
     return mas1[mas1.__len__()-1]

 def mycombination(self, checkComb):
     t = checkComb.fleshRoyal()
     if t == []:
              t = checkComb.check_stritFlush()
              if t == []:
                             t = checkComb.check_kare()
                             if t == 0:
                                          t = checkComb.check_fullHouse()
                                          if t == 0:
                                                       t = checkComb.check_flesh()
                                                       if t == 0:
                                                                  t = checkComb.check_strit()
                                                                  if t == []:
                                                                              t = checkComb.check_set_trips()
                                                                              if t == 0:
                                                                                      t = checkComb.check_2para()
                                                                                      if t == []:
                                                                                             t = checkComb.check_para()
                                                                                             if t == 0:
                                                                                                     t = checkComb.kiker()
                                                                                                     return str("Only kiker :"+str(t))
                                                                                             else:
                                                                                                 return str("para : " + str(t))
                                                                                      else:
                                                                                         return str("2para : " + str(t[0]) + " " + str(t[1]))
                                                                              else:
                                                                                 return str(("set : " + str(t)))
                                                                  else:
                                                                     return str("strit : ")
                                                                    # for i in t:
                                                                     #    print(i.card_rating)
                                                       else:
                                                             return str("flesh: " + str(t))
                                          else:
                                                 return str("FH : " + str(t))
                             else:
                                    return str("kare : " + str(t))
              else:
                return str("SF : ")
               # for i in t:
                #   print(i.card_rating)
     else:
         return str("royal : ")
        # for i in t:
         #   print(i.card_rating)
 def mycombinationForOut(self,):
     t = self.fleshRoyal()
     if t == []:
              t = self.check_stritFlush()
              if t == []:
                             t = self.check_kare()
                             if t == 0:
                                          t = self.check_fullHouse()
                                          if t == 0:
                                                       t = self.check_flesh()
                                                       if t == 0:
                                                                  t = self.check_strit()
                                                                  if t == []:
                                                                              t = self.check_set_trips()
                                                                              if t == 0:
                                                                                      t = self.check_2para()
                                                                                      if t == []:
                                                                                             t = self.check_para()
                                                                                             if t == 0:
                                                                                                     t = self.kiker()
                                                                                                     return str("kiker")
                                                                                             else:
                                                                                                 return str("para")
                                                                                      else:
                                                                                         return str("2para")
                                                                              else:
                                                                                 return str("set")
                                                                  else:
                                                                     return str("strit")
                                                                    # for i in t:
                                                                     #    print(i.card_rating)
                                                       else:
                                                             return str("flesh")
                                          else:
                                                 return str("FH")
                             else:
                                    return str("kare")
              else:
                return str("SF")
               # for i in t:
                #   print(i.card_rating)
     else:
         return str("royal")
        # for i in t:
         #   print(i.card_rating)





#
# dd=Card()
# dd.__myinit__(1,14)
# d0=Card()
# d0.__myinit__(2,10)
# d1=Card()
# d1.__myinit__(2,13)
# d2=Card()
# d2.__myinit__(1,11)
# d3=Card()
# d3.__myinit__(1,12)
# d4=Card()
# d4.__myinit__(2,12)
# d7=Card()
# d7.__myinit__(2,14)
# carti=[dd,d0,d1,d3,d4,d7,d2]
# a=CheckComb(carti)
# t=a.check_flesh()
# if t==0:
#     print("net flesh ")
# else:
#     print("flesh: "+str(t))
#
# t=a.check_kare()
# if t==0:
#         print("net kare ")
# else:
#     print("kare : "+str(t))
#
# t=a.check_set_trips()
# if t==0:
#         print("net set ")
# else:
#     print("set : "+str(t))
#
# t=a.check_para()
# if t==0:
#         print("net pari ")
# else:
#     print("para : "+str(t))
#
# t=a.check_2para()
# if t==[]:
#         print("net 2pari ")
# else:
#     print("2para : "+str(t[0])+" "+str(t[1]))
#
# t=a.check_fullHouse()
# if t==0:
#         print("net FH ")
# else:
#     print("FH : "+str(t))
#
# t=a.check_strit()
# if t==[]:
#         print("net strit ")
# else:
#     print("strit : ")
#     for i in t:
#         print (i.card_rating)
#
# t=a.fleshRoyal()
# if t==[]:
#         print("net Royal ")
# else:
#     print("royal : ")
#     for i in t:
#         print (i.card_rating)
#
# t=a.check_stritFlush()
# if t==[]:
#         print("net SF ")
# else:
#     print("SF : ")
#     for i in t:
#         print (i.card_rating)
#


    # for i in t:
    #     print (i.card_suit)
    #     print (i.card_raiting)


