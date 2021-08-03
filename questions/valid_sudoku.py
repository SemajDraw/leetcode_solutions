
class Solution:
    def isValidSudoku(self, board) -> bool:
        num_set = set()
        
        # Check rows
        for r in board:
            for c in r:
                if c != '.':
                    if c in num_set:
                        return False
                    num_set.add(c)
            num_set = set()

        # Check cols
        for c in range(len(board[0])):
            for r in board:
                if r[c] != '.':
                    if r[c] in num_set:
                        return False
                    num_set.add(r[c])
            num_set = set()

        tr = [0,0,0,3,3,3,6,6,6]
        tc = [0,3,6,0,3,6,0,3,6]
        
        # Check 3x3 grids
        for i in range(len(tr)):
            if not self.check_grid(tr[i], tc[i], set(), board):
                return False
        return True
        
    def check_grid(self, r, c, num_set, board):
        
        for i in range(r, r+3):
            for j in range(c, c+3):
                if board[i][j] != '.':
                    if board[i][j] in num_set:
                        return False
                    num_set.add(board[i][j])
        return True

if __name__ == '__main__':
    sudoku = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

    sudoku2 = [
        [".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]

    sol = Solution()

    sol.isValidSudoku(sudoku2)