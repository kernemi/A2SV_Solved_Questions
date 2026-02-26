t = int(input())
for _ in range(t):
    n = int(input())
    lists = list(map(int,input().split()))
   
    result = [lists[0]]
    posDiff = 0
    p = 1

    while p < n:
        diff = lists[p-1] - lists[p]

        if posDiff > 0 and diff < 0:
            result.append(lists[p-1])
        elif posDiff < 0 and diff > 0:
            result.append(lists[p-1])
        
        if p == n-1:
            result.append(lists[p])
        p += 1
        posDiff = diff
    
    print(len(result))
    print(*result)
