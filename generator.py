import random
import math
from Blocks.SpawnRoom import SpawnRoom

def generate(x, y):
    grid = generateSpace(x, y)
    spawn = generateSpawnRoom(grid)

    return grid


"""
    Generate Space
    x - int -> 3
    y - int -> 3
    ----
    Grid - [[], ...] -> [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
"""
def generateSpace(x, y):
    grid = []
    for row in range(x):
        grid.append([])
        for column in range(y):
            grid[row].append(0)  # Append a cell
    return grid


def generateSpawnRoom(grid):
    room_width = 6
    room_height = 6

    x_s = len(grid)
    y_s = len(grid)

    spawn_x = math.floor(random.random() * (x_s - room_width))
    spawn_y = math.floor(random.random() * (y_s - room_height))

    for x_d in range(room_width):
        for y_d in range(room_height):
            x = spawn_x + x_d
            y = spawn_y + y_d
            grid[x][y] = 1

    return SpawnRoom(spawn_x, spawn_y, room_width, room_height)
    