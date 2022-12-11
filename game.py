import pygame
from cell import Cell

class Game:
    WIDTH, HEIGHT = 1051, 1051
    FPS = 60
    simRunning = False
    stepTime = 120

    def __init__(self):
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Conway's Game Of Life")

        self.WIN.fill((158, 158, 158))
        self.grid = self.init_grid(50)
        self.main_loop()

    def next_step(self):
        nextGrid = []
        for column in self.grid:
            nextGridColumn = []
            nextGrid.append(nextGridColumn)
            for cell in column:
                neighbours = cell.get_neighbours(self.grid)
                if not cell.alive and neighbours == 3:
                    nextGridColumn.append(True)
                elif cell.alive and neighbours < 2:
                    nextGridColumn.append(False)
                elif cell.alive and (neighbours == 2 or neighbours == 3):
                    nextGridColumn.append(True)
                elif cell.alive and neighbours > 3:
                    nextGridColumn.append(False)
                else:
                    nextGridColumn.append(False)
        
        x = 0
        for column in self.grid:
            y = 0
            for cell in column:
                cell.set_alive(nextGrid[x][y])
                y += 1
            
            x += 1

    def set_sim_running(self):
        nextStepEvent = pygame.event.Event(pygame.USEREVENT + 0)
        if not self.simRunning:
            pygame.time.set_timer(nextStepEvent, self.stepTime)
            self.simRunning = True
        else:
            pygame.time.set_timer(nextStepEvent, 0)
            self.simRunning = False

    def click_cell(self, pos):
        for column in self.grid:
            for cell in column:
                if cell.is_in_pos(pos):
                    alive = cell.alive
                    cell.set_alive(not alive)

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
                column.append(Cell(self.WIN, xPos, yPos, i, j, cellSize))
        
        return grid
    
    def main_loop(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(self.FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.click_cell(pygame.mouse.get_pos())
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.set_sim_running()
                elif event.type == pygame.USEREVENT + 0:
                    self.next_step()
            
            pygame.display.update()
        
        pygame.quit()
