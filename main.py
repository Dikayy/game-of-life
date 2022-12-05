import pygame

WIDTH, HEIGHT = 900, 700
FPS = 60
#grid = []

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game Of Life")

class Cell:
    alive = False

    def __init__(self, xPos, yPos, size):
        self.xPos = xPos
        self.yPos = yPos
        self.size = size

        rect = pygame.Rect(self.xPos, self.yPos, self.size, self.size)
        pygame.draw.rect(WIN, (255, 255, 255), rect)
        

def init_grid(size):
    grid = []
    border = 1
    cellSize = 20

    for i in range(size):
        column = []
        grid.append(column)
        for j in range(size):
            xPos = border + i * cellSize + i * border
            yPos = border + j * cellSize + j * border
            column.append(Cell(xPos, yPos, cellSize))

def main():
    clock = pygame.time.Clock()

    WIN.fill((158, 158, 158))
    init_grid(30)

    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
