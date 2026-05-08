from bisect import bisect_left

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    b.sort()
    prev = float("-inf")
    possible = True

    for x in a:
        chances =[]

        if x >= prev:
            chances.append(x)
        
        idx = bisect_left(b,prev + x)

        if idx < m:
            chances.append(b[idx]-x)
        
        if not chances:
            possible = False
            break

        prev = min(chances)

    print("YES" if possible else "NO")