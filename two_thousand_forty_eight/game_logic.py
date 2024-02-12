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
        changed = __move__(matrix, direction)
    changed = __merge__(matrix, direction)
    while changed:
        changed = __move__(matrix, direction)

    return matrix


def __move__(matrix: list, direction: Direction) -> bool:
    """
    Moves all the tiles in the 2D representation in the given direction.

    Args:
        matrix (list): 2D list representing the game board.
        direction (Direction): Direction of movement (LEFT, UP, RIGHT, DOWN).

    Returns:
        tuple: If something has been moved.
    """
    if len(matrix) != 16:
        raise ValueError("Invalid Matrix size:", len(matrix))
    changed = False
    for y in range(4):
        for x in range(4):
            current_position = x + 4 * y
            compare_position = __get_compare_position__(direction, x, y)
            if 0 >= compare_position or compare_position > 16:
                continue
            else:
                if matrix[compare_position] == 0 and matrix[current_position] != 0:
                    matrix[compare_position] = matrix[current_position]
                    matrix[current_position] = 0
                    changed = True
    return changed


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


def __merge__(matrix: list, direction: Direction) -> bool:
    """
    Merges two elements in the given direction if that are equal.

    Args:
        matrix (list): 2D list representing the game board
        direction (Direction): Direction of movement (LEFT, UP, RIGHT, DOWN).
    Returns:
        tuple: If something has been merged.
    """
    if len(matrix) != 16:
        raise ValueError("Invalid Matrix size:", len(matrix))
    changed = False
    for y in range(4):
        for x in range(4):
            current_position = x + 4 * y
            compare_position = __get_compare_position__(direction, x, y)
            if 0 > compare_position or compare_position > 16:
                continue
            else:
                if matrix[compare_position] == matrix[current_position]:
                    if direction in {Direction.DOWN, Direction.RIGHT}:
                        __merge_cell__(matrix, current_position,
                                       compare_position)
                    else:
                        __merge_cell__(matrix, compare_position,
                                       current_position)
                    changed = True
    return changed


def __merge_cell__(matrix: list, this: int, that: int) -> None:
    """
    Merges cell that element into this element.

    Args:
        matrix (list): 2D list representing the game board
        this (int): Index of the element.
        that (int): Index of the element.

    Returns:
        Nothing
    """
    matrix[this] += matrix[that]
    matrix[that] = 0
