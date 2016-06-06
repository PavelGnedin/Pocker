# -*- coding:utf-8 -*-
__author__ = 'Павел'

import Player
from Player import Player

from Card import Card


class Game:
    def my__init__(self, amount_players,a,b,c,d):
        """
        Конструктор
        :rtype: object
        """
        self.myPlayer=Player()
        self.myPlayer.__myinitPlayer__(a,b,c,d)
    def __init__(self, amount_players):
        """
        Конструктор добавляющий определенное количество игроков
        :rtype: object
        """
        self.amount_players = amount_players
        self.players = []
        self.tableCards=[]
        self.myCardWithTable=[]

        self.koloda=[]
        for k in range(0,4):
            self.koloda.append([])
            for i in range(13):
                self.koloda[k].append(i+2)

        self.myPlayer = Player()
        self.myPlayer.__myinit__("MyPlayer")
        #self.myPlayer.__myinitPlayer__(2,13,3,13)
        self.players.append(self.myPlayer)

        for i in range(1,amount_players ):
            p=Player()
            for i in self.players:
              while():
                if(i.card1.card_rating==p.card1.card_rating and i.card1.card_suit==p.card1.card_suit or
                   (i.card2.card_rating==p.card2.card_rating and i.card2.card_suit==p.card2.card_suit) or
                        (i.card2.card_rating==p.card1.card_rating and i.card2.card_suit==p.card1.card_suit )or
                        (i.card1.card_rating==p.card2.card_rating and i.card1.card_suit==p.card2.card_suit)):
                    p=Player()
                else:
                    break
            self.players.append(p)
            print("ИГРОК "+str(p.card1.card_suit)+" "+str(p.card1.card_rating)+" "+str(p.card2.card_suit)+" "+str(p.card2.card_rating))

        self.myCardWithTable.append(self.myPlayer.card1)
        self.myCardWithTable.append(self.myPlayer.card2)

        ratingOFMyPlayerCard1=self.myPlayer.card1.card_rating
        suitOfMyPlayerCard1=self.myPlayer.card1.card_suit
        ratingOFMyPlayerCard2=self.myPlayer.card2.card_rating
        suitOfMyPlayerCard2=self.myPlayer.card2.card_suit
        # print (ratingOFMyPlayerCard1)
        # print (suitOfMyPlayerCard1)
        # print (ratingOFMyPlayerCard2)
        # print (suitOfMyPlayerCard2)
        self.koloda[suitOfMyPlayerCard1-1][ratingOFMyPlayerCard1-2]=0
        self.koloda[suitOfMyPlayerCard2-1][ratingOFMyPlayerCard2-2]=0




    def update_table_flopRandom(self):
        """
        Выложить первые 3 карты(случайно)
        :rtype: object
        """
        self.firstCommonCard=Card()
        while(True):
            if ((self.firstCommonCard.card_suit==self.myPlayer.card1.card_suit and
                self.firstCommonCard.card_rating==self.myPlayer.card1.card_rating)
                    or (self.firstCommonCard.card_suit==self.myPlayer.card2.card_suit
                    and self.firstCommonCard.card_rating==self.myPlayer.card2.card_rating)or

                (self.firstCommonCard.card_suit==self.players[1].card1.card_suit and
                self.firstCommonCard.card_rating==self.players[1].card1.card_rating)
                    or (self.firstCommonCard.card_suit==self.players[1].card2.card_suit
                    and self.firstCommonCard.card_rating==self.players[1].card2.card_rating)or

                (self.firstCommonCard.card_suit==self.players[2].card1.card_suit and
                self.firstCommonCard.card_rating==self.players[2].card1.card_rating)
                    or (self.firstCommonCard.card_suit==self.players[2].card2.card_suit
                    and self.firstCommonCard.card_rating==self.players[2].card2.card_rating)or

                (self.firstCommonCard.card_suit==self.players[3].card1.card_suit and
                self.firstCommonCard.card_rating==self.players[3].card1.card_rating)
                    or (self.firstCommonCard.card_suit==self.players[3].card2.card_suit
                    and self.firstCommonCard.card_rating==self.players[3].card2.card_rating)or

                (self.firstCommonCard.card_suit==self.players[4].card1.card_suit and
                self.firstCommonCard.card_rating==self.players[4].card1.card_rating)
                    or (self.firstCommonCard.card_suit==self.players[4].card2.card_suit
                    and self.firstCommonCard.card_rating==self.players[4].card2.card_rating)or

                (self.firstCommonCard.card_suit==self.players[5].card1.card_suit and
                self.firstCommonCard.card_rating==self.players[5].card1.card_rating)
                    or (self.firstCommonCard.card_suit==self.players[5].card2.card_suit
                    and self.firstCommonCard.card_rating==self.players[5].card2.card_rating)or

                (self.firstCommonCard.card_suit==self.players[6].card1.card_suit and
                self.firstCommonCard.card_rating==self.players[6].card1.card_rating)
                    or (self.firstCommonCard.card_suit==self.players[6].card2.card_suit
                    and self.firstCommonCard.card_rating==self.players[6].card2.card_rating)or

                (self.firstCommonCard.card_suit==self.players[7].card1.card_suit and
                self.firstCommonCard.card_rating==self.players[7].card1.card_rating)
                    or (self.firstCommonCard.card_suit==self.players[7].card2.card_suit
                    and self.firstCommonCard.card_rating==self.players[7].card2.card_rating)or

                (self.firstCommonCard.card_suit==self.players[8].card1.card_suit and
                self.firstCommonCard.card_rating==self.players[8].card1.card_rating)
                    or (self.firstCommonCard.card_suit==self.players[8].card2.card_suit
                    and self.firstCommonCard.card_rating==self.players[8].card2.card_rating)or

                (self.firstCommonCard.card_suit==self.players[9].card1.card_suit and
                self.firstCommonCard.card_rating==self.players[9].card1.card_rating)
                    or (self.firstCommonCard.card_suit==self.players[9].card2.card_suit
                    and self.firstCommonCard.card_rating==self.players[9].card2.card_rating)):
                self.firstCommonCard=Card()
            else:
                break
        self.secondCommonCard=Card()
        while(True):
            if ((self.secondCommonCard.card_suit==self.myPlayer.card1.card_suit and
                self.secondCommonCard.card_rating==self.myPlayer.card1.card_rating)
                    or (self.secondCommonCard.card_suit==self.myPlayer.card2.card_suit
                    and self.secondCommonCard.card_rating==self.myPlayer.card2.card_rating)or
                    (self.secondCommonCard.card_rating==self.firstCommonCard.card_rating and
                             self.secondCommonCard.card_suit==self.firstCommonCard.card_suit)):
                self.secondCommonCard=Card()
            else:
                break
        self.thirdCommonCard=Card()
        while(True):
            if ((self.thirdCommonCard.card_suit==self.myPlayer.card1.card_suit and
                self.thirdCommonCard.card_rating==self.myPlayer.card1.card_rating)
                    or (self.thirdCommonCard.card_suit==self.myPlayer.card2.card_suit
                    and self.thirdCommonCard.card_rating==self.myPlayer.card2.card_rating)|
                    (self.thirdCommonCard.card_suit==self.firstCommonCard.card_suit and
                     self.thirdCommonCard.card_rating==self.firstCommonCard.card_rating)|
                    (self.thirdCommonCard.card_suit==self.secondCommonCard.card_suit and
                     self.thirdCommonCard.card_rating==self.secondCommonCard.card_rating)):
                self.thirdCommonCard=Card()
            else:
                break

        self.tableCards.append(self.firstCommonCard)
        self.tableCards.append(self.secondCommonCard)
        self.tableCards.append(self.thirdCommonCard)
        self.myCardWithTable.extend(self.tableCards)

        firstComCardSuit=self.firstCommonCard.card_suit
        firstComCardRating=self.firstCommonCard.card_rating
        self.koloda[firstComCardSuit-1][firstComCardRating-2]=0

        secondComCardSuit=self.secondCommonCard.card_suit
        secondComCardRating=self.secondCommonCard.card_rating
        self.koloda[secondComCardSuit-1][secondComCardRating-2]=0

        thirdComCardSuit=self.thirdCommonCard.card_suit
        thirdComCardRating=self.thirdCommonCard.card_rating
        self.koloda[thirdComCardSuit-1][thirdComCardRating-2]=0

    def update_table_flop(self,card1,card2,card3):
        """
        Выложить конкретные 3 карты на флоп
        :rtype: object
        """
        self.firstCommonCard=card1
        while(True):
            if ((self.firstCommonCard.card_suit==self.myPlayer.card1.card_suit and
                self.firstCommonCard.card_rating==self.myPlayer.card1.card_rating)
                    or(self.firstCommonCard.card_suit==self.myPlayer.card2.card_suit
                    and self.firstCommonCard.card_rating==self.myPlayer.card2.card_rating)):
                self.firstCommonCard=card1
            else:
                break
        self.secondCommonCard=card2
        while(True):
            if ((self.secondCommonCard.card_suit==self.myPlayer.card1.card_suit and
                self.secondCommonCard.card_rating==self.myPlayer.card1.card_rating)
                    or (self.secondCommonCard.card_suit==self.myPlayer.card2.card_suit
                    and self.secondCommonCard.card_rating==self.myPlayer.card2.card_rating)):
                self.secondCommonCard=card2
            else:
                break
        self.thirdCommonCard=card3
        while(True):
            if ((self.thirdCommonCard.card_suit==self.myPlayer.card1.card_suit and
                self.thirdCommonCard.card_rating==self.myPlayer.card1.card_rating)
                    or(self.thirdCommonCard.card_suit==self.myPlayer.card2.card_suit
                    and self.thirdCommonCard.card_rating==self.myPlayer.card2.card_rating)):
                self.thirdCommonCard=card3
            else:
                break

        self.tableCards.append(self.firstCommonCard)
        self.tableCards.append(self.secondCommonCard)
        self.tableCards.append(self.thirdCommonCard)
        self.myCardWithTable.append()
        self.myCardWithTable.extend(self.tableCards)


        firstComCardSuit=self.firstCommonCard.card_suit
        firstComCardRating=self.firstCommonCard.card_rating
        self.koloda[firstComCardSuit-1][firstComCardRating-2]=0

        secondComCardSuit=self.secondCommonCard.card_suit
        secondComCardRating=self.secondCommonCard.card_rating
        self.koloda[secondComCardSuit-1][secondComCardRating-2]=0

        thirdComCardSuit=self.thirdCommonCard.card_suit
        thirdComCardRating=self.thirdCommonCard.card_rating
        self.koloda[thirdComCardSuit-1][thirdComCardRating-2]=0

    def update_table_ternRandom(self):
        """
        Выложить терн карту(случайно)
        :rtype: object
        """
        self.fourthCommonCard=Card()
        while(True):
            if ((self.fourthCommonCard.card_suit==self.myPlayer.card1.card_suit and
                self.fourthCommonCard.card_rating==self.myPlayer.card1.card_rating)
                    or(self.fourthCommonCard.card_suit==self.myPlayer.card2.card_suit
                    and self.fourthCommonCard.card_rating==self.myPlayer.card2.card_rating)or
                (self.fourthCommonCard.card_suit==self.tableCards[0].card_suit and
                self.fourthCommonCard.card_rating==self.tableCards[0].card_rating)or
                    (self.fourthCommonCard.card_suit==self.tableCards[1].card_suit and
                self.fourthCommonCard.card_rating==self.tableCards[1].card_rating)or
                (self.fourthCommonCard.card_suit==self.tableCards[2].card_suit and
                self.fourthCommonCard.card_rating==self.tableCards[2].card_rating)):
                    self.fourthCommonCard=Card()
            else:
                break
        self.tableCards.append(self.fourthCommonCard)

        self.myCardWithTable.append(self.fourthCommonCard)

        fourthComCardSuit=self.fourthCommonCard.card_suit
        fourthComCardRating=self.fourthCommonCard.card_rating
        self.koloda[fourthComCardSuit-1][fourthComCardRating-2]=0


    def update_table_tern(self,card4):
        """
        Выложить терн карту(конкретную)
        :rtype: object
        """
        self.fourthCommonCard=card4
        while(True):
            if ((self.fourthCommonCard.card_suit==self.myPlayer.card1.card_suit and
                self.fourthCommonCard.card_rating==self.myPlayer.card1.card_rating)
                    and (self.fourthCommonCard.card_suit==self.myPlayer.card2.card_suit
                    and self.fourthCommonCard.card_rating==self.myPlayer.card2.card_rating)or
                (self.fourthCommonCard.card_suit==self.tableCards[0].card_suit and
                self.fourthCommonCard.card_rating==self.tableCards[0].card_rating)or
                    (self.fourthCommonCard.card_suit==self.tableCards[1].card_suit and
                self.fourthCommonCard.card_rating==self.tableCards[1].card_rating)or
                (self.fourthCommonCard.card_suit==self.tableCards[2].card_suit and
                self.fourthCommonCard.card_rating==self.tableCards[2].card_rating)):
                    self.fourthCommonCard=Card()
            else:
                break

        self.tableCards.append(self.fourthCommonCard)

        self.myCardWithTable.append(self.fourthCommonCard)

        fourthComCardSuit=self.fourthCommonCard.card_suit
        fourthComCardRating=self.fourthCommonCard.card_rating
        self.koloda[fourthComCardSuit-1][fourthComCardRating-2]=0

    def update_table_riverRandom(self):
        """
        Выложить ривер карту(случайно)
        :rtype: object
        """
        self.fifthCommonCard=Card()
        while(1):
            if ((self.fifthCommonCard.card_suit==self.myPlayer.card1.card_suit and
                self.fifthCommonCard.card_rating==self.myPlayer.card1.card_rating)
                    or(self.fifthCommonCard.card_suit==self.myPlayer.card2.card_suit
                    and self.fifthCommonCard.card_rating==self.myPlayer.card2.card_rating)or
                (self.fifthCommonCard.card_suit==self.tableCards[0].card_suit and
                self.fifthCommonCard.card_rating==self.tableCards[0].card_rating)or
                    (self.fifthCommonCard.card_suit==self.tableCards[1].card_suit and
                self.fifthCommonCard.card_rating==self.tableCards[1].card_rating)or
                (self.fifthCommonCard.card_suit==self.tableCards[2].card_suit and
                self.fifthCommonCard.card_rating==self.tableCards[2].card_rating)or
                (self.fifthCommonCard.card_suit==self.tableCards[3].card_suit and
                self.fifthCommonCard.card_rating==self.tableCards[3].card_rating)):
                    self.fifthCommonCard=Card()
            else:
                break
        self.tableCards.append(self.fifthCommonCard)

        self.myCardWithTable.append(self.fifthCommonCard)

        fifthComCardSuit=self.fifthCommonCard.card_suit
        fifthComCardRating=self.fifthCommonCard.card_rating
        self.koloda[fifthComCardSuit-1][fifthComCardRating-2]=0

    def update_table_river(self,card5):
        """
        Выложить ривер карту(конкретную)
        :rtype: object
        """
        while(True):
            self.fifthCommonCard=card5
            if ((self.fifthCommonCard.card_suit==self.myPlayer.card1.card_suit and
                self.fifthCommonCard.card_rating==self.myPlayer.card1.card_rating)
                    or(self.fifthCommonCard.card_suit==self.myPlayer.card2.card_suit
                    and self.fifthCommonCard.card_rating==self.myPlayer.card2.card_rating)or
                (self.fifthCommonCard.card_suit==self.tableCards[0].card_suit and
                self.fifthCommonCard.card_rating==self.tableCards[0].card_rating)or
                    (self.fifthCommonCard.card_suit==self.tableCards[1].card_suit and
                self.fifthCommonCard.card_rating==self.tableCards[1].card_rating)or
                (self.fifthCommonCard.card_suit==self.tableCards[2].card_suit and
                self.fifthCommonCard.card_rating==self.tableCards[2].card_rating)or
                (self.fifthCommonCard.card_suit==self.tableCards[3].card_suit and
                self.fifthCommonCard.card_rating==self.tableCards[3].card_rating)):
                self.fifthCommonCard=Card()
            else:
                break

        self.tableCards.append(self.fifthCommonCard)

        self.myCardWithTable.append(self.fifthCommonCard)

        fifthComCardSuit=self.fifthCommonCard.card_suit
        fifthComCardRating=self.fifthCommonCard.card_rating
        self.koloda[fifthComCardSuit-1][fifthComCardRating-2]=0

