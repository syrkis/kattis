from sys import stdin
n, m, q, s = map(int, stdin.readline().strip().split())
D = {}

for i in range(m):
    u, v, w = map(int, stdin.readline().strip().split())
    D[u] = {v: w}
    D[v] = {u: w}

