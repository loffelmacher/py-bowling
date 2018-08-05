import os

class Game(object):
    """This is the main, and only, class in the package."""
    def __init__(self):
        super(Game, self).__init__()
        self.rolls = [None] * 21
        self.rollIndex = 0

    def roll(self, pins):
        print "Entering roll()"
        self.rolls[self.rollIndex] = pins

    def score(self):
        print "Entering score()"
        return 0
