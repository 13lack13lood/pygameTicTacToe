# **********************************************************************************
# Program Author: Harry, Justin
# Revision Date: January 17, 2020
# Program Name: Tic Tac Toe
# Description: A Tic Tac Toe game you can play against the computer or with your friends.
# There are two levels of difficulty which are easy and impossible. On easy mode, the computer
# goes randomly while on impossible mode, an algorithm is used.
# This file is the main file.
# *********************************************************************************

# import libraries
import os
import platform

# import functions and objects
from util import *

# initialize pygame
pygame.init()

# fonts
mainMenuFont = pygame.font.SysFont('Manrope', 140)
mainMenuButtonFont = pygame.font.SysFont('Verdana', 20)
instructionsMenuFont = pygame.font.SysFont('Verdana', 30)
instructionsFont = pygame.font.SysFont('Verdana', 18)
playMenuFont = pygame.font.SysFont('Verdana', 60)
scoreFont = pygame.font.SysFont('Arial', 60)
winningFont = pygame.font.SysFont('Manrope', 75)

# needed to run on school computers
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

# buttons
instructionButton = Button(white, 230, 190, 140, 50, "Instructions", black, 20)
instructionBackButton = Button(white, 230, 470, 140, 50, "Back", black, 20)

playButton = Button(white, 230, 290, 140, 50, "Play", black, 20)
playEasyButton = Button(white, 230, 150, 140, 50, "Easy", black, 20)
playHardButton = Button(white, 230, 250, 140, 50, "Impossible", black, 20)
play2PlayerButton = Button(white, 230, 350, 140, 50, "2 Player", black, 20)
playBackButton = Button(white, 230, 500, 140, 50, "Back", black, 20)

chosePieceXButton = Button(white, 230, 200, 140, 50, "X", black, 20)
chosePieceOButton = Button(white, 230, 300, 140, 50, "O", black, 20)
chosePieceBackButton = Button(white, 230, 500, 140, 50, "Back", black, 20)

endGameRestartGameButton = Button(white, 120, 500, 160, 50, "Restart Game", black, 20)
endGameMainMenuButton = Button(white, 320, 500, 160, 50, "Main Menu", black, 20)

exitButton = Button(white, 230, 520, 140, 50, "Exit", black, 20)

# button arrays
mainMenuButtonArray = [instructionButton, playButton, exitButton]  # all buttons on main menu
instructionMenuButtonArray = [instructionButton, instructionBackButton]  # all buttons in instructions menu
playMenuButtonArray = [playButton, playEasyButton, playHardButton, play2PlayerButton, playBackButton]  # all buttons on the play menu
chosePieceMenuButtonArray = [chosePieceXButton, chosePieceOButton, chosePieceBackButton]  # all buttons on the chose piece menu
endGameMenuButtonArray = [endGameRestartGameButton, endGameMainMenuButton]  # all buttons on the end game menu

# menus
instructionsMenu = InstructionsMenu(instructionsMenuFont, instructionsFont, white, instructionMenuButtonArray)
playMenu = PlayMenu(playMenuFont, white, playMenuButtonArray)
chosePieceMenu = ChosePieceMenu(playMenuFont, white, chosePieceMenuButtonArray, playMenu, x, o)
endGameMenu = EndGame(winningFont, white, endGameMenuButtonArray, winX, winO, tieX, tieO)
exitMenu = ExitButton(exitButton)

# menu array
menuArray = [instructionsMenu, playMenu, exitMenu]

gameExit = False  # game loop variable
xTurn = True  # variable to see whos tern it is  x always goes first
xScore = 0  # score of x
oScore = 0  # score of o
winner = 0   # to know who won the game
startGame = False   # to know if to start the game
mouseClicked = False    # to know if mouse was clicked
page = 1    # to know which menu the user is on
computerPiece = None    # to know which piece the computer will be playing

