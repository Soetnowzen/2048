from .direction import Direction


def execute(matrix: list, direction: Direction) -> list:
    """
    Execute movement on the matrix based on the specified direction.

    Args:
        matrix (list): 2D list representing the game board.
        direction (Direction): Direction of movement (LEFT, UP, RIGHT, DOWN).

    Returns:
        list: Modified matrix after movement.
    """
    if direction not in {Direction.LEFT, Direction.UP, Direction.RIGHT, Direction.DOWN}:
        raise ValueError("Invalid direction")

    changed = True
    while changed:
        matrix, changed = __move__(matrix, direction)
    matrix, changed = __merge__(matrix, direction)
    while changed:
        matrix, changed = __move__(matrix, direction)

    return matrix


def __move__(matrix: list, direction: Direction) -> tuple:
    if len(matrix) > 16:
        raise ValueError("Invalid Matrix size:", len(matrix))
    new_matrix = [0] * 4 * 4
    changed = False
    for y in range(4):
        for x in range(4):
            current_position = x + 4 * y
            compare_position = __get_compare_position__(direction, x, y)
            if 0 >= compare_position or compare_position > 16:
                new_matrix[current_position] = matrix[current_position]
            else:
                if matrix[compare_position] == 0 and matrix[current_position] != 0:
                    new_matrix[compare_position] = matrix[current_position]
                    new_matrix[current_position] = 0
                    matrix[compare_position] = matrix[current_position]
                    matrix[current_position] = 0
                    changed = True
                else:
                    new_matrix[current_position] = matrix[current_position]
    return new_matrix, changed


def __get_compare_position__(direction: Direction, x: int, y: int) -> int:
    if direction == Direction.LEFT and x != 0:
        return (x - 1) + 4 * y
    elif direction == Direction.DOWN and y != 3:
        return x + 4 * (y + 1)
    elif direction == Direction.RIGHT and x != 3:
        return (x + 1) + 4 * y
    elif direction == Direction.UP and y != 0:
        return x + 4 * (y - 1)
    return -1


def __merge__(matrix: list, direction: Direction) -> tuple:
    if len(matrix) != 16:
        raise ValueError("Invalid Matrix size:", len(matrix))
    new_matrix = [0] * 4 * 4
    changed = False
    for y in range(4):
        for x in range(4):
            current_position = x + 4 * y
            compare_position = __get_compare_position__(direction, x, y)
            if 0 > compare_position or compare_position > 16:
                new_matrix[current_position] = matrix[current_position]
            else:
                if matrix[compare_position] == matrix[current_position]:
                    if direction in {Direction.DOWN, Direction.RIGHT}:
                        new_matrix[current_position] = matrix[compare_position] + \
                            matrix[current_position]
                        new_matrix[compare_position] = 0
                        matrix[current_position] += matrix[compare_position]
                        matrix[compare_position] = 0
                    else:
                        new_matrix[compare_position] = matrix[compare_position] + \
                            matrix[current_position]
                        new_matrix[current_position] = 0
                        matrix[compare_position] += matrix[current_position]
                        matrix[current_position] = 0
                    changed = True
                else:
                    new_matrix[current_position] = matrix[current_position]
    return new_matrix, changed
