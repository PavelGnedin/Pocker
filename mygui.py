# -*- coding:utf-8 -*-
import tkinter
from tkinter import *

import math

from CheckHOLEcards import CheckHoleCards
from  CheckHOLEcards import CheckHoleCardsForBot
from  CheckOuts import CheckOuts
from  Game import Game
from  checkCombOnHand import CheckComb

class Diler:
    def __init__(self):
        self.flagOfblind=0
        self.flagofDiler=0
        self.flagOfCall=False
        self.mystavka=0
        self.flagOfBet=False
        self.flagGetWinner=0
        self.flagRound=0
        self.botpower=0
        self.flagOfReStavka=0
        self.flagofbet = 0
        self.stavka = 0
        self.amount_players = 10
        self.bankStack = 0
        self.myPlayerstack = 2000
        self.player1Stack = 2000
        self.player2Stack = 2000
        self.player3Stack = 2000
        self.player4Stack = 2000
        self.player5Stack = 2000
        self.player6Stack = 2000
        self.player7Stack = 2000
        self.player8Stack = 2000
        self.player9Stack = 2000
        self.flagstep = 0
        if (self.amount_players == 10):
            self.diler = 0
            self.smallBlind = self.diler + 1
            self.BigBlind = self.diler + 2
            self.utg = self.diler + 3
            self.utg1 = self.diler + 4
            self.utg2 = self.diler + 5
            self.utg3 = self.diler + 6
            self.utg4 = self.diler + 7
            self.cutOff = self.amount_players - 1
            self.hiJack = self.amount_players - 2
        elif (self.amount_players == 9):
            self.diler = 0
            self.smallBlind = self.diler + 1
            self.BigBlind = self.diler + 2
            self.utg = self.diler + 3
            self.utg1 = self.diler + 4
            self.utg2 = self.diler + 5
            self.utg3 = self.diler + 6
            self.cutOff = self.amount_players - 1
            self.hiJack = self.amount_players - 2
        elif (self.amount_players == 8):
            self.diler = 0
            self.smallBlind = self.diler + 1
            self.BigBlind = self.diler + 2
            self.utg = self.diler + 3
            self.utg1 = self.diler + 4
            self.utg2 = self.diler + 5
            self.cutOff = self.amount_players - 1
            self.hiJack = self.amount_players - 2
        elif (self.amount_players == 7):
            self.diler = 0
            self.smallBlind = self.diler + 1
            self.BigBlind = self.diler + 2
            self.utg = self.diler + 3
            self.utg1 = self.diler + 4
            self.cutOff = self.amount_players - 1
            self.hiJack = self.amount_players - 2
        elif (self.amount_players == 6):
            self.diler = 0
            self.smallBlind = self.diler + 1
            self.BigBlind = self.diler + 2
            self.utg = self.diler + 3
            self.cutOff = self.amount_players - 1
            self.hiJack = self.amount_players - 2
        elif (self.amount_players == 5):
            self.diler = 0
            self.smallBlind = self.diler + 1
            self.BigBlind = self.diler + 2
            self.cutOff = self.amount_players - 1
            self.hiJack = self.amount_players - 2
        elif (self.amount_players == 4):
            self.diler = 0
            self.smallBlind = self.diler + 1
            self.BigBlind = self.diler + 2
            self.cutOff = self.amount_players - 1
        elif (self.amount_players == 3):
            self.diler = 0
            self.smallBlind = self.diler + 1
            self.BigBlind = self.diler + 2
        elif (self.amount_players == 2):
            self.diler = 0
            self.smallBlind = self.diler + 1

    def potOdds(self, playermoney):
        if self.bankStack == 0:
            return -1
        else:
            return math.ceil(playermoney /(playermoney +self.bankStack) * 100)

    def playerOdds(self, amountOfouts):
        if amountOfouts > 1 and amountOfouts <= 3:
            return amountOfouts * 2
        elif amountOfouts > 3 and amountOfouts <= 11:
            return amountOfouts * 2 + 1
        else:
            return amountOfouts * 2 + 2

    def update_position(self):
        if (self.amount_players == 2):
            if (self.diler == 0):
                self.diler = 1
                self.smallBlind = 0
            else:
                self.diler = 0
                self.smallBlind = 1
        elif (self.amount_players == 3):
            if (self.diler == 0):
                self.BigBlind = self.diler
                self.diler = self.diler + 1
                self.smallBlind = self.smallBlind + 1
            elif (self.diler == 1):
                self.smallBlind = self.BigBlind
                self.BigBlind = self.diler
                self.diler = self.diler + 1
            else:
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.BigBlind + 1
        elif (self.amount_players == 4):
            if (self.diler == 0):
                self.cutOff = self.diler
                self.diler = self.diler + 1
                self.smallBlind = self.smallBlind + 1
                self.BigBlind = self.BigBlind + 1
            elif (self.diler == 1):
                self.smallBlind = self.BigBlind
                self.BigBlind = self.cutOff
                self.cutOff = self.diler
                self.diler = self.diler + 1
            elif (self.diler == 2):
                self.smallBlind = self.BigBlind
                self.BigBlind = self.cutOff
                self.cutOff = self.diler
                self.diler = self.diler + 1
            else:
                self.smallBlind = self.BigBlind
                self.BigBlind = self.cutOff
                self.cutOff = self.diler
                self.diler = 0

        elif (self.amount_players == 5):
            if (self.diler == 0):
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.diler + 1
                self.smallBlind = self.smallBlind + 1
                self.BigBlind = self.BigBlind + 1
            elif (self.diler == 1):
                self.smallBlind = self.BigBlind
                self.BigBlind = self.hiJack
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.diler + 1
            elif (self.diler == 2):
                self.smallBlind = self.BigBlind
                self.BigBlind = self.hiJack
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.diler + 1
            elif (self.diler == 3):
                self.smallBlind = self.BigBlind
                self.BigBlind = self.hiJack
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.diler + 1
            else:
                self.smallBlind = self.BigBlind
                self.BigBlind = self.hiJack
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = 0
        elif (self.amount_players == 6):
            if (self.diler == self.amount_players - 1):
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = 0
            elif (self.smallBlind == self.amount_players - 1):
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = 0
            elif (self.BigBlind == self.amount_players - 1):
                self.utg = self.utg + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = 0
            elif (self.utg == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = 0
            elif (self.hiJack == self.amount_players - 1):
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.hiJack = 0
            elif (self.cutOff == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.cutOff = 0
            else:
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1

        elif (self.amount_players == 7):
            if (self.diler == self.amount_players - 1):
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = 0
            elif (self.smallBlind == self.amount_players - 1):
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = 0
            elif (self.BigBlind == self.amount_players - 1):
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = 0
            elif (self.utg == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = 0
                self.utg1 = self.utg1 + 1
            elif (self.hiJack == self.amount_players - 1):
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.hiJack = 0
            elif (self.cutOff == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.cutOff = 0
            elif (self.utg1 == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = 0
                self.cutOff = self.cutOff + 1
            else:
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1

        elif (self.amount_players == 8):
            if (self.diler == self.amount_players - 1):
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = 0
            elif (self.smallBlind == self.amount_players - 1):
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = 0
            elif (self.BigBlind == self.amount_players - 1):
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = 0
            elif (self.utg == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = 0
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
            elif (self.hiJack == self.amount_players - 1):
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.hiJack = 0
            elif (self.cutOff == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.cutOff = 0
            elif (self.utg1 == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg2 = self.utg2 + 1
                self.utg1 = 0
                self.cutOff = self.cutOff + 1
            elif (self.utg2 == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = 0
                self.cutOff = self.cutOff + 1
            else:
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1

        elif (self.amount_players == 9):
            if (self.diler == self.amount_players - 1):
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = 0
            elif (self.smallBlind == self.amount_players - 1):
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = 0
            elif (self.BigBlind == self.amount_players - 1):
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = 0
            elif (self.utg == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = 0
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
            elif (self.hiJack == self.amount_players - 1):
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.hiJack = 0
            elif (self.cutOff == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.cutOff = 0
            elif (self.utg1 == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.utg1 = 0
                self.cutOff = self.cutOff + 1
            elif (self.utg2 == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg3 = self.utg3 + 1
                self.utg2 = 0
                self.cutOff = self.cutOff + 1
            elif (self.utg3 == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = 0
                self.cutOff = self.cutOff + 1
            else:
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1




        elif (self.amount_players == 10):
            if (self.diler == self.amount_players - 1):
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.utg4 = self.utg4 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = 0
            elif (self.smallBlind == self.amount_players - 1):
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.utg4 = self.utg4 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = 0
            elif (self.BigBlind == self.amount_players - 1):
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.utg4 = self.utg4 + 1
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = 0
            elif (self.utg == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = 0
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.utg4 = self.utg4 + 1
            elif (self.hiJack == self.amount_players - 1):
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.utg4 = self.utg4 + 1
                self.hiJack = 0
            elif (self.cutOff == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.utg4 = self.utg4 + 1
                self.cutOff = 0
            elif (self.utg1 == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.utg4 = self.utg4 + 1
                self.utg1 = 0
                self.cutOff = self.cutOff + 1
            elif (self.utg2 == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg3 = self.utg3 + 1
                self.utg4 = self.utg4 + 1
                self.utg2 = 0
                self.cutOff = self.cutOff + 1
            elif (self.utg3 == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg4 = self.utg4 + 1
                self.utg3 = 0
                self.cutOff = self.cutOff + 1
            elif (self.utg4 == self.amount_players - 1):
                self.hiJack = self.cutOff
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1
                self.utg1 = self.utg1 + 1
                self.utg2 = self.utg2 + 1
                self.utg3 = self.utg3 + 1
                self.utg4 = 0
                self.cutOff = self.cutOff + 1
            else:
                self.hiJack = self.cutOff
                self.cutOff = self.diler
                self.diler = self.smallBlind
                self.smallBlind = self.BigBlind
                self.BigBlind = self.utg
                self.utg = self.utg + 1

    def show_position(self):
        if (self.diler == 0):
            return "diler"
        elif (self.smallBlind == 0):
            return "smallBlind"
        elif (self.BigBlind == 0):
            return "BigBlind"
        elif (self.utg == 0):
            return "utg"
        elif (self.utg1 == 0):
            return "utg1"
        elif (self.utg2 == 0):
            return "utg2"
        elif (self.utg3 == 0):
            return "utg3"
        elif (self.utg4 == 0):
            return "utg4"
        elif (self.hiJack == 0):
            return "hijack"
        elif (self.cutOff == 0):
            return "cutOff"

    def show_diler(self):
        return self.diler
class mGUI:
    def metod(self):
         self.diler = Diler()
         self.root = Toplevel()  # окно
         self.root.title("POKER")

    def checkcomb(self, comb):
        # t=self.comb.check_para()
        # if t==0:
        #     self.comblpara=Label(self.master,text="НЕТ ПАРЫ!      ",bg="red")
        #     self.comblpara.place(relx=0.75, rely=0.70, anchor=CENTER)
        # else:
        #     self.comblpara=Label(self.master,text="ПАРА!      "+str(t),bg="red")
        #     self.comblpara.place(relx=0.75, rely=0.70, anchor=CENTER)
        #
        # t=self.comb.check_2para()
        # if t==[]:
        #     self.combl2para=Label(self.master,text="НЕТ 2ПАРЫ!      ",bg="red")
        #     self.combl2para.place(relx=0.75, rely=0.75, anchor=CENTER)
        # else:
        #     print("2para : "+str(t[0])+" "+str(t[1]))
        #     self.combl2para=Label(self.master,text="2ПАРЫ!      "+str(t[0])+" "+str(t[1]),bg="red")
        #     self.combl2para.place(relx=0.75, rely=0.75, anchor=CENTER)

        t = self.comb.mycombination(self.comb)
        # if t==0:
        self.comblset = Label(self.separator1, text="Current Combination:     " + str(t),bg="sea green",fg='#4B0082')
        #self.comblset.place(relx=0.85, rely=0.80, anchor=CENTER)
        self.comblset.place(relx=0.5, rely=0.4, anchor=CENTER)
        # else:
        #   self.comblset=Label(self.master,text="Cэт!      "+str(t),bg="red")
        #  self.comblset.place(relx=0.75, rely=0.80, anchor=CENTER)

    def fall(self):
        if (self.diler.flagofbet == 1):
            self.UpdateLabel()
            self.diler.flagofbet = 0
            self.diler.mystavka=0
        else:
            popupmsg1("Wait Your Step !")
    def check(self):
        if self.diler.stavka==0:
            self.diler.flagofbet = 0
            self.diler.mystavka=0
        else:
            popupmsg1("You Can not check!")
    def call(self):

        if (self.diler.flagofbet == 1):
          if self.diler.myPlayerstack>=self.diler.stavka:
            if self.diler.stavka==0:
                self.diler.stavka=5
            self.diler.bankStack += self.diler.stavka
            self.BANKbet.destroy()
            self.diler.myPlayerstack -= self.diler.stavka
            self.playerbet = Label(self.root,text="YOUR STACK :  " + str(self.diler.myPlayerstack), border=3, font=("Times",10,"bold"),bg="green4", fg="#4B0082")
            self.playerbet.place(relx=0.057, rely=0.785, anchor=CENTER)
            strin="BANK :   " + str(self.diler.bankStack)
            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)
            self.diler.flagofbet = 0
            self.diler.mystavka=self.diler.stavka
          else:
              popupmsg1("You Have No Money!")
        else:
            popupmsg1("Wait Your Step !")
    def botcall(self, botstack, bot):
      if self.game.tableCards==[]:
             cl=CheckHoleCardsForBot(bot.card1,bot.card2,'diler',9,'act_call')
             mystr=cl.check_power()
             print (mystr)
             if mystr=="Fall !":
                bot.active=False
                if (bot == self.game.players[1]):
                    print("OFFFFFF")
                    self.player1s.destroy()
                    self.player1s = Label(self.root,text="OFF", bg="PaleGreen2")
                    self.player1s.place(relx=0.23, rely=0.03, anchor=CENTER)

                elif (bot == self.game.players[2]):
                    self.player2s = Label(self.root,text="OFF", bg="PaleGreen2")
                    self.player2s.place(relx=0.33, rely=0.03, anchor=CENTER)
                elif (bot == self.game.players[3]):
                    self.player3s = Label(self.root,text="OFF", bg="PaleGreen2")
                    self.player3s.place(relx=0.43, rely=0.08, anchor=CENTER)
                elif (bot == self.game.players[4]):
                    self.player4s = Label(self.root,text="OFF", bg="PaleGreen2")
                    self.player4s.place(relx=0.43, rely=0.16, anchor=CENTER)
                elif (bot == self.game.players[5]):
                    self.player5s = Label(self.root,text="OFF", bg="PaleGreen2")
                    self.player5s.place(relx=0.43, rely=0.24, anchor=CENTER)
                elif (bot == self.game.players[6]):
                    self.player6s = Label(self.root,text="OFF", bg="PaleGreen2")
                    self.player6s.place(relx=0.33, rely=0.28, anchor=CENTER)
                elif (bot == self.game.players[7]):
                    self.player7s = Label(self.root,text="OFF", bg="PaleGreen2")
                    self.player7s.place(relx=0.23, rely=0.28, anchor=CENTER)
                elif (bot == self.game.players[8]):
                    self.player8s = Label(self.root,text="OFF", bg="PaleGreen2")
                    self.player8s.place(relx=0.093, rely=0.24, anchor=CENTER)
                elif (bot == self.game.players[9]):
                    self.player9s = Label(self.root,text="OFF", bg="PaleGreen2")
                    self.player9s.place(relx=0.083, rely=0.09, anchor=CENTER)

             elif mystr=="Raise !":
                  raise_stavka=self.diler.stavka+50
                  if bot == self.game.players[1]:
                      self.diler.bankStack+=raise_stavka
                      self.diler.player1Stack -= raise_stavka
                      self.diler.botpower=0
                      self.diler.stavka=raise_stavka
                  elif bot == self.game.players[2]:
                      self.diler.bankStack+=raise_stavka
                      self.diler.player2Stack -= raise_stavka
                      self.diler.botpower=0
                      self.diler.stavka=raise_stavka
                  elif bot == self.game.players[3]:
                      self.diler.bankStack+=raise_stavka
                      self.diler.player3Stack -= raise_stavka
                      self.diler.botpower=0
                      self.diler.stavka=raise_stavka
                  elif bot == self.game.players[4]:
                      self.diler.bankStack+=raise_stavka
                      self.diler.player4Stack -= raise_stavka
                      self.diler.botpower=0
                      self.diler.stavka=raise_stavka
                  elif bot == self.game.players[5]:
                      self.diler.bankStack+=raise_stavka
                      self.diler.player5Stack -= raise_stavka
                      self.diler.botpower=0
                      self.diler.stavka=raise_stavka
                  elif bot == self.game.players[6]:
                      self.diler.bankStack+=raise_stavka
                      self.diler.player6Stack -= raise_stavka
                      self.diler.botpower=0
                      self.diler.stavka=raise_stavka
                  elif bot == self.game.players[7]:
                      self.diler.bankStack+=raise_stavka
                      self.diler.player7Stack -= raise_stavka
                      self.diler.botpower=0
                      self.diler.stavka=raise_stavka
                  elif bot == self.game.players[8]:
                      self. diler.bankStack+=raise_stavka
                      self.diler.player8Stack -= raise_stavka
                      self.diler.botpower=0
                      self.diler.stavka=raise_stavka
                  elif bot == self.game.players[9]:
                      self.diler.bankStack+=raise_stavka
                      self.diler.player9Stack -= raise_stavka
                      self.diler.botpower=0
                      self.diler.stavka=raise_stavka


                  strin="BANK :   " + str(self.diler.bankStack)
                  self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                  self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)

                  if bot == self.game.players[1]:
                        self.player1s = Label(self.root,text=self.diler.player1Stack, bg="PaleGreen2")
                        self.player1s.place(relx=0.23, rely=0.03, anchor=CENTER)
                  elif bot == self.game.players[2]:
                        self.player2s = Label(self.root,text=self.diler.player2Stack, bg="PaleGreen2")
                        self.player2s.place(relx=0.33, rely=0.03, anchor=CENTER)
                  elif bot == self.game.players[3]:
                        self.player3s = Label(self.root,text=self.diler.player3Stack, bg="PaleGreen2")
                        self.player3s.place(relx=0.43, rely=0.08, anchor=CENTER)
                  elif bot == self.game.players[4]:
                        self.player4s = Label(self.root,text=self.diler.player4Stack, bg="PaleGreen2")
                        self.player4s.place(relx=0.43, rely=0.16, anchor=CENTER)
                  elif bot == self.game.players[5]:
                        self.player5s = Label(self.root,text=self.diler.player5Stack, bg="PaleGreen2")
                        self.player5s.place(relx=0.43, rely=0.24, anchor=CENTER)
                  elif bot == self.game.players[6]:
                        self.player6s = Label(self.root,text=self.diler.player6Stack, bg="PaleGreen2")
                        self.player6s.place(relx=0.33, rely=0.28, anchor=CENTER)
                  elif bot == self.game.players[7]:
                        self.player7s = Label(self.root,text=self.diler.player7Stack, bg="PaleGreen2")
                        self.player7s.place(relx=0.23, rely=0.28, anchor=CENTER)
                  elif bot == self.game.players[8]:
                        self.player8s = Label(self.root,text=self.diler.player8Stack, bg="PaleGreen2")
                        self.player8s.place(relx=0.093, rely=0.24, anchor=CENTER)
                  elif bot == self.game.players[9]:
                        self.player9s = Label(self.root,text=self.diler.player9Stack, bg="PaleGreen2")
                        self.player9s.place(relx=0.083, rely=0.09, anchor=CENTER)
             elif mystr=="Call !":
                            self.diler.bankStack += self.diler.stavka
                            if bot == self.game.players[1]:
                                self.diler.player1Stack -=self.diler.stavka
                            elif bot == self.game.players[2]:
                                self.diler.player2Stack -= self.diler.stavka
                            elif bot == self.game.players[3]:
                                self.diler.player3Stack -= self.diler.stavka
                            elif bot == self.game.players[4]:
                                self.diler.player4Stack -=self.diler.stavka
                            elif bot == self.game.players[5]:
                                self.diler.player5Stack -= self.diler.stavka
                            elif bot == self.game.players[6]:
                                self.diler.player6Stack -= self.diler.stavka
                            elif bot == self.game.players[7]:
                                self.diler.player7Stack -= self.diler.stavka
                            elif bot == self.game.players[8]:
                                self.diler.player8Stack -= self.diler.stavka
                            elif bot == self.game.players[9]:
                                self.diler.player9Stack -= self.diler.stavka

                            botstack -= self.diler.stavka
                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)

                            if bot == self.game.players[1]:
                                self.player1s = Label(self.root,text=self.diler.player1Stack, bg="PaleGreen2")
                                self.player1s.place(relx=0.23, rely=0.03, anchor=CENTER)
                            elif bot == self.game.players[2]:
                                self.player2s = Label(self.root,text=self.diler.player2Stack, bg="PaleGreen2")
                                self.player2s.place(relx=0.33, rely=0.03, anchor=CENTER)
                            elif bot == self.game.players[3]:
                                self.player3s = Label(self.root,text=self.diler.player3Stack, bg="PaleGreen2")
                                self.player3s.place(relx=0.43, rely=0.08, anchor=CENTER)
                            elif bot == self.game.players[4]:
                                self.player4s = Label(self.root,text=self.diler.player4Stack, bg="PaleGreen2")
                                self.player4s.place(relx=0.43, rely=0.16, anchor=CENTER)
                            elif bot == self.game.players[5]:
                                self.player5s = Label(self.root,text=self.diler.player5Stack, bg="PaleGreen2")
                                self.player5s.place(relx=0.43, rely=0.24, anchor=CENTER)
                            elif bot == self.game.players[6]:
                                self.player6s = Label(self.root,text=self.diler.player6Stack, bg="PaleGreen2")
                                self.player6s.place(relx=0.33, rely=0.28, anchor=CENTER)
                            elif bot == self.game.players[7]:
                                self.player7s = Label(self.root,text=self.diler.player7Stack, bg="PaleGreen2")
                                self.player7s.place(relx=0.23, rely=0.28, anchor=CENTER)
                            elif bot == self.game.players[8]:
                                self.player8s = Label(self.root,text=self.diler.player8Stack, bg="PaleGreen2")
                                self.player8s.place(relx=0.093, rely=0.24, anchor=CENTER)
                            elif bot == self.game.players[9]:
                                self.player9s = Label(self.root,text=self.diler.player9Stack, bg="PaleGreen2")
                                self.player9s.place(relx=0.083, rely=0.09, anchor=CENTER)


      else:
        if (bot == self.game.players[1]):
                if self.player1s['text']=="OFF":
                    print("OFFFFFF")
                    return 0
        elif (bot == self.game.players[2]):
                if self.player2s['text']=="OFF":
                    print("OFFFFFF")
                    return 0
        elif (bot == self.game.players[3]):
                if self.player3s['text']=="OFF":
                    print("OFFFFFF")
                    return 0
        elif (bot == self.game.players[4]):
                if self.player4s['text']=="OFF":
                    print("OFFFFFF")
                    return 0
        elif (bot == self.game.players[5]):
                if self.player5s['text']=="OFF":
                    print("OFFFFFF")
                    return 0
        elif (bot == self.game.players[6]):
                if self.player6s['text']=="OFF":
                    print("OFFFFFF")
                    return 0
        elif (bot == self.game.players[7]):
                if self.player7s['text']=="OFF":
                    print("OFFFFFF")
                    return 0
        elif (bot == self.game.players[8]):
                if self.player8s['text']=="OFF":
                    print("OFFFFFF")
                    return 0
        elif (bot == self.game.players[9]):
                if self.player9s['text']=="OFF":
                    print("OFFFFFF")
                    return 0

        botandtable = self.game.tableCards.copy()
        if (bot == self.game.players[1]):
            botandtable.append(self.game.players[1].card1)
            print("КАРТА БОТА " + str(self.game.players[1].card1.card_rating) + " " + (
            str(self.game.players[1].card1.card_suit)))
            botandtable.append(self.game.players[1].card2)
            print("КАРТА БОТА " + str(self.game.players[1].card2.card_rating) + " " + (
            str(self.game.players[1].card2.card_suit)))
            gamebot = Game(10)
            gamebot.my__init__(10, self.game.players[1].card1.card_suit,
                               self.game.players[1].card1.card_rating, self.game.players[1].card2.card_suit,
                               self.game.players[1].card2.card_rating)
            gamebot.tableCards = self.game.tableCards.copy()
            print("TABLE CARDS")
            for i in gamebot.tableCards:
                print(str(i.card_rating) + " " + (str(i.card_suit)))
            print("----------------------")
            gamebot.myCardWithTable = botandtable
            gamebot.koloda = []
            for k in range(0, 4):
                gamebot.koloda.append([])
                for i in range(13):
                    gamebot.koloda[k].append(i + 2)

            gamebot.koloda[self.game.players[1].card1.card_suit - 1][self.game.players[1].card1.card_rating - 2] = 0
            gamebot.koloda[self.game.players[1].card2.card_suit - 1][self.game.players[1].card2.card_rating - 2] = 0
            if (gamebot.tableCards != []):
                gamebot.koloda[gamebot.tableCards[0].card_suit - 1][gamebot.tableCards[0].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[1].card_suit - 1][gamebot.tableCards[1].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[2].card_suit - 1][gamebot.tableCards[2].card_rating - 2] = 0


#
#
            print("TABLE CARDS BOTANDTABLE")
            for i in botandtable:
                print(str(i.card_rating) + " " + (str(i.card_suit)))
            print("----------------------")
            bot1hand =CheckComb(botandtable).mycombinationForOut()
            if (bot1hand=="kiker"):
                bot1power=0
            elif (bot1hand=="para"):
                bot1power=1
            elif (bot1hand=="2para"):
                bot1power=2
            elif (bot1hand=="set"):
                bot1power=3
            elif (bot1hand=="strit"):
                bot1power=4
            elif (bot1hand=="flesh"):
                bot1power=5
            elif (bot1hand=="FH"):
                bot1power=6
            elif (bot1hand=="kare"):
                bot1power=7
            elif (bot1hand=="SF"):
                bot1power=8
            elif (bot1hand=="royal"):
                bot1power=9

            self.diler.botpower=bot1power
            print("DILERBOTPOWER:"+str(self.diler.botpower))




            botout = CheckOuts(gamebot, CheckComb(botandtable))
            print("1 bot")
            botout.checkOut()
            amountOfoutsofbot = botout.outs
        elif (bot == self.game.players[2]):
            botandtable.append(self.game.players[2].card1)
            botandtable.append(self.game.players[2].card2)
            gamebot = Game(10)
            gamebot.my__init__(10, self.game.players[2].card1.card_suit,
                               self.game.players[2].card1.card_rating, self.game.players[2].card2.card_suit,
                               self.game.players[2].card2.card_rating)
            gamebot.tableCards = self.game.tableCards
            gamebot.myCardWithTable = botandtable
            gamebot.koloda = []
            for k in range(0, 4):
                gamebot.koloda.append([])
                for i in range(13):
                    gamebot.koloda[k].append(i + 2)

            gamebot.koloda[self.game.players[2].card1.card_suit - 1][self.game.players[2].card1.card_rating - 2] = 0
            gamebot.koloda[self.game.players[2].card2.card_suit - 1][self.game.players[2].card2.card_rating - 2] = 0
            if (gamebot.tableCards != []):
                gamebot.koloda[gamebot.tableCards[0].card_suit - 1][gamebot.tableCards[0].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[1].card_suit - 1][gamebot.tableCards[1].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[2].card_suit - 1][gamebot.tableCards[2].card_rating - 2] = 0



            print("TABLE CARDS BOTANDTABLE")
            for i in botandtable:
                print(str(i.card_rating) + " " + (str(i.card_suit)))
            print("----------------------")
            bot1hand =CheckComb(botandtable).mycombinationForOut()
            if (bot1hand=="kiker"):
                bot1power=0
            elif (bot1hand=="para"):
                bot1power=1
            elif (bot1hand=="2para"):
                bot1power=2
            elif (bot1hand=="set"):
                bot1power=3
            elif (bot1hand=="strit"):
                bot1power=4
            elif (bot1hand=="flesh"):
                bot1power=5
            elif (bot1hand=="FH"):
                bot1power=6
            elif (bot1hand=="kare"):
                bot1power=7
            elif (bot1hand=="SF"):
                bot1power=8
            elif (bot1hand=="royal"):
                bot1power=9

            self.diler.botpower=bot1power
            print("DILERBOTPOWER:"+str(self.diler.botpower))
            botout = CheckOuts(gamebot, CheckComb(botandtable))
            print("2 bot")
            botout.checkOut()
            amountOfoutsofbot = botout.outs
        elif (bot == self.game.players[3]):
            botandtable.append(self.game.players[3].card1)
            botandtable.append(self.game.players[3].card2)
            gamebot = Game(10)
            gamebot.my__init__(10, self.game.players[3].card1.card_suit,
                               self.game.players[3].card1.card_rating, self.game.players[3].card2.card_suit,
                               self.game.players[3].card2.card_rating)
            gamebot.tableCards = self.game.tableCards
            gamebot.myCardWithTable = botandtable
            gamebot.koloda = []
            for k in range(0, 4):
                gamebot.koloda.append([])
                for i in range(13):
                    gamebot.koloda[k].append(i + 2)

            gamebot.koloda[self.game.players[3].card1.card_suit - 1][self.game.players[3].card1.card_rating - 2] = 0
            gamebot.koloda[self.game.players[3].card2.card_suit - 1][self.game.players[3].card2.card_rating - 2] = 0
            if (gamebot.tableCards != []):
                gamebot.koloda[gamebot.tableCards[0].card_suit - 1][gamebot.tableCards[0].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[1].card_suit - 1][gamebot.tableCards[1].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[2].card_suit - 1][gamebot.tableCards[2].card_rating - 2] = 0

            print("TABLE CARDS BOTANDTABLE")
            for i in botandtable:
                print(str(i.card_rating) + " " + (str(i.card_suit)))
            print("----------------------")
            bot1hand =CheckComb(botandtable).mycombinationForOut()
            if (bot1hand=="kiker"):
                bot1power=0
            elif (bot1hand=="para"):
                bot1power=1
            elif (bot1hand=="2para"):
                bot1power=2
            elif (bot1hand=="set"):
                bot1power=3
            elif (bot1hand=="strit"):
                bot1power=4
            elif (bot1hand=="flesh"):
                bot1power=5
            elif (bot1hand=="FH"):
                bot1power=6
            elif (bot1hand=="kare"):
                bot1power=7
            elif (bot1hand=="SF"):
                bot1power=8
            elif (bot1hand=="royal"):
                bot1power=9

            self.diler.botpower=bot1power
            print("DILERBOTPOWER:"+str(self.diler.botpower))

            botout = CheckOuts(gamebot, CheckComb(botandtable))
            print("3 bot")
            botout.checkOut()
            amountOfoutsofbot = botout.outs
        elif (bot == self.game.players[4]):
            botandtable.append(self.game.players[4].card1)
            botandtable.append(self.game.players[4].card2)
            gamebot = Game(10)
            gamebot.my__init__(10, self.game.players[4].card1.card_suit,
                               self.game.players[4].card1.card_rating, self.game.players[4].card2.card_suit,
                               self.game.players[4].card2.card_rating)
            gamebot.tableCards = self.game.tableCards
            gamebot.myCardWithTable = botandtable
            gamebot.koloda = []
            for k in range(0, 4):
                gamebot.koloda.append([])
                for i in range(13):
                    gamebot.koloda[k].append(i + 2)

            gamebot.koloda[self.game.players[4].card1.card_suit - 1][self.game.players[4].card1.card_rating - 2] = 0
            gamebot.koloda[self.game.players[4].card2.card_suit - 1][self.game.players[4].card2.card_rating - 2] = 0
            if (gamebot.tableCards != []):
                gamebot.koloda[gamebot.tableCards[0].card_suit - 1][gamebot.tableCards[0].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[1].card_suit - 1][gamebot.tableCards[1].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[2].card_suit - 1][gamebot.tableCards[2].card_rating - 2] = 0

            print("TABLE CARDS BOTANDTABLE")
            for i in botandtable:
                print(str(i.card_rating) + " " + (str(i.card_suit)))
            print("----------------------")
            bot1hand =CheckComb(botandtable).mycombinationForOut()
            if (bot1hand=="kiker"):
                bot1power=0
            elif (bot1hand=="para"):
                bot1power=1
            elif (bot1hand=="2para"):
                bot1power=2
            elif (bot1hand=="set"):
                bot1power=3
            elif (bot1hand=="strit"):
                bot1power=4
            elif (bot1hand=="flesh"):
                bot1power=5
            elif (bot1hand=="FH"):
                bot1power=6
            elif (bot1hand=="kare"):
                bot1power=7
            elif (bot1hand=="SF"):
                bot1power=8
            elif (bot1hand=="royal"):
                bot1power=9

            self.diler.botpower=bot1power
            print("DILERBOTPOWER:"+str(self.diler.botpower))


            botout = CheckOuts(gamebot, CheckComb(botandtable))
            print("4 bot")
            botout.checkOut()
            amountOfoutsofbot = botout.outs
        elif (bot == self.game.players[5]):
            botandtable.append(self.game.players[5].card1)
            botandtable.append(self.game.players[5].card2)
            gamebot = Game(10)
            gamebot.my__init__(10, self.game.players[5].card1.card_suit,
                               self.game.players[5].card1.card_rating, self.game.players[5].card2.card_suit,
                               self.game.players[5].card2.card_rating)
            gamebot.tableCards = self.game.tableCards
            gamebot.myCardWithTable = botandtable
            gamebot.koloda = []
            for k in range(0, 4):
                gamebot.koloda.append([])
                for i in range(13):
                    gamebot.koloda[k].append(i + 2)

            gamebot.koloda[self.game.players[5].card1.card_suit - 1][self.game.players[5].card1.card_rating - 2] = 0
            gamebot.koloda[self.game.players[5].card2.card_suit - 1][self.game.players[5].card2.card_rating - 2] = 0
            if (gamebot.tableCards != []):
                gamebot.koloda[gamebot.tableCards[0].card_suit - 1][gamebot.tableCards[0].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[1].card_suit - 1][gamebot.tableCards[1].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[2].card_suit - 1][gamebot.tableCards[2].card_rating - 2] = 0


            print("TABLE CARDS BOTANDTABLE")
            for i in botandtable:
                print(str(i.card_rating) + " " + (str(i.card_suit)))
            print("----------------------")
            bot1hand =CheckComb(botandtable).mycombinationForOut()
            if (bot1hand=="kiker"):
                bot1power=0
            elif (bot1hand=="para"):
                bot1power=1
            elif (bot1hand=="2para"):
                bot1power=2
            elif (bot1hand=="set"):
                bot1power=3
            elif (bot1hand=="strit"):
                bot1power=4
            elif (bot1hand=="flesh"):
                bot1power=5
            elif (bot1hand=="FH"):
                bot1power=6
            elif (bot1hand=="kare"):
                bot1power=7
            elif (bot1hand=="SF"):
                bot1power=8
            elif (bot1hand=="royal"):
                bot1power=9

            self.diler.botpower=self.bot1power
            print("DILERBOTPOWER:"+str(self.diler.botpower))

            botout = CheckOuts(gamebot, CheckComb(botandtable))
            print("5 bot")
            botout.checkOut()
            amountOfoutsofbot = botout.outs
        elif (bot == self.game.players[6]):
            botandtable.append(self.game.players[6].card1)
            botandtable.append(self.game.players[6].card2)
            gamebot = Game(10)
            gamebot.my__init__(10, self.game.players[6].card1.card_suit,
                               self.game.players[6].card1.card_rating, self.game.players[6].card2.card_suit,
                               self.game.players[6].card2.card_rating)
            gamebot.tableCards = self.game.tableCards
            gamebot.myCardWithTable = botandtable
            gamebot.koloda = []
            for k in range(0, 4):
                gamebot.koloda.append([])
                for i in range(13):
                    gamebot.koloda[k].append(i + 2)

            gamebot.koloda[self.game.players[6].card1.card_suit - 1][self.game.players[6].card1.card_rating - 2] = 0
            gamebot.koloda[self.game.players[6].card2.card_suit - 1][self.game.players[6].card2.card_rating - 2] = 0
            if (gamebot.tableCards != []):
                gamebot.koloda[gamebot.tableCards[0].card_suit - 1][gamebot.tableCards[0].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[1].card_suit - 1][gamebot.tableCards[1].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[2].card_suit - 1][gamebot.tableCards[2].card_rating - 2] = 0


            print("TABLE CARDS BOTANDTABLE")
            for i in botandtable:
                print(str(i.card_rating) + " " + (str(i.card_suit)))
            print("----------------------")
            bot1hand =CheckComb(botandtable).mycombinationForOut()
            if (bot1hand=="kiker"):
                bot1power=0
            elif (bot1hand=="para"):
                bot1power=1
            elif (bot1hand=="2para"):
                bot1power=2
            elif (bot1hand=="set"):
                bot1power=3
            elif (bot1hand=="strit"):
                bot1power=4
            elif (bot1hand=="flesh"):
                bot1power=5
            elif (bot1hand=="FH"):
                bot1power=6
            elif (bot1hand=="kare"):
                bot1power=7
            elif (bot1hand=="SF"):
                bot1power=8
            elif (bot1hand=="royal"):
                bot1power=9

            self.diler.botpower=bot1power
            print("DILERBOTPOWER:"+str(self.diler.botpower))

            botout = CheckOuts(gamebot, CheckComb(botandtable))
            print("6 bot")
            botout.checkOut()
            amountOfoutsofbot = botout.outs
        elif (bot == self.game.players[7]):
            botandtable.append(self.game.players[7].card1)
            botandtable.append(self.game.players[7].card2)
            gamebot = Game(10)
            gamebot.my__init__(10, self.game.players[7].card1.card_suit,
                               self.game.players[7].card1.card_rating, self.game.players[7].card2.card_suit,
                               self.game.players[7].card2.card_rating)
            gamebot.tableCards = self.game.tableCards
            gamebot.myCardWithTable = botandtable
            gamebot.koloda = []
            for k in range(0, 4):
                gamebot.koloda.append([])
                for i in range(13):
                    gamebot.koloda[k].append(i + 2)

            gamebot.koloda[self.game.players[7].card1.card_suit - 1][self.game.players[7].card1.card_rating - 2] = 0
            gamebot.koloda[self.game.players[7].card2.card_suit - 1][self.game.players[7].card2.card_rating - 2] = 0
            if (gamebot.tableCards != []):
                gamebot.koloda[gamebot.tableCards[0].card_suit - 1][gamebot.tableCards[0].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[1].card_suit - 1][gamebot.tableCards[1].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[2].card_suit - 1][gamebot.tableCards[2].card_rating - 2] = 0

            print("TABLE CARDS BOTANDTABLE")
            for i in botandtable:
                print(str(i.card_rating) + " " + (str(i.card_suit)))
            print("----------------------")
            bot1hand =CheckComb(botandtable).mycombinationForOut()
            if (bot1hand=="kiker"):
                bot1power=0
            elif (bot1hand=="para"):
                bot1power=1
            elif (bot1hand=="2para"):
                bot1power=2
            elif (bot1hand=="set"):
                bot1power=3
            elif (bot1hand=="strit"):
                bot1power=4
            elif (bot1hand=="flesh"):
                bot1power=5
            elif (bot1hand=="FH"):
                bot1power=6
            elif (bot1hand=="kare"):
                bot1power=7
            elif (bot1hand=="SF"):
                bot1power=8
            elif (bot1hand=="royal"):
                bot1power=9

            self.diler.botpower=bot1power
            print("DILERBOTPOWER:"+str(self.diler.botpower))

            botout = CheckOuts(gamebot, CheckComb(botandtable))
            print("7 bot")
            botout.checkOut()
            amountOfoutsofbot = botout.outs
        elif (bot == self.game.players[8]):
            botandtable.append(self.game.players[8].card1)
            botandtable.append(self.game.players[8].card2)
            gamebot = Game(10)
            gamebot.my__init__(10, self.game.players[8].card1.card_suit,
                               self.game.players[8].card1.card_rating, self.game.players[8].card2.card_suit,
                               self.game.players[8].card2.card_rating)
            gamebot.tableCards = self.game.tableCards
            gamebot.myCardWithTable = botandtable
            gamebot.koloda = []
            for k in range(0, 4):
                gamebot.koloda.append([])
                for i in range(13):
                    gamebot.koloda[k].append(i + 2)

            gamebot.koloda[self.game.players[8].card1.card_suit - 1][self.game.players[8].card1.card_rating - 2] = 0
            gamebot.koloda[self.game.players[8].card2.card_suit - 1][self.game.players[8].card2.card_rating - 2] = 0
            if (gamebot.tableCards != []):
                gamebot.koloda[gamebot.tableCards[0].card_suit - 1][gamebot.tableCards[0].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[1].card_suit - 1][gamebot.tableCards[1].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[2].card_suit - 1][gamebot.tableCards[2].card_rating - 2] = 0


            print("TABLE CARDS BOTANDTABLE")
            for i in botandtable:
                print(str(i.card_rating) + " " + (str(i.card_suit)))
            print("----------------------")
            bot1hand =CheckComb(botandtable).mycombinationForOut()
            if (bot1hand=="kiker"):
                bot1power=0
            elif (bot1hand=="para"):
                bot1power=1
            elif (bot1hand=="2para"):
                bot1power=2
            elif (bot1hand=="set"):
                bot1power=3
            elif (bot1hand=="strit"):
                bot1power=4
            elif (bot1hand=="flesh"):
                bot1power=5
            elif (bot1hand=="FH"):
                bot1power=6
            elif (bot1hand=="kare"):
                bot1power=7
            elif (bot1hand=="SF"):
                bot1power=8
            elif (bot1hand=="royal"):
                bot1power=9

            self.diler.botpower=bot1power
            print("DILERBOTPOWER:"+str(self.diler.botpower))

            botout = CheckOuts(gamebot, CheckComb(botandtable))
            print("8 bot")
            botout.checkOut()
            amountOfoutsofbot = botout.outs
        elif (bot == self.game.players[9]):
            botandtable.append(self.game.players[9].card1)
            botandtable.append(self.game.players[9].card2)
            gamebot = Game(10)
            gamebot.my__init__(10, self.game.players[9].card1.card_suit,
                               self.game.players[9].card1.card_rating, self.game.players[9].card2.card_suit,
                               self.game.players[9].card2.card_rating)
            gamebot.tableCards = self.game.tableCards
            gamebot.myCardWithTable = botandtable
            gamebot.koloda = []
            for k in range(0, 4):
                gamebot.koloda.append([])
                for i in range(13):
                    gamebot.koloda[k].append(i + 2)

            gamebot.koloda[self.game.players[9].card1.card_suit - 1][self.game.players[9].card1.card_rating - 2] = 0
            gamebot.koloda[self.game.players[9].card2.card_suit - 1][self.game.players[9].card2.card_rating - 2] = 0
            if (gamebot.tableCards != []):
                gamebot.koloda[gamebot.tableCards[0].card_suit - 1][gamebot.tableCards[0].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[1].card_suit - 1][gamebot.tableCards[1].card_rating - 2] = 0
                gamebot.koloda[gamebot.tableCards[2].card_suit - 1][gamebot.tableCards[2].card_rating - 2] = 0


            print("TABLE CARDS BOTANDTABLE")
            for i in botandtable:
                print(str(i.card_rating) + " " + (str(i.card_suit)))
            print("----------------------")
            bot1hand =CheckComb(botandtable).mycombinationForOut()
            if (bot1hand=="kiker"):
                bot1power=0
            elif (bot1hand=="para"):
                bot1power=1
            elif (bot1hand=="2para"):
                bot1power=2
            elif (bot1hand=="set"):
                bot1power=3
            elif (bot1hand=="strit"):
                bot1power=4
            elif (bot1hand=="flesh"):
                bot1power=5
            elif (bot1hand=="FH"):
                bot1power=6
            elif (bot1hand=="kare"):
                bot1power=7
            elif (bot1hand=="SF"):
                bot1power=8
            elif (bot1hand=="royal"):
                bot1power=9

            self.diler.botpower=bot1power
            print("DILERBOTPOWER:"+str(self.diler.botpower))

            botout = CheckOuts(gamebot, CheckComb(botandtable))
            print("9 bot")
            botout.checkOut()
            amountOfoutsofbot = botout.outs

        # print("BOT-------------------------------------------------------")
        # print("TABLE CARDS :")
        # for i in botandtable:
        #     print(str(i.card_suit) + "  " + str(i.card_rating))
        # print("ENDTABLE CARDS :")
        # print(str(bot.card1.card_suit) + "  " + str(bot.card1.card_rating))
        # print(str(bot.card2.card_suit) + "  " + str(bot.card2.card_rating))
        # print(amountOfoutsofbot)
        # print(diler.playerOdds(amountOfoutsofbot))
        # print(diler.potOdds(diler.stavka))
        # print("END BOT-------------------------------------------------------")
        # botstack-=5
        if self.diler.playerOdds(amountOfoutsofbot) > self.diler.potOdds(self.diler.stavka) or self.diler.botpower>0 :
          print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
          if (self.diler.botpower>0):
            if bot == self.game.players[1]:
              self.diler.bankStack+=50
              self.diler.player1Stack -= 50
              self.diler.botpower=0
              self.diler.stavka=50
            elif bot == self.game.players[2]:
              self.diler.bankStack+=50
              self.diler.player2Stack -= 50
              self.diler.botpower=0
              self.diler.stavka=50
            elif bot == self.game.players[3]:
              self.diler.bankStack+=50
              self.diler.player3Stack -= 50
              self.diler.botpower=0
              self.diler.stavka=50
            elif bot == self.game.players[4]:
              self.diler.bankStack+=50
              self.diler.player4Stack -= 50
              self.diler.botpower=0
              self.diler.stavka=50
            elif bot == self.game.players[5]:
              self.diler.bankStack+=50
              self.diler.player5Stack -= 50
              self.diler.botpower=0
              self.diler.stavka=50
            elif bot == self.game.players[6]:
              self.diler.bankStack+=50
              self.diler.player6Stack -= 50
              self.diler.botpower=0
              self.diler.stavka=50
            elif bot == self.game.players[7]:
              self.diler.bankStack+=50
              self.diler.player7Stack -= 50
              self.diler.botpower=0
              self.diler.stavka=50
            elif bot == self.game.players[8]:
              self.diler.bankStack+=50
              self.diler.player8Stack -= 50
              self.diler.botpower=0
              self.diler.stavka=50
            elif bot == self.game.players[9]:
              self.diler.bankStack+=50
              self.diler.player9Stack -= 50
              self.diler.botpower=0
              self.diler.stavka=50
          else:
            print("PO AUTAM!")
            self.diler.bankStack += self.diler.stavka
            if bot == self.game.players[1]:
                self.diler.player1Stack -= self.diler.stavka
            elif bot == self.game.players[2]:
                self.diler.player2Stack -= self.diler.stavka
            elif bot == self.game.players[3]:
                self.diler.player3Stack -= self.diler.stavka
            elif bot == self.game.players[4]:
                self.diler.player4Stack -= self.diler.stavka
            elif bot == self.game.players[5]:
               self.diler.player5Stack -= self.diler.stavka
            elif bot == self.game.players[6]:
                self.diler.player6Stack -= self.diler.stavka
            elif bot == self.game.players[7]:
                self.diler.player7Stack -= self.diler.stavka
            elif bot == self.game.players[8]:
                self.diler.player8Stack -= self.diler.stavka
            elif bot == self.game.players[9]:
                self.diler.player9Stack -= self.diler.stavka

          botstack -= self.diler.stavka
          strin="BANK :   " + str(self.diler.bankStack)
          self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
          self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)

          if bot == self.game.players[1]:
                self.player1s = Label(self.root,text=self.diler.player1Stack, bg="PaleGreen2")
                self.player1s.place(relx=0.23, rely=0.03, anchor=CENTER)
          elif bot == self.game.players[2]:
                self.player2s = Label(self.root,text=self.diler.player2Stack, bg="PaleGreen2")
                self.player2s.place(relx=0.33, rely=0.03, anchor=CENTER)
          elif bot == self.game.players[3]:
                self.player3s = Label(self.root,text=self.diler.player3Stack, bg="PaleGreen2")
                self.player3s.place(relx=0.43, rely=0.08, anchor=CENTER)
          elif bot == self.game.players[4]:
                self.player4s = Label(self.root,text=self.diler.player4Stack, bg="PaleGreen2")
                self.player4s.place(relx=0.43, rely=0.16, anchor=CENTER)
          elif bot == self.game.players[5]:
                self.player5s = Label(self.root,text=self.diler.player5Stack, bg="PaleGreen2")
                self.player5s.place(relx=0.43, rely=0.24, anchor=CENTER)
          elif bot == self.game.players[6]:
                self.player6s = Label(self.root,text=self.diler.player6Stack, bg="PaleGreen2")
                self.player6s.place(relx=0.33, rely=0.28, anchor=CENTER)
          elif bot == self.game.players[7]:
                self.player7s = Label(self.root,text=self.diler.player7Stack, bg="PaleGreen2")
                self.player7s.place(relx=0.23, rely=0.28, anchor=CENTER)
          elif bot == self.game.players[8]:
                self.player8s = Label(self.root,text=self.diler.player8Stack, bg="PaleGreen2")
                self.player8s.place(relx=0.093, rely=0.24, anchor=CENTER)
          elif bot == self.game.players[9]:
                self.player9s = Label(self.root,text=self.diler.player9Stack, bg="PaleGreen2")
                self.player9s.place(relx=0.083, rely=0.09, anchor=CENTER)


        else:
            if (bot == self.game.players[1]):
                print("OFFFFFF")
                self.player1s.destroy()
                self.player1s = Label(self.root,text="OFF", bg="PaleGreen2")
                self.player1s.place(relx=0.23, rely=0.03, anchor=CENTER)
            elif (bot == self.game.players[2]):
                self.player2s = Label(self.root,text="OFF", bg="PaleGreen2")
                self.player2s.place(relx=0.33, rely=0.03, anchor=CENTER)
            elif (bot == self.game.players[3]):
                self.player3s = Label(self.root,text="OFF", bg="PaleGreen2")
                self.player3s.place(relx=0.43, rely=0.08, anchor=CENTER)
            elif (bot == self.game.players[4]):
                self.player4s = Label(self.root,text="OFF", bg="PaleGreen2")
                self.player4s.place(relx=0.43, rely=0.16, anchor=CENTER)
            elif (bot == self.game.players[5]):
                self.player5s = Label(self.root,text="OFF", bg="PaleGreen2")
                self.player5s.place(relx=0.43, rely=0.24, anchor=CENTER)
            elif (bot == self.game.players[6]):
                self.player6s = Label(self.root,text="OFF", bg="PaleGreen2")
                self.player6s.place(relx=0.33, rely=0.28, anchor=CENTER)
            elif (bot == self.game.players[7]):
                self.player7s = Label(self.root,text="OFF", bg="PaleGreen2")
                self.player7s.place(relx=0.23, rely=0.28, anchor=CENTER)
            elif (bot == self.game.players[8]):
                self.player8s = Label(self.root,text="OFF", bg="PaleGreen2")
                self.player8s.place(relx=0.093, rely=0.24, anchor=CENTER)
            elif (bot == self.game.players[9]):
                self.player9s = Label(self.root,text="OFF", bg="PaleGreen2")
                self.player9s.place(relx=0.083, rely=0.09, anchor=CENTER)
        botandtable.pop()
        botandtable.pop()

        self.diler.botpower=0
      print("AEEEEEEEE"+str(self.player1s.cget("text")))
      if (str(self.player1s.cget("text"))=="OFF" and str(self.player2s.cget("text"))=="OFF"and str(self.player3s.cget("text"))=="OFF"
          and str(self.player4s.cget("text"))=="OFF"and str(self.player5s.cget("text"))=="OFF"and str(self.player6s.cget("text"))=="OFF"
          and str(self.player7s.cget("text"))=="OFF"and str(self.player8s.cget("text"))=="OFF"and str(self.player9s.cget("text"))=="OFF"):
            self.diler.myPlayerstack+=self.diler.bankStack
            self.diler.bankStack=0
            self.playerbet = Label(self.root, text="YOUR STACK :  " + str(self.diler.myPlayerstack), font=("Times",10,"bold"), border=3,bg="green4", fg="#4B0082")
            self.playerbet.place(relx=0.057, rely=0.785, anchor=CENTER)
            strin="BANK :   " + str(self.diler.bankStack)
            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)
            popupmsg1(" You won! Other players fall")


























    def step1(self):

        if(self.diler.flagofDiler==0):
            # if (self.diler.flagofbet == 0):
                self.diler.flagOfBet=True
                if(self.diler.flagOfblind==0):
                        if(self.diler.BigBlind==2):

                            self.diler.bankStack+=6
                            self.diler.player1Stack -= 6
                            self.diler.botpower=0
                            self.diler.stavka=6


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player1s = Label(self.root,text=self.diler.player1Stack, bg="PaleGreen2")
                            self.player1s.place(relx=0.23, rely=0.03, anchor=CENTER)

                            self.diler.bankStack+=12
                            self.diler.player2Stack -= 12
                            self.diler.botpower=0
                            self.diler.stavka=12


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player2s = Label(self.root,text=self.diler.player2Stack, bg="PaleGreen2")
                            self.player2s.place(relx=0.33, rely=0.03, anchor=CENTER)
                            #self.diler.flagstep=self.diler.utg

                        elif(self.diler.BigBlind==3):

                            self.diler.bankStack+=6
                            self.diler.player2Stack -= 6
                            self.diler.botpower=0
                            self.diler.stavka=6


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player2s = Label(self.root,text=self.diler.player2Stack, bg="PaleGreen2")
                            self.player2s.place(relx=0.33, rely=0.03, anchor=CENTER)
                            #self.diler.flagstep=self.diler.utg


                            self.diler.bankStack+=12
                            self.diler.player3Stack -= 12
                            self.diler.botpower=0
                            self.diler.stavka=12


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player3s = Label(self.root,text=self.diler.player3Stack, bg="PaleGreen2")
                            self.player3s.place(relx=0.43, rely=0.08, anchor=CENTER)
                            #self.diler.flagstep=self.diler.utg

                        elif(self.diler.BigBlind==4):

                            self.diler.bankStack+=6
                            self.diler.player3Stack -= 6
                            self.diler.botpower=0
                            self.diler.stavka=6


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player3s = Label(self.root,text=self.diler.player3Stack, bg="PaleGreen2")
                            self.player3s.place(relx=0.43, rely=0.08, anchor=CENTER)


                            self.diler.bankStack+=12
                            self.diler.player4Stack -= 12
                            self.diler.botpower=0
                            self.diler.stavka=12


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player4s = Label(self.root,text=self.diler.player4Stack, bg="PaleGreen2")
                            self.player4s.place(relx=0.43, rely=0.16, anchor=CENTER)

                        elif(self.diler.BigBlind==5):

                            self.diler.bankStack+=6
                            self.diler.player4Stack -= 6
                            self.diler.botpower=0
                            self.diler.stavka=6


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player4s = Label(self.root,text=self.diler.player4Stack, bg="PaleGreen2")
                            self.player4s.place(relx=0.43, rely=0.16, anchor=CENTER)


                            self.diler.bankStack+=12
                            self.diler.player5Stack -= 12
                            self.diler.botpower=0
                            self.diler.stavka=12


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player5s = Label(self.root,text=self.diler.player5Stack, bg="PaleGreen2")
                            self.player5s.place(relx=0.43, rely=0.24, anchor=CENTER)


                        elif(self.diler.BigBlind==6):

                            self.diler.bankStack+=6
                            self.diler.player5Stack -= 6
                            self.diler.botpower=0
                            self.diler.stavka=6


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player5s = Label(self.root,text=self.diler.player5Stack, bg="PaleGreen2")
                            self.player5s.place(relx=0.43, rely=0.24, anchor=CENTER)


                            self.diler.bankStack+=12
                            self.diler.player6Stack -= 12
                            self.diler.botpower=0
                            self.diler.stavka=12


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player6s = Label(self.root,text=self.diler.player6Stack, bg="PaleGreen2")
                            self.player6s.place(relx=0.33, rely=0.28, anchor=CENTER)


                        elif(self.diler.BigBlind==7):

                            self.diler.bankStack+=6
                            self.diler.player6Stack -= 6
                            self.diler.botpower=0
                            self.diler.stavka=6


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player6s = Label(self.root,text=self.diler.player6Stack, bg="PaleGreen2")
                            self.player6s.place(relx=0.33, rely=0.28, anchor=CENTER)


                            self.diler.bankStack+=12
                            self.diler.player7Stack -= 12
                            self.diler.botpower=0
                            self.diler.stavka=12


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player7s = Label(self.root,text=self.diler.player7Stack, bg="PaleGreen2")
                            self.player7s.place(relx=0.23, rely=0.28, anchor=CENTER)


                        elif(self.diler.BigBlind==8):

                            self.diler.bankStack+=6
                            self.diler.player7Stack -= 6
                            self.diler.botpower=0
                            self.diler.stavka=6


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player7s = Label(self.root,text=self.diler.player7Stack, bg="PaleGreen2")
                            self.player7s.place(relx=0.23, rely=0.28, anchor=CENTER)


                            self.diler.bankStack+=12
                            self.diler.player8Stack -= 12
                            self.diler.botpower=0
                            self.diler.stavka=12


                            strin="BANK :   " + str(self.diler.bankStack)
                            self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                            self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                            self.player8s = Label(self.root,text=self.diler.player8Stack, bg="PaleGreen2")
                            self.player8s.place(relx=0.093, rely=0.24, anchor=CENTER)

                        # elif(self.diler.BigBlind==9):
                        #
                        #     self.diler.bankStack+=6
                        #     self.diler.player8Stack -= 6
                        #     self.diler.botpower=0
                        #     self.diler.stavka=6
                        #
                        #
                        #     strin="BANK :   " + str(self.diler.bankStack)
                        #     self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                        #     self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)
                        #
                        #
                        #     self.player8s = Label(self.root,text=self.diler.player8Stack, bg="PaleGreen2")
                        #     self.player8s.place(relx=0.093, rely=0.24, anchor=CENTER)
                        #
                        #
                        #     self.diler.bankStack+=12
                        #     self.diler.player9Stack -= 12
                        #     self.diler.botpower=0
                        #     self.diler.stavka=12
                        #
                        #
                        #     strin="BANK :   " + str(self.diler.bankStack)
                        #     self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                        #     self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)
                        #
                        #
                        #     self.player9s = Label(self.root,text=self.diler.player9Stack, bg="PaleGreen2")
                        #     self.player9s.place(relx=0.083, rely=0.09, anchor=CENTER)





                self.diler.flagstep=self.diler.utg

                while (self.diler.flagstep != 9):
                    if(self.diler.flagstep==1):
                        self.diler.stavka=self.diler.stavka-6;
                        self.step()
                        self.diler.stavka=self.diler.stavka+6;
                    else:
                        self.step()
                self.botcall(self.diler.player9Stack, self.game.players[9])
                self.diler.flagstep = 1
                self.diler.flagofbet = 1
                self.diler.flagofDiler=1


            # else:
            #     self.diler.flagofbet = 1
            #     popupmsg1("You Dont Make Step")


        else:
            if (self.diler.flagofbet == 0):
                self.diler.flagOfBet=True
                self.diler.flagstep=1

                while (self.diler.flagstep != self.diler.utg):
                    self.step()
                self.botcall(self.diler.player9Stack, self.game.players[9])
                self.diler.flagstep = 1
                self.diler.flagofbet = 1
                self.diler.flagofDiler=0
            else:
                self.diler.flagofbet = 1
                popupmsg1("You Dont Make Step")
        if (self.diler.potOdds(self.diler.stavka) == -1):
                                self.lbodds = Label(self.separator, text="Pot odds can not be determined at this time ",
                                                    bg="sea green",fg='#4B0082')
        else:
                                self.lbodds = Label(self.separator, text="Pot Odds: " + str(self.diler.potOdds(self.diler.mystavka)) + " %",
                                                    bg="sea green",fg='#4B0082')
        self.lbodds.place(relx=0.5, rely=0.4, anchor=CENTER)



    def step2(self):
        if (self.diler.flagofbet == 0):
            self.diler.flagOfBet=True
            while (self.diler.flagstep != 9):
                self.step()
            self.botcall(self.diler.player9Stack, self.game.players[9])
            self.diler.flagstep = 1
            self.diler.flagofbet = 1
        else:
            popupmsg1("You Dont Make Step")

    def step(self):
        if (self.diler.flagstep == 1):
            self.botcall(self.diler.player1Stack, self.game.players[1])

            self.diler.flagstep = 2
        elif (self.diler.flagstep == 2):
            self.botcall(self.diler.player2Stack, self.game.players[2])

            self.diler.flagstep = 3
        elif (self.diler.flagstep == 3):
            self.botcall(self.diler.player3Stack, self.game.players[3])

            self.diler.flagstep = 4
        elif (self.diler.flagstep == 4):
            self.botcall(self.diler.player4Stack, self.game.players[4])

            self.diler.flagstep = 5
        elif (self.diler.flagstep == 5):
            self.botcall(self.diler.player5Stack, self.game.players[5])

            self.diler.flagstep = 6
        elif (self.diler.flagstep == 6):
            self.botcall(self.diler.player6Stack, self.game.players[6])

            self.diler.flagstep = 7
        elif (self.diler.flagstep == 7):
            self.botcall(self.diler.player7Stack, self.game.players[7])

            self.diler.flagstep = 8
        elif (self.diler.flagstep == 8):
            self.botcall(self.diler.player8Stack, self.game.players[8])

            self.diler.flagstep = 9
        elif (self.diler.flagstep == 9):
            self.botcall(self.diler.player9Stack, self.game.players[9])

            self.diler.flagstep = 1

    def mraise(self):
        if (self.diler.flagofbet == 1):
            self.scal = self.scale1.get()
            if (self.scal > self.diler.myPlayerstack):
                popupmsg("YOU HAVE NO MONEY!Try to make make less bet")
            else:
              if self.scal<=self.diler.stavka:
                  popupmsg1("You Cant Bet Less Then Current:    "+str(self.diler.stavka))
              else:
                self.diler.stavka = self.scal
                self.diler.bankStack += self.scal
                self.BANKbet.destroy()
                self.diler.myPlayerstack -= self.scal
                self.playerbet = Label(self.root,text="YOUR STACK :  " + str(self.diler.myPlayerstack), font=("Times",10,"bold"),border=3,bg="green4", fg="#4B0082")
                self.playerbet.place(relx=0.057, rely=0.785, anchor=CENTER)
                strin="BANK :   " + str(self.diler.bankStack)
                self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)
                self.diler.mystavka=self.scal
            self.diler.flagofbet = 0
        else:
            popupmsg1("Wait Your Step!")
    def getWinner(self):
        if (self.flagGetWinner==1):
                      bot= self.game.players[self.comb.checkWinner1(self.comb, self.game.players, self.game.tableCards)]
                      if bot == self.game.players[1]:
                        self.diler.player1Stack+=self.diler.bankStack
                        self.diler.bankStack=0
                        self.player1s = Label(self.root,text=self.diler.player1Stack, bg="PaleGreen2")
                        self.player1s.place(relx=0.23, rely=0.03, anchor=CENTER)
                      elif bot == self.game.players[2]:
                            self.diler.player2Stack+=self.diler.bankStack
                            self.diler.bankStack=0
                            self.player2s = Label(self.root,text=self.diler.player2Stack, bg="PaleGreen2")
                            self.player2s.place(relx=0.33, rely=0.03, anchor=CENTER)
                      elif bot == self.game.players[3]:
                            self.diler.player3Stack+=self.diler.bankStack
                            self.diler.bankStack=0
                            self.player3s = Label(self.root,text=self.diler.player3Stack, bg="PaleGreen2")
                            self.player3s.place(relx=0.43, rely=0.08, anchor=CENTER)
                      elif bot == self.game.players[4]:
                            self.diler.player4Stack+=self.diler.bankStack
                            self.diler.bankStack=0
                            self.player4s = Label(self.root,text=self.diler.player4Stack, bg="PaleGreen2")
                            self.player4s.place(relx=0.43, rely=0.16, anchor=CENTER)
                      elif bot == self.game.players[5]:
                            self.diler.player5Stack+=self.diler.bankStack
                            self.diler.bankStack=0
                            self.player5s = Label(self.root,text=self.diler.player5Stack, bg="PaleGreen2")
                            self.player5s.place(relx=0.43, rely=0.24, anchor=CENTER)
                      elif bot == self.game.players[6]:
                            self.diler.player6Stack+=self.diler.bankStack
                            self.diler.bankStack=0
                            self.player6s = Label(self.root,text=self.diler.player6Stack, bg="PaleGreen2")
                            self.player6s.place(relx=0.33, rely=0.28, anchor=CENTER)
                      elif bot == self.game.players[7]:
                            self.diler.player7Stack+=self.diler.bankStack
                            self.diler.bankStack=0
                            self.player7s = Label(self.root,text=self.diler.player7Stack, bg="PaleGreen2")
                            self.player7s.place(relx=0.23, rely=0.28, anchor=CENTER)
                      elif bot == self.game.players[8]:
                            self.diler.player8Stack+=self.diler.bankStack
                            self.diler.bankStack=0
                            self.player8s = Label(self.root,text=self.diler.player8Stack, bg="PaleGreen2")
                            self.player8s.place(relx=0.093, rely=0.24, anchor=CENTER)
                      elif bot == self.game.players[9]:
                            self.diler.player9Stack+=self.diler.bankStack
                            self.diler.bankStack=0
                            self.player9s = Label(self.root,text=self.diler.player9Stack, bg="PaleGreen2")
                            self.player9s.place(relx=0.083, rely=0.09, anchor=CENTER)
                      elif bot == self.game.players[0]:
                            self.diler.myPlayerstack+=self.diler.bankStack
                            self.diler.bankStack=0
                            self.playerbet = Label(self.root, text="YOUR STACK :  " + str(self.diler.myPlayerstack), font=("Times",10,"bold"), border=3,bg="green4", fg="#4B0082")
                            self.playerbet.place(relx=0.057, rely=0.785, anchor=CENTER)



                      strin="BANK :   " + str(self.diler.bankStack)
                      self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                      self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)


                      popupmsg2(self.comb.checkWinner(self.comb, self.game.players, self.game.tableCards),
                          self.game.players[self.comb.checkWinner1(self.comb, self.game.players, self.game.tableCards)])


                      # self.diler.massive=[]
                      # if (bot == self.game.players[0]):
                      #               self.diler.massive.append(self.game.players[0])
                      #
                      # if (bot == self.game.players[1]):
                      #           if self.player1s['text']!="OFF":
                      #               self.diler.massive.append(self.game.players[1])
                      #
                      # elif (bot == self.game.players[2]):
                      #           if self.player2s['text']!="OFF":
                      #               self.diler.massive.append(self.game.players[2])
                      #
                      # elif (bot == self.game.players[3]):
                      #           if self.player3s['text']!="OFF":
                      #               self.diler.massive.append(self.game.players[3])
                      # elif (bot == self.game.players[4]):
                      #           if self.player4s['text']!="OFF":
                      #               self.diler.massive.append(self.game.players[4])
                      # elif (bot == self.game.players[5]):
                      #           if self.player5s['text']!="OFF":
                      #               self.diler.massive.append(self.game.players[5])
                      # elif (bot == self.game.players[6]):
                      #           if self.player6s['text']!="OFF":
                      #              self.diler.massive.append(self.game.players[6])
                      # elif (bot == self.game.players[7]):
                      #           if self.player7s['text']!="OFF":
                      #               self.diler.massive.append(self.game.players[7])
                      # elif (bot == self.game.players[8]):
                      #           if self.player8s['text']!="OFF":
                      #               self.diler.massive.append(self.game.players[8])
                      # elif (bot == self.game.players[9]):
                      #           if self.player9s['text']!="OFF":
                      #               self.diler.massive.append(self.game.players[9])
                      #
                      #
                      # strin="BANK :   " + str(self.diler.bankStack)
                      # self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
                      # self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)
                      #
                      #
                      # popupmsg2(self.comb.checkWinner(self.comb, self.diler.massive, self.game.tableCards),
                      #     self.diler.massive[self.comb.checkWinner1(self.comb, self.diler.massive, self.game.tableCards)])
                      #

    def openriver(self):
        self.diler.flagofDiler=0
        print(self.diler.mystavka)
        print(self.diler.stavka)
        if self.diler.mystavka<self.diler.stavka:
                self.diler.flagOfReStavka=1
        else:
            self.diler.flagOfReStavka=0
        if(self.diler.flagOfReStavka==0):
                  if (self.diler.flagOfBet):
                    self.diler.flagOfBet=False
                    self.lbodds.destroy()
                    self.lpodds.destroy()
                    self.diler.flagGetWinner=0
                    if (self.flagtern != 0):
                        if (self.flagriver != 1):
                            self.diler.stavka=0
                            # self.comblpara.destroy()
                            # self.combl2para.destroy()
                            self.comblset.destroy()
                            # self.combl.destroy()
                            self.flagriver = 1
                            self.game.update_table_riverRandom()
                            self.river = self.game.tableCards[4]
                            if (self.river.card_suit == 1):
                                self.flag5 = "б"
                            elif (self.river.card_suit == 2):
                                self.flag5 = "ч"
                            elif (self.river.card_suit == 3):
                                self.flag5 = "п"
                            elif (self.river.card_suit == 4):
                                self.flag5 = "к"

                            self.card5flop = str(self.flag5) + str(self.river.card_rating)
                            self.photof5 = PhotoImage(file="./images/" + self.card5flop + ".gif")
                            self.cardf5 = Label(self.root, image=self.photof5)
                            self.cardf5.place(relx=0.93, rely=0.225, anchor=CENTER)
                            self.comb = CheckComb(self.game.myCardWithTable)
                            self.combl = Label(self.separator1, text="Combinations:      ", bg="green",fg='#4B0082')
                            #self.combl.place(relx=0.75, rely=0.65, anchor=CENTER)
                            self.combl.place(relx=0.3, rely=0.2, anchor=CENTER)
                            self.checkcomb(self.comb)
                            self.mcombl.destroy()

                        if (self.diler.potOdds(self.diler.mystavka) == -1):
                            self.lbodds = Label(self.separator, text="Pot odds can not be determined at this time ",
                                               bg="sea green",fg='#4B0082')
                        else:
                            self.lbodds = Label(self.separator, text="Pot Odds: " + str(self.diler.potOdds(self.diler.mystavka)) + " %",
                                                bg="sea green",fg='#4B0082')
                        #self.lbodds.place(relx=0.144, rely=0.90, anchor=CENTER)
                        self.lbodds.place(relx=0.5, rely=0.4, anchor=CENTER)

                        self.lpodds = Label(self.separator, text="Your ODDS: " + str(self.diler.playerOdds(self.amountOfouts)) + " %",
                                            bg="sea green",fg='#4B0082')
                        #self.lpodds.place(relx=0.112, rely=0.95, anchor=CENTER)
                        self.lpodds.place(relx=0.5, rely=0.6, anchor=CENTER)
                        for i in self.game.tableCards:
                            print(str(i.card_rating) + " " + str(i.card_suit))
                        self.flagGetWinner=1
                        # popupmsg2(self.comb.checkWinner(self.comb, self.game.players, self.game.tableCards),
                        #           self.game.players[self.comb.checkWinner1(self.comb, self.game.players, self.game.tableCards)])
                        self.flagofbet = 0
                        self.diler.flagofbet = 0
                        self.diler.flagOfblind=1
        else:
                 popupmsg1("You Can not make open because you don't equalize!")

    def opentern(self):
        self.diler.flagofDiler=0
        print(self.diler.mystavka)
        print(self.diler.stavka)
        if self.diler.mystavka<self.diler.stavka:
                self.diler.flagOfReStavka=1
        else:
         self.diler.flagOfReStavka=0
        if(self.diler.flagOfReStavka==0):
              if (self.diler.flagOfBet):
                self.diler.flagOfBet=False
                self.diler.flagGetWinner=0
                self.lbodds.destroy()
                self.lpodds.destroy()
                if (self.flagtern != 1):
                    self.diler.stavka=0
                    # self.comblpara.destroy()
                    # self.combl2para.destroy()
                    self.comblset.destroy()
                    self.mcombl.destroy()
                    # self.combl.destroy()
                    self.flagtern = 1
                    self.game.update_table_ternRandom()
                    self.tern = self.game.tableCards[3]
                    if (self.tern.card_suit == 1):
                        self.flag5 = "б"
                    elif (self.tern.card_suit == 2):
                        self.flag5 = "ч"
                    elif (self.tern.card_suit == 3):
                        self.flag5 = "п"
                    elif (self.tern.card_suit == 4):
                        self.flag5 = "к"
                    self.card4flop = str(self.flag5) + str(self.tern.card_rating)
                    self.photof4 = PhotoImage(file="./images/" + self.card4flop + ".gif")
                    self.cardf4 = Label(self.root, image=self.photof4)
                    self.cardf4.place(relx=0.84, rely=0.225, anchor=CENTER)
                    self.comb = CheckComb(self.game.myCardWithTable)
                    self.combl = Label(self.separator1, text="Combinations:      ", bg="green",fg='#4B0082')
                    #self.combl.place(relx=0.75, rely=0.65, anchor=CENTER)
                    self.combl.place(relx=0.3, rely=0.2, anchor=CENTER)
                    self.checkcomb(self.comb)
                    self.out = CheckOuts(self.game, CheckComb(self.game.myCardWithTable))
                    self.out.checkOut()
                    self.amountOfouts = self.out.outs
                    self.mcombl = Label(self.separator1, text="Amounts of OUTS:    " + str(self.amountOfouts), bg="sea green",fg='#4B0082')
                    #self.mcombl.place(relx=0.85, rely=0.65, anchor=CENTER)
                    self.mcombl.place(relx=0.5, rely=0.6, anchor=CENTER)
                    if (self.diler.potOdds(self.diler.stavka) == -1):
                        self.lbodds = Label(self.separator,text="Pot odds can not be determined at this time ",
                                          bg="sea green",fg='#4B0082')
                    else:
                        self.lbodds = Label(self.separator,text="Pot Odds: " + str(self.diler.potOdds(self.diler.mystavka)) + " %",
                                            bg="sea green",fg='#4B0082')
                    #self.lbodds.place(relx=0.144, rely=0.90, anchor=CENTER)
                    self.lbodds.place(relx=0.5, rely=0.4, anchor=CENTER)
                    self.lpodds = Label(self.separator, text="Your ODDS: " + str(self.diler.playerOdds(self.amountOfouts)) + " %",
                                        bg="sea green",fg='#4B0082')
                    #self.lpodds.place(relx=0.112, rely=0.95, anchor=CENTER)
                    self.lpodds.place(relx=0.5, rely=0.6, anchor=CENTER)
                    self.flagofbet = 0
                    self.diler.flagofbet = 0
                    self.diler.flagOfblind=1
        else:
                 popupmsg1("You Can not make open because you don't equalize!")
    def openflop(self):
            self.diler.flagofDiler=0
            if self.diler.mystavka<self.diler.stavka:
                print(self.diler.mystavka)
                print(self.diler.stavka)
                self.diler.flagOfReStavka=1
            else:
                print(self.diler.mystavka)
                print(self.diler.stavka)
                self.diler.flagOfReStavka=0
            if(self.diler.flagOfReStavka==0):
                      if (self.diler.flagOfBet):
                        self.diler.flagOfBet=False
                        self.diler.flagGetWinner=0
                        if (self.flagofflop != 1):
                            self.flagofflop = 1
                            self.diler.stavka=0
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
                            self.card2flop = str(self.flag3) + str(self.flop[1].card_rating)
                            self.card3flop = str(self.flag4) + str(self.flop[2].card_rating)

                            # self.flopCard = Label(self.master, text="Карты стола:      ", bg="red")
                            # self.flopCard.place(relx=0.75, rely=0.03, anchor=CENTER)
                            self.photof1 = PhotoImage(file="./images/" + self.card1flop + ".gif")
                            self.cardf1 = Label(self.root, image=self.photof1)
                            self.cardf1.place(relx=0.55, rely=0.225, anchor=CENTER)

                            self.photof2 = PhotoImage(file="./images/" + self.card2flop + ".gif")
                            self.cardf2 = Label(self.root, image=self.photof2)
                            self.cardf2.place(relx=0.65, rely=0.225, anchor=CENTER)

                            self.photof3 = PhotoImage(file="./images/" + self.card3flop + ".gif")
                            self.cardf3 = Label(self.root, image=self.photof3)
                            self.cardf3.place(relx=0.75, rely=0.225, anchor=CENTER)

                            self.comb = CheckComb(self.game.myCardWithTable)
                            self.combl = Label(self.separator1, text="Combinations:      ", bg="green",fg='#4B0082')
                            #self.combl.place(relx=0.75, rely=0.65, anchor=CENTER)
                            self.combl.place(relx=0.3, rely=0.2, anchor=CENTER)
                            self.checkcomb(self.comb)

                            self.out = CheckOuts(self.game, CheckComb(self.game.myCardWithTable))
                            self.out.checkOut()
                            self.amountOfouts = self.out.outs
                            self.mcombl = Label(self.separator1, text="Amounts of OUTS:    " + str(self.amountOfouts),bg="sea green",fg='#4B0082')
                            #self.mcombl.place(relx=0.85, rely=0.65, anchor=CENTER)
                            self.mcombl.place(relx=0.5, rely=0.6, anchor=CENTER)
                            if (self.diler.potOdds(self.diler.stavka) == -1):
                                self.lbodds = Label(self.separator, text="Pot odds can not be determined at this time ",
                                                    bg="sea green",fg='#4B0082')
                            else:
                                self.lbodds = Label(self.separator, text="Pot Odds: " + str(self.diler.potOdds(self.diler.mystavka)) + " %",
                                                    bg="sea green",fg='#4B0082')
                            #self.lbodds.place(relx=0.144, rely=0.90, anchor=CENTER)
                            self.lbodds.place(relx=0.5, rely=0.4, anchor=CENTER)
                            self.lpodds = Label(self.separator, text="Your ODDS: " + str(self.diler.playerOdds(self.amountOfouts)) + " %",
                                                bg="sea green",fg='#4B0082')
                           # self.lpodds.place(relx=0.112, rely=0.95, anchor=CENTER)
                            self.lpodds.place(relx=0.5, rely=0.6, anchor=CENTER)
                            self.flagofbet = 0
                            self.diler.flagofbet = 0
                            self.diler.flagOfblind=1
            else:
                 popupmsg1("You Can not make open because you don't equalize!")


    def UpdateLabel(self):
        #self.lbodds.destroy()
        #self.lpodds.destroy()

        self.diler.flagOfblind=0
        self.diler.flagofDiler=0
        self.flagofbet = 0
        self.diler.flagofbet = 0
        self.diler.stavka=0
        self.diler.flagOfBet=False
        self.diler.flagGetWinner=0
        self.diler.bankStack = 0
        self.BANKbet.destroy()
        strin="BANK :   " + str(self.diler.bankStack)
        self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
        self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)
        self.delete()
        for i in self.game.players:
            i.active=True
        self.MyPosition.destroy()
        self.dilerPosition.destroy()
        self.my__init__(self.root, self.diler)
        self.diler.update_position()
        self.MyPosition.destroy()
        self.MyPosition = Label(self.root,text=self.diler.show_position(), bg='green4',fg='#00ffBB')
        self.MyPosition.place(relx=0.1, rely=0.43, anchor=CENTER)
        self.dilerPosition.destroy()
        self.dilerPosition = Label(self.root,text="Diler", bg='gray20',fg='#00ffBB',font=("Times", 10,"bold"))
        if (self.diler.show_diler() == 0):
            self.playerYOU = Label(self.root,self.root, text="YOU :   ", bg='gray20',fg='red2',font=("Times", 15,"bold"))
            self.playerYOU.place(relx=0.132, rely=0.03, anchor=CENTER)
            self.dilerPosition.place(relx=0.102, rely=0.43, anchor=CENTER)
        elif (self.diler.show_diler() == 1):
            self.dilerPosition.place(relx=0.25, rely=0.04, anchor=CENTER)
        elif (self.diler.show_diler() == 2):
            self.dilerPosition.place(relx=0.35, rely=0.04, anchor=CENTER)
        elif (self.diler.show_diler() == 3):
            self.dilerPosition.place(relx=0.45, rely=0.09, anchor=CENTER)
        elif (self.diler.show_diler() == 4):
            self.dilerPosition.place(relx=0.45, rely=0.17, anchor=CENTER)
        elif (self.diler.show_diler() == 5):
            self.dilerPosition.place(relx=0.45, rely=0.25, anchor=CENTER)
        elif (self.diler.show_diler() == 6):
            self.dilerPosition.place(relx=0.35, rely=0.25, anchor=CENTER)
        elif (self.diler.show_diler() == 7):
            self.dilerPosition.place(relx=0.25, rely=0.25, anchor=CENTER)
        elif (self.diler.show_diler() == 8):
            self.dilerPosition.place(relx=0.113, rely=0.25, anchor=CENTER)
        elif (self.diler.show_diler() == 9):
            self.dilerPosition.place(relx=0.103, rely=0.1, anchor=CENTER)
            # self.mcombl.destroy()

    def my__init__(self, master, diler):
        #self.metod()
        self.diler.flagGetWinner=0
        self.flagtern = 0
        self.flagofflop = 0
        self.flagriver = 0
        self.master = master
        self.game = Game(10)
        self.bankStack = diler.bankStack
        self.playerbet = diler.myPlayerstack
        self.comb = CheckComb(self.game.myCardWithTable)
        # print(self.game.myPlayer.card1.card_suit)
        # print(self.game.myPlayer.card1.card_rating)
        # print(self.game.myPlayer.card2.card_suit)
        # print(self.game.myPlayer.card2.card_rating)

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

        self.playerCard = Label(self.root, text="YOUR POSITION :      ", bg="green4", fg="#4B0082",font=("Times",10,"bold"))
        self.playerCard.place(relx=0.048, rely=0.43, anchor=CENTER)

        #self.playerb = Label(self.root, text="Your BET :      ", bg="black", fg="green")
        #self.playerb.place(relx=0.058, rely=0.79, anchor=CENTER)

        self.scale1 = Scale(self.root, orient=HORIZONTAL, width=5, length=300, from_=5, to=2000, tickinterval=350,
                            resolution=5, bg='gray5',fg='#00ffBB',font=("Times", 11,"bold"))

        self.scale1.place(relx=0.118, rely=0.650, anchor=CENTER)

        self.playerbet = Label(self.root, text="YOUR STACK :  " + str(diler.myPlayerstack),  font=("Times",10,"bold"),border=3,bg="green4", fg="#4B0082")
        self.playerbet.place(relx=0.057, rely=0.785, anchor=CENTER)

        strin="BANK :   " + str(self.diler.bankStack)
        self.BANKbet = Label(self.root,text='%-13s' % strin, bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
        self.BANKbet.place(relx=0.74, rely=0.05, anchor=CENTER)

        self.player1 = Label(self.root, text="Lucke  :      ", bg='gray20',fg='RoyalBlue2',font=("Times", 10,"bold"))
        self.player1.place(relx=0.2, rely=0.03, anchor=CENTER)

        self.player2 = Label(self.root, text="Olivia :      ", bg='gray20',fg='RoyalBlue2',font=("Times", 10,"bold"))
        self.player2.place(relx=0.3, rely=0.03, anchor=CENTER)

        self.player3 = Label(self.root, text="Ashley :      ", bg='gray20',fg='RoyalBlue2',font=("Times", 10,"bold"))
        self.player3.place(relx=0.4, rely=0.08, anchor=CENTER)

        self.player4 = Label(self.root, text="Jacob  :      ", bg='gray20',fg='RoyalBlue2',font=("Times", 10,"bold"))
        self.player4.place(relx=0.4, rely=0.16, anchor=CENTER)

        self.player5 = Label(self.root, text="Ethan  :      ", bg='gray20',fg='RoyalBlue2',font=("Times", 10,"bold"))
        self.player5.place(relx=0.4, rely=0.24, anchor=CENTER)

        self.player6 = Label(self.root, text="Daniel :      ", bg='gray20',fg='RoyalBlue2',font=("Times", 10,"bold"))
        self.player6.place(relx=0.3, rely=0.28, anchor=CENTER)

        self.player7 = Label(self.root, text="Kayla  :      ", bg='gray20',fg='RoyalBlue2',font=("Times", 10,"bold"))
        self.player7.place(relx=0.2, rely=0.28, anchor=CENTER)

        self.player8 = Label(self.root, text="John   :      ", bg='gray20',fg='RoyalBlue2',font=("Times", 10,"bold"))
        self.player8.place(relx=0.062, rely=0.24, anchor=CENTER)

        self.player9 = Label(self.root, text="Tyler  :      ", bg='gray20',fg='RoyalBlue2',font=("Times", 10,"bold"))
        self.player9.place(relx=0.062, rely=0.09, anchor=CENTER)

        self.playerYOU = Label(self.root, text="YOU :   ", bg='gray20',fg='#00ffBB',font=("Times", 15,"bold"))
        self.playerYOU.place(relx=0.132, rely=0.03, anchor=CENTER)

        self.player1s = Label(self.root, text=diler.player1Stack,bg='turquoise4',fg='PaleGreen2')
        self.player1s.place(relx=0.23, rely=0.03, anchor=CENTER)

        self.player2s = Label(self.root, text=diler.player2Stack,bg='turquoise4',fg='PaleGreen2')
        self.player2s.place(relx=0.33, rely=0.03, anchor=CENTER)

        self.player3s = Label(self.root, text=diler.player3Stack, bg='turquoise4',fg='PaleGreen2')
        self.player3s.place(relx=0.43, rely=0.08, anchor=CENTER)

        self.player4s = Label(self.root, text=diler.player4Stack, bg='turquoise4',fg='PaleGreen2')
        self.player4s.place(relx=0.43, rely=0.16, anchor=CENTER)

        self.player5s = Label(self.root, text=diler.player5Stack, bg='turquoise4',fg='PaleGreen2')
        self.player5s.place(relx=0.43, rely=0.24, anchor=CENTER)

        self.player6s = Label(self.root, text=diler.player6Stack, bg='turquoise4',fg='PaleGreen2')
        self.player6s.place(relx=0.33, rely=0.28, anchor=CENTER)

        self.player7s = Label(self.root, text=diler.player7Stack, bg='turquoise4',fg='PaleGreen2')
        self.player7s.place(relx=0.23, rely=0.28, anchor=CENTER)

        self.player8s = Label(self.root, text=diler.player8Stack, bg='turquoise4',fg='PaleGreen2')
        self.player8s.place(relx=0.093, rely=0.24, anchor=CENTER)

        self.player9s = Label(self.root, text=diler.player9Stack, bg='turquoise4',fg='PaleGreen2')
        self.player9s.place(relx=0.083, rely=0.09, anchor=CENTER)

        self.photoMycard1 = PhotoImage(file="./images/" + self.card1inc + ".gif")
        self.card1 = Label(self.root,image=self.photoMycard1)
        self.card1.place(relx=0.032, rely=0.53, anchor=CENTER)


        self.photoMycard2 = PhotoImage(file="./images/" + self.card2inc + ".gif")
        self.card2 = Label(self.root, image=self.photoMycard2)
        self.card2.place(relx=0.1, rely=0.53, anchor=CENTER)
        self.amount_players = self.game.amount_players
        # if (self.amount_players == 10):
        #     self.diler = 0
        #     self.smallBlind = self.diler + 1
        #     self.BigBlind = self.diler + 2
        #     self.utg = self.diler + 3
        #     self.utg1 = self.diler + 4
        #     self.utg2 = self.diler + 5
        #     self.utg3 = self.diler + 6
        #     self.utg4 = self.diler + 7
        #     self.cutOff = self.amount_players - 1
        #     self.hiJack = self.amount_players - 2
        # elif (self.amount_players == 9):
        #     self.diler = 0
        #     self.smallBlind = self.diler + 1
        #     self.BigBlind = self.diler + 2
        #     self.utg = self.diler + 3
        #     self.utg1 = self.diler + 4
        #     self.utg2 = self.diler + 5
        #     self.utg3 = self.diler + 6
        #     self.cutOff = self.amount_players - 1
        #     self.hiJack = self.amount_players - 2
        # elif (self.amount_players == 8):
        #     self.diler = 0
        #     self.smallBlind = self.diler + 1
        #     self.BigBlind = self.diler + 2
        #     self.utg = self.diler + 3
        #     self.utg1 = self.diler + 4
        #     self.utg2 = self.diler + 5
        #     self.cutOff = self.amount_players - 1
        #     self.hiJack = self.amount_players - 2
        # elif (self.amount_players == 7):
        #     self.diler = 0
        #     self.smallBlind = self.diler + 1
        #     self.BigBlind = self.diler + 2
        #     self.utg = self.diler + 3
        #     self.utg1 = self.diler + 4
        #     self.cutOff = self.amount_players - 1
        #     self.hiJack = self.amount_players - 2
        # elif (self.amount_players == 6):
        #     self.diler = 0
        #     self.smallBlind = self.diler + 1
        #     self.BigBlind = self.diler + 2
        #     self.utg = self.diler + 3
        #     self.cutOff = self.amount_players - 1
        #     self.hiJack = self.amount_players - 2
        # elif (self.amount_players == 5):
        #     self.diler = 0
        #     self.smallBlind = self.diler + 1
        #     self.BigBlind = self.diler + 2
        #     self.cutOff = self.amount_players - 1
        #     self.hiJack = self.amount_players - 2
        # elif (self.amount_players == 4):
        #     self.diler = 0
        #     self.smallBlind = self.diler + 1
        #     self.BigBlind = self.diler + 2
        #     self.cutOff = self.amount_players - 1
        # elif (self.amount_players == 3):
        #     self.diler = 0
        #     self.smallBlind = self.diler + 1
        #     self.BigBlind = self.diler + 2
        # elif (self.amount_players == 2):
        #     self.diler = 0
        #     self.smallBlind = self.diler + 1


        self.MyPosition = Label(self.root, text=diler.show_position(), bg='green4',fg='#00ffBB')
        self.MyPosition.place(relx=0.1, rely=0.43, anchor=CENTER)

        self.dilerPosition = Label(self.root, text="Diler", bg='gray20',fg='#00ffBB',font=("Times", 10,"bold"))
        if (diler.show_diler() == 0):
            self.dilerPosition.place(relx=0.102, rely=0.43, anchor=CENTER)
        elif (diler.show_diler() == 1):
            self.dilerPosition.place(relx=0.102, rely=0.5, anchor=CENTER)
        elif (diler.show_diler() == 2):
            self.dilerPosition.place(relx=0.102, rely=0.7, anchor=CENTER)
        elif (diler.show_diler() == 3):
            self.dilerPosition.place(relx=0.102, rely=0.03, anchor=CENTER)
        elif (diler.show_diler() == 4):
            self.dilerPosition.place(relx=0.102, rely=0.03, anchor=CENTER)
        elif (diler.show_diler() == 5):
            self.dilerPosition.place(relx=0.102, rely=0.03, anchor=CENTER)
        elif (diler.show_diler() == 6):
            self.dilerPosition.place(relx=0.102, rely=0.29, anchor=CENTER)
        elif (diler.show_diler() == 7):
            self.dilerPosition.place(relx=0.102, rely=0.43, anchor=CENTER)
        elif (diler.show_diler() == 8):
            self.dilerPosition.place(relx=0.102, rely=0.03, anchor=CENTER)

        self.dilerPosition.place(relx=0.102, rely=0.43, anchor=CENTER)
        self.preflop = CheckHoleCards(self.game.myPlayer.card1, self.game.myPlayer.card2, diler.show_position(),
                                      self.game.amount_players, "act_raise")
        self.powerPreflop = self.preflop.check_power()
        self.separator = Frame(self.root,bg="green",height=150,width=300, bd=1, relief=SUNKEN)
        self.separator.place(relx=0.3, rely=0.9, anchor=CENTER)
        self.separator1 = Frame(self.root,bg="green",height=150,width=300, bd=1, relief=SUNKEN)
        self.separator1.place(relx=0.64, rely=0.9, anchor=CENTER)
        self.power = Label(self.separator, text="Actions On Preflop:      " + str(self.powerPreflop), bg="sea green",fg='#4B0082')
        self.power.place(relx=0.5, rely=0.2, anchor=CENTER)
        #self.power.place(relx=0.113, rely=0.85, anchor=CENTER)
        # self.powerpreflop=Label(master,text=str(self.powerPreflop),bg="grey")
        # self.powerpreflop.place(relx=0.062, rely=0.59, anchor=CENTER)

        self.buttonNewGame = Button(self.root, text="New Game: ",width=10,fg='#00ffBB', bg='gray20',font=("Times", 15,"bold"), command=self.UpdateLabel)
        # self.buttonNewGame.bind("<Button-1>",newGame)
        self.buttonNewGame.place(relx=0.87, rely=0.6, anchor=CENTER)

        self.buttonflop = Button(self.root, text="Open Flop: ",width=10,fg='#00ffBB', bg='gray20',font=("Times", 15,"bold"), command=self.openflop)
        # self.buttonNewGame.bind("<Button-1>",newGame)
        self.buttonflop.place(relx=0.87, rely=0.68, anchor=CENTER)

        self.buttontern = Button(self.root, text="Open Tern: ",width=10,fg='#00ffBB', bg='gray20',font=("Times", 15,"bold"), command=self.opentern)
        # self.buttonNewGame.bind("<Button-1>",newGame)
        self.buttontern.place(relx=0.87, rely=0.74, anchor=CENTER)

        self.buttonriver = Button(self.root, text="Open River: ", width=10,fg='#00ffBB', bg='gray20',font=("Times", 15,"bold"),command=self.openriver)
        # self.buttonNewGame.bind("<Button-1>",newGame)
        self.buttonriver.place(relx=0.87, rely=0.8, anchor=CENTER)

        self.buttonCALL = Button(self.root, text="Call", command=self.call, fg='#00ffBB', bg='gray20',width=10,font=("Times", 15,"bold"),)
        # self.buttonNewGame.bind("<Button-1>",newGame)
        self.buttonCALL.place(relx=0.067, rely=0.72, anchor=CENTER)

        self.buttonFALL = Button(self.root, text="Fall", fg='#00ffBB', bg='gray20',width=10,font=("Times", 15,"bold"),command=self.fall)
        # self.buttonNewGame.bind("<Button-1>",newGame)
        self.buttonFALL.place(relx=0.165, rely=0.72, anchor=CENTER)

        self.buttonRaise = Button(self.root, text="Raise", command=self.mraise, fg='#00ffBB', bg='gray20',width=10,font=("Times", 15,"bold"),)
        # self.buttonNewGame.bind("<Button-1>",newGame)
        self.buttonRaise.place(relx=0.287, rely=0.65, anchor=CENTER)

        self.buttonCheck = Button(self.root, text="Check", command=self.check, fg='#00ffBB', bg='gray20',width=10,font=("Times", 15,"bold"),)
        # self.buttonNewGame.bind("<Button-1>",newGame)
        self.buttonCheck.place(relx=0.287, rely=0.725, anchor=CENTER)

        self.buttonSTEP = Button(self.root, text="STEP", fg='#00ffBB', bg='gray20',width=10,font=("Times", 15,"bold"),command=self.step1)
        # self.buttonNewGame.bind("<Button-1>",newGame)
        self.buttonSTEP.place(relx=0.87, rely=0.9, anchor=CENTER)

        self.buttonGetWinner = Button(self.root, text="Get Winner", fg='#00ffBB',width=10, bg='gray20',font=("Times", 15,"bold"),command=self.getWinner)
        # self.buttonNewGame.bind("<Button-1>",newGame)
        self.buttonGetWinner.place(relx=0.87, rely=0.95, anchor=CENTER)
    def delete(self):
        self.power.destroy()
        self.BANKbet.destroy()
        if self.flagofflop == 1:
            self.cardf1.destroy()
            self.cardf2.destroy()
            self.cardf3.destroy()
            # self.comblpara.destroy()
            # self.combl2para.destroy()
            self.comblset.destroy()
            self.mcombl.destroy()
        if self.flagtern == 1:
            self.cardf4.destroy()
            # self.comblpara.destroy()
            # self.combl2para.destroy()
            self.comblset.destroy()
            self.mcombl.destroy()

        if self.flagriver == 1:
            self.cardf5.destroy()
            # self.comblpara.destroy()
            # self.combl2para.destroy()
            self.comblset.destroy()
            self.mcombl.destroy()







def popupmsg(msg):
    popup = Toplevel()
    popup["bg"] = "OrangeRed3"
    popup.wm_title("!Be careful!")
    label = Label(popup, text=msg, fg="white", bg="red4")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Ok", command=popup.destroy, fg="white", bg="red4")
    B1.pack()
    popup.mainloop()


def popupmsg1(msg):
    popup = Toplevel()
    popup["bg"] = "OrangeRed3"
    popup.wm_title("!Be careful!")
    label = Label(popup, text=msg, fg="white", bg="red4")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Ok", command=popup.destroy, fg="white", bg="red4")
    B1.pack()
    popup.mainloop()


def popupmsg2(msg, player):
    mpopup = Toplevel()
    mpopup["bg"] = "OrangeRed3"
    mpopup.wm_title("!winner!")
    flag = ""
    flag1 = ""

    if (player.card1.card_suit == 1):
        flag = "б"
    elif (player.card1.card_suit == 2):
        flag = "ч"
    elif (player.card1.card_suit == 3):
        flag = "п"
    elif (player.card1.card_suit == 4):
        flag = "к"
    if (player.card2.card_suit == 1):
        flag1 = "б"
    elif (player.card2.card_suit == 2):
        flag1 = "ч"
    elif (player.card2.card_suit == 3):
        flag1 = "п"
    elif (player.card2.card_suit == 4):
        flag1 = "к"

    card1inc = str(flag) + str(player.card1.card_rating)
    card2inc = str(flag1) + str(player.card2.card_rating)

    label = Label(mpopup, text=msg, fg='#00ffBB', bg='gray20')
    label.pack(side="top", fill="x", pady=10)

    photoMycard111 = PhotoImage(file="./images/" + card1inc + ".gif")
    card1 = Label(mpopup, image=photoMycard111)
    card1.pack(side="left", pady=50, padx=10)

    photoMycard222 = PhotoImage(file="./images/" + card2inc + ".gif")
    card2 = Label(mpopup, image=photoMycard222)
    card2.pack(side="right", pady=50, padx=10)

    B1 = Button(mpopup, text="OK", command=mpopup.destroy, fg='#00ffBB', bg='gray20')
    B1.pack(side="bottom")
    x = (mpopup.winfo_screenwidth() - mpopup.winfo_reqwidth()) / 2
    y = (mpopup.winfo_screenheight() - mpopup.winfo_reqheight()) / 2
    mpopup.wm_geometry("+%d+%d" % (x, y))
    mpopup.mainloop()


def mymain():
    t=mGUI()
    t.metod()


    canvas = Canvas(t.root,width=50, height=900,highlightbackground='green4', bg = 'green4')
    canvas.place(relx=0.47, rely=0.5, anchor=CENTER)
    canvas.create_line(25, 0, 25, 900,fill="black",width=5)

    csanvas = Canvas(t.root,width=700, height=50,highlightbackground='green4', bg = 'green4')
    csanvas.place(relx=0.21, rely=0.41, anchor=CENTER)
    csanvas.create_line(0, 25, 700, 25,fill="black",width=5)

    # csanvas1 = Canvas(t.root,width=1700, height=50,highlightbackground='green4', bg = 'green4')
    # csanvas1.place(relx=0.9, rely=0.63, anchor=CENTER)
    # csanvas1.create_line(0, 25, 1700, 25,fill="black")

    canvas1 = Canvas(t.root,width=50, height=50,highlightbackground='green4', bg = 'green4')
    canvas1.place(relx=0.132, rely=0.09, anchor=CENTER)

    image1 = tkinter.PhotoImage(file = './ImPeople/p11.png')
    canvas1.create_image(0, 0,image = image1, anchor = NW)

    t.canvas2 = Canvas(t.root,width=50, height=50,highlightbackground='green4', bg = 'green4')
    t.canvas2.place(relx=0.22, rely=0.09, anchor=CENTER)

    t.image2 = tkinter.PhotoImage(file = './ImPeople/p222.png')
    t.canvas2.create_image(0, 0,image = t.image2, anchor = NW)

    t.canvas3 = Canvas(t.root,width=50, height=50,highlightbackground='green4', bg = 'green4')
    t.canvas3.place(relx=0.32, rely=0.09, anchor=CENTER)

    t.image3 = tkinter.PhotoImage(file = './ImPeople/p101010.png')
    t.canvas3.create_image(0, 0,image = t.image3, anchor = NW)

    t.canvas4 = Canvas(t.root,width=50, height=50,highlightbackground='green4', bg = 'green4')
    t.canvas4.place(relx=0.42, rely=0.13, anchor=CENTER)

    t.image4 = tkinter.PhotoImage(file = './ImPeople/p333.png')
    t.canvas4.create_image(0, 0,image = t.image4, anchor = NW)


    t.canvas5 = Canvas(t.root,width=50, height=50,highlightbackground='green4', bg = 'green4')
    t.canvas5.place(relx=0.42, rely=0.215, anchor=CENTER)

    t.image5 = tkinter.PhotoImage(file = './ImPeople/p444.png')
    t.canvas5.create_image(0, 0,image = t.image5, anchor = NW)

    t.canvas6 = Canvas(t.root,width=50, height=50,highlightbackground='green4', bg = 'green4')
    t.canvas6.place(relx=0.42, rely=0.3, anchor=CENTER)

    t.image6 = tkinter.PhotoImage(file = './ImPeople/p666.png')
    t.canvas6.create_image(0, 0,image = t.image6, anchor = NW)

    t.canvas7 = Canvas(t.root,width=50, height=50,highlightbackground='green4', bg = 'green4')
    t.canvas7.place(relx=0.32, rely=0.33, anchor=CENTER)

    t.image7 = tkinter.PhotoImage(file = './ImPeople/p777.png')
    t.canvas7.create_image(0, 0,image = t.image7, anchor = NW)


    t.canvas8 = Canvas(t.root,width=50, height=50,highlightbackground='green4', bg = 'green4')
    t.canvas8.place(relx=0.08, rely=0.3, anchor=CENTER)

    t.image8 = tkinter.PhotoImage(file = './ImPeople/p888.png')
    t.canvas8.create_image(0, 0,image = t.image8, anchor = NW)

    t.canvas9 = Canvas(t.root,width=50, height=50,highlightbackground='green4', bg = 'green4')
    t.canvas9.place(relx=0.08, rely=0.15, anchor=CENTER)

    t.image9 = tkinter.PhotoImage(file = './ImPeople/p555.png')
    t.canvas9.create_image(0, 0,image = t.image9, anchor = NW)

    t.canvas10 = Canvas(t.root,width=50, height=50,highlightbackground='green4', bg = 'green4')
    t.canvas10.place(relx=0.22, rely=0.34, anchor=CENTER)

    t.image10 = tkinter.PhotoImage(file = './ImPeople/p999.png')
    t.canvas10.create_image(0, 0,image = t.image10, anchor = NW)


    t.canvas = Canvas(t.root,width=700, height=550, highlightbackground='green4',bg = 'green4')
    t.canvas.place(relx=0.74, rely=0.37, anchor=CENTER)


    t.image = tkinter.PhotoImage(file = './mfon/table1.png')
    t.canvas.create_image(0, 0, image = t.image, anchor = NW)



    t.root["bg"] = "green4"
#    t.root.protocol('WM_DELETE_WINDOW', t.root.destroy())
    t.root.state("zoomed")
    t.root.resizable(False, False)
    t.my__init__(t.root, t.diler)

    t.root.mainloop()
