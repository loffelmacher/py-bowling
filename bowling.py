import os

class Game(object):
    """This is the main, and only, class in the package."""
    _score = 0
    _rolls = [0] * 21
    _currentRoll = 0

    def __init__(self):
        super(Game, self).__init__()

    def roll(self, pins):
        # print "Entering roll()"
        self._rolls[self._currentRoll] = pins
        self._currentRoll += 1

    def score(self):
        # print "Entering score()"
        score = 0
        ii = 0
        for frame in range(0, 10):
            if self._rolls[ii] + self._rolls[ii+1] == 10:
                score += 10 + self._rolls[ii+2]
            else:
                score += self._rolls[ii] + self._rolls[ii+1]
            ii += 2
        return score

