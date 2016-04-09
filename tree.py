import random


class Tree:

    def __init__(self, x, y, forest_size, age=0):
        self.location = (x, y)
        self.months_old = age  # 12 at initialization step, 0 otherwise
        self.forest_size = forest_size

    def pass_month(self, trees):

        # Check if still a sapling.
        if self.months_old < 12:
            return

        # Roll for every open space around tree to see if it spawns new tree.
        for x in range(self.location[0] - 1, self.location[0] + 1):
            for y in range(self.location[1] - 1, self.location[1] + 1):

                # Account for overflow or underflow on forest grid
                if x > self.forest_size:
                    x = 0
                if x < 0:
                    x = self.forest_size
                if y > self.forest_size:
                    y = 0
                if y < 0:
                    y = self.forest_size

                # Can't have a new tree at own location
                if (x,y) == self.location:
                    continue

                # Returns true and we continue if there is a tree in this adjacent space
                if self.is_tree_adjacent(x, y, trees):
                    continue

                baby_roll = random.randint(0,100)

                # A 120-month-old tree has a 20% chance to spawn a baby
                if self.months_old >= 120 and baby_roll < 20:
                    trees.append(Tree(x,y))
                elif self.months_old >= 12 and baby_roll < 10:
                    trees.append(Tree(x, y))

        self.months_old += 1
        return

    def is_tree_adjacent(self, x, y, trees):
        for other_tree in trees:
            if other_tree.location == zip(x, y):
                return True
