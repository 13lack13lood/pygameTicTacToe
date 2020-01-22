# **********************************************************************************
# Program Author: Harry, Justin
# Revision Date: January 17, 2020
# Program Name: Tic Tac Toe
# Description: A Tic Tac Toe game you can play against the computer or with your friends.
# There are two levels of difficulty which are easy and impossible. On easy mode, the computer
# goes randomly while on impossible mode, an algorithm is used.
# This file is where all the classes are stored.
# *********************************************************************************

# import libraries
import pygame


class Grid:
    def __init__(self, gridColor, gridSquareSize, gridLineSize, gridXPos, gridYPos, gridArray):
        self.gridColor = gridColor
        self.gridSquareSize = gridSquareSize
        self.gridLineSize = gridLineSize
        self.GRID_WIDTH = (3 * gridSquareSize) + (2 * gridLineSize)
        self.gridXPos = gridXPos    # top left corner
        self.gridYPos = gridYPos
        self.gridArray = gridArray

    def loadGrid(self, display):
        pygame.draw.rect(display, self.gridColor, pygame.Rect((self.gridXPos + self.gridSquareSize, self.gridYPos), (self.gridLineSize, self.GRID_WIDTH)))
        pygame.draw.rect(display, self.gridColor, pygame.Rect((self.gridXPos + (2 * self.gridSquareSize) + self.gridLineSize, self.gridYPos), (self.gridLineSize, self.GRID_WIDTH)))
        pygame.draw.rect(display, self.gridColor, pygame.Rect((self.gridXPos, self.gridYPos + self.gridSquareSize), (self.GRID_WIDTH, self.gridLineSize)))
        pygame.draw.rect(display, self.gridColor, pygame.Rect((self.gridXPos, self.gridYPos + (2 * self.gridSquareSize) + self.gridLineSize), (self.GRID_WIDTH, self.gridLineSize)))

    def drawLine(self, display, grid, lineWidth, x, o, xColor, oColor):
        # horizontal win
        for i in range(3):
            if grid.gridArray[i][0] == x and grid.gridArray[i][1] == x and grid.gridArray[i][2] == x:
                linePosX1 = self.gridXPos
                linePosX2 = self.gridXPos + self.GRID_WIDTH
                linePosY = self.gridYPos + (i * self.gridSquareSize) + (i * self.gridLineSize) + (self.gridSquareSize / 2)

                pygame.draw.line(display, xColor, (linePosX1, linePosY), (linePosX2, linePosY), lineWidth)
            if grid.gridArray[i][0] == o and grid.gridArray[i][1] == o and grid.gridArray[i][2] == o:
                linePosX1 = self.gridXPos
                linePosX2 = self.gridXPos + self.GRID_WIDTH
                linePosY = self.gridYPos + (i * self.gridSquareSize) + (i * self.gridLineSize) + (self.gridSquareSize / 2)

                pygame.draw.line(display, oColor, (linePosX1, linePosY), (linePosX2, linePosY), lineWidth)

        # vertical win
        for i in range(3):
            if grid.gridArray[0][i] == x and grid.gridArray[1][i] == x and grid.gridArray[2][i] == x:
                linePosX = self.gridXPos + (i * self.gridSquareSize) + (i * self.gridLineSize) + (self.gridSquareSize / 2)
                linePosY1 = self.gridYPos
                linePosY2 = self.gridYPos + self.GRID_WIDTH

                pygame.draw.line(display, xColor, (linePosX, linePosY1), (linePosX, linePosY2), lineWidth)
            if grid.gridArray[0][i] == o and grid.gridArray[1][i] == o and grid.gridArray[2][i] == o:
                linePosX = self.gridXPos + (i * self.gridSquareSize) + (i * self.gridLineSize) + (self.gridSquareSize / 2)
                linePosY1 = self.gridYPos
                linePosY2 = self.gridYPos + self.GRID_WIDTH

                pygame.draw.line(display, oColor, (linePosX, linePosY1), (linePosX, linePosY2), lineWidth)

        # diagonal win:
        if grid.gridArray[0][0] == x and grid.gridArray[1][1] == x and grid.gridArray[2][2] == x:
            linePosX1 = self.gridXPos + 20
            linePosY1 = self.gridYPos + 20
            linePosX2 = self.gridXPos + self.GRID_WIDTH - 20
            linePosY2 = self.gridYPos + self.GRID_WIDTH - 20

            pygame.draw.line(display, xColor, (linePosX1, linePosY1), (linePosX2, linePosY2), lineWidth)
        if grid.gridArray[2][0] == x and grid.gridArray[1][1] == x and grid.gridArray[0][2] == x:
            linePosX1 = self.gridXPos + 20
            linePosY1 = self.gridYPos + self.GRID_WIDTH - 20
            linePosX2 = self.gridXPos + self.GRID_WIDTH - 20
            linePosY2 = self.gridYPos + 20

            pygame.draw.line(display, xColor, (linePosX1, linePosY1), (linePosX2, linePosY2), lineWidth)
        if grid.gridArray[0][0] == o and grid.gridArray[1][1] == o and grid.gridArray[2][2] == o:
            linePosX1 = self.gridXPos + 20
            linePosY1 = self.gridYPos + 20
            linePosX2 = self.gridXPos + self.GRID_WIDTH - 20
            linePosY2 = self.gridYPos + self.GRID_WIDTH - 20

            pygame.draw.line(display, oColor, (linePosX1, linePosY1), (linePosX2, linePosY2), lineWidth)
        if grid.gridArray[2][0] == o and grid.gridArray[1][1] == o and grid.gridArray[0][2] == o:
            linePosX1 = self.gridXPos + 20
            linePosY1 = self.gridYPos + self.GRID_WIDTH - 20
            linePosX2 = self.gridXPos + self.GRID_WIDTH - 20
            linePosY2 = self.gridYPos + 20

            pygame.draw.line(display, oColor, (linePosX1, linePosY1), (linePosX2, linePosY2), lineWidth)


