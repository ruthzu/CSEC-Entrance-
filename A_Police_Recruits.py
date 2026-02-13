n=int(input())
arr=[num for num in input().split()]
p,c=0,0

for i in arr:
    if int(i) == -1:
        if int(p) > 0:
            p-=1
        else:
            c+=1
    else:
        p+=int(i)
    # print(i,c,p)
print(c)
