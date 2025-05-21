def robhouse(i,houses,memo={}):
    if i in memo:
        return memo[i]
    if i<0:
        return  0
    memo[i]=max(robhouse(i-1,houses,memo),houses[i]+robhouse(i-2,houses,memo))
    return memo[i]
    pass

houses=[2,7,9,4,1]
print(robhouse(len(houses)-1,houses))
