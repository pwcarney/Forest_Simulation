from utils import *

import random


class Lumberjack:

    def __init__(self, x, y, forest_size):

        self.location = (x, y)
        self.forest_size = forest_size
        self.lumber = 0

        self.new_position_tries = 0

    def pass_month(self, trees, lumberjacks):

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
            while True:
                new_position = (random.choice(range(self.location[0] - 1, self.location[0] + 2)),
                                random.choice(range(self.location[1] - 1, self.location[1] + 2)))

                if self.location == new_position:
                    continue

                # Account for overflow or underflow on forest grid
                new_position = check_overflow(new_position, self.forest_size)

                # Make sure there are no lumberjacks at new position
                bad_position = False
                for lumberjack in lumberjacks:
                    if lumberjack.location == new_position:
                        bad_position = True
                        self.new_position_tries += 1

                # If we have already tried to find a new location twice, stop for the month
                if bad_position and self.new_position_tries > 2:
                    self.new_position_tries = 0
                    return trees
                elif bad_position:
                    continue
                else:
                    self.new_position_tries = 0
                    self.location = new_position
                    break

        return trees
