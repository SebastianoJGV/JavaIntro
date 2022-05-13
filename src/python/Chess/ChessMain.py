'''
Description : This is our main driver file, responsible for handling user input and current GameState.
Author : Sebastiano Giannelli Viscardi
Date : May 13th, 2022
Status : WIP, non functioning
'''
import pygame as p
from Chess.ChessEngine import ChessEngine

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
        IMAGES[piece] = p.image.load("Chess/Chess/images/"+piece+".png")
        #Saves images in dictionary to appropriate piece, eg. IMAGES['wP'] = wP.png

'''
Main driver, will handle user input and graphics updating every frame
'''
def main():
    p.init()#Pygame intialization
    screen = p.display.set_mode((WIDTH, HEIGHT))#Set screen size
    p.display.set_caption("Chess")
    clock = p.time.Clock()#Clock for FPS cap
    screen.fill(p.Color("white"))#Background colour
    loadImages()
    game = ChessEngine.GameState()#Initialize game state
    print(gs.board)