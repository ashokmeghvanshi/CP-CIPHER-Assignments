class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        l=[1]
        for i in range(1,len(nums)):
            ans=1
            for j in range(i):
                if nums[i]>nums[j]:
                    ans=max(ans,1+l[j])
            l.insert(i,ans)
        
        return max(l)
        
