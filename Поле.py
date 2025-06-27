import pygame as pg
import sys

width, height = 400, 400
board_size = 3
cell_size = width // board_size

white = (255, 255, 255)
line_color = (50, 50, 50)

def draw_grid():
    screen.fill(white)
    pg.draw.line(screen, line_color, (cell_size, 0), (cell_size, height), 3)
    pg.draw.line(screen, line_color, (2*cell_size, 0), (2*cell_size, height), 3)
    pg.draw.line(screen, line_color, (0, cell_size), (width, cell_size), 3)
    pg.draw.line(screen, line_color, (0, 2*cell_size), (width, 2*cell_size), 3)

pg.init()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Хрестики-Нулики")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    draw_grid()
    pg.display.flip()
pg.quit()
sys.exit()