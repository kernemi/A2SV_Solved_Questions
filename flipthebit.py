for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    zerocount = a.count('0')
    onecount = n - zerocount
    flip = False
    ok = True

    for i in range(n - 1, -1, -1):
        current = a[i]
        
        if flip:
            current = '1' if current == '0' else '0'

        if current != b[i]:
            if zerocount != onecount:
                ok = False
                break
            flip = not flip

        if a[i] == '0':
            zerocount -= 1
        else:
            onecount -= 1

    print("YES" if ok else "NO")
