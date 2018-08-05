import os

class Game(object):
    """This is the main, and only, class in the package."""
    _score = 0
    _rolls = [None] * 21
    _rollIndex = 0

    def __init__(self):
        super(Game, self).__init__()

    def roll(self, pins):
        # print "Entering roll()"
        # self.rolls[self.rollIndex] = pins
        self._score = self._score + pins

    def score(self):
        # print "Entering score()"
        return self._score
