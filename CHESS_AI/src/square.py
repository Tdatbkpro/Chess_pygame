class Square:
    def __init__(self, row,col, piece=None):
        self.row = row
        self.col =col
        self.piece = piece

        pass
    def has_piece(self):
        return self.piece != None
    
    def __eq__(self, value):
        return self.row == value.row and self.col == value.col
    
    @staticmethod
    def in_board(*args):
        for arg in args:
            if arg<0 or arg > 7:
                return False
        return True
    def isempty(self):
        return not self.has_piece()
    def can_rival(self, color):
        return self.has_piece() and self.piece.color != color 
    def isempty_or_rival(self, color):
        if not self.has_piece():
            return True
        elif self.piece.color != color:
            return True

        return False
    def has_team(self, color):
        return self.has_piece() and self.piece.color == color 