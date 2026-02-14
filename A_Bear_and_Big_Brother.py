a,b=map(int,input().split())
year=0
while a <= b:
    a=3*a
    b=2*b
    year+=1

print(year)