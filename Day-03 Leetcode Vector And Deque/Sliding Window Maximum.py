def MaxSlidingWindow(nums,k):
    maxelement = max(nums[0:k])

    msw = [maxelement]
    
    for i in range(k,len(nums)):

        if nums[i-k] == maxelement:

            maxelement = max(nums[i-k+1:i+1])

        elif nums[i] > maxelement:

            maxelement = nums[i]
        
        msw.append(maxelement)
    
    return msw

print(MaxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
