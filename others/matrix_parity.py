#!/usr/bin/python3
"""matrix_parity.py
"""

import numpy as np

def solve(incoming: str) -> str:
    """Determines matrix parity
    Args:
        incoming - string representation of a matrix
    Returns:
        OK or Corrupt
    """
    matrix_size, *matrix = incoming.strip().split('\n')
    matrix_size = int(matrix_size)

    matrix = np.array([list(map(int, row.split())) for row in matrix])

    def is_parity_property(matrix):
        row_sums = np.sum(matrix, axis=1)
        col_sums = np.sum(matrix, axis=0)

        return np.all(row_sums % 2 == 0) and np.all(col_sums % 2 == 0)

    if is_parity_property(matrix):
        return "OK"
    else:
        for i in range(matrix_size):
            for j in range(matrix_size):
                flipped_matrix = matrix.copy()
                flipped_matrix[i, j] = 1 - flipped_matrix[i, j]
                if is_parity_property(flipped_matrix):
                    return f"Change bit ({i + 1},{j + 1})"
        return "Corrupt"
