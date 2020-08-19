
def Tribonacci(n,dp):
    
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
         if n not in dp.keys():
                dp[n] = Tribonacci(n-2,dp)+ Tribonacci(n-1,dp) + Tribonacci(n-3,dp)
    return dp[n]



dp={}
print(Tribonacci(5,dp))
    
