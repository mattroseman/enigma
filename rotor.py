import random

# Rotor is a class representing a rotor in an Enigma machine.
# A rotor has a mapping from input to output, and has some rotational orientation.
# The input and output space is the list of alphabetical characters.
# The rotational orientation is just a numbber which increments by 1 for every rotation.
# The mapping is a dictionary of mappings from some index to another. An index can map to itself, but the mappings must be one-to-one.
# Given some alphabetical character, represent it as an integer.
# For example, a becomes 0, b becomes 1, ..., z becomes 25, 0 becomes 26, 1 becomes 27, ..., 25 becomes 51.
# The Rotor takes some input character, converts it to it's integer counterpart, applies the rotational orientation, and applies the mapping to this resulting integer.
# The final number is the ouput.


class Rotor:
    def __init__(self, num_inputs=36):
        self.num_inputs = num_inputs
        self.rotational_orientation = 0
        self.mapping = self.generate_mapping()

    def generate_mapping(self):
        mapping = {}
        numbers = list(range(self.num_inputs))
        random.shuffle(numbers)
        for i in range(self.num_inputs):
            mapping[i] = numbers[i]
        return mapping

    def rotate(self):
        self.rotational_orientation += 1
        self.rotational_orientation %= 26

    def map(self, input):
        return self.mapping[(input + self.rotational_orientation) % 26]

    def __str__(self):
        return f'rotational_orientation: {self.rotational_orientation}\nmapping: {self.mapping}'