class X:
    def __init__(self, color, width, lineWidth):
        self.color = color
        self.width = width
        self.lineWidth = lineWidth

    # draw the X
    def draw(self, display, grid, square):
        if square == 1 or square == 4 or square == 7:
            xPos1 = grid.gridXPos + (grid.gridSquareSize - self.width) / 2
            xPos2 = grid.gridXPos + grid.gridSquareSize - (grid.gridSquareSize - self.width) / 2

            if square == 1:
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + grid.gridSquareSize - (grid.gridSquareSize - self.width) / 2), self.lineWidth)
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + grid.gridSquareSize - (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + (grid.gridSquareSize - self.width) / 2), self.lineWidth)
            elif square == 4:
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + grid.gridSquareSize + grid.gridLineSize + (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + (2 * grid.gridSquareSize) + grid.gridLineSize - (grid.gridSquareSize - self.width) / 2), self.lineWidth)
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + (2 * grid.gridSquareSize) + grid.gridLineSize - (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + grid.gridSquareSize + grid.gridLineSize + (grid.gridSquareSize - self.width) / 2), self.lineWidth)
            elif square == 7:
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + (2 * grid.gridSquareSize) + (2 * grid.gridLineSize) + (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + grid.GRID_WIDTH - (grid.gridSquareSize - self.width) / 2), self.lineWidth)
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + grid.GRID_WIDTH - (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + (2 * grid.gridSquareSize) + (2 * grid.gridLineSize) + (grid.gridSquareSize - self.width) / 2), self.lineWidth)

        if square == 2 or square == 5 or square == 8:
            xPos1 = grid.gridXPos + grid.gridSquareSize + grid.gridLineSize + (grid.gridSquareSize - self.width) / 2
            xPos2 = grid.gridXPos + (2 * grid.gridSquareSize) + grid.gridLineSize - (grid.gridSquareSize - self.width) / 2

            if square == 2:
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + grid.gridSquareSize - (grid.gridSquareSize - self.width) / 2), self.lineWidth)
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + grid.gridSquareSize - (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + (grid.gridSquareSize - self.width) / 2), self.lineWidth)
            elif square == 5:
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + grid.gridSquareSize + grid.gridLineSize + (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + (2 * grid.gridSquareSize) + grid.gridLineSize - (grid.gridSquareSize - self.width) / 2), self.lineWidth)
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + (2 * grid.gridSquareSize) + grid.gridLineSize - (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + grid.gridSquareSize + grid.gridLineSize + (grid.gridSquareSize - self.width) / 2), self.lineWidth)
            elif square == 8:
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + (2 * grid.gridSquareSize) + (2 * grid.gridLineSize) + (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + grid.GRID_WIDTH - (grid.gridSquareSize - self.width) / 2), self.lineWidth)
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + grid.GRID_WIDTH - (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + (2 * grid.gridSquareSize) + (2 * grid.gridLineSize) + (grid.gridSquareSize - self.width) / 2), self.lineWidth)

        if square == 3 or square == 6 or square == 9:
            xPos1 = grid.gridXPos + grid.GRID_WIDTH - (grid.gridSquareSize - self.width) / 2
            xPos2 = grid.gridXPos + grid.GRID_WIDTH - grid.gridSquareSize + (grid.gridSquareSize - self.width) / 2

            if square == 3:
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + grid.gridSquareSize - (grid.gridSquareSize - self.width) / 2), self.lineWidth)
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + grid.gridSquareSize - (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + (grid.gridSquareSize - self.width) / 2), self.lineWidth)
            elif square == 6:
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + grid.gridSquareSize + grid.gridLineSize + (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + (2 * grid.gridSquareSize) + grid.gridLineSize - (grid.gridSquareSize - self.width) / 2), self.lineWidth)
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + (2 * grid.gridSquareSize) + grid.gridLineSize - (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + grid.gridSquareSize + grid.gridLineSize + (grid.gridSquareSize - self.width) / 2), self.lineWidth)
            elif square == 9:
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + (2 * grid.gridSquareSize) + (2 * grid.gridLineSize) + (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + grid.GRID_WIDTH - (grid.gridSquareSize - self.width) / 2), self.lineWidth)
                pygame.draw.line(display, self.color, (xPos1, grid.gridYPos + grid.GRID_WIDTH - (grid.gridSquareSize - self.width) / 2), (xPos2, grid.gridYPos + (2 * grid.gridSquareSize) + (2 * grid.gridLineSize) + (grid.gridSquareSize - self.width) / 2), self.lineWidth)


