# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # initialize an array full of infinities to show that unreachable 
        # amounts would take infinite coins
        dp = [float('inf')] * (amount + 1)
        
        # set the total number of coins needed to reach amount 0 to 0
        dp[0] = 0
        # iterate through all of the coins
        for coin in coins:
            # loop through the amount until you reach the point 
            # where the coin outsizes the amount
            for i in range(coin, amount + 1):
                # save the lowest value between the previously saved value
                # and the new value +1 coin -coin's value from remaining amount 
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        if dp[amount] == float('inf'):
            return -1 
        else:
            return dp[amount]