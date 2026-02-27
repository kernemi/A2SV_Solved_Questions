n,k = map(int,input().split())
s = list(map(int,input().split()))

total = 0
sums = 0
left = 0

for right in range(n):
    total += s[right]
    while total >= k:
        total -= s[left]
        left += 1
    sums += right - left + 1
print(((n*(n+1))//2) - sums)


