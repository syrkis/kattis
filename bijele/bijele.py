# vim bijele.py
#   a kattis problem sollution
# by: Noah Syrkis

# imports
import sys

# setup
_has = sys.stdin.readline()
_has = [int(i) for i in _has.split()]
_tar = [1, 1, 2, 2, 2, 8]
_out = []

# output
for i in range(len(_has)):
    _out.append(str(_tar[i] - _has[i]))
print(" ".join(_out))
