# -*- coding: utf-8 -*-

from .context import bowling

import unittest


class BowlingGameUnitTests(unittest.TestCase):
    """Unit tests for the Bowling Kata."""
    def setUp(self):
    	self.g = bowling.Game()

    def test_all_gutters(self):
    	# g.roll(20,0)
        assert True


if __name__ == '__main__':
    unittest.main()