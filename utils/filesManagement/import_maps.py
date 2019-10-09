def build_grid_from_file(file):
    """
    According a text file used as map generating a grid for a level
    :param file:
    :return: grid . Type 2 dimension Array
    """
    grid = []
    with open(file, "r") as f:
        for line in f:
            row = []
            for c in line[:-1]:
                row.append(c)
            grid.append(row)
        return grid

