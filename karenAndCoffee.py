n,k,q = map(int,input().split())
maxT = 200000
difference = [0] *(maxT + 2)

for _ in range(n):
    a,b = map(int,input().split())
    difference[a] += 1
    difference[b+1] -= 1

prefixsum = [0] *(maxT + 1);
track = 0

for i in range(1,maxT + 1):
    track += difference[i]
    prefixsum[i] = track

advisable = [0] *(maxT + 1)
for i in range(1,maxT + 1):
    if prefixsum[i] >= k:
        advisable[i] = 1

advisableSum = [0]*(maxT + 1)
for i in range(1,maxT + 1):
    advisableSum[i] = advisableSum[i-1] + advisable[i]


for _ in range(q):
    a,b = map(int,input().split())
    print(advisableSum[b]-advisableSum[a-1])

    
