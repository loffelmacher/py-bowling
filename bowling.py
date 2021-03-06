import os

class Game(object):
    """This is the main, and only, class in the package."""

    def __init__(self):
        super(Game, self).__init__()
        self._score = 0
        self._currentRoll = 0
        self._rolls = [0] * 21

    def roll(self, pins):
        self._rolls[self._currentRoll] = pins
        self._currentRoll += 1

    def score(self):
        score = 0
        frameIndex = 0
        for frame in range(0, 10):
            if self.isStrike(frameIndex):
                score += 10 + self._rolls[frameIndex+1] + self._rolls[frameIndex+2]
                frameIndex += 1
            elif self.isSpare(frameIndex):
                score += 10 + self._rolls[frameIndex+2]
                frameIndex += 2
            else:
                score += self._rolls[frameIndex] + self._rolls[frameIndex+1]
                frameIndex += 2
        return score

    def isSpare(self, frameIndex):
        return self._rolls[frameIndex] + self._rolls[frameIndex+1] == 10

    def isStrike(self, frameIndex):
        return self._rolls[frameIndex] == 10