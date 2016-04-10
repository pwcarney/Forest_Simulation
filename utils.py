def check_overflow(location, forest_size):
    x = location[0]
    y = location[1]

    if x == forest_size:
        x = 0
    if x < 0:
        x = forest_size
    if y == forest_size:
        y = 0
    if y < 0:
        y = forest_size

    return x, y