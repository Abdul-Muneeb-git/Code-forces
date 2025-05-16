def minimum_seconds_to_upload(t, test_cases):
    results = []
    for case in test_cases:
        n, k = case
        # Calculate the minimum seconds required
        min_seconds = (n - 1) * k + 1
        results.append(min_seconds)
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    test_cases.append((n, k))

# Get the results
results = minimum_seconds_to_upload(t, test_cases)

# Print the results
for result in results:
    print(result)










