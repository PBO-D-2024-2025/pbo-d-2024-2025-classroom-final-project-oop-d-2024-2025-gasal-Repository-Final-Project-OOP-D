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
    # score 100
    pass

class Strawberry_Food(object_food):
    # extra score 2500
    pass

class Blueberry_Food(object_food):
    # power up ghost killer
    pass

class Banana_Food(object_food):
    # power up ghost hunter (banish ghost(randomly)) # ghost house if there is one
    pass

class Apple_Food(object_food):
    # power up invicibility
    pass
# =============================================================================