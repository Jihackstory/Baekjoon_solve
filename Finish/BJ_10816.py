# 백준 10816 숫자 카드 2
# 자료구조, 이분탐색, 해시를 사용한 집합과 맵
# 실버 4

import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
check_card = list(map(int, sys.stdin.readline().split()))

# 시간초과됨
# for idx in range(M):
#     print(card.count(check_card[idx]), end=' ')

# 시간초과됨
card_num = {}
for idx in card:

    if str(idx) in card_num:
        card_num[str(idx)] += 1
    else:
        card_num[str(idx)] = 1

for idx in check_card:

    if str(idx) in card_num:
        print(card_num[str(idx)], end=' ')
    else:
        print('0', end=' ')

# 시간초과
# for idx in check_card:
#
#     if idx in card:
#         print(card.count(idx), end=' ')
#     else:
#         print('0', end=' ')
