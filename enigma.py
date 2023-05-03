import random

from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard


CHARACTER_TO_INTEGER = {chr(i + ord('a')): i for i in range(26)}
CHARACTER_TO_INTEGER.update({chr(i + ord('0')): i + 26 for i in range(10)})
INTEGER_TO_CHARACTER = {v: k for k, v in CHARACTER_TO_INTEGER.items()}

class Enigma:
    """
    An Enigma class is a collection of classes which act as ciphers in sequence.
    There is a plugboard which bookends all the ciphers.
    it will swap some input values with others, and then swap those same output values with the input after all the other ciphers.
    There are 3 rotors which run in sequence, each passing its output to the next
    This means a character is fed into the first rotor, that rotor's output character is fed into the second rotor as it's input, and so on.
    The output of the third rotor is passed to the reflector.
    The reflector maps the input to some output, similar to the rotors, and then feeds that output back into the rotors in reverse.
    So the input goes from rotor 1 to rotor 2 to rotor 3 to reflector to rotor 3 to rotor 2 to rotor 1.
    After the first output is generated, the first rotor is rotated by 1.
    Once the first rotor has rotated a multiple of 26 times, i.e. returned to its original rotational orientation, the second rotor is rotated by 1.
    Once the second rotor has rotated a multiple of 26 times, the third rotor is rotated by 1.
    """
    def __init__(self):
        self.rotors = [Rotor(), Rotor(), Rotor()]
        self.reflector = Reflector()
        self.plugboard = Plugboard()

    # turnover is the method which rotates the rotors.
    # It rotates the first rotor by 1. If the first rotor has returned to it's original rotational orientation, it rotates the second rotor by 1.
    # If the second rotor has returned to it's original rotational orientation, it rotates the third rotor by 1.
    def turnover(self):
        """
        turnover which rotates the rotors.
        The first rotor every time, the seoncd when the first makes a full revolution, and the third when the second makes a full revolution.
        """
        self.rotors[0].rotate()
        if self.rotors[0].rotational_orientation == 0:
            self.rotors[1].rotate()
            if self.rotors[1].rotational_orientation == 0:
                self.rotors[2].rotate()

    def map(self, character):
        # if character isn't an alphanumeric one, return it as is
        if character.lower() not in CHARACTER_TO_INTEGER:
            return character

        output = CHARACTER_TO_INTEGER[character.lower()]

        output = self.plugboard.map(output)

        for rotor in self.rotors:
            output = rotor.map(output)
        output = self.reflector.map(output)
        for rotor in reversed(self.rotors):
            output = rotor.map(output)

        self.turnover()

        output = self.plugboard.map(output)

        return INTEGER_TO_CHARACTER[output]

    def encrypt(self, plaintext):
        ciphertext = ''
        for character in plaintext:
            ciphertext += self.map(character)
        return ciphertext

    def __str__(self):
        return f'rotors: {self.rotors}'

if __name__ == '__main__':
    enigma = Enigma()
    print(enigma.encrypt("Hello World!"))