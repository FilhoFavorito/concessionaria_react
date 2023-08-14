def change(amount, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                print(dp[i])

        return dp[-1]

change(5,[1,2,5])