import pygame as pg
from constants import *


def init_game():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Хрестики-Нулики")
    return screen, pg.time.Clock()


def draw_grid(screen):
    screen.fill(WHITE)
    for i in range(1, BOARD_SIZE):
        pg.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 3)
    for i in range(1, BOARD_SIZE):
        pg.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 3)


def draw_moves(screen, board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            center_x = col * CELL_SIZE + CELL_SIZE // 2
            center_y = row * CELL_SIZE + CELL_SIZE // 2
            radius = CELL_SIZE // 3

            if board[row][col] == 'X':
                pg.draw.line(screen, X_COLOR, (center_x - radius, center_y - radius),
                             (center_x + radius, center_y + radius), 5)
                pg.draw.line(screen, X_COLOR, (center_x - radius, center_y + radius),
                             (center_x + radius, center_y - radius), 5)
            elif board[row][col] == 'O':
                pg.draw.circle(screen, O_COLOR, (center_x, center_y), radius, 5)