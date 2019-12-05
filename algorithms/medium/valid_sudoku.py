""" Medium Difficulty"""

def one2nine():
    return {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}


def is_valid_sudoku(board) -> bool:
    # Check Rows
    for row in board:
        temp = one2nine()
        for val in row:
            if val in temp.keys():
                temp[val] += 1
        for key, val in temp.items():
            if val > 1:
                return False

    # Check Columns
    row = 0
    column = 0
    while column != 9:
        temp = one2nine()
        while row != 9:
            val = board[row][column]
            if val in temp.keys():
                temp[val] += 1
            row += 1
        row = 0
        for key, val in temp.items():
            if val > 1:
                return False
        column += 1

    # Check 3 x 3 boxes
    box_rows = 3
    box_columns = 3
    rows = cols = 0
    row_count = 3
    col_count = 3
    while box_rows != 0:
        while box_columns != 0:
            temp = one2nine()
            while rows < row_count:
                while cols < col_count or cols == 8:
                    box_val = board[rows][cols]
                    if box_val in temp.keys():
                        temp[box_val] += 1
                    cols += 1
                cols -= 3
                rows += 1
            for key, val in temp.items():
                if val > 1:
                    return False
            if col_count == 9:
                col_count = 0
            col_count += 3
            cols += 3
            rows -= 3
            box_columns -= 1
        box_columns = 3
        box_rows -= 1
        row_count += 3
        cols = 0
        rows = row_count - 3

    return True


if __name__ == '__main__':
    print(is_valid_sudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ]))
