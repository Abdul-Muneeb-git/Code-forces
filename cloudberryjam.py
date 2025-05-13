def cloudberryjam(n):
    k=n*3
    j=int((k*4)/6)
    return j
    pass

t=int(input())
for _ in range(t):
    x=int(input())
    w= cloudberryjam(x)
    print(w)
