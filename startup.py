def startup(brands,n,k):
    totals=[]
    for costs in brands.values():
        totals.append(sum(costs))
    totals.sort(reverse=True)
    maxi=0
    for i in range(min(n, len(totals))):
        maxi += totals[i]
    return maxi



    pass
t=int(input())
for _ in range(t):
    n,k=map(int, input().split())
    brands={}
    for i in range(k):
        brand, cost = map(int, input().split())
        brands.setdefault(brand, []).append(cost)
    print(startup(brands,n,k))