class O:
    def __init__(self, color, radius, lineWidth):
        self.color = color
        self.radius = radius
        self.lineWidth = lineWidth

    def draw(self, display, grid, square):
        if square == 1 or square == 4 or square == 7:
            xPos = int(grid.gridXPos + (grid.gridSquareSize / 2))

            if square == 1:
                pygame.draw.circle(display, self.color, (xPos, int(int(grid.gridYPos + (grid.gridSquareSize / 2)))), self.radius, self.lineWidth)
            elif square == 4:
                pygame.draw.circle(display, self.color, (xPos, int(grid.gridYPos + (grid.GRID_WIDTH / 2))), self.radius, self.lineWidth)
            elif square == 7:
                pygame.draw.circle(display, self.color, (xPos, int(grid.gridYPos + grid.GRID_WIDTH - (grid.gridSquareSize / 2))), self.radius, self.lineWidth)

        if square == 2 or square == 5 or square == 8:
            xPos = int(grid.gridXPos + (grid.GRID_WIDTH / 2))

            if square == 2:
                pygame.draw.circle(display, self.color, (xPos, int(grid.gridYPos + (grid.gridSquareSize / 2))), self.radius, self.lineWidth)
            elif square == 5:
                pygame.draw.circle(display, self.color, (xPos, int(grid.gridYPos + (grid.GRID_WIDTH / 2))), self.radius, self.lineWidth)
            elif square == 8:
                pygame.draw.circle(display, self.color, (xPos, int(grid.gridYPos + grid.GRID_WIDTH - (grid.gridSquareSize / 2))), self.radius, self.lineWidth)

        if square == 3 or square == 6 or square == 9:
            xPos = int(grid.gridXPos + grid.GRID_WIDTH - (grid.gridSquareSize / 2))

            if square == 3:
                pygame.draw.circle(display, self.color, (xPos, int(grid.gridYPos + (grid.gridSquareSize / 2))), self.radius, self.lineWidth)
            elif square == 6:
                pygame.draw.circle(display, self.color, (xPos, int(grid.gridYPos + (grid.GRID_WIDTH / 2))), self.radius, self.lineWidth)
            elif square == 9:
                pygame.draw.circle(display, self.color, (xPos, int(grid.gridYPos + grid.GRID_WIDTH - (grid.gridSquareSize / 2))), self.radius, self.lineWidth)


