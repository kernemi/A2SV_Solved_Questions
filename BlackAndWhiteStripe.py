t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    lists = input()
    left = 0
    right = 0
    minimum = float("inf")
    track = 0
    
    while right < n:
        if lists[right] == "W":
            track += 1

        if right-left +1 == k:
            minimum = min(minimum,track)
            if lists[left] == "W":
                track -= 1
            left += 1
        right += 1
    print(minimum)
            
