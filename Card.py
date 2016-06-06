# -*- coding:utf-8 -*-
__author__ = 'Павел'
import random
class Card:
 def __myinit__(self, card_suit,card_rating):
     """
    Конструктор, создающий карту с заданными значением и мастью
     :rtype: object
     """
     self.card_suit =card_suit
     self.card_rating= card_rating
 def __init__(self):
    """
 Конструктор по умолчанию
     :rtype: object
    """
    random_suit=random.randint(1,4)#1-буби 2-черви 3-пики 4-крести
    random_rating=random.randint(2,14) #11- валет 12-дама 13- король 14-туз
    self.card_suit =random_suit
    self.card_rating= random_rating



