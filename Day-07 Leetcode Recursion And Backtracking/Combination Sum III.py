class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        from itertools import combinations
        comb = combinations([1, 2, 3,4,5,6,7,8,9], k)
        p=[]
        for i in list(comb): 
            if sum(i)==n:
                p.append(list(i))
        return p
