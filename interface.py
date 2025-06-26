def handle_events():
    global current_player, game_over, winner

    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False

        if not game_over and event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            col, row = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE

            if board[row][col] is None:
                board[row][col] = current_player
                winner = check_winner()
                if winner:
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
    return True


def show_result():
    if game_over:
        font = pg.font.Font(None, 36)
        if winner == 'нічия':
            text = font.render("Нічия!", True, BLACK)
        else:
            text = font.render(f"Переможець: {winner}!", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))
