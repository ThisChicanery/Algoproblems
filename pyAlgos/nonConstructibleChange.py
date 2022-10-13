def nonConstructibleChange(coins):
    coins.sort()
    currentSum = 0
    for i in range(len(coins)):
        currentSum += coins[i]
    pass