t= int(input())
for i in range(1, t+1):
    n= int(input())
    num= list(map(int, input().split()))
    # print(num[0])
    check_arr=[]
    for a in range(0, n):
        for b in range (a+1, n):
            # print("here ",a,b)
            
            sum=num[a]+num[b]+(b+1)-(a+1)
            # print(f"{num[a]}+{num[b]}+{(a+1)}-{(b+1)}= {sum}")
            check_arr.append(sum)
    mn=min(check_arr)
    print(mn)
    # print(" ".join(map(str,check_arr)))