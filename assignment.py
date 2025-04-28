from scipy.optimize import linear_sum_assignment
import numpy as np

def solve_assignment_problem(cost_matrix):
    cost = np.array(cost_matrix)
    row_ind, col_ind = linear_sum_assignment(cost)
    total_cost = cost[row_ind, col_ind].sum()

    assignments = list(zip(row_ind, col_ind))

    return assignments, total_cost

# Example
cost_matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

assignments, total_cost = solve_assignment_problem(cost_matrix)

print("Optimal Assignments (worker -> task):")
for worker, task in assignments:
    print(f"Worker {worker} assigned to Task {task}")

print(f"Minimum Total Cost: {total_cost}")
