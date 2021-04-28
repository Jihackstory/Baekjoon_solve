# 백준 1181 단어 정렬
# 문자열, 정렬

import sys

N = int(sys.stdin.readline())

data = set()

for _ in range(N):
    data.add(str(sys.stdin.readline()))

data = list(data)

data = sorted(data, key=lambda x: (len(x), x))

print(''.join(data))

