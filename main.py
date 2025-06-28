import pygame as pg
from board import init_game, draw_grid, draw_moves
from interface import handle_events, show_result


def main():
    screen, clock = init_game()
    board = [[None for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False
    winner = None

    running = True
    while running:
        running, board, current_player, game_over, winner = handle_events(
            board, current_player, game_over)

        draw_grid(screen)
        draw_moves(screen, board)

        if game_over:
            show_result(screen, game_over, winner)
            pg.display.flip()
            pg.time.wait(3000)
            running = False

        pg.display.flip()
        clock.tick(60)

    pg.quit()
if __name__ == "__main__":
    main()