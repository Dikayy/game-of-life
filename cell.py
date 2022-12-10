import pygame

class Cell:
    alive = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, WIN, xPos, yPos, xGridPos, yGridPos, size):
        self.WIN = WIN
        self.xPos = xPos
        self.yPos = yPos
        self.xGridPos = xGridPos
        self.yGridPos = yGridPos
        self.size = size

        self.rect = pygame.Rect(self.xPos, self.yPos, self.size, self.size)
        pygame.draw.rect(self.WIN, self.WHITE, self.rect)

    def get_neighbours(self, grid):
        neighbours = 0
        for x in range(self.xGridPos - 1, self.xGridPos + 2):
            for y in range(self.yGridPos - 1, self.yGridPos + 2):
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]):
                    cell = grid[x][y]
                    if cell != self and cell.alive:
                        neighbours += 1

        return neighbours

    def is_in_pos(self, pos):
        return self.rect.collidepoint(pos)
    
    def set_alive(self, alive):
        if alive:
            pygame.draw.rect(self.WIN, self.BLACK, self.rect)
        else:
            pygame.draw.rect(self.WIN, self.WHITE, self.rect)
        
        self.alive = alive
    