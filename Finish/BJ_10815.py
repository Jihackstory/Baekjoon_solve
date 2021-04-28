# 8분
import sys

N = int(sys.stdin.readline())
S_card = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
check_card = list(map(int, sys.stdin.readline().split()))

for card in check_card:

    print('1' if card in S_card else '0', end=' ')