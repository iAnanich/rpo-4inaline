""" This module contains algorithms. """


# helpers
def greatest_common_divisor(a, b):
    """ Euclid's algorithm """
    while b:
        a, b = b, a % b
    return a


class Unique:
    all = []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def register(self):
        for item in self.all:
            if self == item:
                del self
                break
        else:
            self.all.append(self)


class Dot(Unique):
    """ Represents dots on the xOy (e.g. checkers on the field). """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hands = []
        self.register()


class Hand(Unique):
    """ Represents connections between Dots (e.g. lines between checkers). """

    def __init__(self, dot1, dot2):
        self.x, self.y = self.calculate_vector(dot1, dot2)
        self.register()

    @staticmethod
    def calculate_vector(dot1: Dot, dot2: Dot):
        x = abs(dot1.x - dot2.x)
        y = abs(dot1.y - dot2.y)
        gcd = greatest_common_divisor(x, y)
        return x/gcd, y/gcd


class Chain(Unique):
    """ Represents groups of Dots connected with the same Hands (e.g. checkers on one line). """

    def __init__(self, hand, dot1, dot2):
        self.hand = hand
        self.dots = [dot1, dot2]
        self.register()

    def _add_dot(self, dot):
        if not dot in self.dots:
            self.dots.append(dot)

    def add(self, dot):
        self._add_dot(dot)
        return len(self.dots)


# steps
def init_dots(array):
    for x, y in array:
        Dot(x, y)


# main function
def calculate(x_long, y_long, total_dots, goal, input_array):
    """
    :param input_array: array with `y_long` arrays each one with `x_long` boolean integer (e.g. 0, 1)
    :param x_long: long of side A (x axis)
    :param y_long: long of side B (y axis)
    :param total_dots: number of checkers
    :param goal: minimum of checkers on the one line
    :return: points
    """
    init_dots(input_array)

    points = 0
    return points
