# 백준 19236 청소년 상어
#
# 골드 2
#

import sys


data = []
graph = [[] for _ in range(17)]
for i in range(4):
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp2 = []

    for j in range(4):
        tmp2 += [(tmp[2*j], tmp[2*j+1]-1)]

        graph[tmp[2*j]] = [i, j, tmp[2*j+1]]
    data.append(tmp2)



dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

shark = [0, 0]

for tmp in graph:
    print(tmp)