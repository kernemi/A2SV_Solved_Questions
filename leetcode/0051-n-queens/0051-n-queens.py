class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        def solve(row,board):
            if row == n:
                for r1 in range(n):
                    temp = ""
                    for c1 in range(n):
                        if board[r1][c1] == '#':
                            temp += '.'
                        else:
                            temp += 'Q'
                    board[r1] = temp
                    
                answer.append(board)
                return

            for col in range(n):
                if board[row][col] == '.':
                    newboard = deepcopy(board)
                    newboard[row][col] = 'Q'
                    for r in range(n):
                        for c in range(n):
                            if r == row and c == col:
                                continue
                            if r == row or c == col or r + c == row + col or r - c == row - col:
                                newboard[r][c] = '#'
                    solve(row+1,newboard)

        solve(0,[['.' for _ in range(n)] for _ in range(n)])
        return answer

        