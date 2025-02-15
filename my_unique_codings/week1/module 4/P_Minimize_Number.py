n=input()
arr=list(map(int, input().split()))
# print(arr)
div_list=[]
for num in arr:
    # print(num)
    cnt=0
    a=num
    while a%2 ==0:
        # print(a)
        a=a/2
        cnt+=1
    div_list.append(cnt)
# print(*div_list)
print(min(div_list))
           
