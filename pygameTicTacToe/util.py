# **********************************************************************************
# Program Author: Harry, Justin
# Revision Date: January 17, 2020
# Program Name: Tic Tac Toe
# Description: A Tic Tac Toe game you can play against the computer or with your friends.
# There are two levels of difficulty which are easy and impossible. On easy mode, the computer
# goes randomly while on impossible mode, an algorithm is used.
# This file is where all the functions are stored.
# *********************************************************************************

# import libraries
import random
from objects import *

pygame.init()

# display width, height, size
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600

DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

# setting up display and clock
display = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()

# display caption
pygame.display.set_caption("Tic Tac Toe")

# all images
scoreImg = pygame.image.load("res/score.png").convert()

# colors
background = (20, 189, 172)
gridColor = (13, 161, 146)
xColor = (84, 84, 84)
oColor = (242, 235, 211)
black = (0, 0, 0)
white = (255, 255, 255)

# objects
grid = Grid(gridColor, 120, 16, 104, 165, [[None for i in range(3)] for j in range(3)])
x = X(xColor, 80, 10)
tieX = X(xColor, 160, 20)
winX = X(xColor, 200, 40)
o = O(oColor, 42, 10)
winO = O(oColor, 150, 40)
tieO = O(oColor, 84, 20)


# fill the background
def fillBackground(display):
    display.fill(background)


# checks if the mouse is on a square
def checkSquareNumber(grid, mousePos):
    if grid.gridXPos <= mousePos[0] <= grid.gridXPos + grid.gridSquareSize:     # checks first column
        if grid.gridYPos <= mousePos[1] <= grid.gridYPos + grid.gridSquareSize:
            return 1
        if grid.gridYPos + grid.gridSquareSize + grid.gridLineSize <= mousePos[1] <= grid.gridYPos + (2 * grid.gridSquareSize) + grid.gridLineSize:
            return 4
        if grid.gridYPos + (2 * grid.gridSquareSize) + (2 * grid.gridLineSize) <= mousePos[1] <= grid.gridYPos + grid.GRID_WIDTH:
            return 7
    if grid.gridXPos + grid.gridSquareSize + grid.gridLineSize <= mousePos[0] <= grid.gridXPos + (2 * grid.gridSquareSize) + grid.gridLineSize:     # checks second column
        if grid.gridYPos <= mousePos[1] <= grid.gridYPos + grid.gridSquareSize:
            return 2
        if grid.gridYPos + grid.gridSquareSize + grid.gridLineSize <= mousePos[1] <= grid.gridYPos + (2 * grid.gridSquareSize) + grid.gridLineSize:
            return 5
        if grid.gridYPos + (2 * grid.gridSquareSize) + 2 * grid.gridLineSize <= mousePos[1] <= grid.gridYPos + grid.GRID_WIDTH:
            return 8
    if grid.gridXPos + (2 * grid.gridSquareSize) + grid.gridLineSize <= mousePos[0] <= grid.gridXPos + grid.GRID_WIDTH: # checks third column
        if grid.gridYPos <= mousePos[1] <= grid.gridYPos + grid.gridSquareSize:
            return 3
        if grid.gridYPos + grid.gridSquareSize + grid.gridLineSize <= mousePos[1] <= grid.gridYPos + (2 * grid.gridSquareSize) + grid.gridLineSize:
            return 6
        if grid.gridYPos + (2 * grid.gridSquareSize) + 2 * grid.gridLineSize <= mousePos[1] <= grid.gridYPos + grid.GRID_WIDTH:
            return 9

    return None  # return None if mouse is not on any of the squares


# converts the value from the checkMousePos function to a value which can be inputted to the grid array
def convertMousePosToGridPos(square):
    square -= 1

    if square < 3:
        return [0, square]
    else:
        square -= 3

        if square < 3:
            return [1, square]
        else:
            square -= 3

            return [2, square]


# convert the index of the piece from the grid to the corresponding square number
def convertGridPosToMousePos(gridPos):
    if gridPos[0] == 0:
        return gridPos[1] + 1
    elif gridPos[0] == 1:
        return gridPos[1] + 1 + 3
    elif gridPos[0] == 2:
        return gridPos[1] + 1 + 6


# load the previous pieces played
def loadPieces(display, grid, piece):
    for i in range(3):
        for j in range(3):
            if grid.gridArray[i][j] == piece:
                piece.draw(display, grid, convertGridPosToMousePos([i, j]))


# check if someone wins
def checkWin(grid, piece):
    # horizontal win
    for i in range(3):
        if grid.gridArray[i][0] == piece and grid.gridArray[i][1] == piece and grid.gridArray[i][2] == piece:
            return True

    # vertical win
    for i in range(3):
        if grid.gridArray[0][i] == piece and grid.gridArray[1][i] == piece and grid.gridArray[2][i] == piece:
            return True

    # diagonal win:
    if grid.gridArray[0][0] == piece and grid.gridArray[1][1] == piece and grid.gridArray[2][2] == piece:
        return True
    if grid.gridArray[2][0] == piece and grid.gridArray[1][1] == piece and grid.gridArray[0][2] == piece:
        return True


# check tie
def checkTie(grid):
    squareCounter = 0

    for i in range(3):
        for j in range(3):
            if type(grid.gridArray[i][j]) == X or type(grid.gridArray[i][j]) == O:
                squareCounter += 1

    if squareCounter == 9:
        return True
    else:
        return False


