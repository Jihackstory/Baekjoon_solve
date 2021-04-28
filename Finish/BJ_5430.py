# 백준 5430 AC
# 구현, 자료구조, 문자열, 파싱, 덱
# 골드 5

import sys

T = int(sys.stdin.readline())

for _ in range(T):

    func_set = str(sys.stdin.readline().strip())
    N = int(sys.stdin.readline())
    data = str(sys.stdin.readline().strip())
    data = list(data[1:-1].split(','))
    if data[0] == '':
        data = []
    R_num = 0
    error = 0
    tmp = 0

    for func in func_set:

        if func == 'R':
            R_num += 1

        elif func == 'D':
            if data:
                data.pop(tmp)
            else:
                error = 1
                break

        if R_num % 2:
            tmp = -1
        else:
            tmp = 0

    if R_num % 2:
        data = data[::-1]

    if error:
        print('error')
    else:
        print('[' + ','.join(data) + ']')


