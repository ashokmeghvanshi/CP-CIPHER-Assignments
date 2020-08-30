class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits)==0:
            return []
        
        d={'2':'abc','3':'def',
           '4':'ghi','5':'jkl',
           '6':'mno','7':'pqrs',
           '8':'tuv','9':'wxyz'}

        def combination(path, digits, result, d):

            if len(digits) == 0:

                result.append(path)
                
                return

            for c in d[digits[0]]:

                combination(path+c,digits[1:],result,d)
        
        self.result=[]

        combination('', digits, self.result, d)

        return self.result
    
