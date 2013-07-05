import random
import unittest

from Game import *
from NPC import *
from Player import *
from Stats import *
from Tile import *
from Wall import *
from functions import *


class TestEVERYTHING(unittest.TestCase):

    def setUp(self):
        self.map_list = ['tm (1).bmp', 'tm (2).bmp',
                         'tm (3).bmp', 'tm (4).bmp']
        self.game = None

    def test_map_all_white(self):
        # You should not generate random maps like that
        self.game = Game('/tests/' + self.map_list[1])
        self.assertRaises(NO_PLAYER, self.game.main())

    def test_map_all_black(self):
        self.game = Game('/tests/' + self.map_list[2])
        self.assertRaises(NO_PLAYER, self.game.main())

    def test_map_all_grass(self):
        self.game = Game('/tests/' + self.map_list[3])
        self.assertEqual(generate_map(self.game), -1)

    def test_map_non_existant(self):
        self.map = '/not_really_there/007.bmp'
        self.game = Game(self.map)
        self.AssertionError("Couldn't open " + MEDIA_PATH + self.map)

if __name__ == '__main__':
    unittest.main()
