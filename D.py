from sys import stdin

R, C = map(int, stdin.readline().strip().split())
east = list(map(int, stdin.readline().strip().split()))
north = list(map(int, stdin.readline().strip().split()))

print('possible') if max(east) == max(north) else print('impossible')
