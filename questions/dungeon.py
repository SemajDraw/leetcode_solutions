import sys
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
            
        rows = len(dungeon)
        cols = len(dungeon[0])

        minHp = [[0 for a in range(cols)] for b in range(rows)]

        minHp[rows-1][cols-1] = max(1, 1 - dungeon[rows-1][cols-1])

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows -1 and j == cols -1:
                    continue
                elif i == rows -1:
                    minHp[i][j] = max(minHp[i][j+1] - dungeon[i][j], 1)
                elif j == cols - 1:
                    minHp[i][j] = max(minHp[i+1][j] - dungeon[i][j], 1)
                else:
                    minHp[i][j] = max(min(minHp[i][j+1] - dungeon[i][j], minHp[i+1][j] - dungeon[i][j]), 1)
                    
        return minHp[0][0]
                