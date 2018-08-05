# -*- coding: utf-8 -*-

from .context import bowling

import unittest


class BowlingGameUnitTests(unittest.TestCase):
    """Unit tests for the Bowling Kata."""
    def setUp(self):
    	self.g = bowling.Game()

    def test_all_gutters(self):
    	self.rollMany(20, 0)
    	# print 'Score is: ',  self.g.score()
        assert self.g.score() == 0

    def test_all_ones(self):
    	self.rollMany(20, 1)
    	# print 'Score is: ',  self.g.score()
    	assert self.g.score() == 20

    def test_one_spare(self):
    	# self.rollMany(2, 5)
    	self.g.roll(5)
    	self.g.roll(5)
    	self.g.roll(3)
    	self.rollMany(17, 0)
    	# print 'Score is: ',  self.g.score()
    	assert self.g.score() == 16

    def rollMany(self, nn, pins):
    	for xx in range(0, nn):
    		self.g.roll(pins)

    def rollSpare(self):
    	self.g.roll(5)
    	self.g.roll(5)

if __name__ == '__main__':
    unittest.main()