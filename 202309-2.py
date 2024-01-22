# 坐标变换（其二）
from math import sin, cos

n, m  = map(int, input().split())

def num(x):
    if '.' in x:
        return float(x)
    else:
        return int(x)

listT = []
for i in range(n):
    listT.append(list(map(num, input().split())))

listM = []
for i in range(m):
    listM.append(list(map(int, input().split())))

for i in range(m):
    x, y = listM[i][2], listM[i][3]
    for j in range(listM[i][0]-1, listM[i][1]):
        if listT[j][0] == 1:
            x *= listT[j][1]
            y *= listT[j][1]
        else:
            x, y = x * cos(listT[j][1]) - y * sin(listT[j][1]), x * sin(listT[j][1]) + y * cos(listT[j][1])
    print('%.3f'%x, '%.3f'%y)
