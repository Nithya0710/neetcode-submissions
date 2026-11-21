class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for x in range(1, amount+1):
            for c in coins:
                if c<=x:
                    dp[x]=min(dp[x], 1+dp[x-c])
        if dp[amount]==amount+1:
            return -1
        return dp[-1]