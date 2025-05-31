def mincost(cost):
    n=len(cost)
    memo=[-1]*(n-1)
    for i in range(n+1):
        if i=0 or i=1:
            return memo[i]
        else:
            memo[i]=min(memo[i-1]+cost[i-1],memo[i-2],cost[i-2])
    return memo[n]
