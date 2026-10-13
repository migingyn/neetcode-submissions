class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1) #O(n) array
        dp[0] = 0
        offset = 1 #O(1) extra space, 1 bc highest power for 0 is 1?
        
        for i in range(1, n+1): #O(n)
            if i == 2 * offset: #Move the leading 1 up per higher power
                offset = i
            dp[i] = 1 + dp[i-offset] #Recurrence relation, a_n = 1 + a_n-x
        
        return dp