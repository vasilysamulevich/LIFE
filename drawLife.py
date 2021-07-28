from time import sleep

import pygame
from collections import namedtuple
from random import randint, randrange

WIDTH = 800
HEIGHT = 800
FPS = 10
colors = {"WHITE": (255, 255, 255),
          "GREEN": (0, 255, 0),
          "BLACK": (0, 0, 0),
          "BLUE": (0, 0, 255),
          "RED": (255, 0, 0)
          }

Cell = namedtuple("Cell", "is_alive number_of_living_cells_around")
Coord = namedtuple("Coord", "x y")
living_cells = {Coord(randrange(0, WIDTH, 10), randrange(0, HEIGHT, 10)): Cell(True, 0) for _ in range(randint(3000, 5000))}


def new_living_cells(cells: dict):
    old_cells = cells.copy()
    for coord in old_cells:
        for i in range(-10, 20, 10):
            for j in range(-10, 20, 10):
                if not i == j == 0:
                    new_coord = Coord(coord.x + i, coord.y + j)
                    if new_coord in old_cells.keys():  # if point living
                        cells[new_coord] = Cell(cells[new_coord].is_alive, cells[new_coord].number_of_living_cells_around + 1)
                    else:
                        cells[new_coord] = Cell(False, 1)

    old_cells = cells.copy()
    for cell in old_cells:
        if not old_cells[cell].is_alive and old_cells[cell].number_of_living_cells_around == 3:
            cells[cell] = Cell(True, old_cells[cell].number_of_living_cells_around)
        if old_cells[cell].is_alive and old_cells[cell].number_of_living_cells_around not in (2, 3):
            cells.pop(cell)
    for cell in cells:
        cells[cell] = Cell(True, 0)
    



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LIFE")
clock = pygame.time.Clock()
screen.fill(colors["WHITE"])
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check for closing window
            running = False

    screen.fill(colors["BLACK"])
    for cell in living_cells:
        pygame.draw.rect(screen, colors["GREEN"], (*cell, 10, 10))
    pygame.display.update() #pygame.display.flip()

    new_living_cells(living_cells)
    # Держим цикл на правильной скорости
    clock.tick(FPS)

pygame.quit()
quit()
