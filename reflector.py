import random

# Reflector class represents a class in an Enigma machine.
# A reflector has a mapping from some input to an ouput. Unlike a rotor, it has no rotational orientation.
# A reflector cannot map an input to itself, and also abides by the one-to-one mapping constraint.

class Reflector:
    def __init__(self, num_inputs=36):
        self.num_inputs = num_inputs
        self.mapping = self.generate_derangement_mapping()

    # generate_derangement_mapping is a helper method which generates a mapping which is a derangement, i.e. no number maps to itself.
    # The keys and values are numbers in the range [0, num_inputs).
    # The method is to generate the random mapping, check if any keys and values are the same number, and if so, regenerate the whole mapping.
    def generate_derangement_mapping(self): 
        mapping = {}
        numbers = list(range(self.num_inputs))
        random.shuffle(numbers)
        for i in range(self.num_inputs):
            mapping[i] = numbers[i]
        for k, v in mapping.items():
            if k == v:
                return self.generate_derangement_mapping()
        return mapping

    def map(self, input):
        return self.mapping[input]

    def __str__(self):
        return f'mapping: {self.mapping}'