import pygame
from const import *
from board import *
from dragger import *
from config import*

class Game:
    def __init__(self):
        self.next_play = 'white'
        self.board = Board()
        self.hover_sqr = None
        self.dragger = Dragger()
        self.config = Config()
        pass
    def show_bg(self, surface):
        theme_bg = self.config.theme.bg
        for row in range(ROWS):
            for col in range(COLS):
                color = theme_bg.light if (row + col) % 2 == 0 else theme_bg.dark
                rect = (col*SQSIZE,row*SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)
            

                if col == 0:
                    color = theme_bg.light if (row + col) % 2 == 1 else theme_bg.dark 
                    lbl = self.config.font.render(str(ROWS-row), 1, color)
                    lbl_pos = (5, 5+ row*SQSIZE)
                    surface.blit(lbl,lbl_pos)
                if row == 7:
                    color = theme_bg.light if (row + col) % 2 == 1 else theme_bg.dark 
                    lbl = self.config.font.render(chr(col+97), 1, color)
                    lbl_pos = (col * SQSIZE + SQSIZE - 15, SQSIZE * 8 - 25)
                    surface.blit(lbl,lbl_pos)
    def show_pieces(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    #print()
                    if piece is not self.dragger.piece: 
                        img = pygame.image.load(piece.set_texture())
                        img_center = col*SQSIZE + SQSIZE//2 , row*SQSIZE + SQSIZE//2
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, piece.texture_rect)
    

    def show_moves(self, surface):
        theme_moves = self.config.theme.moves
        if self.dragger.isDragger:
            piece = self.dragger.piece
            for move in piece.moves:
                color = theme_moves.light if (move.final.row +move.final.col)%2 else theme_moves.dark

                rect = (move.final.col*SQSIZE, move.final.row*SQSIZE, SQSIZE,SQSIZE)
                pygame.draw.rect(surface,color,rect)

    def show_last_move(self,surface):
        theme_trace = self.config.theme.trace
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial,final]:
                color = theme_trace.light if (pos.row + pos.col) %2 == 0 else theme_trace.dark
                rect = (pos.col *SQSIZE, pos.row*SQSIZE, SQSIZE,SQSIZE)
                pygame.draw.rect(surface,color,rect)
            
    def show_hover(self, surface):
        if self.hover_sqr:
            color = (180,180,180)
            rect = (self.hover_sqr.col * SQSIZE, self.hover_sqr.row * SQSIZE, SQSIZE,SQSIZE)
            pygame.draw.rect(surface,color,rect)


    def next_turn(self):
        self.next_play = 'white' if self.next_play is 'black' else 'black'

    def change_theme(self):
        self.config.change_themes()

    def sound_effect(self, capture=False):
        if capture:
            self.config.capture_sound.play()
        else :
            self.config.move_sound.play()
