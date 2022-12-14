from collections import deque
customers = deque(int(x) for x in input().split(", "))
taxi_drivers = deque(int(x) for x in input().split(", "))
total_minutes = 0
while customers and taxi_drivers:
    current_taxi = taxi_drivers.pop()
    if customers[0] <= current_taxi:
        total_minutes += customers.popleft()
if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {total_minutes} minutes")
elif customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
