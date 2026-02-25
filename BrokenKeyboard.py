from collections import Counter
t = int(input())
for _ in range(t):
    s = input().strip()
    tempo = []
    if len(s) <= 1:
        print(s)
    else:
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i] == s[i+1]:
                i += 2
            elif i+1 == len(s):
                tempo.append(s[i])
                break
            else:
                tempo.append(s[i])
                i += 1 
        tempo.sort()
        dicts = Counter(tempo)
        result = ""
        for j in dicts:
            result += j
        print(result)   