# for i in range(9):
#     game=Game(5)
#     mas=game.koloda
# # for i in game.koloda:
# #         print(i)
#     game.update_table_flopRandom()
# print("CARDS :")
# for i in game.koloda:
#         print(i)
# for i in game.myCardWithTable:
#     print(i.card_suit)
#     print(i.card_rating)
# print("table cards: ")
# for i in game.tableCards:
#     print (i.card_suit)
#     print(i.card_rating)

# print("TERN: ")
#     game.update_table_ternRandom()
# # for i in game.tableCards:
# #     print (i.card_suit)
# #     print(i.card_rating)
# #
# # for i in game.koloda:
# #     print(i)
#
# # print("River: ")
#     game.update_table_riverRandom()
# # for i in game.tableCards:
# #     print (i.card_suit)
# #     print(i.card_rating)
# #
# # for i in game.koloda:
# #     print(i)
#     o=0
#     for i in game.koloda:
#      for j in i:
#         if(j==0):
#            o=o+1
#     print (o)
# print("flop: ")
# game.update_table_flopRandom()
# print(game.firstCommonCard.card_suit)
# print(game.firstCommonCard.card_rating)
# print(game.secondCommonCard.card_suit)
# print(game.secondCommonCard.card_rating)
# print(game.thirdCommonCard.card_suit)
# print(game.thirdCommonCard.card_rating)
# for i in game.koloda:
#     print(i)