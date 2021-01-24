from sys import stdin
import math

H, v = map(int, stdin.readline().strip().split())
if v <= 180:
    print('safe')

else:
    B = abs(270 - v)
    B = math.radians(B)
    l = H / math.cos(B)
    print(int(l))
