import pygame as pg
import sys
Width, height = 400, 400
Board_size = 3 
Cell_size = Width // Board_size 
white = (255, 255, 255) 
Black = (0, 0, 0)        
Line_color = (50, 50, 50) 
pg.init()
screen = pg.display.set_mode((Width, height))
pg.display.set_caption("Хрестики-Нулики")
def draw_grid():
    screen.fill(white)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    draw_grid()
    pg.display.flip()
pg.quit()
sys.exit()