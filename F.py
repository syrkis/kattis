from sys import stdin

K = int(stdin.readline().strip())
A, B = map(int, stdin.readline().strip().split())

class Board:

    board = None

    def __init__(self, **kwargs):
        exec(f"self.{k} = {v}")

    def genesis(self):
        self.board = [[''] * (self.A + 2)] * (self.B * 2)

    def populate(self, x, y, t):
        self.board[y+1][x+1] = t

    def move(self, robot, kind, count):
              

bot = Robot(p=(1, 1) d='E')

