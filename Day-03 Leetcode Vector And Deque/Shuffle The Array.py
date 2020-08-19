def ShuffleTheArray(nums,n):
    a,b=[],[]
    for i in range(n):
        a.append(nums[i])

    for j in range(n,len(nums)):
        b.append(nums[j]
                 )        

    x=[]
    for i,j in zip(a,b):
        x.append(i)
        x.append(j)
    return x

print(ShuffleTheArray([2,5,1,3,4,7],3))
