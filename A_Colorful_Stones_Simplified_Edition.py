x=input()
y=input()
m=1
n=1
while n<=len(y):
    if x[m-1]==y[n-1]:
        m+=1
        n+=1
    else:
        n+=1
print(m)