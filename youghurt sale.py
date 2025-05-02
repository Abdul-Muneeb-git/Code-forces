def youghurtsale(n):
    outputs=[]
    for i in range(n):
        a=list(map(int,input().split()))
        if a[0]==0:
            outputs.append("purchase youghurt first")
            break
        if a[0]==1:
            outputs.append(a[1])
            continue
        if a[0]==2:
            p=a[0]*a[1]
            outputs.append(min(p,a[2]))
            continue
        pb=a[2]+(a[1]*(a[0]-2))
        pa=a[0]*a[1]
        if pb<=pa:
           outputs.append(pb)
        else:
            outputs.append(pa)
    return outputs
n=int(input())
outputs=youghurtsale(n)
for output in outputs:
    print(output)
