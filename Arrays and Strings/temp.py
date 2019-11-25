
def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    
    rows = len(board)
    columns = len(board[0])

    new_board = [[0]*columns for i in range(rows)]

    for row in range(rows):
        for column in range(columns):
            new_board[row][column] = 1 if doesLive(
                board, row, column, rows, columns) else 0

    board[:] = new_board


def doesLive(board, row, column, rows, columns):
    ones = 0

    for i in range(row-1, row + 2):
        if i < 0 or i >= rows:
            continue
        for j in range(column-1, column + 2):
            if j < 0 or j >= columns:
                continue

            if i == row and j == column:
                continue

            if board[i][j] == 1:
                ones += 1

    if board[row][column] == 1:
        if 2 <= ones <= 3:
            return True
        return False
    else:
        if ones == 3:
            return True

        return False
    
if __name__ == '__main__':
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    gameOfLife(board)
    print(board)

