from sys import stdin

n = int(stdin.readline().strip())
bricks = list(map(int, stdin.readline().split()))

towers = 0
i = 0
for brick in bricks:
    i += 1
    if brick > i:
        towers += 1
        i = 1
    else:
        i += 1

print(towers)
