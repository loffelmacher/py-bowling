# -*- coding: utf-8 -*-

from .context import bowling

import unittest


class BowlingGameUnitTests(unittest.TestCase):
    """Unit tests for the Bowling Kata."""
    def setUp(self):
    	self.g = bowling.Game()

    def test_all_gutters(self):
    	for xx in range(0,20):
    		self.g.roll(0)
        assert self.g.score() == 0


if __name__ == '__main__':
    unittest.main()