import random

import numpy as np


def create_field(n):
    return np.ones((n, n), dtype=str)


def choice_position(field_shape: tuple):
    row = random.choice(range(0, field_shape[0]))
    col = random.choice(range(0, field_shape[1]))
    return row, col


def choice_bombs(n, field_shape: tuple):
    bombs = set()
    while len(bombs) < n:
        row, col = choice_position(field_shape)
        bombs.add((row, col))
    return bombs


def set_in_position(field: np.array, position: tuple, val: str):
    field[position[0], position[1]] = val


def setup_bombs(field, choosen_bombs: set):
    # TODO: find a matrix solution for setting up bombs ([] * [])
    for tup in choosen_bombs:
        set_in_position(field, tup, 'B')
    return field


def check_attack_is_on_bomb(bombs: set, attack: tuple):
    if attack in bombs:
        return True
    return False


def make_attack(field_shape: tuple, bombs: set):
    attack_is_on_bomb = True
    while attack_is_on_bomb:
        row, col = choice_position(field_shape)
        attack = (row, col)
        attack_is_on_bomb = check_attack_is_on_bomb(bombs, attack)
    return attack


def find_neighbours(field_shape: tuple, attack: tuple, neighbourhood=2):
    row, col = attack
    neighbours = []
    # TODO: find a better way to find neighbours ---> maybe we should make 2*2 matrix in attack position
    for c in range(0, neighbourhood + 1):
        col_left = col - c
        col_right = col + c
        for r in range(0, neighbourhood + 1):
            row_up = row + r
            row_down = row - r
            for neighbour in [
                (row_up, col_left),
                (row_down, col_left),
                (row_up, col_right),
                (row_down, col_right)
            ]:
                n_row, n_col = neighbour
                if n_row in range(0, field_shape[0]) and n_col in range(0, field_shape[1]):
                    neighbours.append(neighbour)
    return neighbours


def make_calculations(attack, neighbours, field):
    # setting attack on its position
    set_in_position(field, attack, 'A')
    for neighbour in neighbours:
        if field[neighbour[0], neighbour[1]] == 'B':
            set_in_position(field, neighbour, 'X')
        elif field[neighbour[0], neighbour[1]] == '1':
            set_in_position(field, neighbour, '0')
    return field


