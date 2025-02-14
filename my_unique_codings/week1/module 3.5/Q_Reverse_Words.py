# word= input().split()

# rev_word=[w[::-1] for w in word]
# result=" ".join(rev_word)
# print(result)
""" VERDICT: ACCEPTED """

word= input().split()
rev_word=[]
for i in word:
    rev=i[::-1]
    rev_word.append(rev)
result= " ".join(rev_word)
print(result)

""" VERDICT : TLE """