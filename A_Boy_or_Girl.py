from collections import Counter
username=input()
count=Counter(username)
if len(count) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")