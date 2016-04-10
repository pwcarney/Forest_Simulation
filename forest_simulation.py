from tree import Tree
from bear import Bear
from lumberjack import Lumberjack

import random
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

        print("Starting with " + len(self.trees) + " trees.")
        print("Starting with " + len(self.lumberjacks) + " trees.")
        print("Starting with " + len(self.bears) + " trees.")

    def pass_month(self):

        self.month_counter += 1
        #print("The current month is",self.month_counter)

        [tree.pass_month(self.trees) for tree in self.trees]

        for lumberjack in self.lumberjacks:
            self.trees = lumberjack.pass_month(self.trees)

        for bear in self.bears:
            self.lumberjacks = bear.pass_month(self.lumberjacks)

        return len(self.trees)

    def pass_year(self):

        # Hire new lumberjacks based on the amount of lumber gathered. Too little lumber? Fire a jack at random.
        total_lumber = sum([lumberjack.lumber for lumberjack in self.lumberjacks])
        if total_lumber >= len(self.lumberjacks):
            for new_lumberjack in range(0,floor(total_lumber / len(self.lumberjacks))):
                x_pos = random.choice(range(self.forest_size))
                y_pos = random.choice(range(self.forest_size))
                self.lumberjacks.append(Lumberjack(x_pos, y_pos, self.forest_size))
        elif len(self.lumberjacks) > 1:
            random.shuffle(self.lumberjacks)
            self.lumberjacks.pop()

        # If there are no mawings for a year, add a bear, otherwise, remove one at random
        #total_mawings = sum([bear.maws for bear in self.bears])
        #if total_mawings == 0:
        #    x_pos = random.choice(range(self.forest_size))
        #    y_pos = random.choice(range(self.forest_size))
        #    self.bears.append(Lumberjack(x_pos, y_pos, self.forest_size))
        #else:
        #    random.shuffle(self.bears)
        #    self.bears.pop()


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