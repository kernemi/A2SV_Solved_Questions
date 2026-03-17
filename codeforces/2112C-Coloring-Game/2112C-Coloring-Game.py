t = int(input())
for _ in range(t):
    n = int(input())
    lists = list(map(int,input().split()))
    count = 0
    maxx = lists[-1]

    for i in range(n-1,1,-1):
        left = 0
        for j in range(i-1,0,-1):
            while (lists[left] + lists[j] <= lists[i] and left < j) or (lists[i] + lists[left] + lists[j] <= maxx and left < j):
                left += 1

            if left == j:
                break
            
            count += j - left
    print(count)