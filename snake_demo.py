import pygame, sys, random

# khai bao cac bien
# kich thuoc cua so
FRAME_WIDTH = 600
FRAME_HEIGHT = 600

# kich thuoc 1 o
GRID_SIZE = 20
GRID_WIDTH = FRAME_WIDTH // GRID_SIZE
GRID_HEIGHT = FRAME_HEIGHT // GRID_SIZE

# huong di cua ran
UP = (0, -1)
DOWN = (0, 1)
RIGHT = (-1, 0)
LEFT = (1, 0)

# 3 mau co ban
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
# ve khung hinh
def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*GRID_SIZE, y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x*GRID_SIZE, y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (84, 194, 205), rr)
             

# ham main
def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((FRAME_WIDTH, FRAME_HEIGHT))
    surface = pygame.Surface(screen.get_size())
    pygame.display.update() 
    drawGrid(surface)
    game_over = False
    while(not game_over):
        clock.tick(10)
        drawGrid(surface)
        for event in pygame.event.get():
            print(event)  
            if event.type == pygame.QUIT:
                game_over = True
    pygame.quit()
    quit()
main()
        