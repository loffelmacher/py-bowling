# -*- coding: utf-8 -*-

from .context import bowling

import unittest


class BowlingGameUnitTests(unittest.TestCase):
    """Unit tests for the Bowling Kata."""
    def setUp(self):
    	self.g = bowling.Game()

    def test_all_gutters(self):
    	self.rollMany(20, 0)
        assert self.g.score() == 0

    def test_all_ones(self):
    	self.rollMany(20, 1)
    	assert self.g.score() == 20

    def test_one_spare(self):
    	self.g.roll(5)
    	self.g.roll(5)
    	self.g.roll(3)
    	self.rollMany(17, 0)
    	assert self.g.score() == 16

    def test_one_strike(self):
    	self.rollStrike()
    	self.g.roll(3)
    	self.g.roll(4)
    	self.rollMany(16,0)
    	assert self.g.score() == 24

    def test_perfect_game(self):
    	self.rollMany(12, 10)
    	assert self.g.score() == 300

    def test_arbitrary_game(self):
    	self.rollSpare()
    	self.rollStrike()
    	self.g.roll(1)
    	self.g.roll(2)
    	assert self.g.score() == 36

    def test_another_arbitrary_game(self):
    	self.rollSpare()
    	self.rollStrike()
    	self.g.roll(1)
        self.g.roll(1)
        self.rollStrike()
        self.rollSpare()
        self.g.roll(1)
        self.g.roll(1)
        assert self.g.score() == 67

    def rollMany(self, nn, pins):
    	for xx in range(0, nn):
    		self.g.roll(pins)

    def rollSpare(self):
    	self.g.roll(5)
    	self.g.roll(5)

    def rollStrike(self):
    	self.g.roll(10)


if __name__ == '__main__':
    unittest.main()