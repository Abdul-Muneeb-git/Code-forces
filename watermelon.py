def weight(w):
    if w % 2 == 0 and w != 2:
        p = "yes"
    if w == 2 or w % 2 != 0:
        p = "no"
    return p


i = int(input())
o = weight(i)
print(o)
