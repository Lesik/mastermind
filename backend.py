#! /usr/bin/env python3
import random

__author__ = 'lesik'


class Backend:

    code = []
    global code_length
    shapes = ['Pik', 'Herz', 'Caro', 'Ventilator']
    colours = ['blue', 'green', 'rot', 'yellow']

    def __init__(self, code_length = 4):
        self.code_length = code_length

    def get_shapes(self):
        return self.shapes

    def get_colours(self):
        return self.colours

    def get_code_length(self):
        return self.code_length

    def save_code(self):
        self.code = self.generate_code()

    def generate_code(self):
        shapes = list(range(0, len(self.shapes)))
        colours = list(range(0, len(self.colours)))
        random.shuffle(shapes)
        random.shuffle(colours)

        code = []
        for i in range(0, self.code_length):
            code.append([shapes[i], colours[i]])
        return code

    def get_code(self):
        return self.code

    def check_code(self, code_input):
        print('eingegeben ', code_input)
        a = 0
        b = 0
        c = 0

        for i in range(0, self.code_length):
            if (code_input[i][0] == self.code[i][0]):
                # korrekte Form aber falsche Farbe
                a += 1
            elif (code_input[i][1] == self.code[i][1]):
                # korrekte Farbe aber falsche Form
                b += 1
            elif (code_input[i] == self.code[i]):
                # alles korrekt
                c += 1

        return [a, b, c]