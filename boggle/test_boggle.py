import unittest
import boggle
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):
    """
    Our test suite for boggle solver
    """
    def test_can_create_an_empty_grid(self):
        """
        Test to see if we canc reat an empty grid
        """
        grid = boggle.make_grid(0, 0) # Pass two arguments height and widt, or row and column. The simplest grid is one with no rows and columns
        self.assertEqual(len(grid), 0)
    
    def test_grid_size_is_width_by_height(self):
        """
        Test is to ensure that the total soze of the grid is equal to width * height
        """
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
    
    def test_grid_coordinates(self):
        """
        Test to ensure that all of the coordinates inside of the grid can be accessed
        """
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)

    def test_grid_is_filled_with_letters(self):
        """
        Ensure that each of the coordinates on the grid contains letters
        """
        grid = boggle.make_grid(2, 3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
    
    def test_neighbours_of_position(self):
        """
        Ensure that a position has 8 neighbors
        """
        coords = (1, 2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)

    def test_all_grid_neighbours(self):
        """
        Ensure that all of the grid positions have neighbours
        """
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.all_grid_neighbours(grid)       # This is a dictionary where the key is a position
        self.assertEqual(len(neighbours), len(grid))        # just like with the grid itself but the value is a list of neighboring positions. This next line can assert the correct length of the neighbors dictionary
        for pos in grid:
            others = list(grid) # create a new list from the dictionary's keys
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))

    def test_converting_a_path_to_a_word(self):
        """
        Ensure that paths can be converted to words
        """
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])             # Our test checks that the path to word function returns the same strings we manually construct in the test.
        twoLetterWord = boggle.path_to_word(grid, [(0 ,0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])
    
    def test_search_grid_for_words(self):
        """
        Ensure that certain pattersn can be found in path_to_word
        """
        grid = {(0, 0): "A", (0, 1): "B", (1, 0): "C", (1, 1): "D"}     # Define a mock grid to control the letters
        twoLetterWord = "AB"
        threeLetterWord = "ABC"                                         # We also define a dictionary of three words
        notThereWord = "EEE"
        dictionary = [twoLetterWord, threeLetterWord, notThereWord]

        foundWords = boggle.search(grid, dictionary)

        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)

    def test_get_dictionary(self):
        """
        Test that the 'get_dictionary' function returns a dictionary that has a length
        greater than 0
        """
        dictionary = boggle.get_dictionary('words.txt')
        self.assertGreater(len(dictionary), 0)

