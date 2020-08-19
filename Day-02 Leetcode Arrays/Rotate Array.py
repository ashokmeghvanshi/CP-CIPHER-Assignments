def RotateArray(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    nums[:]=nums[-k%len(nums):]+nums[:-k%len(nums)]
    return nums

print(RotateArray([1,2,3,4,5,6,7], 3))