while not gameExit:
    if not startGame:   # load main menu
        # set up
        clock.tick(60)  # start clock
        mousePos = pygame.mouse.get_pos()  # get mouse position

        # draw the background
        fillBackground(display)

        # check if to display end screen
        if winner is None or winner == x or winner == o:
            page = 6

        # main menu
        if page == 1:
            mainMenu(display, mainMenuFont, mousePos, mainMenuButtonArray)
            if mouseClicked and instructionsMenu.isClicked(mousePos):
                mouseClicked = False
                page = 2
            elif mouseClicked and playMenu.isClicked(mousePos):
                mouseClicked = False
                page = 3
            elif mouseClicked and exitMenu.isClicked(mousePos):
                exit()

        if page == 2:   # instructions menu
            instructionsMenu.drawMenu(display, background, mouseClicked, mousePos)
            if instructionsMenu.menuBack:
                page = 1
        elif page == 3:  # play menu
            playMenu.drawMenu(display, background, mouseClicked, mousePos)

            # bring to the chose piece menu only if the user plays with computer
            if playMenu.playEasy or playMenu.playImpossible:
                mouseClicked = False
                page = 4
            elif playMenu.play2Player:  # bring user directly to the game
                page = 5

            if playMenu.menuBack:
                mouseClicked = False
                playMenu.playEasy = False
                playMenu.playImpossible = False
                page = 1
        elif page == 4:  # chose piece menu
            chosePieceMenu.drawMenu(display, background, mouseClicked, mousePos)  # draw menu

            # let the user chose the piece they want to play
            if chosePieceMenu.pickedPiece is not None:
                if chosePieceMenu.pickedPiece == x:
                    computerPiece = o   # let computer know which piece to use
                elif chosePieceMenu.pickedPiece == o:
                    computerPiece = x   # let computer know which piece to use

                mouseClicked = False
                page = 5    # start game
            elif chosePieceMenu.menuBack:
                playMenu.playEasy = False   # deactivate everything
                playMenu.playImpossible = False   # <----|
                playMenu.play2Player = False      # <----|
                mouseClicked = False              # <----|
                page = 1
        elif page == 5:  # start game
            mouseClicked = False
            startGame = True
        elif page == 6:     # game end menu
            endGameMenu.winner = winner     # know who is the winner
            endGameMenu.drawMenu(display, grid, mouseClicked, mousePos)

            if endGameMenu.restartGame:
                endGameMenu.restartGame = False
                startGame = True
                winner = 0
            elif endGameMenu.mainMenu:
                endGameMenu.mainMenu = False    # deactivate everything
                mouseClicked = False                # <----|
                page = 1                            # <----|
                xTurn = True                        # <----|
                winner = 0                          # <----|
                xScore = 0                          # <----|
                oScore = 0                          # <----|
                playMenu.play2Player = False        # <----|
                playMenu.playEasy = False           # <----|
                playMenu.playImpossible = False     # <----|
                chosePieceMenu.pickedPiece = None   # <----|
                computerPiece = None                # <----|

        mouseClicked = False

        for event in pygame.event.get():
            # exit
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked = True

        pygame.display.update()
        pygame.time.delay(1)
    else:   # load game
        # set up
        clock.tick(60)  # start clock
        mousePos = pygame.mouse.get_pos()  # get mouse position

        # draw the background
        fillBackground(display)

        # load score and grid
        loadScore(display, xScore, oScore, scoreFont)
        grid.loadGrid(display)

        if playMenu.playEasy:   # set the computer level
            mouseClicked = False

            if computerPiece == x:
                if xTurn:
                    computerSquare = random.randint(1, 9)   # computer goes randomly
                    if not containPiece(grid, convertMousePosToGridPos(computerSquare)):
                        grid.gridArray[convertMousePosToGridPos(computerSquare)[0]][convertMousePosToGridPos(computerSquare)[1]] = x  # put the piece into the square
                        xTurn = False  # let the other person go

                for event in pygame.event.get():
                    # exit
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouseClicked = True
                        if not xTurn:
                            if checkSquareNumber(grid, mousePos) is not None:
                                if not containPiece(grid, [convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0], convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]]):    # check if the square already contains something
                                    grid.gridArray[convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0]][convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]] = o      # put the piece into the square
                                    xTurn = True    # let the other person go

            if computerPiece == o:
                mouseClicked = False

                for event in pygame.event.get():
                    # exit
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouseClicked = True
                        if xTurn:
                            if checkSquareNumber(grid, mousePos) is not None:
                                if not containPiece(grid, [convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0], convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]]):  # check if the square already contains something
                                    grid.gridArray[convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0]][convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]] = x  # put the piece into the square
                                    xTurn = False  # let the other person go

                if not xTurn:
                    computerSquare = random.randint(1, 9)
                    if not containPiece(grid, convertMousePosToGridPos(computerSquare)):
                        grid.gridArray[convertMousePosToGridPos(computerSquare)[0]][convertMousePosToGridPos(computerSquare)[1]] = o  # put the piece into the square
                        xTurn = True  # let the other person go

        if playMenu.playImpossible:  # set computer level
            mouseClicked = False

            if computerPiece == x:
                if xTurn:
                    computerSquare = playImpossible(grid, computerPiece)
                    if not containPiece(grid, computerSquare):
                        grid.gridArray[computerSquare[0]][computerSquare[1]] = x  # put the piece into the square
                        xTurn = False  # let the other person go

                for event in pygame.event.get():
                    # exit
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouseClicked = True
                        if not xTurn:
                            if checkSquareNumber(grid, mousePos) is not None:
                                if not containPiece(grid, [convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0], convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]]):  # check if the square already contains something
                                    grid.gridArray[convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0]][convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]] = o  # put the piece into the square
                                    xTurn = True  # let the other person go

            if computerPiece == o:
                mouseClicked = False

                if not xTurn:
                    computerSquare = playImpossible(grid, computerPiece)
                    if not containPiece(grid, computerSquare):
                        grid.gridArray[computerSquare[0]][computerSquare[1]] = o  # put the piece into the square
                        xTurn = True  # let the other person go

                for event in pygame.event.get():
                    # exit
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouseClicked = True
                        if xTurn:
                            if checkSquareNumber(grid, mousePos) is not None:
                                if not containPiece(grid, [convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0], convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]]):  # check if the square already contains something
                                    grid.gridArray[convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0]][convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]] = x  # put the piece into the square
                                    xTurn = False  # let the other person go

        if playMenu.play2Player:    # 2 player
            for event in pygame.event.get():
                # exit
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseClicked = True

                    if checkSquareNumber(grid, mousePos) is not None:
                        if xTurn:
                            if not containPiece(grid, [convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0], convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]]):    # check if the square already contains something
                                grid.gridArray[convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0]][convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]] = x      # put the piece into the square
                                xTurn = False   # let the other person go
                        elif not xTurn:
                            if not containPiece(grid, [convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0], convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]]):    # check if the square already contains something
                                grid.gridArray[convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[0]][convertMousePosToGridPos(checkSquareNumber(grid, mousePos))[1]] = o      # put the piece into the square
                                xTurn = True    # let the other person go
        # load the pieces
        loadPieces(display, grid, x)
        loadPieces(display, grid, o)

        # check who won or if it was a tie
        if checkWin(grid, x):
            grid.drawLine(display, grid, 12, x, o, xColor, oColor)
            pygame.display.update()
            pygame.time.delay(1500)

            clearGridArray(grid)
            xScore += 1
            winner = x
            xTurn = True
            startGame = False
        elif checkWin(grid, o):
            grid.drawLine(display, grid, 12, x, o, xColor, oColor)
            pygame.display.update()
            pygame.time.delay(1500)

            oScore += 1
            winner = o
            xTurn = True
            clearGridArray(grid)
            startGame = False
        elif checkTie(grid):
            pygame.display.update()
            pygame.time.delay(1500)

            winner = None
            clearGridArray(grid)
            xTurn = True
            startGame = False

        mouseClicked = False

        pygame.display.update()
        pygame.time.delay(1)
