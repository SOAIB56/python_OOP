a, b= map(int, input().split())
num=input().strip()
# print(type(num))
cnt=0
for i in num:
    cnt+=1
    # print(i)
    if a+1== cnt:
        if i=='-':
            print("Yes")
        else:
            print("No")