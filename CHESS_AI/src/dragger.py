from const import *
import pygame

class Dragger:
    def __init__(self):
        self.isDragger = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
        self.piece = None

    def update_mouse(self, pos):
        x, y = pos
        # ép chuột nằm trong bàn cờ
        self.mouseX = max(0, min(x, WIDTH - 1))
        self.mouseY = max(0, min(y, HEIGHT - 1))


    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.isDragger = True
    
    def undrag_piece(self):
        self.isDragger = False
        self.piece = None

    def update_surface(self, surface):
        if self.piece:
            self.piece.set_texture(size=128)  # load ảnh to hơn khi kéo
            img = pygame.image.load(self.piece.texture)
            self.piece.texture_rect = img.get_rect(center=(self.mouseX, self.mouseY))
            surface.blit(img, self.piece.texture_rect)
