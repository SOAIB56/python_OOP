a, b = map(int, input().split())
lucky_num = []

def check_lucky(num):
    for dig in str(num):
        if dig != '4' and dig != '7':
            return False
    return True

for i in range(a, b + 1):
    if check_lucky(i):
        lucky_num.append(i)

if lucky_num:
    print(" ".join(map(str, lucky_num)))
else:
    print("-1")
