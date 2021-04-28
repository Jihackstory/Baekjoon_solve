# 백준 1002 터렛
# 수학, 기하학
# 실버 4

import sys

data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    x1, y1, r1, x2, y2, r2 = data[i]
    tmp = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    big, small = max(r1, r2), min(r1, r2)
    if tmp < big:
        if tmp == 0 and r1 == r2:
            print(-1)
        elif tmp + small < big:
            print(0)
        elif tmp + small == big:
            print(1)
        elif tmp + small > big:
            print(2)
    else:
        if tmp > r1 + r2:
            print(0)
        elif tmp == r1 + r2:
            print(1)
        elif tmp < r1 + r2:
            print(2)
