type_projection = input()
number_of_rows = int(input())
number_of_columns = int(input())
full_hall = number_of_rows * number_of_columns
price = 0
if type_projection == "Premiere":
    price = 12
elif type_projection == "Normal":
    price = 7.50
else:
    price = 5.00
total = price * full_hall
print(f"{total:.2f} leva")
