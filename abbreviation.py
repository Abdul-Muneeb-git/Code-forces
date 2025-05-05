def abbr(n):
    i=0
    abb=[None]*n
    while i <= n-1:
        w = input()
        if len(w) > 10:
            abb[i]=w[0]+str(len(w)-2)+w[len(w)-1]
        else:
            abb[i]= w
        i+=1
    return abb

number=int(input())
abbreviations= abbr(number)
print("\n")
for abbreviation in abbreviations:
    print(abbreviation)
