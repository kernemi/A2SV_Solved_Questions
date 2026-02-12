def solve():
    n = int(input())
    s = input()
    if n < 2:
        print(-1)
    else:
        s = list(s)
        for i in range(2,8):
            if i > n:
                break 
            tempo = s[:i]
            for j in range(len(s)-(i-1)):
                if tempo.count('a') > tempo.count('b') and tempo.count('a') > tempo.count('c'):
                    return len(tempo)
                tempo.pop(0)
                if i+j >= len(s):
                    break
                tempo.append(s[i+j])
    return -1
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        answer = solve()
        print(answer) 
