def TopKFrequent(nums, k):
    
    element_freq_count = {}

    for i in nums:

        if i not in element_freq_count:

            element_freq_count[i] = 1

        else:

            element_freq_count[i] = element_freq_count[i]+1

    element_freq_count_sort=sorted(element_freq_count.items(), key=lambda x: x[1])

    result = []

    for i in range(k,0,-1):

        result.append(element_freq_count_sort[-i][0])

    return result

print(TopKFrequent( [1,1,1,2,2,3],2))
