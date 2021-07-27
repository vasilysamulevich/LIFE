from array import array
from collections import deque
from pprint import pprint

import drawLife

height = width = 50
number_of_generations = 20
field = [array('b', (0 for _ in range(height))) for _ in range(width)]     # List of boolean arrays
generations = deque([], maxlen=number_of_generations)


def life_or_death(x, y, field) -> bool:
    """ Cell with coordinates (x, y) must die or live.
    """
    start_x = 0 if x == 0 else -1   # Extreme cases / field boundaries
    start_y = 0 if y == 0 else -1
    end_x = 1 if x == 0 else 2
    end_y = 1 if y == 0 else 2
    number_of_living_cells = 0      # Count life cells
    for i in range(start_x, end_x):     # Check 8 cells around
        for j in range(start_y, end_y):
            if not i == j == 0 and field[x + i][y + j] == 1:    # Found all life cells
                number_of_living_cells += 1
    if number_of_living_cells not in (2, 3) and field[x][y] == 1:   # Around life cell NOT 2 or 3 life cells
        return False    # Cell must death
    if number_of_living_cells == 3 and field[x][y] == 0:    # Around death cell 3 life cells
        return True     # Cell must life


def continue_game(field, generations):
    """ The game ends if all cells are dead or such a field has been encountered before.
    """
    if field in generations:    # The same field has been created
        return -1   # "За последние 20 поколений такое поле уже встречалось"
    if not all(map(all, field)):    # All cells contain zero
        return 0    # "На поле все клетки мёртвые"
    return 1   # True - continue game


if __name__=='__main__':
    drawLife
