

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
    boxes = 1
    row = col = 0
    row_boxs = 3
    col_boxs = 3
    while boxes != 3:
        temp = one2nine()
        while row != row_boxs:
            while col != col_boxs:
                val = board[row][col]
                if val in temp.keys():
                    temp[val] += 1
                col += 1
            row += 1
            col = 0
        row = 0
        for key, val in temp.items():
            if val > 1:
                return False



if __name__ == '__main__':
    is_valid_sudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ])
