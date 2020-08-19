
def FindKthLargest(nums, k):
    nums.sort()
    return nums[-k]

print(FindKthLargest([3,2,1,5,6,4], 2))
