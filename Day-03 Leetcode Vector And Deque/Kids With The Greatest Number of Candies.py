
def KidsWithCandies(candies, extraCandies):

    m=max(candies)
    
    for i in range(len(candies)):
        p=candies[i]+extraCandies
        if p<m:
            candies[i]=False
        else:
            candies[i]=True

    return candies

print([2,3,5,1,3])
print(KidsWithCandies([2,3,5,1,3],3))

