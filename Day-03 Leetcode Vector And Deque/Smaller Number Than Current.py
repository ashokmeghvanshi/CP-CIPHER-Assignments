def SmallerNumbersThanCurrent(nums):
    t=[]
    for i in nums:
        y=0
        for j in nums:
            if i>j: 
                y=y+1
        t.append(y)
    return t

print(SmallerNumbersThanCurrent([8,1,1,2,2,3]))
