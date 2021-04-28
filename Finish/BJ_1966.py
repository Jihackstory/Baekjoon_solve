# 백준 1966 프린터 큐
# 구현, 자료구조, 시뮬레이션, 큐
# 실버 3

import sys

N = int(sys.stdin.readline())

for _ in range(N):

    M, num = list(map(int, sys.stdin.readline().split()))
    data = list(map(int, sys.stdin.readline().split()))

    # 오름차순으로 데이터 정렬
    data_index = sorted(data)
    result = [0] * M
    idx = 0
    count = 1

    while data_index:

        if data_index[-1] == data[idx]:
            result[idx] = count
            count += 1
            data_index.pop()

        idx = (idx + 1) % M

    print(result[num])
