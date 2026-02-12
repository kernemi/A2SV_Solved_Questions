lists = [0]*5
onerow = 0
onecol = 0
for i in range(5):
    lists[i] = list(map(int,input().split()))
    if 1 in lists[i]:
        for j in range(5):
            if lists[i][j] == 1:
                onecol = j
                onerow = i
                break
result = abs(2-onerow) + abs(2-onecol)
print(result)

