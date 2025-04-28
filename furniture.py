from scipy.optimize import linprog

c = [-20, -30]
A = [
    [1, 5],  
    [3, 1],  
]
b = [125, 80]

x_bounds = (0, None)
y_bounds = (0, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

if result.success:
    x_opt = result.x[0]  
    y_opt = result.x[1]  
    max_profit = -result.fun 
    
    print(f"Optimal number of chairs: {int(x_opt)}")
    print(f"Optimal number of tables: {int(y_opt)}")
    print(f"Maximum profit: ${max_profit:.2f}")
else:
    print("No solution found.")