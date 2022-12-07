import pygame
from cell import Cell

class Game:
    WIDTH, HEIGHT = 900, 700
    FPS = 60
    #grid = []

    def __init__(self):
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Conway's Game Of Life")

        self.WIN.fill((158, 158, 158))
        self.init_grid(30)
        self.main_loop()
    
    def main_loop(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(self.FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            pygame.display.update()
        
        pygame.quit()

    def init_grid(self, size):
        grid = []
        border = 1
        cellSize = 20

        for i in range(size):
            column = []
            grid.append(column)
            for j in range(size):
                xPos = border + i * cellSize + i * border
                yPos = border + j * cellSize + j * border
                column.append(Cell(self.WIN, xPos, yPos, cellSize))
    