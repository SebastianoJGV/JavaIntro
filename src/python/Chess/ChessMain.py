'''
Description : This is our main driver file, responsible for handling user input and current GameState.
Author : Sebastiano Giannelli Viscardi
Date : May 13th, 2022
Status : WIP, non functioning
'''
import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512 #400 Is another option tho quality is lower
DIMENSION = 8 #Board is 8x8
SQUARE_SIZE = HEIGHT//DIMENSION
FPS_CAP = 15 #Frames per second cap for animations
IMAGES={} #Dictionary storing all images

'''
Initialize global dictinary of images to reference, this will only be called on once
'''

def loadImages():
    pieces=['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.image.load("src/python/Chess/images/"+piece+".png")
        #Saves images in dictionary to appropriate piece, eg. IMAGES['wP'] = wP.png

'''
Main driver, will handle user input and graphics updating every frame
'''
def main():
    p.init()#Pygame intialization
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption("Chess")
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    loadImages() # Only done once, will load all images into memory
    isRunning = True # Keeps track of gamestate
    while isRunning:
        for n in p.event.get():
            if n.type == p.QUIT:
                isRunning = False
        clock.tick(FPS_CAP)
        p.display.flip()


'''
Responsible for graphics within current game state
'''
def drawGameState(screen, gs):
    drawBoard(screen) # Draw Squares
    drawPieces(screen, gs.board) # Draw pieces on top of quares

def drawBoard(screen):
    for x in range(DIMENSION):
        for y in range(DIMENSION):
            if (x+y)%2 == 0:
                p.draw.rect(screen, p.Color("white"), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                p.draw.rect(screen, p.Color("black"), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def drawPieces(screen, board):
    for x in range(DIMENSION):
        for y in range(DIMENSION):
            piece = board[x][y]
            if piece != "--":
                screen.blit(IMAGES[piece], p.rect(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

if __name__ == "__main__":
    main()