'''
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. Each item can only be selected once, as we don’t have multiple quantities of any item.
Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
'''


def solve_knapsack(profits, weights, capacity):
    if (not profits) or (not capacity) or (not weights):
        return 0

    dp = [[0 for _ in range(capacity + 1)] for x in range(2)]

    for i in range(2):
        dp[i][0] = 0

    for i in range(1, capacity + 1):
        dp[0][i] = profits[0] if i >= weights[0] else 0

    for i in range(1, len(weights)):
        for c in range(1, capacity + 1):
            profit1,profit2 = 0,0
            
            if c>=weights[i]:
                profit1 = profits[i] + dp[(i-1)%2][c-weights[i]]
                
            profit2 = dp[(i-1)%2][c]
            
            dp[i % 2][c] = max(profit1,profit2)

    return dp[(len(weights)-1) % 2][capacity]


if __name__ == '__main__':
    weights = [1, 2, 3, 5]
    profits = [1, 6, 10, 16]
    capacity = 7

    print(solve_knapsack(profits, weights, capacity))
