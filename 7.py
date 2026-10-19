
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    used = [-1] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used[i] = coin

    if dp[amount] == float('inf'):
        return -1, []

    result = []
    while amount > 0:
        coin = used[amount]
        result.append(coin)
        amount -= coin

    return len(result), result


coins = [1, 3, 4]
amount = 6

count, selected = coin_change(coins, amount)

print("Minimum Coins:", count)
print("Coins Used:", selected)
