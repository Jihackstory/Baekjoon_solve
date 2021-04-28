# 백준 10867 중복 빼고 정렬하기
# 정렬
# 실버 5

import sys

N = int(sys.stdin.readline())

data = set(map(int, sys.stdin.readline().split()))
data = sorted(list(data))
print(' '.join(map(str, data)))