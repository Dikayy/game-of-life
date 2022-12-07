import pygame

class Cell:
    alive = False
    WHITE = (255, 255, 255)

    def __init__(self, WIN, xPos, yPos, size):
        #self.WIN = WIN
        self.xPos = xPos
        self.yPos = yPos
        self.size = size

        rect = pygame.Rect(self.xPos, self.yPos, self.size, self.size)
        pygame.draw.rect(WIN, self.WHITE, rect)
