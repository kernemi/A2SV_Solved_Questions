n, k = map(int,input().split())
lists = list(map(int,input().split()))
difference = []
for i in range(n-1):
    difference.append(lists[i+1] - lists[i])
difference.sort(reverse=True)
print(sum(difference[k-1:]))
