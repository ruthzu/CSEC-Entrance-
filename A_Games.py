from collections import Counter
n=int(input())
host,guests=[],[]
ans=0
for _ in range(n):
    h, g = map(int,input().split())
    host.append(h)
    guests.append(g)

for h in host:
    if h in guests:
        ans+=guests.count(h)
print(ans)
    
