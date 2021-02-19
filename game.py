from models import Player, Enemy
from settings import current_lives
from exceptions import *


def play():
    player = Player(input('Enter ur name: '))
    player.lives = current_lives[input('Choose current level: ')]
    level = 1
    enemy = Enemy(level)
    while True:
        try:
            player.attack(enemy)
            player.defence()
        except EnemyDown:
            print('Enemy down')
            level += 1
            player.score += 5
            enemy = Enemy(level)


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye')

