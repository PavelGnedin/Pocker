# -*- coding:utf-8 -*-
__author__ = 'Павел'


class CheckHoleCards:
     def __init__(self,card1,card2,position,players,action):
         self.card1=card1
         self.card2=card2
         self.position=position
         self.players=players
         self.action=action
     def check_position(self):
       if self.players>=8:
         if(self.position=="BigBlind" or self.position=="smallBlind"):
             return "blind_position"
         elif (self.position=="diler" or self.position=="cutOff"):
             return "pozd_position"
         elif(self.position=="utg" or self.position=="utg1"or self.position=="utg2"):
             return "rannie_position"
         else :
             return "srednie_position"
       # elif (self.players>=4):
       #   if(self.position=="BigBlind" or self.position=="smallBlind"):
       #       return "blind_position"
       #   elif (self.position=="diler" or self.position=="cutOff"):
       #       return "pozd_osition"
       #   else :
       #       return "srednie_position"



     def check_odnomast(self):
         if(self.card1.card_suit==self.card2.card_suit):
             return True
         else:
             return False


     def check_power(self):
         self.powerPosition=self.check_position()
         if self.powerPosition=="blind_position":
             if((self.card1.card_rating==14 and self.card2.card_rating==14) or (self.card1.card_rating==13 and self.card2.card_rating==13)or
                (self.card1.card_rating==12 and self.card2.card_rating==12)):
                 return "You have a MONSTER!Raise!"
             elif (self.card1.card_rating==11 and self.card2.card_rating==11) or (self.card1.card_rating==10 and self.card2.card_rating==10):
                 if self.action=="act_raise":
                     return "Call !"
                 else:
                    return "Raise !"
             elif ((self.card1.card_rating==9 and self.card2.card_rating==9) or (self.card1.card_rating==8 and self.card2.card_rating==8)or
                (self.card1.card_rating==7 and self.card2.card_rating==7) or (self.card1.card_rating==6 and self.card2.card_rating==6)
                or (self.card1.card_rating==5 and self.card2.card_rating==5)or
                (self.card1.card_rating==4 and self.card2.card_rating==4)
                or (self.card1.card_rating==3 and self.card2.card_rating==3)or
                (self.card1.card_rating==2 and self.card2.card_rating==2)):
                if self.action=="act_fall":
                    return "Call !"
                elif self.action=="act_call":
                    return "Call !"
                else:
                   return "Call !"

             elif ((self.card1.card_rating==14 and self.card2.card_rating==13) or (self.card1.card_rating==13 and self.card2.card_rating==14)):
                 return "Raise !"
             elif ((self.card1.card_rating==14 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==14)):
                if self.action=="act_fall":
                    return "Raise !"
                elif self.action=="act_call":
                    return "Call !"
                else:
                   return "Fall !"
             elif(self.check_odnomast()==True):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"

                 elif ((self.card1.card_rating==14 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==14)or
                     (self.card1.card_rating==14 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==14)or
                    (self.card1.card_rating==14 and self.card2.card_rating==3) or (self.card1.card_rating==3 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==2) or (self.card1.card_rating==2 and self.card2.card_rating==14)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"

                 elif  ((self.card1.card_rating==10 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==10)or
                   (self.card1.card_rating==9 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==9)or
                   (self.card1.card_rating==8 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==8)or
                     (self.card1.card_rating==7 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==7)or
                   (self.card1.card_rating==6 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==6)or
                   (self.card1.card_rating==5 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==5)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             elif(self.check_odnomast()==False):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"

             else:
                    print("ALLILUYA!")
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"



         elif self.powerPosition=="pozd_position":
             if((self.card1.card_rating==14 and self.card2.card_rating==14) or (self.card1.card_rating==13 and self.card2.card_rating==13)or
                (self.card1.card_rating==12 and self.card2.card_rating==12)):
                 return "You have a MONSTER!Raise!"
             elif (self.card1.card_rating==11 and self.card2.card_rating==11) or (self.card1.card_rating==10 and self.card2.card_rating==10):
                 if self.action=="act_raise":
                     return "Call !"
                 else:
                    return "Raise !"
             elif ((self.card1.card_rating==9 and self.card2.card_rating==9) or (self.card1.card_rating==8 and self.card2.card_rating==8)or
                (self.card1.card_rating==7 and self.card2.card_rating==7) or (self.card1.card_rating==6 and self.card2.card_rating==6)
                or (self.card1.card_rating==5 and self.card2.card_rating==5)or
                (self.card1.card_rating==4 and self.card2.card_rating==4)
                or (self.card1.card_rating==3 and self.card2.card_rating==3)or
                (self.card1.card_rating==2 and self.card2.card_rating==2)):
                if self.action=="act_fall":
                    return "Raise !"
                elif self.action=="act_call":
                    return "Call !"
                else:
                   return "Call !"

             elif ((self.card1.card_rating==14 and self.card2.card_rating==13) or (self.card1.card_rating==13 and self.card2.card_rating==14)):
                 return "Raise !"
             elif ((self.card1.card_rating==14 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==14)):
                if self.action=="act_fall":
                    return "Raise !"
                elif self.action=="act_call":
                    return "Raise !"
                else:
                   return "Fall !"
             elif(self.check_odnomast()==True):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"

                 elif ((self.card1.card_rating==14 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==14)or
                     (self.card1.card_rating==14 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==14)or
                    (self.card1.card_rating==14 and self.card2.card_rating==3) or (self.card1.card_rating==3 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==2) or (self.card1.card_rating==2 and self.card2.card_rating==14)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"

                 elif  ((self.card1.card_rating==10 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==10)or
                   (self.card1.card_rating==9 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==9)or
                   (self.card1.card_rating==8 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==8)or
                     (self.card1.card_rating==7 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==7)or
                   (self.card1.card_rating==6 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==6)or
                   (self.card1.card_rating==5 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==5)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             elif(self.check_odnomast()==False):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             else:
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"







         elif self.powerPosition=="rannie_position":
             if((self.card1.card_rating==14 and self.card2.card_rating==14) or (self.card1.card_rating==13 and self.card2.card_rating==13)or
                (self.card1.card_rating==12 and self.card2.card_rating==12)):
                 return "You have a MONSTER!Raise!"
             elif (self.card1.card_rating==11 and self.card2.card_rating==11) or (self.card1.card_rating==10 and self.card2.card_rating==10):
                 if self.action=="act_raise":
                     return "Call !"
                 else:
                    return "Raise !"
             elif ((self.card1.card_rating==9 and self.card2.card_rating==9) or (self.card1.card_rating==8 and self.card2.card_rating==8)or
                (self.card1.card_rating==7 and self.card2.card_rating==7) or (self.card1.card_rating==6 and self.card2.card_rating==6)
                or (self.card1.card_rating==5 and self.card2.card_rating==5)or
                (self.card1.card_rating==4 and self.card2.card_rating==4)
                or (self.card1.card_rating==3 and self.card2.card_rating==3)or
                (self.card1.card_rating==2 and self.card2.card_rating==2)):
                if self.action=="act_fall":
                    return "Fall !"
                elif self.action=="act_call":
                    return "Fall !"
                else:
                   return "Fall !"

             elif ((self.card1.card_rating==14 and self.card2.card_rating==13) or (self.card1.card_rating==13 and self.card2.card_rating==14)):
                 return "Raise !"


             elif ((self.card1.card_rating==14 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==14)):
                if self.action=="act_fall":
                    return "Fall !"
                elif self.action=="act_call":
                    return "Fall !"
                else:
                   return "Fall !"
             elif(self.check_odnomast()==True):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"


                 elif ((self.card1.card_rating==14 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==14)or
                     (self.card1.card_rating==14 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==14)or
                    (self.card1.card_rating==14 and self.card2.card_rating==3) or (self.card1.card_rating==3 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==2) or (self.card1.card_rating==2 and self.card2.card_rating==14)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"

                 elif  ((self.card1.card_rating==10 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==10)or
                   (self.card1.card_rating==9 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==9)or
                   (self.card1.card_rating==8 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==8)or
                     (self.card1.card_rating==7 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==7)or
                   (self.card1.card_rating==6 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==6)or
                   (self.card1.card_rating==5 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==5)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             elif(self.check_odnomast()==False):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             else:
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"





         elif self.powerPosition=="srednie_position":
             if((self.card1.card_rating==14 and self.card2.card_rating==14) or (self.card1.card_rating==13 and self.card2.card_rating==13)or
                (self.card1.card_rating==12 and self.card2.card_rating==12)):
                 return "You have a MONSTER!Raise!"
             elif (self.card1.card_rating==11 and self.card2.card_rating==11) or (self.card1.card_rating==10 and self.card2.card_rating==10):
                 if self.action=="act_raise":
                     return "Call !"
                 else:
                    return "Raise !"
             elif ((self.card1.card_rating==9 and self.card2.card_rating==9) or (self.card1.card_rating==8 and self.card2.card_rating==8)or
                (self.card1.card_rating==7 and self.card2.card_rating==7) or (self.card1.card_rating==6 and self.card2.card_rating==6)
                or (self.card1.card_rating==5 and self.card2.card_rating==5)or
                (self.card1.card_rating==4 and self.card2.card_rating==4)
                or (self.card1.card_rating==3 and self.card2.card_rating==3)or
                (self.card1.card_rating==2 and self.card2.card_rating==2)):
                if self.action=="act_fall":
                    return "Call !"
                elif self.action=="act_call":
                    return "Call !"
                else:
                   return "Call !"

             elif ((self.card1.card_rating==14 and self.card2.card_rating==13) or (self.card1.card_rating==13 and self.card2.card_rating==14)):
                 return "Raise !"


             elif ((self.card1.card_rating==14 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==14)):
                if self.action=="act_fall":
                    return "Raise !"
                elif self.action=="act_call":
                    return "Fall !"
                else:
                   return "Fall !"
             elif(self.check_odnomast()==True):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"

                 elif ((self.card1.card_rating==14 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==14)or
                     (self.card1.card_rating==14 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==14)or
                    (self.card1.card_rating==14 and self.card2.card_rating==3) or (self.card1.card_rating==3 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==2) or (self.card1.card_rating==2 and self.card2.card_rating==14)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"

                 elif  ((self.card1.card_rating==10 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==10)or
                   (self.card1.card_rating==9 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==9)or
                   (self.card1.card_rating==8 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==8)or
                     (self.card1.card_rating==7 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==7)or
                   (self.card1.card_rating==6 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==6)or
                   (self.card1.card_rating==5 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==5)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             elif(self.check_odnomast()==False):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             else:
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"


class CheckHoleCardsForBot:
     def __init__(self,card1,card2,position,players,action):
         self.card1=card1
         self.card2=card2
         self.position=position
         self.players=players
         self.action=action
     def check_position(self):
       if self.players>=8:
         if(self.position=="BigBlind" or self.position=="smallBlind"):
             return "blind_position"
         elif (self.position=="diler" or self.position=="cutOff"):
             return "pozd_position"
         elif(self.position=="utg" or self.position=="utg1"or self.position=="utg2"):
             return "rannie_position"
         else :
             return "srednie_position"
       # elif (self.players>=4):
       #   if(self.position=="BigBlind" or self.position=="smallBlind"):
       #       return "blind_position"
       #   elif (self.position=="diler" or self.position=="cutOff"):
       #       return "pozd_osition"
       #   else :
       #       return "srednie_position"



     def check_odnomast(self):
         if(self.card1.card_suit==self.card2.card_suit):
             return True
         else:
             return False


     def check_power(self):
         self.powerPosition=self.check_position()
         if self.powerPosition=="blind_position":
             if((self.card1.card_rating==14 and self.card2.card_rating==14) or (self.card1.card_rating==13 and self.card2.card_rating==13)or
                (self.card1.card_rating==12 and self.card2.card_rating==12)):
                 return "Raise !"
             elif (self.card1.card_rating==11 and self.card2.card_rating==11) or (self.card1.card_rating==10 and self.card2.card_rating==10):
                 if self.action=="act_raise":
                     return "Call !"
                 else:
                    return "Raise !"
             elif ((self.card1.card_rating==9 and self.card2.card_rating==9) or (self.card1.card_rating==8 and self.card2.card_rating==8)or
                (self.card1.card_rating==7 and self.card2.card_rating==7) or (self.card1.card_rating==6 and self.card2.card_rating==6)
                or (self.card1.card_rating==5 and self.card2.card_rating==5)or
                (self.card1.card_rating==4 and self.card2.card_rating==4)
                or (self.card1.card_rating==3 and self.card2.card_rating==3)or
                (self.card1.card_rating==2 and self.card2.card_rating==2)):
                if self.action=="act_fall":
                    return "Call !"
                elif self.action=="act_call":
                    return "Call !"
                else:
                   return "Call !"

             elif ((self.card1.card_rating==14 and self.card2.card_rating==13) or (self.card1.card_rating==13 and self.card2.card_rating==14)):
                 return "Raise !"
             elif ((self.card1.card_rating==14 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==14)):
                if self.action=="act_fall":
                    return "Raise !"
                elif self.action=="act_call":
                    return "Call !"
                else:
                   return "Fall !"
             elif(self.check_odnomast()==True):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"

                 elif ((self.card1.card_rating==14 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==14)or
                     (self.card1.card_rating==14 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==14)or
                    (self.card1.card_rating==14 and self.card2.card_rating==3) or (self.card1.card_rating==3 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==2) or (self.card1.card_rating==2 and self.card2.card_rating==14)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"

                 elif  ((self.card1.card_rating==10 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==10)or
                   (self.card1.card_rating==9 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==9)or
                   (self.card1.card_rating==8 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==8)or
                     (self.card1.card_rating==7 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==7)or
                   (self.card1.card_rating==6 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==6)or
                   (self.card1.card_rating==5 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==5)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             elif(self.check_odnomast()==False):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"

             else:
                    print("ALLILUYA!")
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"



         elif self.powerPosition=="pozd_position":
             if((self.card1.card_rating==14 and self.card2.card_rating==14) or (self.card1.card_rating==13 and self.card2.card_rating==13)or
                (self.card1.card_rating==12 and self.card2.card_rating==12)):
                 return "Raise !"
             elif (self.card1.card_rating==11 and self.card2.card_rating==11) or (self.card1.card_rating==10 and self.card2.card_rating==10):
                 if self.action=="act_raise":
                     return "Call !"
                 else:
                    return "Raise !"
             elif ((self.card1.card_rating==9 and self.card2.card_rating==9) or (self.card1.card_rating==8 and self.card2.card_rating==8)or
                (self.card1.card_rating==7 and self.card2.card_rating==7) or (self.card1.card_rating==6 and self.card2.card_rating==6)
                or (self.card1.card_rating==5 and self.card2.card_rating==5)or
                (self.card1.card_rating==4 and self.card2.card_rating==4)
                or (self.card1.card_rating==3 and self.card2.card_rating==3)or
                (self.card1.card_rating==2 and self.card2.card_rating==2)):
                if self.action=="act_fall":
                    return "Raise !"
                elif self.action=="act_call":
                    return "Call !"
                else:
                   return "Call !"

             elif ((self.card1.card_rating==14 and self.card2.card_rating==13) or (self.card1.card_rating==13 and self.card2.card_rating==14)):
                 return "Raise !"
             elif ((self.card1.card_rating==14 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==14)):
                if self.action=="act_fall":
                    return "Raise !"
                elif self.action=="act_call":
                    return "Raise !"
                else:
                   return "Fall !"
             elif(self.check_odnomast()==True):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"

                 elif ((self.card1.card_rating==14 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==14)or
                     (self.card1.card_rating==14 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==14)or
                    (self.card1.card_rating==14 and self.card2.card_rating==3) or (self.card1.card_rating==3 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==2) or (self.card1.card_rating==2 and self.card2.card_rating==14)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"

                 elif  ((self.card1.card_rating==10 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==10)or
                   (self.card1.card_rating==9 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==9)or
                   (self.card1.card_rating==8 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==8)or
                     (self.card1.card_rating==7 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==7)or
                   (self.card1.card_rating==6 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==6)or
                   (self.card1.card_rating==5 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==5)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             elif(self.check_odnomast()==False):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Raise !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             else:
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"







         elif self.powerPosition=="rannie_position":
             if((self.card1.card_rating==14 and self.card2.card_rating==14) or (self.card1.card_rating==13 and self.card2.card_rating==13)or
                (self.card1.card_rating==12 and self.card2.card_rating==12)):
                 return "Raise !"
             elif (self.card1.card_rating==11 and self.card2.card_rating==11) or (self.card1.card_rating==10 and self.card2.card_rating==10):
                 if self.action=="act_raise":
                     return "Call !"
                 else:
                    return "Raise !"
             elif ((self.card1.card_rating==9 and self.card2.card_rating==9) or (self.card1.card_rating==8 and self.card2.card_rating==8)or
                (self.card1.card_rating==7 and self.card2.card_rating==7) or (self.card1.card_rating==6 and self.card2.card_rating==6)
                or (self.card1.card_rating==5 and self.card2.card_rating==5)or
                (self.card1.card_rating==4 and self.card2.card_rating==4)
                or (self.card1.card_rating==3 and self.card2.card_rating==3)or
                (self.card1.card_rating==2 and self.card2.card_rating==2)):
                if self.action=="act_fall":
                    return "Fall !"
                elif self.action=="act_call":
                    return "Fall !"
                else:
                   return "Fall !"

             elif ((self.card1.card_rating==14 and self.card2.card_rating==13) or (self.card1.card_rating==13 and self.card2.card_rating==14)):
                 return "Raise !"


             elif ((self.card1.card_rating==14 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==14)):
                if self.action=="act_fall":
                    return "Fall !"
                elif self.action=="act_call":
                    return "Fall !"
                else:
                   return "Fall !"
             elif(self.check_odnomast()==True):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"


                 elif ((self.card1.card_rating==14 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==14)or
                     (self.card1.card_rating==14 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==14)or
                    (self.card1.card_rating==14 and self.card2.card_rating==3) or (self.card1.card_rating==3 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==2) or (self.card1.card_rating==2 and self.card2.card_rating==14)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"

                 elif  ((self.card1.card_rating==10 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==10)or
                   (self.card1.card_rating==9 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==9)or
                   (self.card1.card_rating==8 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==8)or
                     (self.card1.card_rating==7 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==7)or
                   (self.card1.card_rating==6 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==6)or
                   (self.card1.card_rating==5 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==5)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             elif(self.check_odnomast()==False):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             else:
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"





         elif self.powerPosition=="srednie_position":
             if((self.card1.card_rating==14 and self.card2.card_rating==14) or (self.card1.card_rating==13 and self.card2.card_rating==13)or
                (self.card1.card_rating==12 and self.card2.card_rating==12)):
                 return "You have a MONSTER!Raise!"
             elif (self.card1.card_rating==11 and self.card2.card_rating==11) or (self.card1.card_rating==10 and self.card2.card_rating==10):
                 if self.action=="act_raise":
                     return "Call !"
                 else:
                    return "Raise !"
             elif ((self.card1.card_rating==9 and self.card2.card_rating==9) or (self.card1.card_rating==8 and self.card2.card_rating==8)or
                (self.card1.card_rating==7 and self.card2.card_rating==7) or (self.card1.card_rating==6 and self.card2.card_rating==6)
                or (self.card1.card_rating==5 and self.card2.card_rating==5)or
                (self.card1.card_rating==4 and self.card2.card_rating==4)
                or (self.card1.card_rating==3 and self.card2.card_rating==3)or
                (self.card1.card_rating==2 and self.card2.card_rating==2)):
                if self.action=="act_fall":
                    return "Call !"
                elif self.action=="act_call":
                    return "Call !"
                else:
                   return "Call !"

             elif ((self.card1.card_rating==14 and self.card2.card_rating==13) or (self.card1.card_rating==13 and self.card2.card_rating==14)):
                 return "Raise !"


             elif ((self.card1.card_rating==14 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==14)):
                if self.action=="act_fall":
                    return "Raise !"
                elif self.action=="act_call":
                    return "Fall !"
                else:
                   return "Fall !"
             elif(self.check_odnomast()==True):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"

                 elif ((self.card1.card_rating==14 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==14)or
                     (self.card1.card_rating==14 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==14)or
                    (self.card1.card_rating==14 and self.card2.card_rating==3) or (self.card1.card_rating==3 and self.card2.card_rating==14)or
                   (self.card1.card_rating==14 and self.card2.card_rating==2) or (self.card1.card_rating==2 and self.card2.card_rating==14)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"

                 elif  ((self.card1.card_rating==10 and self.card2.card_rating==9) or (self.card1.card_rating==9 and self.card2.card_rating==10)or
                   (self.card1.card_rating==9 and self.card2.card_rating==8) or (self.card1.card_rating==8 and self.card2.card_rating==9)or
                   (self.card1.card_rating==8 and self.card2.card_rating==7) or (self.card1.card_rating==7 and self.card2.card_rating==8)or
                     (self.card1.card_rating==7 and self.card2.card_rating==6) or (self.card1.card_rating==6 and self.card2.card_rating==7)or
                   (self.card1.card_rating==6 and self.card2.card_rating==5) or (self.card1.card_rating==5 and self.card2.card_rating==6)or
                   (self.card1.card_rating==5 and self.card2.card_rating==4) or (self.card1.card_rating==4 and self.card2.card_rating==5)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Call !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             elif(self.check_odnomast()==False):
                 if ((self.card1.card_rating==13 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==11) or (self.card1.card_rating==11 and self.card2.card_rating==13)or
                   (self.card1.card_rating==13 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==13)or
                     (self.card1.card_rating==11 and self.card2.card_rating==12) or (self.card1.card_rating==12 and self.card2.card_rating==11)or
                   (self.card1.card_rating==12 and self.card2.card_rating==10) or (self.card1.card_rating==12 and self.card2.card_rating==10)or
                   (self.card1.card_rating==11 and self.card2.card_rating==10) or (self.card1.card_rating==10 and self.card2.card_rating==11)):
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"
                 else:
                     return "Fall !"
             else:
                    if self.action=="act_fall":
                          return "Fall !"
                    elif self.action=="act_call":
                          return "Fall !"
                    else:
                          return "Fall !"
# card1=Card()
# print ("card 1: suite :"+str(card1.card_suit)+" rating :"+str(card1.card_rating))
# card2=Card()
# print ("card 2: suite :"+str(card2.card_suit)+" rating :"+str(card2.card_rating))
# players=10
# action="act_call"
# position="smallBlind"
#
# f=CheckHoleCards(card1,card2,position,players,action)
# str=f.check_power()
# print (str)