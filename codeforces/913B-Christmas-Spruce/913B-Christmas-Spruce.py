from collections import defaultdict

n = int(input())
dicts = defaultdict(list)

for i in range(2,n+1):
    a = int(input())
    dicts[a].append(i)

for i in dicts:
    count = 0
    for x in dicts[i]:
        if x not in dicts:
            count += 1
    if count < 3:
        print("No")
        break
else:
    print("Yes")