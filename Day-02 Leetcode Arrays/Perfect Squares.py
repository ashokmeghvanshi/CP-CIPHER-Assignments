class Solution:

    def numSquares(self, n: int) -> int:

        x=10000

        squares = []

        for i in range(1, int(math.sqrt(n))+1):

            squares.append(i*i)

        dp = [x]*(n+1)

        dp[0] = 0

        for i in range(1, n+1):

            for j in squares:

                if i<j:

                    break

                dp[i] = min(dp[i], dp[i-j]+1)

        return dp[n]
