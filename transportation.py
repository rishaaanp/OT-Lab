import numpy as np

def vogel_approximation_method(cost_matrix, supply, demand):
    supply = supply.copy()
    demand = demand.copy()
    m, n = len(supply), len(demand)
    allocation = [[0] * n for _ in range(m)]
    cost = np.array(cost_matrix)

    while True:
        row_penalties = []
        for i in range(m):
            row = [cost[i][j] for j in range(n) if demand[j] > 0]
            if supply[i] > 0 and len(row) >= 2:
                sorted_row = sorted(row)
                penalty = sorted_row[1] - sorted_row[0]
            elif supply[i] > 0 and len(row) == 1:
                penalty = row[0]
            else:
                penalty = -1
            row_penalties.append(penalty)

        col_penalties = []
        for j in range(n):
            col = [cost[i][j] for i in range(m) if supply[i] > 0]
            if demand[j] > 0 and len(col) >= 2:
                sorted_col = sorted(col)
                penalty = sorted_col[1] - sorted_col[0]
            elif demand[j] > 0 and len(col) == 1:
                penalty = col[0]
            else:
                penalty = -1
            col_penalties.append(penalty)

        max_row_penalty = max(row_penalties)
        max_col_penalty = max(col_penalties)

        if max_row_penalty == -1 and max_col_penalty == -1:
            break  

        if max_row_penalty >= max_col_penalty:
            i = row_penalties.index(max_row_penalty)
            min_cost = float('inf')
            for j in range(n):
                if demand[j] > 0 and cost[i][j] < min_cost:
                    min_cost = cost[i][j]
                    min_index = j
        else:
            j = col_penalties.index(max_col_penalty)
            min_cost = float('inf')
            for i in range(m):
                if supply[i] > 0 and cost[i][j] < min_cost:
                    min_cost = cost[i][j]
                    min_index = i
            i = min_index

        j = min_index
        x = min(supply[i], demand[j])
        allocation[i][j] = x
        supply[i] -= x
        demand[j] -= x

    return allocation

def calculate_total_cost(allocation, cost_matrix):
    total = 0
    for i in range(len(allocation)):
        for j in range(len(allocation[0])):
            total += allocation[i][j] * cost_matrix[i][j]
    return total

# Example 
cost_matrix = [
    [19, 30, 50, 10],
    [70, 30, 40, 60],
    [40, 8, 70, 20]
]

supply = [7, 9, 18]
demand = [5, 8, 7, 14]

allocation = vogel_approximation_method(cost_matrix, supply, demand)

print("Initial feasible allocation (VAM):")
for row in allocation:
    print(row)

total_cost = calculate_total_cost(allocation, cost_matrix)
print(f"Total transportation cost: {total_cost}")
