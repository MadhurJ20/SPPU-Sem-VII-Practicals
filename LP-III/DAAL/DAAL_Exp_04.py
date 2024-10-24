'''
Madhur Jaripatke
Roll No. 52
BE A Computer
RMDSSOE, Warje, Pune
'''
'''
Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and 
bound strategy.
'''
def knapsack_01(values, weights, capacity):
    n = len(values)
    
    # Create a table to store the maximum values for different subproblems
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the items selected
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    selected_items.reverse()

    return dp[n][capacity], selected_items

# Example usage
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    max_capacity = 50

    max_value, selected_items = knapsack_01(values, weights, max_capacity)

    print("Selected Items:")
    for item in selected_items:
        print(f"Item with weight {weights[item]} and value {values[item]}")

    print(f"Maximum value achievable: {max_value}")