class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
    
        def solve(r,c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0:
                return 1

            if (r,c) in visited:
                return 0

            visited.add((r,c))

            return solve(r+1,c) + solve(r-1,c) + solve(r,c+1) + solve(r,c-1)

        
        rows,cols = len(grid),len(grid[0])
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return solve(i,j)

        
