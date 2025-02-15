a= input().strip()
l_cnt=0
r_cnt=0
final_cnt=0
ans_arr=[]
temp_arr=""
for i in a:
    temp_arr+=i
    if i=='L':
        l_cnt+=1
       
    elif i=='R':
        r_cnt+=1
       
    if l_cnt==r_cnt:
        final_cnt+=1
        ans_arr.append(temp_arr)
        temp_arr=""

print(final_cnt)
for i in ans_arr:
    print(i)
    