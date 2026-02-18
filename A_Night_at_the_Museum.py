w=input().lower()
c="abcdefghijklmnopqrstuvwxyz"
p='a'
i,ans=0,0
while i < len(w):
    a=c.index(p)
    b=c.index(w[i])
    clo=len(c)-max(a,b) +min(a,b)
    anti=b - a
    ans+=min(abs(clo),abs(anti))
    p=w[i]
    i+=1
print(ans)
