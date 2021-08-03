class Solution:
    def combinationSum(self, candidates, target: int):
        combos = []
        paths = []
        
        def dfs(i):
            paths.append(i)
            tot = sum(paths)
            if tot == target:
                return True
            if tot > target:
                return False
            
            for j in range(i, len(candidates)):
                if dfs(j):
                    combos.append(paths)
                    paths = []
                else:
                    p = []
            
            
        for i in range(len(candidates)):
            dfs(i)
        # print()
        # print(combos)