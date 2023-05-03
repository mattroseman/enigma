import unittest
from plugboard import Plugboard

class TestPlugboard(unittest.TestCase):
    def setUp(self):
        self.plugboard = Plugboard()

    def test_generate_swaps(self):
        swaps = self.plugboard.generate_swaps(10)

        self.assertLessEqual(len(swaps), 10)

        # test that no swaps contain the same number twice
        for swap in swaps:
            self.assertEqual(len(swap), 2)
            self.assertNotEqual(swap[0], swap[1])

        # check that no number is repeated in any of the swaps
        numbers = [number for swap in swaps for number in swap]
        self.assertEqual(len(set(numbers)), 2 * len(swaps))

    def test_generate_mapping(self):
        swaps = [(0, 1), (2, 3), (4, 5)]
        mapping = self.plugboard.generate_mapping(swaps)

        self.assertEqual(len(mapping), 36)
        self.assertEqual(mapping[0], 1)
        self.assertEqual(mapping[1], 0)
        self.assertEqual(mapping[2], 3)
        self.assertEqual(mapping[3], 2)
        self.assertEqual(mapping[4], 5)
        self.assertEqual(mapping[5], 4)
        for i in range(6, 36):
            self.assertEqual(mapping[i], i)

    def test_map(self):
        swaps = [(0, 1), (2, 3), (4, 5)]
        mapping = self.plugboard.generate_mapping(swaps)
        self.plugboard.mapping = mapping

        self.assertEqual(self.plugboard.map(0), 1)
        self.assertEqual(self.plugboard.map(1), 0)
        self.assertEqual(self.plugboard.map(2), 3)
        self.assertEqual(self.plugboard.map(3), 2)
        self.assertEqual(self.plugboard.map(4), 5)
        self.assertEqual(self.plugboard.map(5), 4)
        for i in range(6, 36):
            self.assertEqual(self.plugboard.map(i), i)

if __name__ == '__main__':
    unittest.main()