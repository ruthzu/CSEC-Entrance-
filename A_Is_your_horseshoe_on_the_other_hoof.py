from collections import Counter
shoes= [shoe for shoe in input().split()]
colorCount=Counter(shoes)
ans=0
for k,v in colorCount.items():
    if v >1:
        ans+=v-1

print(ans)