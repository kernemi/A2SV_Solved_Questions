row,col = map(int,input().split())
lists = []
for _ in range(row):
    lists.append(input())

horizontal = [[0] * (col +1) for _ in range(row + 1)]
vertical = [[0] * (col +1) for _ in range(row + 1)]

for i in range(1,row+1):
    for j in range(1,col+1):
        horizontal[i][j] = horizontal[i-1][j] + horizontal[i][j-1] - horizontal[i-1][j-1]
        vertical[i][j] = vertical[i-1][j] + vertical[i][j-1] - vertical[i-1][j-1]

        if j < col and lists[i-1][j-1] == '.' and lists[i-1][j] == '.':
            horizontal[i][j] += 1
        
        if i < row and lists[i-1][j-1] == '.' and lists[i][j-1] == '.':
            vertical[i][j] += 1

t = int(input())
for _ in range(t):
    r1,c1,r2,c2 = map(int,input().split())

    x = horizontal[r2][c2-1] - horizontal[r1-1][c2-1] - horizontal[r2][c1-1] + horizontal[r1-1][c1-1]
    y = vertical[r2 - 1][c2] - vertical[r1-1][c2] - vertical[r2 - 1][c1-1] + vertical[r1-1][c1-1]

    print(x+y)