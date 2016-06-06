# -*- coding:utf-8 -*-
__author__ = 'Павел'
from Card import Card


class Player:
    def __myinit__(self, name):

        """
        Конструктор задающий игрока с именем
        :rtype: object
        """
        self.name = name
        self.card1 = Card()
        while (True):
            self.card2 = Card()
            if not (self.card1.card_suit == self.card2.card_suit and self.card1.card_rating == self.card2.card_rating):
                break
        self.active=True

    def __myinitPlayer__(self, card1s, card1r, card2s, card2r):
        """
        Метод,задающий карты игроку
        :param card1s: Масть 1 карты
        :type card1s:
        :param card1r: Значение 1 карты
        :type card1r:
        :param card2s: Масть 2 карты
        :type card2s:2
        :param card2r: Значение 1 карты
        :type card2r:
        """
        self.card1 = Card()
        self.card1.__myinit__(card1s, card1r)
        self.card2 = Card()
        self.card2.__myinit__(card2s, card2r)
        self.active=True

    def __init__(self):
        """
        Конструктор по умолчанию
        :rtype: object
        """
        self.name = "Bot"
        self.card1 = Card()
        while (True):
            self.card2 = Card()
            if not (self.card1.card_suit == self.card2.card_suit and self.card1.card_rating == self.card2.card_rating):
                break
        self.active=True

