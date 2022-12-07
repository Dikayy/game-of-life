import pygame

class Cell:
    alive = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, WIN, xPos, yPos, size):
        self.WIN = WIN
        self.xPos = xPos
        self.yPos = yPos
        self.size = size

        self.rect = pygame.Rect(self.xPos, self.yPos, self.size, self.size)
        pygame.draw.rect(self.WIN, self.WHITE, self.rect)

    def is_in_pos(self, pos):
        return self.rect.collidepoint(pos)
    
    def set_alive(self, alive):
        if alive:
            pygame.draw.rect(self.WIN, self.BLACK, self.rect)
        else:
            pygame.draw.rect(self.WIN, self.WHITE, self.rect)
        
        self.alive = alive
    