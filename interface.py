import pygame as pg
from constants import *
from logic import check_winner


def handle_events(board, current_player, game_over):
    winner = None
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False, board, current_player, game_over, None

        if not game_over and event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            col = mouse_x // CELL_SIZE
            row = mouse_y // CELL_SIZE

            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] is None:
                board[row][col] = current_player
                winner = check_winner(board)
                if winner:
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    return True, board, current_player, game_over, winner


def show_result(screen, game_over, winner):
    if game_over and winner:
        font = pg.font.Font(None, 48)
        if winner == 'нічия':
            text = font.render("Нічия!", True, BLACK)
        else:
            text = font.render(f"Перемога {winner}!", True, BLACK)

        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        pg.draw.rect(screen, WHITE, text_rect.inflate(20, 20))
        screen.blit(text, text_rect)