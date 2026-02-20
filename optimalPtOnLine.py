n = int(input())
lists = list(map(int,input().split()))
lists.sort()
print(lists[(n-1)//2])
