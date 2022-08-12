length_of_the_side_of_object = int(input())
width_of_one_tail = float(input())
length_of_one_tail = float(input())
width_of_the_bench = int(input())
length_of_the_bench = int(input())
area_of_object = length_of_the_side_of_object * length_of_the_side_of_object
area_of_one_tile = width_of_one_tail * length_of_one_tail
area_of_the_bench = width_of_the_bench * length_of_the_bench
tails_to_put = (area_of_object - area_of_the_bench) / area_of_one_tile
time_needed = tails_to_put * 0.2
print(f"{tails_to_put:.2f}")
print(f"{time_needed:.2f}")