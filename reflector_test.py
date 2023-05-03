import unittest
from reflector import Reflector

class TestReflector(unittest.TestCase):
    def setUp(self):
        self.reflector = Reflector()

    def test_init(self):
        self.assertEqual(self.reflector.num_inputs, 36)
        self.assertEqual(len(self.reflector.mapping), 36)

    def test_generate_derangement_mapping(self):
        self.reflector.generate_derangement_mapping()
        self.assertEqual(len(self.reflector.mapping), 36)
        self.assertEqual(len(set(self.reflector.mapping.values())), 36)

    def test_map(self):
        self.assertEqual(self.reflector.map(0), self.reflector.mapping[0])
        self.assertEqual(self.reflector.map(1), self.reflector.mapping[1])
        self.assertEqual(self.reflector.map(33), self.reflector.mapping[33])
        self.assertEqual(self.reflector.map(35), self.reflector.mapping[35])

    def test_derangement_mapping_has_no_reflective_mappings(self):
        for k, v in self.reflector.mapping.items():
            self.assertNotEqual(k, v)

    def test_str(self):
        self.assertEqual(str(self.reflector), f'mapping: {self.reflector.mapping}')

if __name__ == '__main__':
    unittest.main()