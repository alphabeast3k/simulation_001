

class EnemyManager:
    def __init__(self, spawn_points: list[tuple]):
        # spawn points are indexed by row and column of the tile rather then screen position
        self.spawn_points = spawn_points
    
    def get_spawn_points(self):
        return self.spawn_points