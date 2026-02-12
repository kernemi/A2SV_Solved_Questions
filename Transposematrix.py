class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        new = [[] for _ in range(col)]
        for i in range(row):
            for j in range(col):
                new[j].append(matrix[i][j])
        return new
