from collections import Counter
n=input()
arr=list(map(int, input().split()))
number_cnt=[]
freq = Counter(arr)
remove=0
# print(freq)
for i, j in freq.items():
    if i<j:
       
        remove+=abs(j-i)
    elif i>j:
        # print(f'{i}: {j}')
        remove=remove+j
    elif i==j:
        # print(f'{i}: {j}')
        continue
    # print(f'{i}: {j}')
print(remove)