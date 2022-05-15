'''
Description : Stores information regarding current game state, determines valid moves of pieces selected, and stores move logs.
Author : Sebastiano Giannelli Viscardi
Date : May 13th, 2022
Status : WIP, non functioning
'''
'''
Legend:
-- == blank space
bP == black pawn
bR == black rook
bN == black knight
bB == black bishop
bQ == black queen
bK == black king
wP == white pawn
wR == white rook
wN == white knight
wB == white bishop
wQ == white queen
wK == white king
'''
class GameState():
    def __init__(self):
        #Lists containing all pieces on the board, seperated into ranks from whites perspective
        self.board = [
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bP','bP','bP','bP','bP','bP','bP','bP'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],#Two dashes is a blank space, makes comparisons easier in the long run
            ['--','--','--','--','--','--','--','--'],
            ['wP','wP','wP','wP','wP','wP','wP','wP'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR'],
        ]
        self.whiteToMove = True
        self.moveLog=[]
        