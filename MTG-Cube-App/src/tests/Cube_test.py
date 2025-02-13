import unittest
from entities.cube import Cube
from unittest.mock import patch
from io import StringIO

class TestCube(unittest.TestCase):
    def setUp(self) -> None:
        self.cube = Cube("TestCube")

    def test_cube_named_right(self):
        self.assertEqual(str(self.cube), "TestCube")

    def test_empty_cube_is_empty(self):
        self.assertEqual(
            [self.cube.collection, self.cube.card_names], [[], []])

    def test_adding_cards_works(self):
        self.cube.add_card("forest")
        self.assertEqual([self.cube.card_names, len(
            self.cube.collection)], [["Forest"], 1])

    def test_adding_duplicate_cards_doesnt_work(self):
        self.cube.add_card("forest")
        self.cube.add_card("forest")
        self.assertEqual([self.cube.card_names, len(
            self.cube.collection)], [["Forest"], 1])

    def test_removing_card_successfully(self):
        self.cube.add_card("forest")
        self.cube.remove_card("Forest")
        self.assertEqual([self.cube.card_names, self.cube.collection], [[],[]])

    @patch('sys.stdout', new_callable= StringIO)
    def test_removing_card_fail(self, stdout):
        self.cube.remove_card("Forest")
        self.assertEqual(stdout.getvalue(), "Forest nimellä ei löytynyt korttia Cubesta\n")