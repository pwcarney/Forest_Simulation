from lumberjack import Lumberjack
from utils import *

import random


class Bear:

    def __init__(self, x, y, forest_size):

        self.location = (x, y)
        self.forest_size = forest_size
        self.maws = 0

        self.new_position_tries = 0

    def pass_month(self, lumberjacks, bears):

        # Travel 5 times per month
        for i in range(0, 5):

            # Check for lumberjack at current location
            for index, lumberjack in enumerate(lumberjacks):
                if lumberjack.location == self.location:

                    self.maws += 1
                    del lumberjacks[index]

                    # If that put us to 0 lumberjacks, spawn a new one at a random location.
                    if len(lumberjacks) == 0:
                        x_pos = random.choice(range(self.forest_size))
                        y_pos = random.choice(range(self.forest_size))
                        lumberjacks.append(Lumberjack(x_pos, y_pos, self.forest_size))

                    return lumberjacks

            # Otherwise, move in a random direction
            while True:
                new_position = (random.choice(range(self.location[0] - 1, self.location[0] + 2)),
                                random.choice(range(self.location[1] - 1, self.location[1] + 2)))

                if self.location == new_position:
                    continue

                # Account for overflow or underflow on forest grid
                new_position = check_overflow(new_position, self.forest_size)

                # Make sure there are no bears at new position
                bad_position = False
                for bear in bears:
                    if bear.location == new_position:
                        bad_position = True
                        self.new_position_tries += 1

                # If we have already tried to find a new location twice, stop for the month
                if bad_position and self.new_position_tries > 2:
                    self.new_position_tries = 0
                    return lumberjacks
                elif bad_position:
                    continue
                else:
                    self.location = new_position
                    break

        return lumberjacks
