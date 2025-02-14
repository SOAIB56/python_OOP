t= int(input())
a= list(map(int, input().split()))
i=0
j=len(a)-1
if t==2:
    print("NO")
else:
    flag=True
    while i<=j:
        if a[i] != a[j]:
            flag=False
            break
        i+=1
        j-=1
    if flag:
        print("YES")
    else:
        print("NO")

t= int(input())
a=list(map(int, input().split()))
if a== a[::-1]:
    print("YES")
else:
    print("NO")