import pygame as pg
import sys
WIDTH, HEIGHT = 400, 400
BOARD_SIZE = 3 
CELL_SIZE = WIDTH // BOARD_SIZE 
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)        
LINE_COLOR = (50, 50, 50) 
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Хрестики-Нулики")
def draw_grid():
    screen.fill(WHITE)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    draw_grid()
    pg.display.flip()
pg.quit()
sys.exit()