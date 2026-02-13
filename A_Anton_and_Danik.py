from collections import Counter
n=int(input())
s=input()
count=Counter(s)
if count["D"] > count["A"] :
    print("Danik")
elif count["D"] < count["A"]:
    print("Anton")
else:
    print("Friendship")
    
