from sys import stdin
n, k = map(int, stdin.readline().strip().split())
data = [int(entry) if entry[-1].isnumeric() else entry for entry in stdin.readline().strip().split()]
tmp = []

for i in range(len(data)):
    if data[i] != 'undo' and data[i-1] != 'undo':
        tmp.append(data[i])  
    elif data[i-1] == 'undo':
        tmp = tmp[:-data[i]]
    else:
        pass
    
print sum(tmp) % n
