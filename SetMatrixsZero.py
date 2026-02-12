class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        zerorows = set()
        zerocols = set()
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zerorows.add(i)
                    zerocols.add(j)
        for i in zerorows:
            matrix[i] = [0] * col
        for j in zerocols:
            for i in range(row):
                matrix[i][j] = 0
        
        
