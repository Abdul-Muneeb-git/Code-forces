def fixtheexpression(a):
    if (a[1]=="=" and int(a[0])==int(s[2])) or (a[1]=="<" and int(a[0])<int(s[2])) or (a[1]==">" and int(a[0])>int(s[2])):
       return a
    else:
       if int (a[0]) < int( a[2]):
          c[0]=a[0]
          c[1]="<"
          c[2]=a[2]
          return c
       if int (a[0]) > int( a[2]):
          c[0]=a[0]
          c[1]=">"
          c[2]=a[2]
          return c
       if int (a[0]) == int( a[2]):
          c[0]=a[0]
          c[1]="="
          c[2]=a[2]
          return c

def main():
    t=int(input())
    for i in range(t):
        a=input()
        print(fixtheexpression(a))


