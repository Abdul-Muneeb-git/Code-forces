def partition_labels(s):
    last = {ch: i for i, ch in enumerate(s)}

    partitions = []
    left = 0
    max_right = 0

    for right in range(len(s)):
        max_right = max(max_right, last[s[right]])

        if right == max_right:
            partitions.append(right - left + 1)
            left = right + 1

    return partitions
t= int(input())
for i in range(t):
    s = input().strip()
    print(" ".join(map(str, partition_labels(s))))
