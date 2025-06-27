import pygame as pg
import sys

width, height = 400, 400
board_size = 3
cell_size = width // board_size

white = (255, 255, 255)
line_color = (50, 50, 50)
X_COLOR = (200, 0, 0)  
O_COLOR = (0, 0, 200)  

def draw_grid():
    screen.fill(white)
    pg.draw.line(screen, line_color, (cell_size, 0), (cell_size, height), 3)
    pg.draw.line(screen, line_color, (2*cell_size, 0), (2*cell_size, height), 3)
    pg.draw.line(screen, line_color, (0, cell_size), (width, cell_size), 3)
    pg.draw.line(screen, line_color, (0, 2*cell_size), (width, 2*cell_size), 3)

pg.init()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Хрестики-Нулики")
board = [['' for _ in range(board_size)] for _ in range(board_size)]
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
def draw_moves():
    for row in range(board_size):
        for col in range(board_size):
            center_x = col * cell_size + cell_size // 2
            center_y = row * cell_size + cell_size // 2
            radius = cell_size // 3
            
            if board[row][col] == 'X':
                pg.draw.line(screen, X_COLOR, (center_x - radius, center_y - radius),
                            (center_x + radius, center_y + radius), 5)
                pg.draw.line(screen, X_COLOR, (center_x - radius, center_y + radius),
                            (center_x + radius, center_y - radius), 5)
            elif board[row][col] == 'O':
                pg.draw.circle(screen, O_COLOR, (center_x, center_y), radius, 3)

    draw_grid()
    pg.display.flip()
pg.quit()
sys.exit()