from sys import stdin

K = int(stdin.readline().strip())

for i in range(K):
    A, B = map(int, stdin.readline().strip().split())
    N, M = map(int, stdin.readline().strip().split())
    state = {}
    for i in range(N):
        pos = stdin.readline().strip().split()
        state[i] = {'cord': [pos[0], pos[1]], 'dir': pos[2]}

    for i in range(M):
        mov = stdin.readline().strip().split()
        bot = mov[0]
        kin = mov[1]
        rep = mov[2]
        
        for i in range(rep):
            # execure move on state
            

def crash():

