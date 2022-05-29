def coinChange(coins, amount):
    dp = [amount+1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1+dp[a-c])
    return dp[amount] if dp[amount] != amount+1 else -1

def coinChange(coins, amount):
    dp = [0] + [float('inf') for i in range(amount)]
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                # print(f'dp[i-coin] = {dp[i-coin]}, dp{i} = {dp[i]}')
                dp[i] = min(dp[i], dp[i-coin] + 1)
    print(dp)
    if dp[-1] == float('inf'):
        return -1
    return dp[-1]


coins = [1,2,5]
amount = 11

print(coinChange(coins, amount))
# coins = [1,2,5]
# coins.sort()
# coins = coins[::-1]
# print(coins)