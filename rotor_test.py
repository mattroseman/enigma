import unittest
from rotor import Rotor

class TestRotor(unittest.TestCase):
    def setUp(self):
        self.rotor = Rotor()

    def test_init(self):
        self.assertEqual(self.rotor.num_inputs, 36)
        self.assertEqual(self.rotor.rotational_orientation, 0)
        self.assertEqual(len(self.rotor.mapping), 36)

    def test_generate_mapping(self):
        self.rotor.generate_mapping()
        self.assertEqual(len(self.rotor.mapping), 36)
        self.assertEqual(len(set(self.rotor.mapping.values())), 36)

    def test_rotate(self):
        self.rotor.rotate()
        self.assertEqual(self.rotor.rotational_orientation, 1)
        self.rotor.rotate()
        self.assertEqual(self.rotor.rotational_orientation, 2)
        self.rotor.rotational_orientation = 35
        self.rotor.rotate()
        self.assertEqual(self.rotor.rotational_orientation, 0)

    def test_map(self):
        self.assertEqual(self.rotor.map(0), self.rotor.mapping[0])
        self.assertEqual(self.rotor.map(1), self.rotor.mapping[1])
        self.assertEqual(self.rotor.map(33), self.rotor.mapping[33])
        self.assertEqual(self.rotor.map(35), self.rotor.mapping[35])

    def test_map_with_rotation(self):
        self.rotor.rotational_orientation = 2
        self.assertEqual(self.rotor.map(0), self.rotor.mapping[2])
        self.assertEqual(self.rotor.map(1), self.rotor.mapping[3])
        self.assertEqual(self.rotor.map(33), self.rotor.mapping[35])
        self.assertEqual(self.rotor.map(35), self.rotor.mapping[1])


    def test_str(self):
        self.assertEqual(str(self.rotor), f'rotational_orientation: {self.rotor.rotational_orientation}\nmapping: {self.rotor.mapping}')

if __name__ == '__main__':
    unittest.main()