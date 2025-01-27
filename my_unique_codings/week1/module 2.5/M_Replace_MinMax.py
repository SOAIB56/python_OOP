n= int(input())
numbers= list(map(int, input().split()))
mx=max(numbers)
mn=min(numbers)
mx_ind=numbers.index(mx)
mn_ind=numbers.index(mn)
numbers[mn_ind]=mx
numbers[mx_ind]=mn
print(" ".join(map(str, numbers)))