class Button:   # make a button
    def __init__(self, color, x, y, width, height, text='', textColor=None, textSize=0):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textColor = textColor
        self.textSize = textSize

    def draw(self, display, outline=None):  # draw button
        if outline:  # draw outline
            pygame.draw.rect(display, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':     # draw text on it
            font = pygame.font.SysFont('Verdana', self.textSize)
            text = font.render(self.text, 1, self.textColor)
            display.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


class InstructionsMenu:     # instructions menu
    def __init__(self, titleFont, instructionsFont, fontColor, buttonArray, menuClicked=False, menuBack=False):
        self.titleFont = titleFont
        self.instructionsFont = instructionsFont
        self.fontColor = fontColor
        self.buttonArray = buttonArray
        self.menuClicked = menuClicked
        self.menuBack = menuBack

    def drawMenu(self, display, background, mouseClicked, mousePos):
        display.fill(background)
        display.blit(self.titleFont.render("INSTRUCTIONS".encode("utf-8"), True, self.fontColor), (200, 36))
        display.blit(self.instructionsFont.render("Click on a square to put the piece in it.".encode("utf-8"), True, self.fontColor), (50, 100))
        display.blit(self.instructionsFont.render("There is a winner once there is 3 of one piece in a line.".encode("utf-8"), True, self.fontColor), (50, 140))
        display.blit(self.instructionsFont.render("There is a tie if no one wins.".encode("utf-8"), True, self.fontColor), (50, 180))
        display.blit(self.instructionsFont.render("There are 2 levels of difficulty:".encode("utf-8"), True, self.fontColor), (50, 220))
        display.blit(self.instructionsFont.render("     Easy - Where the computer goes randomly".encode("utf-8"), True, self.fontColor), (50, 260))
        display.blit(self.instructionsFont.render("     Impossible - Where you will be facing an algorithm".encode("utf-8"), True, self.fontColor), (50, 300))
        display.blit(self.instructionsFont.render("You can also play the 2 player mode with someone else.".encode("utf-8"), True, self.fontColor), (50, 340))

        for i in range(len(self.buttonArray)):  # load all buttons
            if i > 0:
                if self.buttonArray[i].isOver(mousePos):
                    self.buttonArray[i].draw(display, 10)
                else:
                    self.buttonArray[i].draw(display)

        if self.menuBack:
            self.backButton()
        elif mouseClicked and self.buttonArray[len(self.buttonArray) - 1].isOver(mousePos):
            self.menuBack = True

    def isClicked(self, mousePos):
        if self.buttonArray[0].isOver(mousePos):
            return True
        return False

    def backButton(self):
        self.menuClicked = False
        self.menuBack = False


class PlayMenu:
    def __init__(self, font, fontColor, buttonArray, menuClicked=False, playEasy=False, playImpossible=False, play2Player=False, menuBack=False):
        self.font = font
        self.fontColor = fontColor
        self.buttonArray = buttonArray
        self.menuClicked = menuClicked
        self.playEasy = playEasy
        self.playImpossible = playImpossible
        self.play2Player = play2Player
        self.menuBack = menuBack

    def drawMenu(self, display, background, mouseClicked, mousePos):
        display.fill(background)
        display.blit(self.font.render("PLAY".encode("utf-8"), True, self.fontColor), (228, 35))

        for i in range(len(self.buttonArray)):  # load all buttons
            if i > 0:
                if self.buttonArray[i].isOver(mousePos):
                    self.buttonArray[i].draw(display, 10)
                else:
                    self.buttonArray[i].draw(display)

        if mouseClicked and self.buttonArray[1].isOver(mousePos):
            self.playEasy = True
            self.menuClicked = False

        if mouseClicked and self.buttonArray[2].isOver(mousePos):
            self.playImpossible = True
            self.menuClicked = False

        if mouseClicked and self.buttonArray[3].isOver(mousePos):
            self.play2Player = True
            self.menuClicked = False

        if self.menuBack:
            self.backButton()
        elif mouseClicked and self.buttonArray[len(self.buttonArray) - 1].isOver(mousePos):
            self.menuBack = True

    def isClicked(self, mousePos):
        if self.buttonArray[0].isOver(mousePos):
            return True
        return False

    def backButton(self):
        self.menuClicked = False
        self.menuBack = False


class ChosePieceMenu:
    def __init__(self, font, fontColor, buttonArray, playMenu, x, o, pickedPiece=None, menuClicked=False, menuBack=False):
        self.font = font
        self.fontColor = fontColor
        self.buttonArray = buttonArray
        self.playMenu = playMenu
        self.x = x
        self.o = o
        self.pickedPiece = pickedPiece
        self.menuClicked = menuClicked
        self.menuBack = menuBack

    def drawMenu(self, display, background, mouseClicked, mousePos):
        display.fill(background)
        display.blit(self.font.render("Pick Side".encode("utf-8"), True, self.fontColor), (175, 50))

        for i in range(len(self.buttonArray)):  # load all buttons
            if self.buttonArray[i].isOver(mousePos):
                self.buttonArray[i].draw(display, 10)
            else:
                self.buttonArray[i].draw(display)

        if mouseClicked and self.buttonArray[0].isOver(mousePos):
            self.pickedPiece = self.x
            self.menuClicked = False

        if mouseClicked and self.buttonArray[1].isOver(mousePos):
            self.pickedPiece = self.o
            self.menuClicked = False

        if self.menuBack:
            self.backButton()
        elif mouseClicked and self.buttonArray[len(self.buttonArray) - 1].isOver(mousePos):
            self.menuBack = True

    def isClicked(self, mousePos):
        if self.buttonArray[0].isOver(mousePos):
            return True
        return False

    def backButton(self):
        self.menuClicked = False
        self.menuBack = False


class EndGame:
    def __init__(self, font, fontColor, buttonArray, winX, winO, tieX, tieO, winner=0, restartGame=False, mainMenu=False):
        self.font = font
        self.fontColor = fontColor
        self.buttonArray = buttonArray
        self.winX = winX
        self.winO = winO
        self.tieX = tieX
        self.tieO = tieO
        self.winner = winner
        self.restartGame = restartGame
        self.mainMenu = mainMenu

    def drawMenu(self, display, grid, mouseClicked, mousePos):
        # draw the end screens
        if type(self.winner) == X:  # x win
            self.winX.draw(display, grid, 2)
            display.blit(self.font.render("Winner!".encode("utf-8"), True, self.fontColor), (207, 400))

        if type(self.winner) == O:  # o win
            self.winO.draw(display, grid, 2)
            display.blit(self.font.render("Winner!".encode("utf-8"), True, self.fontColor), (207, 400))

        if self.winner is None:  # tie
            self.tieX.draw(display, grid, 1)
            self.tieO.draw(display, grid, 3)
            display.blit(self.font.render("Tie!".encode("utf-8"), True, self.fontColor), (253, 400))

        for i in range(len(self.buttonArray)):  # load all buttons
            if self.buttonArray[i].isOver(mousePos):
                self.buttonArray[i].draw(display, 10)
            else:
                self.buttonArray[i].draw(display)

        if mouseClicked and self.buttonArray[0].isOver(mousePos):
            self.restartGame = True

        if mouseClicked and self.buttonArray[len(self.buttonArray) - 1].isOver(mousePos):
            self.mainMenu = True


class ExitButton:   # button for exiting the game in the main menu
    def __init__(self, button, menuClicked=False):
        self.button = button
        self.menuClicked = menuClicked

    def isClicked(self, mousePos):
        if self.button.isOver(mousePos):
            return True
        return False
