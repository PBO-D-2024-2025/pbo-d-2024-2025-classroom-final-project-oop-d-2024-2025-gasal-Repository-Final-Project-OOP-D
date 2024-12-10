import pygame
import sys
import os

def get_base_path():
    if getattr(sys, 'frozen', False): # executable
        return sys._MEIPASS
    else:
        return os.path.dirname(__file__)

base_path = get_base_path()

sys.path.append(os.path.join(base_path, '../classes'))
sys.path.append(os.path.join(base_path, '../classes/Game'))
sys.path.append(os.path.join(base_path, '../classes/Progress'))
sys.path.append(os.path.join(base_path, '../classes/User_Interface'))
sys.path.append(os.path.join(base_path, '../classes/Error'))
sys.path.append(os.path.join(base_path, '../classes/Database'))

import Game_Controller

pygame.init()

# Tile dimensions
TILE_SIZE = 20
TILES_X = 30  # Number of tiles horizontally
TILES_Y = 30  # Number of tiles vertically

# Screen dimensions based on tiles
SCREEN_WIDTH = TILE_SIZE * TILES_X
SCREEN_HEIGHT = TILE_SIZE * TILES_Y

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Draw Test")

if __name__ == '__main__':
    print('Hello, World!')