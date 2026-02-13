n,h=[int(x) for x in input().split()]
arr=[int(y) for y in input().split()]
sol=0
for i in arr:
    if i>h:
        sol+=2
    else:
        sol+=1
print(sol)
