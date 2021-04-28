# 백준 11650 좌표 정렬하기
# 정렬
# 실버 5

import sys

N = int(sys.stdin.readline())

data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort()

for idx in range(N):
    print(f'{data[idx][0]} {data[idx][1]}')

