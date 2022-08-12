number_of_easter_breads = int(input())
number_of_eggs = int(input())
kg_of_cookies = int(input())
easter_bread = 3.20
eggs = 4.35     # for 1 carton = 12 quantity
cookies = 5.40
paint_for_eggs = 0.15
cartons = number_of_eggs * 12
total = (number_of_easter_breads * easter_bread) + (number_of_eggs * eggs) + (kg_of_cookies * cookies) + (cartons * paint_for_eggs)
print(f"{total:.2f}")
