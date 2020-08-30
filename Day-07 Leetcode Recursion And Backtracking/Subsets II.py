class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    
        subset=[]
        nums=sorted(nums)
        nums.sort()
        def createsubset(start,emptylist):
            
            subset.append(emptylist)
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
            
                    continue
                createsubset(i+1, emptylist+[nums[i]])
        start=0
        emptylist=[]
        createsubset(start,emptylist)
        return subset
