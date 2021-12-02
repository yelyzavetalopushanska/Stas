from random import choice

def print_field(field):
    # печатает поле
    for i in field:
        print(i)


def cell_input(player):
    # ввод номера ячейки
    return input(f"Ход {player}, введите число: ")


def valid(cell_move, player, field, fill_field):
    # проверка валидности ячейки
    state = False
    for i in range(len(field)):
        for j in range(len(field)):
            if cell_move == field[i][j] and cell_move != 'X' and cell_move != 'O':
                # присваиваем ячейке крестик или нолик
                field[i][j] = player
                fill_field.remove(cell_move)
                state = True
    return state


def bot_move(field, fill_field, player='O'):
    move = choice(fill_field)
    fill_field.remove(move)

    for i in range(len(field)):
        for j in range(len(field)):
            if move == field[i][j]:
                field[i][j] = player


def _horizontal_win(player, field):
    for i in range(len(field)):
        if field[i].count(player) == len(field):
            return True


def _vertical_win(player, field):
    for i in range(len(field)):
        vertical = []
        for j in range(len(field)):
            vertical.append(field[j][i])
        if vertical.count(player) == len(field):
            return True


def _left_diagonal_win(player, field):
    state = True
    for i in range(len(field)):
        if field[i][i] != player:
            state = False
    return state


def _right_diagonal(player, field):
    state = True
    for i in range(len(field)):
        if field[i][len(field) - 1 - i] != player:
            state = False
    return state


def winner(player, field):
    return _horizontal_win(player, field) \
           or _vertical_win(player, field) \
           or _left_diagonal_win(player, field) \
           or _right_diagonal(player, field)
