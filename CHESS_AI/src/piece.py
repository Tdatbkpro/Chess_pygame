import os
class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect = None):
        self.name = name
        self.color = color
        self.dir = -1 if color == 'white' else 1
        self.moves =[]
        self.list_moved = []
        self.moved = False
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.texture_rect = texture_rect
        self.texture = texture

    def set_texture(self,size = 80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )
        return self.texture
    def _add_moves(self,move):
        self.moves.append(move)
        pass
    def clear_moves(self):
        self.moves = []
    def add_moved(self,move):
        self.list_moved.append(move)


class Pawn(Piece):
    def __init__(self,color):
        super().__init__('pawn', color,1.0)
class Knight(Piece):
    def __init__(self,color):
        super().__init__('Knight', color,3.0)
class Bishop(Piece):
    def __init__(self,color):
        super().__init__('Bishop', color,3.0001)
class Rook(Piece):
    def __init__(self,color):
        super().__init__('rook', color,5.0)
class Queen(Piece):
    def __init__(self,color):
        super().__init__('Queen', color,9.0)
class King(Piece):
    def __init__(self,color):
        super().__init__('King', color,10000.0)
