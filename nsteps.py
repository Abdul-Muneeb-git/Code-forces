def nsteps(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return 1
    memo[n]=nsteps(n-1,memo)+nsteps(n-2,memo)
    return memo[n]

    pass
print(nsteps(3))
