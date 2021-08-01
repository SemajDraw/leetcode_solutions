def maxProfit(prices):
    return calculate(prices, 0)


def calculate(prices, s):
    if s >= len(prices):
        return 0

    max = 0
    start = s
    while start < len(prices):
        maxprofit = 0
        i = start + 1
        while i < len(prices):
            if prices[start] < prices[i]:

                profit = calculate(prices, i + 1) + prices[i] - prices[start]
                if profit > maxprofit:
                    maxprofit = profit
            i += 1

        if maxprofit > max:
            max = maxprofit

        start += 1

    return max


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
