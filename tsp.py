def totalCost(mask, curr, n, cost, memo, path_tracker):
    if mask == (1 << n) - 1:      
        return cost[curr][0]
    
    if memo[curr][mask] != -1:
        return memo[curr][mask]

    ans = float('inf')
    best_next_city = -1
    for i in range(n):      
        if (mask & (1 << i)) == 0: 
            result = cost[curr][i] + totalCost(mask | (1 << i), i, n, cost, memo, path_tracker)
            if result < ans:
                ans = result
                best_next_city = i

    memo[curr][mask] = ans
    path_tracker[curr][mask] = best_next_city
    return ans

def reconstructPath(n, cost, memo, path_tracker):
    mask = 1  
    curr = 0
    path = [curr]
    while True:
        next_city = path_tracker[curr][mask]
        if next_city == -1:
            break
        path.append(next_city)
        mask |= (1 << next_city)
        curr = next_city
    return path

def tsp(cost):
    n = len(cost)
    memo = [[-1] * (1 << n) for _ in range(n)]
    path_tracker = [[-1] * (1 << n) for _ in range(n)]
    total_cost = totalCost(1, 0, n, cost, memo, path_tracker)

    path = reconstructPath(n, cost, memo, path_tracker)
    return total_cost, path

# Example
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
total_cost, path = tsp(cost)

print(f"Minimum Cost: {total_cost}")
print(f"Optimal Path: {path}")