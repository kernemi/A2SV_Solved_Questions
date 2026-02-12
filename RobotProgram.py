def solve():
    n,x,k = map(int, input().split())
    strings = input()
    i = 0
    while k > 0 and i < n:
        x += 1 if strings[i] == "R" else -1
        k -= 1
        i += 1
        if x == 0:
            i = 0
            break
    else:
        return 0
    steps = k
    while k > 0 and i < n:
        x += 1 if strings[i] == "R" else -1
        k -= 1
        i += 1
        if x == 0:
            break
    else:
        return 1
    
    return (steps // i) + 1    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        answer = solve()
        print (answer)
  
