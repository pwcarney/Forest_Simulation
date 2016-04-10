from tree import Tree
from bear import Bear
from lumberjack import Lumberjack

import random


class ForestSimulation:

    def __init__(self, forest_size):

        self.forest_size = forest_size

        self.forest = []
        self.trees = []
        self.lumberjacks = []
        self.bears = []

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

    def pass_month(self):

        [tree.pass_month(self.trees) for tree in self.trees]

        for lumberjack in self.lumberjacks:
            self.trees = lumberjack.pass_month(self.trees)

        for bear in self.bears:
            bear.pass_month(self.lumberjacks)


def main():
    simulation = ForestSimulation(10)
    for year in range(400):
        for month in range(12):
            simulation.pass_month()

main()
