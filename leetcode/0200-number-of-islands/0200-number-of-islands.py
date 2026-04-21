class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def solve(r,c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == "0":
                return 1

            if (r,c) in visited:
                return 0

            visited.add((r,c))

            return solve(r+1,c) + solve(r-1,c) + solve(r,c+1) + solve(r,c-1)

        
        rows,cols = len(grid),len(grid[0])
        visited = set()
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    answer = solve(i,j)
                  
                    if answer > 0:
                        count += 1
        return count