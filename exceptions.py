from settings import Score


class GameOver(Exception):
    def __init__(self, score, name):
        f = open('scores.txt', 'a')
        f.write(f'{name}:{score}.\n')
        f.close()


class EnemyDown(Exception):
    pass
