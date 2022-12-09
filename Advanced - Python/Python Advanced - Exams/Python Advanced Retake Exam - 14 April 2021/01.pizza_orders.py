from collections import deque
pizza_orders = deque(int(x) for x in input().split(", ") if 0 < int(x) <= 10)
employees = deque(int(x) for x in input().split(", "))
total_pizzas = 0
while pizza_orders and employees:
    current_order = pizza_orders.popleft()
    employee_capacity = employees.pop()
    if current_order > employee_capacity:
        current_order -= employee_capacity
        total_pizzas += employee_capacity
        pizza_orders.appendleft(current_order)
        continue
    total_pizzas += current_order
if not pizza_orders:
    print(f"""
    All orders are successfully completed!
    Total pizzas made: {total_pizzas}
    Employees: {', '.join(str(x) for x in employees)}
""")
elif pizza_orders:
    print(f"""
    Not all orders are completed.
    Orders left: {', '.join(str(x) for x in pizza_orders)}
""")
