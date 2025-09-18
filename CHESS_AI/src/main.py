import pygame
import sys
from const import *
from game import Game
from square import *
from move import *

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess AI")
        self.game = Game()   # Game đã có sẵn board và dragger

    def mainLoop(self):
        screen = self.screen
        game = self.game
        board = game.board
        dragger = game.dragger

        while True:
            # vẽ lại background và pieces
            game.show_bg(screen)
            
            game.show_last_move(screen)
            game.show_pieces(screen)

            
            mouseX,mouseY = pygame.mouse.get_pos()
            mouse_col,mouse_row = mouseX//SQSIZE,mouseY//SQSIZE
            game.hover_sqr = Square(mouse_row,mouse_col)
            game.show_hover(screen)
            
            

            # vẽ quân đang kéo
            if dragger.isDragger:
                
                game.show_moves(screen)
                game.show_hover(screen)
                game.show_pieces(screen)
                
                dragger.update_surface(screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        if game.next_play == piece.color:
                            board.calc_possiable_piece(piece,clicked_row,clicked_col)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                        

                elif event.type == pygame.MOUSEMOTION:
                    
                    if dragger.isDragger:
                        dragger.update_mouse(event.pos)
                        mottion_row, mottion_col = min(event.pos[1]// SQSIZE,7),min(event.pos[0]// SQSIZE ,7)
                        game.hover_sqr = Square(mottion_row,mottion_col)
                        
                        print(mottion_row, mottion_col)
                        
                        
                        

                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.isDragger:
                        released_x, released_y = event.pos
                        released_row,released_col = released_y//SQSIZE, released_x//SQSIZE
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final_piece = board.squares[released_row][released_col].piece
                        print(final_piece)
                        final = Square(released_row,released_col,final_piece)
                        move = Move(initial,final)
                        
                        if board.valid_move(dragger.piece,move):
                            capture = board.squares[released_row][released_col].has_piece()
                            
                            board.move(dragger.piece, move)
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            game.sound_effect(capture)
                            game.next_turn()

                    dragger.undrag_piece()
                
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                        print("Press T")
                        game.change_theme()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        print("Press R")   
                        game.reset() 
                        game = self.game
                        board = game.board
                        dragger  = game.dragger

                    

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()
main.mainLoop()
