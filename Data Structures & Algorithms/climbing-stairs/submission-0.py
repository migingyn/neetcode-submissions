class Solution:
    # given n, climb 1
    # climb n 1's
    #
    # given n, climb 2
    # climb n-2 2's + n-1 1's
    #

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]