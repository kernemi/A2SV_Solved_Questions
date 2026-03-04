n, k = map(int, input().split())
lists = list(map(int, input().split()))

dicts = {}
left = 0
bestLeft = 0
bestRight = 0
distinct = 0

for right in range(n):

    if lists[right] not in dicts or dicts[lists[right]] == 0:
        distinct += 1

    if lists[right] in dicts:
        dicts[lists[right]] += 1
    else:
        dicts[lists[right]] = 1

    while distinct > k:
        dicts[lists[left]] -= 1
        if dicts[lists[left]] == 0:
            distinct -= 1
        left += 1

    if right - left > bestRight - bestLeft:
        bestLeft, bestRight = left, right

print(bestLeft + 1, bestRight + 1)
