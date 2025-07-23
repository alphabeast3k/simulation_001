

class GameManager:
    def __init__(self):
        self.should_redraw_board = False

    def toggle_should_redraw_board(self):
        self.should_redraw_board = not self.should_redraw_board
    
    def set_should_redraw_board(self, flag: bool):
        self.set_should_redraw_board = flag
    
    def get_should_redraw_board(self):
        return self.should_redraw_board