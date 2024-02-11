from .direction import Direction


def convert_to_matrix(data):
    """
    Convert string representation of matrix and direction to data types.

    Args:
        data (str): String representation of matrix and direction.

    Returns:
        tuple: Tuple containing the matrix (list of lists) and direction (Direction enum).
    """
    matrix = []
    for i, row in enumerate(data.split('\n')):
        for cell in row.strip().split():
            matrix.append(int(cell))
    direction = Direction(int(matrix[16]))
    matrix = matrix[0:16]
    return matrix, direction
