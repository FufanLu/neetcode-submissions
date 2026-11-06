class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])
        zero_row_flag = False
        for i in range(n):
            if matrix[0][i] == 0:
                zero_row_flag = True
                break

        zero_col_flag = False

        for j in range(m):
            if matrix[j][0] == 0:
                zero_col_flag = True
                break
        

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if zero_row_flag:
            for i in range(n):
                matrix[0][i] = 0

        if zero_col_flag:
            for i in range(m):
                matrix[i][0] = 0


        
        