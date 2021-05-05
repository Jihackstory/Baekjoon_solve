# 백준 1004 어린 왕자
# 다이나믹 프로그래밍
# 실버 3

import sys

data = []
n = int(sys.stdin.readline())

for i in range(n):
    tmp = []
    tmp.append(list(map(int, sys.stdin.readline().split())))
    m = int(sys.stdin.readline())

    for j in range(m):
        tmp.append(list(map(int, sys.stdin.readline().split())))
    data.append(tmp)

    count = 0
    x1, y1, x2, y2 = data[i][0]
    for j in range(1, len(data[i])):

        c_x, c_y, c_r = data[i][j]
        check_1 = (x1 - c_x) ** 2 + (y1 - c_y) ** 2
        check_2 = (x2 - c_x) ** 2 + (y2 - c_y) ** 2

        # XOR 연산
        if (check_1 < c_r ** 2) ^ (check_2 < c_r ** 2):
            count += 1

    print(count)