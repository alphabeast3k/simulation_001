
# should manage the enemies and the locations
# different thing sto consider but necessary now
# ideally spawn an enemy not sure if that should be handled by the game board but this class should handle smooth motion for the enemy ensuring constant speed
class EnemyManager:
    def __init__(self, spawn_points: list[tuple]):
        # spawn points are indexed by row and column of the tile rather then screen position
        self.spawn_points = spawn_points
    
    def get_spawn_points(self):
        return self.spawn_points