import pygame
import random
import sys
import os

def get_base_path():
    if getattr(sys, 'frozen', False): # executable
        return sys._MEIPASS
    else:
        return os.path.dirname(__file__)
base_path = get_base_path()
sys.path.append(os.path.join(base_path, '../classes/Game'))
from Level import Graph



# Initialize Pygame
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
pygame.display.set_caption("Test Ghost")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SHADOW_COLOR = (50, 50, 50)  # Dark gray for shadow

def get_image_surface(file_path):
    image = pygame.image.load(file_path).convert()
    return image

ghostcolor = {
    0: (255, 0, 0, 255),
    1: (255, 128, 255, 255),
    2: (128, 255, 255, 255),
    3: (255, 128, 0, 255),
    4: (50, 50, 255, 255),
    5: (255, 255, 255, 255)}

class ghost:
    def __init__(self, id):
        self.cur_x = (TILES_X // TILE_SIZE) // 2
        self.cur_y = (TILES_Y // TILE_SIZE) // 2
        
        self.maze = None
        
        self.path = []
        
        for i in range(1, 7, 1):
            self.anim[i] = get_image_surface(
                os.path.join(base_path, "../resources", "sprite", "ghost " + str(i) + ".gif"))

            # change the ghost color in this frame
            for y in range(0, 30, 1):
                for x in range(0, 30, 1):

                    if self.anim[i].get_at((x, y)) == (255, 0, 0, 255):
                        # default, red ghost body color
                        self.anim[i].set_at((x, y), ghostcolor[self.id])

        self.animFrame = 1
        self.animDelay = 0
        
    def set_maze(self, maze):
        self.maze = maze
        
    def move(self):
        pass
    
    def update_path(self, goal=[random.randint(0, TILES_X)*TILE_SIZE, random.randint(0, TILES_Y)*TILE_SIZE]):
        pass
    
    def draw(self):
        pass
    
    def control(self, player=None):
        if player:
            self.update_path(player.get_pos())
        else:
            if not self.path:
                self.path = self.update_path()
                
        self.move()

# Create a sprite group and add the player sprite
# all_sprites = pygame.sprite.Group()
# player = Player()
# all_sprites.add(player)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    
    # keys = pygame.key.get_pressed()
    # player.move(keys)
    # player.draw()
    
    # pygame.display.flip()
    pygame.display.update()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()