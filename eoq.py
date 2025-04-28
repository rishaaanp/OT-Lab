import math

def calculate_eoq(annual_demand, ordering_cost, holding_cost_per_unit):
    eoq = math.sqrt((2 * annual_demand * ordering_cost) / holding_cost_per_unit)
    return eoq

#Example
annual_demand = 1000  
ordering_cost = 50    
holding_cost_per_unit = 2  

eoq = calculate_eoq(annual_demand, ordering_cost, holding_cost_per_unit)

print(f"Optimal Economic Order Quantity (EOQ): {eoq:.2f} units")
