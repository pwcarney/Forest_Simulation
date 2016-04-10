import random

from utils import *


class Bear:
    def __init__(self, x, y, forest_size):
        self.location = (x, y)
        self.forest_size = forest_size
        self.maws = 0

    def pass_month(self, lumberjacks):

        # Travel 5 times per month
        for i in range(0, 5):

            # Check for tree at current location
            for index, lumberjack in enumerate(lumberjacks):
                if lumberjack.location == self.location:

                    self.maws += 1

                    # We are done for the month if we chopped down a tree
                    del lumberjacks[index]
                    return lumberjacks

            # Otherwise, move in a random direction
            self.location = (random.choice((self.location[0] - 1, self.location[0] + 2)),
                             random.choice((self.location[1] - 1, self.location[1] + 2)))

            # Account for overflow or underflow on forest grid
            self.location = check_overflow(self.location, self.forest_size)

        return lumberjacks