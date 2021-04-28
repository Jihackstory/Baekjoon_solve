# 백준 9012 괄호
# 자료구조, 문자열, 스택
# 실버 4

import sys

N = int(sys.stdin.readline())

for _ in range(N):
    check = 0
    data = sys.stdin.readline().strip()

    for idx in data:
        if idx == '(':
            check += 1
        else:
            check -= 1

        if check < 0:
            break
    if check == 0:
        print('YES')
    else:
        print('NO')

