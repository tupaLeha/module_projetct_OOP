import random
from exceptions import *


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = 0

    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            return 0
        elif defense - attack == 1 or defense - attack == -2:
            return 1
        else:
            return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver(self.score, self.name)

    def attack(self, target):
        select_attack = int(input('Choose attack: '))
        fight_result = self.fight(select_attack, Enemy.select_attack())
        if fight_result == 0:
            print('Its a draw')
        elif fight_result == 1:
            print('You attacked successfully')
            target.decrease_lives()
        elif fight_result == -1:
            print('You missed')

    def defence(self):
        select_defence = int(input('Choose defence: '))
        defence_result = self.fight(Enemy.select_attack(), select_defence)
        if defence_result == 0:
            print('Its a draw')
        elif defence_result == 1:
            print('Enemy attacked successfully')
            self.decrease_lives()
        elif defence_result == -1:
            print('Enemy missed')
