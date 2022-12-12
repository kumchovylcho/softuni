jobs = [int(x) for x in input().split(", ")]
task_position = int(input())
cycles = 0
job_to_get_done = jobs[task_position]
while job_to_get_done in jobs:
    cycles += min(jobs)
    jobs.remove(min(jobs))
print(cycles)