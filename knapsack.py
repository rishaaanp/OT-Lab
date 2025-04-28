def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  
            w -= weights[i - 1]

    selected_items.reverse()  
    return dp[n][capacity], selected_items

#Example 
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, selected_items = knapsack_01(values, weights, capacity)

print("Maximum Value that can be obtained:", max_value)
print("Indices of items included in the knapsack:", selected_items)

print("Items included:")
for idx in selected_items:
    print(f"Item {idx}: Value = {values[idx]}, Weight = {weights[idx]}")
