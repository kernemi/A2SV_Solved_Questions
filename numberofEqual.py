from collections import Counter
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ca = Counter(a)
cb = Counter(b)
total = 0
for num in cb:
    if num in ca:
        total += (cb[num] * ca[num])
print(total)
