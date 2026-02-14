n=int(input())
nums=list(map(int,input().split()))
i=0
j=n-1
s,d=0,0
turn="s"
while i <= j:
    if turn == "s":
        turn = "d"
        if nums[i] < nums[j]:
            s+=nums[j]
            j-=1
        else:
            s+=nums[i]
            i+=1
    else:
        turn="s"
        if nums[i] <  nums[j]:
            d+=nums[j]
            j-=1
        else:
            d+=nums[i]
            i+=1
    
    
print(s,d)