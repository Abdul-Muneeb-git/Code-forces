def coinstransformation(n):
    if n <= 3:
        return 1
    coins = 1

    while n > 3:
        n //= 4
        coins *= 2
    return coins



t=int(input())
for _ in range(t):
    x=int(input())
    w= coinstransformation(x)
    print(w)
