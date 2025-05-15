def magicoak(n, k):
    start = n - k + 1
    end = n
    leaf_sum = (end - start + 1) * (start + end) // 2
    if leaf_sum % 2 == 0:
        return "YES"
    else:
        return "NO"


t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    results.append(magicoak(n, k))

print("\n".join(results))
