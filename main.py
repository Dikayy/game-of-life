import pygame

WIDTH, HEIGHT = 900, 500
FPS = 60

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
    pass

def main():
    clock = pygame.time.Clock()

    cell = Cell(100, 100, 10)

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
