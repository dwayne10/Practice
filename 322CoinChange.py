class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if not coins or amount is None:
            return -1
        if amount == 0:
            return 0
        res = [amount + 1 for _ in range(amount + 1)]
        res[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                res[i] = min(res[i], res[i - coin] + 1)

        return -1 if res[amount] > amount else res[amount]

    