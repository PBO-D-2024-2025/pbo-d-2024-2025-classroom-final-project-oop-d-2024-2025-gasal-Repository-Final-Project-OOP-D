"""
Object.py

This file contains the classes for the objects in the game.
"""

from Game_Controller import *

# =============================================================================
# Abstract
class object_wall:
    pass

class object_food:
    pass
# =============================================================================

# =============================================================================
# Child
class Pellet_Food(object_food):
    def __init__(self):
        self.score = 100
        self.xpos = 0
        self.ypos = 0
        
    def set_pos(self, x, y):
        pass
    
    def draw(self):
        food_color = (255, 255, 0)
        pygame.draw.circle(screen, food_color, (self.x, self.y), self.radius)
    
    def check_collision(self):
        pass

class Strawberry_Food(object_food):
    # extra score 1500
    
    pass

class Blueberry_Food(object_food):
    # power up ghost killer
    # extra score 500
    pass

class Banana_Food(object_food):
    # power up ghost hunter (banish ghost(randomly)) # ghost house if there is one
    # extra score 500
    pass

class Apple_Food(object_food):
    # power up invicibility
    # extra score 500
    pass

class Orange_Food(object_food):
    # power up speed 25%
    # extra score 500
    pass

class Poison_Food(object_food):
    # nerf speed 25%
    # score -1000
    pass
# =============================================================================