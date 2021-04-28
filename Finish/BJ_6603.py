# 백준 6603 로또
# 수학, 조합론, 백트래킹, 재귀
# 실버 2

import sys


def search(subS, index):

    if len(subS) == 6:
        return print(' '.join(subS))
    for idx in range(index, len(S)):
        search(subS+[S[idx]], idx+1)


while 1:
    data = list(map(str, sys.stdin.readline().split()))
    K = data[0]
    if K == '0':
        break
    S = data[1:]

    search([], 0)
    print('')

# 두번째 풀이
# from itertools import combinations
# import sys
#
# input = sys.stdin.readline
#
# while True:
#     ary = input().split()  # 문자열 -> 리스트
#
#     if (ary.pop(0) == '0'):  # 0번 index를 꺼내었을 때 0이라면
#         break
#
#     for i in combinations(ary, 6):
#         print(" ".join(i))
#
#     print()
