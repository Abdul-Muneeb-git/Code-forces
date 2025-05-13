import  math
def sqchk(n):
    i=1
    outputs=[]
    for i in range(n):
        a=int(input())
        boxes=list(map(int,input().split()))
        s=0
        for j in boxes:
            s=s+j
        sqrt_num = math.sqrt(s)
        if sqrt_num.is_integer():
            outputs.append("yes")
        else:
            outputs.append("no")
    return outputs
n=int(input())
outputs= sqchk(n)
for output in outputs:
    print(output)

