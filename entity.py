
#Would like all objects in a scene to be a entity that can be selected but leaving this until refactor can be done
class Entity:
    def __init__(self):
        self.selected = False
    
    def toggle_selection(self) -> bool:
        self.selected = not self.selected
        return self.selected
