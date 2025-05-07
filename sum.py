def sumchk(n):
     i=1
     outputs=[]
     for i in range(n):
        inputs=list(map(int,input().split()))
        if inputs[0]==inputs[1]+inputs[2] or inputs[1]==inputs[0]+inputs[2] or inputs[2]==inputs[1]+inputs[0]:
            outputs.append("yes")
        else:
            outputs.append("no")
     return outputs

n=int(input())
a=sumchk(n)
for output in a:
    print(output)


