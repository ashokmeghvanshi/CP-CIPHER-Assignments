
def TwoSum(nums, target):
    
    ''''for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]'''
    
    for i in range(len(nums)):
        t=target-nums[i]
        if t in nums and nums.index(t)!=i:
            return [i,nums.index(t)]

print(TwoSum([2,7,11,15],22))
        

        
    
