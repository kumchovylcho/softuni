v = int(input())
pipe_1_debit_for_one_hour = int(input())
pipe_2_debit_for_one_hour = int(input())
hours_of_missing_worker = float(input())
first_pipe = pipe_1_debit_for_one_hour * hours_of_missing_worker
second_pipe = pipe_2_debit_for_one_hour * hours_of_missing_worker
total_liters = first_pipe + second_pipe
percentage_fill = (total_liters / v) * 100
percentage_pipe_1 = first_pipe / total_liters * 100
percentage_pipe_2 = second_pipe / total_liters * 100
if total_liters <= v:
    print(f"The pool is {percentage_fill:.2f}% full. Pipe 1: {percentage_pipe_1:.2f}%. Pipe 2: {percentage_pipe_2:.2f}%.")
else:
    overflow = total_liters - v
    print(f"For {hours_of_missing_worker} hours the pool overflows with {overflow:.2f} liters.")
