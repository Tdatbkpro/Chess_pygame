from const import *
from square import *
from piece import *
from move import *

class Board:
    def __init__(self):
        self.squares = []
        self.last_move = None
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")
        

    def move(self, piece, move):
        initial = move.initial
        final = move.final

        # xoá quân ở ô ban đầu
        self.squares[initial.row][initial.col].piece = None
        # đặt quân vào ô mới
        self.squares[final.row][final.col].piece = piece

        piece.clear_moves()
        self.last_move = move
        piece.moved = True

        # ===== Nhập thành =====
        if piece.name == "King":
            # nhập thành ngắn (sang phải 2 ô)
            if final.col - initial.col == 2:
                rook_initial = Square(initial.row, 7)   # xe ở h1/h8
                rook_final   = Square(initial.row, 5)   # xe về f1/f8
                rook = self.squares[rook_initial.row][rook_initial.col].piece

                self.squares[rook_initial.row][rook_initial.col].piece = None
                self.squares[rook_final.row][rook_final.col].piece = rook
                rook.moved = True

            # nhập thành dài (sang trái 2 ô)
            elif final.col - initial.col == -2:
                rook_initial = Square(initial.row, 0)   # xe ở a1/a8
                rook_final   = Square(initial.row, 3)   # xe về d1/d8
                rook = self.squares[rook_initial.row][rook_initial.col].piece

                self.squares[rook_initial.row][rook_initial.col].piece = None
                self.squares[rook_final.row][rook_final.col].piece = rook
                rook.moved = True


    
    def valid_move(self, piece, move):
        # print(move)
        for p_move in piece.moves:
            if p_move == move:
                return True
        return False
        
    

    def _create(self):
        # Tạo bàn cờ 8x8 rỗng
        self.squares = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        # Gán từng ô là một Square
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(col, row)

    def calc_possiable_piece(self, piece, row,col):
        pass
        def knight_moves():
             possiable_moves = [
                  (row-2, col-1),
                  (row-1, col-2),
                  (row-1, col+2),
                  (row-2, col+1),
                  (row+1, col-2),
                  (row+2, col-1),
                  (row+1, col+2),
                  (row+2, col+1),
             ]

             for move_row,move_col in possiable_moves:
                  if Square.in_board(move_col,move_row):
                       if self.squares[move_row][move_col].isempty_or_rival(piece.color):
                            initial = Square(row,col)
                            final = Square(move_row,move_col)
                            move = Move(initial,final)
                            piece._add_moves(move)
        def pawn_moves():
            steps = 1 if piece.moved  else 2
            start = row + piece.dir
            end = row + (piece.dir*(1 + steps))
            for move_row in range(start, end, piece.dir):
                 if Square.in_board(move_row):
                      if self.squares[move_row][col].isempty():
                           initial = Square(row,col)
                           final = Square(move_row,col)
                           move = Move(initial,final)
                           piece._add_moves(move)
                      else:break
                 else:break
            possiable_move_row = row + piece.dir   # chỉ một giá trị
            possiable_move_cols = [col-1, col+1]   # có thể 2 hướng chéo

            for move_col in possiable_move_cols:
                move_row = possiable_move_row
                if Square.in_board(move_row, move_col):
                    if self.squares[move_row][move_col].can_rival(piece.color):
                        initial = Square(row, col)
                        final = Square(move_row, move_col)
                        move = Move(initial, final)
                        piece._add_moves(move)
                    

        def straightline_moves(incrs):
            for row_incr, col_incr in incrs:
                move_row = row + row_incr
                move_col = col + col_incr

                # duyệt theo đường thẳng cho đến khi ra ngoài hoặc gặp quân cản
                while Square.in_board(move_row, move_col):

                    initial = Square(row, col)
                    final = Square(move_row, move_col)
                    move = Move(initial, final)

                    # Nếu ô trống → add move và tiếp tục đi tiếp
                    if self.squares[move_row][move_col].isempty():
                        piece._add_moves(move)

                    # Nếu có quân đối thủ → add move rồi dừng lại (không đi xuyên qua)
                    elif self.squares[move_row][move_col].can_rival(piece.color):
                        piece._add_moves(move)
                        break

                    # Nếu có quân cùng màu → dừng lại, không add move
                    else:
                        break

                    # tiến thêm một bước trên cùng hướng
                    move_row += row_incr
                    move_col += col_incr

        def king_moves():
            # các ô kề vua
            adjs = [
                (row-1,col-1),(row-1,col),(row-1,col+1),
                (row,col-1),             (row,col+1),
                (row+1,col-1),(row+1,col),(row+1,col+1)
            ]

            for move_row, move_col in adjs:
                if Square.in_board(move_row, move_col):
                    if self.squares[move_row][move_col].isempty_or_rival(piece.color):
                        initial = Square(row, col)
                        final = Square(move_row, move_col)
                        move = Move(initial, final)
                        piece._add_moves(move)

            # ---- Nhập thành ----
            if not piece.moved:
                # Nhập thành ngắn (kingside)
                rook = self.squares[row][7].piece
                if rook and rook.name == 'rook' and not rook.moved:
                    if self.squares[row][5].isempty() and self.squares[row][6].isempty():
                        initial = Square(row, col)
                        final = Square(row, col+2)  # vua đi sang phải 2 ô
                        move = Move(initial, final)
                        piece._add_moves(move)

                # Nhập thành dài (queenside)
                rook = self.squares[row][0].piece
                if rook and rook.name == 'rook' and not rook.moved:
                    if self.squares[row][1].isempty() and self.squares[row][2].isempty() and self.squares[row][3].isempty():
                        initial = Square(row, col)
                        final = Square(row, col-2)  # vua đi sang trái 2 ô
                        move = Move(initial, final)
                        piece._add_moves(move)




        if isinstance(piece,Pawn):
            pawn_moves()
        elif isinstance(piece,Knight):
            knight_moves()
        elif isinstance(piece,Bishop):
            straightline_moves([(1,1), (-1,1), (1,-1), (-1,-1)])        
        elif isinstance(piece,Queen):
            straightline_moves([(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)])
        elif isinstance(piece,King):
            king_moves()
        elif isinstance(piece,Rook):
            straightline_moves([(1,0), (-1,0), (0,1), (0,-1)])

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        

        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))


b = Board()
b._create()
