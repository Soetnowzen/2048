import sys
from .matrix_operations import convert_to_matrix
from .game_logic import execute


if __name__ == '__main__':
    try:
        first_argument = sys.argv[1]
        matrix, direction = convert_to_matrix(first_argument)
        execute(matrix, direction)
    except IndexError:
        print("Usage: python __init__.py <matrix_representation>", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)