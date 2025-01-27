a= int (input().strip())
arr=[0]*(a+1)
arr[1]=0

if a>=2:
    arr[2]=1
    for i in range(3,a+1):
        arr[i]=arr[i-1]+arr[i-2]
print(arr[a])
