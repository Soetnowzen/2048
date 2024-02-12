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
    """
    Moves all the tiles in the 2D representation in the given direction.

    Args:
        matrix (list): 2D list representing the game board.
        direction (Direction): Direction of movement (LEFT, UP, RIGHT, DOWN).

    Returns:
        tuple: If something has been moved, and the updated matrix.
    """
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
    """
    Gets the compare_position based on the direction.

    Args:
        direction (Direction): Direction of movement (LEFT, UP, RIGHT, DOWN).
        x (int): The x axis position of a matrix.
        y (int); The y axis position of a matrix.
    Returns:
        int: Either a value between 0 to 16 if successful.
            Or -1 if a errnouious movement.
    """
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
    """
    Merges two elements in the given direction if that are equal.

    Args:
        matrix (list): 2D list representing the game board
        direction (Direction): Direction of movement (LEFT, UP, RIGHT, DOWN).
    Returns:
        tuple: If something has been merged, and the updated matrix.
    """
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
                        __merge_cell__(new_matrix, matrix,
                                       current_position, compare_position)
                    else:
                        __merge_cell__(new_matrix, matrix,
                                       compare_position, current_position)
                    changed = True
                else:
                    new_matrix[current_position] = matrix[current_position]
    return new_matrix, changed


def __merge_cell__(new_matrix: list, matrix: list, this: int, that: int) -> None:
    """
    Merges cell that element into this element.

    Args:
        new_matrix (list): A updated matrix
        matrix (list): 2D list representing the game board
        this (int): Index of the element.
        that (int): Index of the element.

    Returns:
        Nothing
    """
    new_matrix[this] = matrix[that] + matrix[this]
    new_matrix[that] = 0
    matrix[this] += matrix[that]
    matrix[that] = 0
