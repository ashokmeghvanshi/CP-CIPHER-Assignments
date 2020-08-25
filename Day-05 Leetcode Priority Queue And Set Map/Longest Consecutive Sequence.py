class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)==0:

            return 0

        l1=list(dict.fromkeys(nums))

        s=0

        l1=sorted(l1)

        i=0

        c=0

        while i<len(l1)-1:

            if l1[i]+1==l1[i+1]:

                s=s+1

                if s>c:

                    c=s
            else:

                if s>c:

                    c=s

                s=0

            i=i+1
            
        return c+1
                    
