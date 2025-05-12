def animals(n):
    outputs=[]
    for i in range(n):
        legs=int(input())
        m = legs// 4 + (legs% 4) // 2
        outputs.append(m)
    return outputs
a=int(input())
outputs=animals(n)
for output in outputs:
    print(output)

