from .direction import Direction


def execute(matrix, direction):
    """
    Execute movement on the matrix based on the specified direction.

    Args:
        matrix (list): 2D list representing the game board.
        direction (Direction): Direction of movement (LEFT, UP, RIGHT, DOWN).

    Returns:
        list: Modified matrix after movement.
    """
    if direction == Direction.LEFT:
        changed = True
        while changed:
            matrix, changed = __move_left(matrix)
        matrix, changed = __merge_left(matrix)
        while changed:
            matrix, changed = __move_left(matrix)
    elif direction == Direction.UP:
        changed = True
        while changed:
            matrix, changed = __move_up(matrix)
        matrix, changed = __merge_up(matrix)
        while changed:
            matrix, changed = __move_up(matrix)
    elif direction == Direction.RIGHT:
        changed = True
        while changed:
            matrix, changed = __move_right(matrix)
        matrix, changed = __merge_right(matrix)
        while changed:
            matrix, changed = __move_right(matrix)
    elif direction == Direction.DOWN:
        changed = True
        while changed:
            matrix, changed = __move_down(matrix)
        matrix, changed = __merge_down(matrix)
        while changed:
            matrix, changed = __move_down(matrix)
    else:
        # Errounious direction given.
        matrix = None
    return matrix

def __move_left(matrix):
    new_matrix = [[0]*4, [0]*4, [0]*4, [0]*4]
    changed = False
    for y in range(len(matrix[0:4])):
        for x, cell in enumerate(matrix[y]):
            if x == 0 or matrix[y][x] == 0:
                new_matrix[y][x] = cell
            else:
                previous = matrix[y][x-1]
                if previous == 0:
                    new_matrix[y][x-1] = cell
                    new_matrix[y][x] = 0
                    matrix[y][x-1] = cell
                    matrix[y][x] = 0
                    changed = True
                else:
                    new_matrix[y][x] = cell
    return new_matrix, changed

def __merge_left(matrix):
    new_matrix = [[0]*4, [0]*4, [0]*4, [0]*4]
    changed = False
    for y in range(len(matrix[0:4])):
        for x in range(len(matrix[y])):
            if x == 0 or matrix[y][x] == 0:
                new_matrix[y][x] = matrix[y][x]
            else:
                previous = matrix[y][x-1]
                if previous == matrix[y][x]:
                    new_matrix[y][x-1] = previous + matrix[y][x]
                    new_matrix[y][x] = 0
                    matrix[y][x-1] = matrix[y][x]
                    matrix[y][x] = 0
                    changed = True
                else:
                    new_matrix[y][x] = matrix[y][x]
    return new_matrix, changed

def __move_up(matrix):
    new_matrix = [[0]*4, [0]*4, [0]*4, [0]*4]
    changed = False
    for y in range(len(matrix[0:4])):
        for x in range(len(matrix[y])):
            if y == 0 or matrix[y][x] == 0:
                new_matrix[y][x] = matrix[y][x]
            else:
                previous = matrix[y-1][x]
                if previous == 0:
                    new_matrix[y-1][x] = matrix[y][x]
                    new_matrix[y][x] = 0
                    changed = True
                else:
                    new_matrix[y][x] = matrix[y][x]
    return new_matrix, changed

def __merge_up(matrix):
    new_matrix = [[0]*4, [0]*4, [0]*4, [0]*4]
    changed = False
    for y in range(len(matrix[0:4])):
        for x in range(len(matrix[y])):
            if y == 0 or matrix[y][x] == 0:
                new_matrix[y][x] = matrix[y][x]
            else:
                previous = matrix[y-1][x]
                if previous == matrix[y][x]:
                    new_matrix[y-1][x] = previous + matrix[y][x]
                    new_matrix[y][x] = 0
                    changed = True
                else:
                    new_matrix[y][x] = matrix[y][x]
    return new_matrix, changed

def __move_right(matrix):
    new_matrix = [[0]*4, [0]*4, [0]*4, [0]*4]
    changed = False
    for y in range(len(matrix[0:4])):
        for x in range(len(matrix[y])):
            if x >= 3 or matrix[y][x] == 0:
                new_matrix[y][x] = matrix[y][x]
            else:
                post = matrix[y][x+1]
                if post == 0:
                    new_matrix[y][x+1] = matrix[y][x]
                    new_matrix[y][x] = 0
                    matrix[y][x+1] = matrix[y][x]
                    matrix[y][x] = 0
                    changed = True
                else:
                    new_matrix[y][x] = matrix[y][x]
    return new_matrix, changed

def __merge_right(matrix):
    new_matrix = [[0]*4, [0]*4, [0]*4, [0]*4]
    changed = False
    for y in reversed(range(len(matrix[0:4]))):
        for x in reversed(range(len(matrix[y]))):
            if x >= 3 or matrix[y][x] == 0:
                new_matrix[y][x] = matrix[y][x]
            else:
                post = matrix[y][x+1]
                if post == matrix[y][x]:
                    new_matrix[y][x+1] = post + matrix[y][x]
                    new_matrix[y][x] = 0
                    matrix[y][x+1] = post + matrix[y][x]
                    matrix[y][x] = 0
                    changed = True
                else:
                    new_matrix[y][x] = matrix[y][x]
    return new_matrix, changed

def __move_down(matrix):
    new_matrix = [[0]*4, [0]*4, [0]*4, [0]*4]
    changed = False
    for y in range(len(matrix[0:4])):
        for x in range(len(matrix[y])):
            if y >= 3 or matrix[y][x] == 0:
                new_matrix[y][x] = matrix[y][x]
            else:
                post = matrix[y+1][x]
                if post == 0:
                    new_matrix[y+1][x] = matrix[y][x]
                    new_matrix[y][x] = 0
                    matrix[y+1][x] = matrix[y][x]
                    matrix[y][x] = 0
                    changed = True
                else:
                    new_matrix[y][x] = matrix[y][x]
    return new_matrix, changed

def __merge_down(matrix):
    new_matrix = [[0]*4, [0]*4, [0]*4, [0]*4]
    changed = False
    for y in range(len(matrix[0:4])):
        for x in range(len(matrix[y])):
            if y >= 3 or matrix[y][x] == 0:
                new_matrix[y][x] = matrix[y][x]
            else:
                previous = matrix[y-1][x]
                if previous == matrix[y][x]:
                    new_matrix[y-1][x] = previous + matrix[y][x]
                    new_matrix[y][x] = 0
                    changed = True
                else:
                    new_matrix[y][x] = matrix[y][x]
    return new_matrix, changed