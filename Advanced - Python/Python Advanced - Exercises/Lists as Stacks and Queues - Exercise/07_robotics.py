from collections import deque


def create_timer(timer: int) -> str:
    hrs = timer // 3600 % 24
    mins = (timer % 3600) // 60
    secs = timer % 60

    return f"{hrs:02}:{mins:02}:{secs:02}"


def timer_to_seconds(timer: str) -> int:
    hrs, mins, secs = [int(x) for x in timer.split(":")]
    return (hrs * 60 * 60) + (mins * 60) + secs


stop_command = "End"
robots = input().split(";")
starting_time = timer_to_seconds(input())
robots_que = []

for robot in robots:
    robot_name, robot_time = robot.split("-")
    robots_que.append({
        "name": robot_name,
        "work_every": int(robot_time),
        "available_at": starting_time
    })


products_que = deque()
command = input()
while command != stop_command:
    products_que.append(command)
    command = input()

while products_que:
    starting_time += 1
    product = products_que.popleft()

    for i in range(len(robots_que)):
        robot = robots_que[i]
        if starting_time >= robot["available_at"]:
            robots_que[i]["available_at"] = starting_time + robot["work_every"]
            print(f"{robot['name']} - {product} [{create_timer(starting_time)}]")
            break
    else:
        products_que.append(product)
