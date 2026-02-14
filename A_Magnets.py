t = int(input())
p = input()
ans = 1
for _ in range(t - 1):
    c = input()
    if c != p:
        ans += 1
        p = c
print(ans)