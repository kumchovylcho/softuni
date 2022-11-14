from collections import deque
price_of_bullet = int(input())
gun_barrel = int(input())
bullets = [int(bullet) for bullet in input().split()]
locks = deque([int(lock) for lock in input().split()])
reward = int(input())
bullets_shot = 0
while bullets and locks:
    bullet_damage = bullets.pop()
    if locks[0] >= bullet_damage:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    bullets_shot += 1
    if bullets_shot % gun_barrel == 0 and bullets:
        print("Reloading!")
if not locks:
    earned_money = reward - (bullets_shot * price_of_bullet)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
elif locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")