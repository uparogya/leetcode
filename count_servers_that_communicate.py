class Solution:
    def countServers(grid: list[list[int]]) -> int:
        row_holders = {}
        col_holders = {}
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == 1:
                    if i in row_holders:
                        row_holders[i] += 1
                    else:
                        row_holders[i] = 1
                    
                    if j in col_holders:
                        col_holders[j] += 1
                    else:
                        col_holders[j] = 1
        
        can_communicate = 0
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == 1:
                    if (i in row_holders and row_holders[i] > 1) or (j in col_holders and col_holders[j] > 1):
                        can_communicate += 1
        
        return can_communicate

print(Solution.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))