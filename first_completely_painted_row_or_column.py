class Solution:
    def firstCompleteIndex(arr: list[int], mat: list[list[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])

        if m == 1 or n == 1:
            return 0

        row_col_map = {}
        for i, row in enumerate(mat):
            for j, col in enumerate(row):
                row_col_map[col] = (i,j)
        
        row_painted = {}
        column_painted = {}
        
        # print('m: ', m, "n: ", n)

        for i, val in enumerate(arr):
            row, col = row_col_map[val]

            print(val, (row, col))

            if row in row_painted:
                row_painted[row] += 1
                if row_painted[row] == n:
                    return i
            else:
                row_painted[row] = 1

            if col in column_painted:
                column_painted[col] += 1
                if column_painted[col] == m:
                    return i
            else:
                column_painted[col] = 1

        # print(row_col_map)

print(Solution.firstCompleteIndex([2,8,7,4,1,3,5,6,9],[[3,2,5],[1,4,6],[8,7,9]]))