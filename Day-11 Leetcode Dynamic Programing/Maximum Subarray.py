class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = [0 for _ in range(len(nums))]
        sum1 = nums[0]
        result[0]=nums[0]
        
        for i in range(1,len(nums)):
            if sum1 > 0:
                sum1 = sum1 + nums[i]
            else:
                sum1 = nums[i]
            result[i] = max(result[i-1], sum1)
            
        return result[len(nums)-1]
        
