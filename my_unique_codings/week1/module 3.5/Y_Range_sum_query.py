n, t=map(int, input().split())
arr=list(map(int, input().split()))
range_arr=[]
sum=0
for i in range(0,n):
    sum= sum+arr[i]
    range_arr.append(sum)

# print(*range_arr)
# print(*arr)
while t!=0:
    l, r=map(int, input().split())
    
    l=l-1
    r=r-1
    # print(l,r)
    if l==0:
        print(range_arr[r])
    else:
        # a=range_arr[l-1]
        # b=range_arr[r]
        # sm=b-a
        # # print(a,b)
        sm=range_arr[r]-range_arr[l-1]
        print(sm)
    t=t-1