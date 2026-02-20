t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    result = []

    for i in range(n):
        for j in range(n-i-1):

            if a[j] > a[j+1]:
                a[j + 1],a[j] = a[j],a[j + 1]
                result.append([1,j+1])
            if b[j] > b[j+1]:
                b[j+1],b[j] = b[j],b[j+1]
                result.append([2,j+1])
    
    for i in range(n):
        if a[i] > b[i]:
            a[i],b[i] = b[i],a[i]
            result.append([3,i+1])
    
    print(len(result))
    for i in range(len(result)):
        a,b = result[i]
        print(f"{a} {b}")

        

