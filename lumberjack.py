from utils import *

import random


class Lumberjack:

    def __init__(self, x, y, forest_size):
        self.location = (x, y)
        self.forest_size = forest_size
        self.lumber = 0

    def pass_month(self, trees):

        # Travel 3 times per month
        for i in range(0, 3):

            # Check for tree at current location
            for index, tree in enumerate(trees):
                if tree.location == self.location and tree.months_old >= 12:

                    # Old trees are worth more lumber
                    if tree.months_old >= 120:
                        self.lumber += 2
                    else:
                        self.lumber += 1

                    # We are done for the month if we chopped down a tree
                    del trees[index]
                    return trees

            # Otherwise, move in a random direction
            self.location = (random.choice((self.location[0] - 1, self.location[0] + 2)),
                             random.choice((self.location[1] - 1, self.location[1] + 2)))

            # Account for overflow or underflow on forest grid
            self.location = check_overflow(self.location, self.forest_size)

        return