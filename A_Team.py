from collections import Counter
n=int(input())
ans=0
for _ in range(n):
    arr=[num for num in input().split()]
    count=Counter(arr)
    if count['1']>=2:
        ans+=1
print(ans)