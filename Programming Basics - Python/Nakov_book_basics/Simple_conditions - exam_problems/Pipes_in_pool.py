import math
volume_of_the_pool = int(input())
debit_pipe_one_for_one_hour = int(input())
debit_pipe_two_for_one_hour = int(input())
hours_missing_worker = float(input())
water = (debit_pipe_one_for_one_hour + debit_pipe_two_for_one_hour) * hours_missing_worker
if water <= volume_of_the_pool:
    first_pipe_percentage = math.trunc((((debit_pipe_one_for_one_hour * hours_missing_worker) / water) * 100))
    second_pipe_percentage = math.trunc((((debit_pipe_two_for_one_hour * hours_missing_worker) / water) * 100))
    water_in_pool_percentage = math.trunc(((water / volume_of_the_pool) * 100))
    print(f"The pool is {water_in_pool_percentage}% full.Pipe 1:{first_pipe_percentage}%.Pipe 2:{second_pipe_percentage}%.")
elif water > volume_of_the_pool:
    overflow = water - volume_of_the_pool
    print(f"For {hours_missing_worker} hours the pool overflows with {overflow} liters.")
