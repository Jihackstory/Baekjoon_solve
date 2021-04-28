# 10분 55초
import sys

N = int(sys.stdin.readline())

MAX_N = 10000
sort_set = [0]*MAX_N

for i in range(N):

    sort_set[int(sys.stdin.readline())-1] += 1

for i in range(MAX_N):

    if sort_set[i]:
        print('\n'.join(map(str, [i+1] * sort_set[i])))
