# t= int (input())
# arr= list(map(int, input().split()))
# mx=max(arr)
# mn= min(arr)
# for i, j in enumerate(arr):
#     if mx==j:
#         arr[i]= mn
#     if mn==j:
#         arr[i]=mx
# print(*arr)

t= int (input())
arr= list(map(int, input().split()))
mn= min(arr)
mx= max(arr)
mx_index= arr.index(mx)
mn_index= arr.index(mn)
arr[mx_index]=mn
arr[mn_index]=mx
# print(*arr)
joined= " ".join(map(str,arr))
print(joined)