# cetvrta.py
#   sollution to a kattis problem
# by: Noah Syrkis

# imports
import sys

# reading
_as = []; _bs = []
for line in sys.stdin:
    ab = line.split()
    a = int(ab[0]) 
    b = int(ab[1])
    _as.append(a)
    _bs.append(b)

# determination
_as.sort()
_bs.sort()

if _as[0] == _as[1]:
    x = _as[-1]
else:
    x = _as[0]

if _bs[0] == _bs[1]:
    y = _bs[-1]
else:
    y = _bs[0]

# output
sys.stdout.write(f"{x} {y}\n")
