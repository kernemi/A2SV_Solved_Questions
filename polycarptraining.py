n = int(input())
lists = list(map(int,input().split()))
lists.sort()
count = 0
k = 1
for i in lists:
    if k > i:
        continue
    else:
        count += 1
        k += 1
print(count)
