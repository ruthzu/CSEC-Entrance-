a1,a2,a3,a4=map(int,input().split())
s=list(map(int,input()))
c=0
for i in s:
    if i== 1:
        c+=a1
    elif i == 2:
        c+=a2
    elif i == 3:
        c+=a3
    else:
        c+=a4
print(c)