def fizzbuzz(n):
    e=0
    for i in range(n%15 +1):
        if i%3==i%5:
            e+=1
    return (n//15*3)+e

t=int(input())
for _ in range(t):
    x=int(input())
    w= fizzbuzz(x)
    print(w)
