class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        t=0
        y=[0]*len(nums)
        y[0]=nums[0]
        y[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            
            y[i]=max(y[i-1],y[i-2]+nums[i])
        return max(y)
        
        
        
