def coinChange(coins, amount):
    dp = [amount+1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1+dp[a-c])
    return dp[amount] if dp[amount] != amount+1 else -1




a = [1,2,5]
b = 11

print(coinChange(a,b))
# coins = [1,2,5]
# coins.sort()
# coins = coins[::-1]
# print(coins)