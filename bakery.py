from scipy.optimize import linprog

c = [-5, -3]  

A = [
    [2, 1],  
    [1, 1]     
]
b = [500, 400]

x_bounds = (100, None) 
y_bounds = (50, None)   

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

if result.success:
    chocolate_cakes = result.x[0]
    vanilla_cakes = result.x[1]
    max_revenue = -result.fun  
    print(f"Chocolate cakes: {chocolate_cakes:.2f}")
    print(f"Vanilla cakes: {vanilla_cakes:.2f}")
    print(f"Maximum revenue: ${max_revenue:.2f}")
else:
    print("No feasible solution found.")
