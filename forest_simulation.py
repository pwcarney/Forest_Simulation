from tree import Tree
from bear import Bear
from lumberjack import Lumberjack

import random
import time
from math import floor


class ForestSimulation:

    def __init__(self, forest_size):

        self.forest_size = forest_size

        self.forest = []
        self.trees = []
        self.lumberjacks = []
        self.bears = []

        self.month_counter = 0

        for row in range(forest_size):
            for col in range(forest_size):

                # Roll for tree
                if random.randint(1, 100) < 50:
                    self.trees.append(Tree(row, col, self.forest_size, 12))

                # Roll for lumberjack
                if random.randint(1, 100) < 10:
                    self.lumberjacks.append(Lumberjack(row, col, self.forest_size))

                # Roll for bears
                if random.randint(1, 100) < 2:
                    self.bears.append(Bear(row, col, self.forest_size))

        print("In a {0}x{1} forest:".format(self.forest_size, self.forest_size))
        print("Starting with {0} trees.".format(len(self.trees)))
        print("Starting with {0} lumberjacks.".format(len(self.lumberjacks)))
        print("Starting with {0} bears.".format(len(self.bears)))

    def pass_month(self):

        self.month_counter += 1
        print("Month {0}:".format(self.month_counter))

        pre_grow_tree_len = len(self.trees)
        [tree.pass_month(self.trees) for tree in self.trees]
        post_grow_tree_len = len(self.trees)
        print("{0} new saplings".format(post_grow_tree_len-pre_grow_tree_len))

        pre_lumber_tree_len = len(self.trees)
        for lumberjack in self.lumberjacks:
            self.trees = lumberjack.pass_month(self.trees)
        post_lumber_tree_len = len(self.trees)
        print("{0} trees chopped down".format(pre_lumber_tree_len - post_lumber_tree_len))

        pre_bear_lumber_len = len(self.lumberjacks)
        for bear in self.bears:
            self.lumberjacks = bear.pass_month(self.lumberjacks)
        post_bear_lumber_len = len(self.lumberjacks)
        print("{0} lumberjacks mauled".format(pre_bear_lumber_len - post_bear_lumber_len))

        #time.sleep(1)

        return len(self.trees)

    def pass_year(self):

        print("Year {0} Report:".format(self.month_counter/12))

        print("Forest has {0} trees, {1} lumberjacks, and {2} bears."
              .format(len(self.trees), len(self.lumberjacks), len(self.bears)))

        # Hire new lumberjacks based on the amount of lumber gathered. Too little lumber? Fire a jack at random.
        total_lumber = sum([lumberjack.lumber for lumberjack in self.lumberjacks])
        print("Lumber gathered: {0}".format(total_lumber))
        if total_lumber >= len(self.lumberjacks):
            for new_lumberjack in range(0,floor(total_lumber / len(self.lumberjacks))):
                x_pos = random.choice(range(self.forest_size))
                y_pos = random.choice(range(self.forest_size))
                self.lumberjacks.append(Lumberjack(x_pos, y_pos, self.forest_size))
        elif len(self.lumberjacks) > 1:
            random.shuffle(self.lumberjacks)
            self.lumberjacks.pop()

        # If there are no mawings for a year, add a bear, otherwise, remove one at random
        total_mawings = sum([bear.maws for bear in self.bears])
        print("Bear mawings: {0}".format(total_mawings))
        if total_mawings == 0:
            x_pos = random.choice(range(self.forest_size))
            y_pos = random.choice(range(self.forest_size))
            self.bears.append(Bear(x_pos, y_pos, self.forest_size))
        else:
            random.shuffle(self.bears)
            self.bears.pop()


def main():
    simulation = ForestSimulation(10)
    for year in range(400):
        for month in range(12):
            if simulation.pass_month() == 0:
                print("No more trees!")
                return
        simulation.pass_year()

if __name__ == "__main__":
    main()