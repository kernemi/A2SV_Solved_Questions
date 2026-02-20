t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    lists = []

    for i in range(n):
        left,right,real = map(int,input().split())
        lists.append((left,right,real))
    lists.sort()
    for i in range(n):
        if lists[i][0] <= k <= lists[i][1]:
            k = max(k,lists[i][2])

    print(k)
