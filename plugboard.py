import random

class Plugboard:
    def __init__(self, num_inputs=36):
        self.num_inputs = num_inputs
        swaps = self.generate_swaps(min(10, num_inputs // 2))
        self.mapping = self.generate_mapping(swaps)

    def generate_swaps(self, max_swaps=10):
        """
        Generate a random number of swaps between 0 and max_swaps.
        Swaps are pairs of different numbers that represent a 2-way mapping.
        @param max_swaps: the maximum number of swaps to generate.
        @return: a list of tuples, each containing 2 unique numbers, representing the swaps. No number will be repeated in multiple swaps.
        """
        num_swaps = random.randint(0, 10)

        # get all the numbers which will be swapped
        swap_numbers = random.sample(range(self.num_inputs), k=num_swaps * 2)
        random.shuffle(swap_numbers)
        # create a set of tuples where index 0 pairs with index 1, 2 with 3, etc.
        swaps = set(zip(swap_numbers[::2], swap_numbers[1::2]))

        return swaps

    def generate_mapping(self, swaps):
        """
        Generate the mappings for inputs given the set of swaps to apply. A swap indicates that the first number maps to the second, and the second maps to the first.
        Any number not found in a swap maps to itself.
        @param swaps: a list of tuples, each containing 2 unique numbers
        @return: a dictionary mapping each input number
        """
        mapping = {i: i for i in range(self.num_inputs)}
        for swap in swaps:
            mapping[swap[0]] = swap[1]
            mapping[swap[1]] = swap[0]
        return mapping

    def map(self, input):
        return self.mapping[input]

    def __str__(self):
        return f'mapping: {self.mapping}'