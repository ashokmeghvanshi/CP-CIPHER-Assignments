
def MoveZeroes(nums):
    
    ''''t=0
    while 0 in nums: 
        nums.remove(0)
        t=t+1
    
    for i in range(t):
        nums.insert(len(nums),0)'''
    p,q=0,0
    while q<len(nums):
        if nums[q]==0:
            q=q+1
        else:
            nums[p],nums[q]=nums[q],nums[p]
            p=p+1
            q=q+1
        
    return nums
print(MoveZeroes([0,1,0,3,12]))
    
    
    
