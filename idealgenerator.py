def idealgenerator(n):
    a='yes'
    b='no'
    if n%2==1:
        return a
    else :
        return b
    pass

t=int(input())
for _ in range(t):
    x=int(input())
    w= idealgenerator(x)
    print(w)
