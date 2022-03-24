def maxProfit(prices):
    length = len(prices)
    diff = []
    for i in range(length - 1):
        for j in range(i+1, length):
            if prices[i] < prices[j]:
                # print(prices[i], prices[j])
                diff.append(prices[j] - prices[i])
    print(diff)

    # if len(diff) != 0:
    #     return max(diff)
    # else:
    #     return 0                 

x = [7,6,4,3,1]
y = [7,1,5,3,6,4]

# print(maxProfit(x))
# print(maxProfit(y))
# print(maxProfit(z))

# #######effcient solution #########
def maxProfit0(prices):
    left, right = 0, 1
    max_profit = 0
    while right < len(prices):
        c_profit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            max_profit = max(c_profit, max_profit)
        else:
            left = right
        right += 1
            
    return max_profit

