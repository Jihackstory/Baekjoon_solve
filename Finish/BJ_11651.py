# 백준 11651 좌표 정렬하기
# 정렬
# 실버 5

import sys

N = int(sys.stdin.readline())

data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort()
data.sort(key=lambda k: k[1])

for idx in range(N):
    print(f'{data[idx][0]} {data[idx][1]}')

