def skibidus(s):
    stack = []
    if len(s) == 2 and s[0] != s[1]:
        return 2
    else:
        return 1

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return len(stack)
    pass


t = int(input())
for _ in range(t):
    x = input()
    w = skibidus(x)
    print(w)
