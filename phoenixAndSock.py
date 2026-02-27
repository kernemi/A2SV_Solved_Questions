from collections import Counter

t = int(input())

for _ in range(t):
    n,leftCount, rightCount = map(int,input().split())
    colors = list(map(int, input().split()))

    LeftList = Counter(colors[:leftCount])
    RightList = Counter(colors[leftCount:])

    for i in LeftList:
        if i in RightList:
            minimum = min(LeftList[i], RightList[i])
            LeftList[i] -= minimum
            RightList[i] -= minimum
            leftCount -= minimum
            rightCount -= minimum
    
    if leftCount > rightCount:
        LeftList, RightList =RightList,  LeftList
        leftCount, rightCount = rightCount, leftCount
        
    
    diff = (rightCount - leftCount) // 2
    cost = diff
    
    rem_pairs = 0
    for i in RightList:
        rem_pairs += RightList[i] // 2
        
    can_fix_by_flipping = min(diff, rem_pairs)
    
    print(cost + (leftCount + (diff - can_fix_by_flipping)))
