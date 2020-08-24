class Solution:

    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
        def zigzag(nums,start):

            result=0

            for i in range(start,len(nums),2):

                n=nums[i]

                if i>0:

                    n=min(n,nums[i-1]-1)

                if i+1<len(nums):

                    n=min(n,nums[i+1]-1)

                result=result+nums[i]-n

            return result

        return min(zigzag(nums,0),zigzag(nums,1))