# function to clear the grid
def clearGridArray(grid):
    for i in range(3):
        for j in range(3):
            grid.gridArray[i][j] = None


# function to know if a piece is on the grid with given position
def containPiece(grid, squarePos):
    if type(grid.gridArray[squarePos[0]][squarePos[1]]) == X or type(grid.gridArray[squarePos[0]][squarePos[1]]) == O:
        return True
    return False


# increase score
def loadScore(display, xScore, oScore, font):
    display.blit(scoreImg, (50, 35))
    display.blit(scoreImg, (DISPLAY_WIDTH - 250, 35))

    if xScore == 0:
        display.blit(font.render(str("X       " + "-").encode("utf-8"), True, black), (70, 36))
    if oScore == 0:
        display.blit(font.render(str("O       " + "-").encode("utf-8"), True, black), (370, 36))
    if 0 < xScore <= 9:
        display.blit(font.render(str("X       " + str(xScore)).encode("utf-8"), True, black), (70, 36))
    if 0 < oScore <= 9:
        display.blit(font.render(str("O       " + str(oScore)).encode("utf-8"), True, black), (370, 36))
    if xScore > 9:
        display.blit(font.render(str("X      " + str(xScore)).encode("utf-8"), True, black), (70, 36))
    if oScore > 9:
        display.blit(font.render(str("O      " + str(oScore)).encode("utf-8"), True, black), (370, 36))


# load main menu
def mainMenu(display, mainMenuFont, mousePos, buttonArray):
    display.blit(mainMenuFont.render(str("Tic Tac Toe").encode("utf-8"), True, white), (45, 50))

    for button in buttonArray:
        if button.isOver(mousePos):
            button.draw(display, 10)
        else:
            button.draw(display)


# load impossible computer algorithm
def playImpossible(grid, computerPiece):
    humanPiece = None
    if computerPiece == x:
        humanPiece = o
    elif computerPiece == o:
        humanPiece = x

    # check to see if there is a winning move
    for i in range(3):
        for j in range(3):
            if not containPiece(grid, [i, j]):
                grid.gridArray[i][j] = computerPiece

                if checkWin(grid, computerPiece):
                    grid.gridArray[i][j] = None
                    return [i, j]

                grid.gridArray[i][j] = None

    # check if there is a win that needs to be blocked
    for i in range(3):
        for j in range(3):
            if not containPiece(grid, [i, j]):
                grid.gridArray[i][j] = humanPiece

                if checkWin(grid, humanPiece):
                    grid.gridArray[i][j] = None
                    return [i, j]

                grid.gridArray[i][j] = None

    # check if the center is empty
    if grid.gridArray[1][1] is None:
        return [1, 1]

    # # check if there is a fork
    if ((grid.gridArray[0][0] == grid.gridArray[2][2] == humanPiece) or
            (grid.gridArray[0][2] == grid.gridArray[2][0] == humanPiece)):
        if not grid.gridArray[1][2]:
            return [1, 2]

    if grid.gridArray[1][0] == humanPiece:
        if grid.gridArray[0][1] == humanPiece:
            if not grid.gridArray[0][0]:
                return [0, 0]

    if grid.gridArray[1][0] == humanPiece:
        if grid.gridArray[2][1] == humanPiece:
            if not grid.gridArray[2][0]:
                return [2, 0]

    if grid.gridArray[0][1] == humanPiece:
        if grid.gridArray[1][2] == humanPiece:
            if not grid.gridArray[0][2]:
                return [0, 2]

    if grid.gridArray[2][1] == humanPiece:
        if grid.gridArray[1][2] == humanPiece:
            if not grid.gridArray[2][2]:
                return [2, 2]

    if grid.gridArray[0][2] == humanPiece:
        if grid.gridArray[2][1] == humanPiece:
            if not grid.gridArray[1][2]:
                return [1, 2]
        elif grid.gridArray[1][0]:
            if not grid.gridArray[0][1]:
                return [0, 1]

    if grid.gridArray[2][2] == humanPiece:
        if grid.gridArray[0][1] == humanPiece:
            if not grid.gridArray[1][2]:
                return [1, 2]
        elif grid.gridArray[1][0] == humanPiece:
            if not grid.gridArray[2][1]:
                return [2, 1]

    if grid.gridArray[0][0] == humanPiece:
        if grid.gridArray[2][1] == humanPiece:
            if not grid.gridArray[1][0]:
                return [1, 0]
        elif grid.gridArray[1][2] == humanPiece:
            if not grid.gridArray[0][1]:
                return [0, 1]

    if grid.gridArray[2][0] == humanPiece:
        if grid.gridArray[1][2] == humanPiece:
            if not grid.gridArray[2][1]:
                return [2, 1]
        elif grid.gridArray[0][1] == humanPiece:
            if not grid.gridArray[1][0]:
                return [1, 0]

    # check if corner is open
    cornerList = [[0, 0], [0, 2], [2, 0], [2, 2]]
    random.shuffle(cornerList)  # randomize the corner

    for corner in cornerList:
        if not containPiece(grid, corner):
            return corner

    # check if a side is open
    edgeList = [[0, 1], [1, 0], [1, 2], [2, 1]]
    random.shuffle(edgeList)

    for edge in edgeList:
        if not containPiece(grid, edge):
            return edge

    # just in case none of the other checks are triggered go to the next spot
    for i in range(3):
        for j in range(3):
            if not containPiece(grid, [i, j]):
                return [i, j]
