# =============================================================================
# Abstract
# class Behavior:
#     # speed
#     # position
#     pass

class Entity:
    # speed
    # position
    pass

class ghost(Entity):
    pass
# =============================================================================

# =============================================================================
# Player
class player(Entity):
    pass
# =============================================================================

# =============================================================================
# Ghost
class dumb_ghost(ghost):
    pass

class greedy_ghost(ghost):
    pass

class wanderer_ghost(ghost):
    pass

class guardian_ghost(ghost):
    pass

class hunter_ghost(ghost):
    # bfs for game ballance
    pass
# =============================================================================