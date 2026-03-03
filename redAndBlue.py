t = int(input())
for _ in range(t):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))
    
    maxRed = current = 0
    for x in red:
        current += x
        maxRed = max(maxRed, current)
    
    maxBlue = current = 0
    for x in blue:
        current += x
        maxBlue = max(maxBlue, current)
    
    print(maxRed + maxBlue)
