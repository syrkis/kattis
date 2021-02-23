from sys import stdin
from sys import stdout
from sys import exit
from collections import deque

_map = {}
_mov = ['right', 'up', 'left', 'down']

def bfs(x=0,y=0):
    Q = deque()
    Q.append((x,y))
    seen = set()
    while Q:
        pos = Q.popleft()
        seen.add(pos)
        moves = navigator(pos[0], pos[1])
        if moves:
            for mov in moves:
                if mov not in seen:
                    Q.append(mov)
    print("no way out")

def PosUpdate(x,y,d):
    if d == 'right':
        return (x+1,y)
    if d == 'up':
        return (x,y+1)
    if d == 'left':
        return (x-1,y)
    else:
        return (x,y-1)
        
def navigator(x, y):
    _map[(x, y)] = {'posMoves' : []}
    for idx, d in enumerate(_mov):
        stdout.flush()
        print(d)
        res = stdin.readline().strip()
        _map[(x, y)][d] = res
        if res == "wall":
            pass
        elif res == "ok":
            _map[(x,y)]['posMoves'].append(PosUpdate(x,y,d))
            _rev = (idx + 2) % 2
            print(_mov[_rev])
            stdout.flush()
        elif res == "wrong":
            exit()
        else:
            exit()
                
bfs()