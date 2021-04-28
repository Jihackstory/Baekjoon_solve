# 백준 1158 요세푸스 문제
# 자료구조, 큐
# 실버 5

import sys

N, K = list(map(int, sys.stdin.readline().split()))
data = [i+1 for i in range(N)]
result = []
loc = 0
while data:

    # 첫번째 도전
    # loc = K % len(data) - 1
    # data = data[loc:] + data[:loc]
    # result.append(str(data.pop(0)))

    # 두번째 도전
    loc = (loc + K - 1) % len(data)
    result.append(str(data.pop(loc)))

print('<' + ', '.join(result) + '>')

