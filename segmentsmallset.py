from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = defaultdict(int)

l = 0
distinct = 0
ans = 0

for r in range(n):
    if freq[a[r]] == 0:
        distinct += 1
    freq[a[r]] += 1

    while distinct > k:
        freq[a[l]] -= 1
        if freq[a[l]] == 0:
            distinct -= 1
        l += 1

    ans += (r - l + 1)

print(ans)
