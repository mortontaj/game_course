class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            level - self._level

        else:
            ("That is not a level")
            self._level = 1

    def _get_score(self):
        score = self._level * 1000 - 1000
        self._score = score
        return self._score

    def _set_score(self):
        score = self._level * 1000 - 1000
        self._score = score

    score = property(_get_score, _set_score)
    level = property(_get_level, _set_level)
    lives = property(_get_lives, _set_lives)

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)
 