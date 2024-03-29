'''
You are given an integer array 'coins' representing coins of different denominations and an integer 'amount' representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.

ex.1
Input: amount = 5, coins = [1,2,5]
Output: 4 
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1

ex.2
Input: amount = 3, coins = [2]
Output: 0

ex.3
Input: amount = 10, coins = [10]
Output: 1
'''
def change(amount, coins):
    dp = [0] * (amount+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, amount+1):
            # print(i)
            if coin <=i:
                print(i-coin)
                dp[i] += dp[i - coin]
    print(dp)
    return dp[amount]

amount = 5
coins = [1,2,5]
print(change(amount, coins))