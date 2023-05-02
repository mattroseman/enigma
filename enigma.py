# A Rotor class for the Enigma machine.
# A rotor contains some mapping of each alphanumeric character to another.
# It can also map to itself, but there must be a one-to-one relationship between characters.

import string
import random

class Rotor:
    def __init__(self):
        self._original_mapping = Rotor._random_mapping()
        self._mapping = self._original_mapping.copy()
        self._reverse_mapping = {v: k for k, v in self._mapping.items()}
        self._rotation = 0

    @staticmethod
    def _random_mapping():
        chars = list(string.ascii_uppercase)
        random.shuffle(chars)
        return {k: v for k, v in zip(string.ascii_uppercase, chars)}

    def map(self, char):
        rotated_mapping = {k: self._mapping[k-self._rotation] for k in self._mapping.keys()}
        return rotated_mapping[char]

    def reverse_map(self, char):
        rotated_reverse_mapping = {k: self.reverse_mapping[k-self._rotation] for k in self.reverse_mapping.keys()}
        return self.reverse_mapping[char]

    def rotate(self):
        self._rotation = (self._rotation + 1) % len(self._original_mapping)
        self._mapping = {k: self._original_mapping[k-self._rotation] for k in self._original_mapping.keys()}
        self._reverse_mapping = {v: k for k, v in self._mapping.items()}

    def __str__(self):
        return str(self._mapping)

if __name__ == '__main__':
    rotor = Rotor()
    print(rotor)
    rotor.rotate()
    print(rotor)