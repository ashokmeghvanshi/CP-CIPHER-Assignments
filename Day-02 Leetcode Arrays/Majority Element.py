def MajorityElement(nums):
    t=len(nums)//2
    for i in list(dict.fromkeys(nums)):
        if nums.count(i)>t:
            return i

print(MajorityElement([2,2,1,1,1,2,2]))
