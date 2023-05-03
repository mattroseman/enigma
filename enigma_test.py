import unittest
from unittest.mock import MagicMock
from enigma import Enigma

class TestEnigma(unittest.TestCase):
    def setUp(self):
        self.enigma = Enigma()

        self.enigma.rotors = [MagicMock(), MagicMock(), MagicMock()]
        self.enigma.reflector = MagicMock()
        for rotor in self.enigma.rotors:
            rotor.map.return_value = 0
        self.enigma.reflector.map.return_value = 0

    def test_init(self):
        self.assertEqual(len(self.enigma.rotors), 3)
        self.assertIsNotNone(self.enigma.reflector)

    def test_first_rotor_rotates_every_turnover(self):
        self.enigma.turnover()
        self.assertEqual(self.enigma.rotors[0].rotate.call_count, 1)
        self.enigma.turnover()
        self.assertEqual(self.enigma.rotors[0].rotate.call_count, 2)
        self.enigma.turnover()
        self.assertEqual(self.enigma.rotors[0].rotate.call_count, 3)

    def test_second_rotor_rotates_when_first_rotor_returns_to_original_position(self):
        self.enigma.rotors[0].rotate.side_effect = lambda: setattr(self.enigma.rotors[0], 'rotational_orientation', 0)
        self.enigma.turnover()
        self.assertEqual(self.enigma.rotors[1].rotate.call_count, 1)

    def test_third_rotor_rotates_when_second_rotor_returns_to_original_position(self):
        self.enigma.rotors[0].rotate.side_effect = lambda: setattr(self.enigma.rotors[0], 'rotational_orientation', 0)
        self.enigma.rotors[1].rotate.side_effect = lambda: setattr(self.enigma.rotors[1], 'rotational_orientation', 0)
        self.enigma.turnover()
        self.assertEqual(self.enigma.rotors[2].rotate.call_count, 1)

    def test_map_triggers_turnover(self):
        self.enigma.map('a')
        self.assertEqual(self.enigma.rotors[0].rotate.call_count, 1)
        self.enigma.map('a')
        self.assertEqual(self.enigma.rotors[0].rotate.call_count, 2)

    def test_map_does_nothing_to_non_alphanumeric_characters(self):
        self.assertEqual(self.enigma.map('!'), '!')
        self.assertEqual(self.enigma.map(' '), ' ')
        self.assertEqual(self.enigma.map('😀'), '😀')

    def test_map_calls_rotor_map_twice_and_reflector_map_once(self):
        self.enigma.map('a')
        for rotor in self.enigma.rotors:
            self.assertEqual(rotor.map.call_count, 2)
        self.assertEqual(self.enigma.reflector.map.call_count, 1)
    

if __name__ == '__main__':
    unittest.main()