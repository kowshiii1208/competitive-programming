t = int(input())

while t:
    t -= 1

    n = int(input())
    s = input()

    c = 0
    m = 0

    for ch in s:
        if ch == '#':
            c += 1
            m = max(m, c)
        else:
            c = 0

    print((m + 1) // 2)
