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
        return sum(self._rolls)
