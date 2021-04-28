# 백준 13460 구슬 탈출 2
# 구현, 그래프이론, 그래프탐색, 너비우선탐색, BFS
# 골드 2

n, m = list(map(int, input().strip().split()))
mapp = []
for _ in range(n):
    mapp.append(input())

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)
q = []
def init():
    rx, ry, bx, by, d = [0] * 5
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 'R':
                rx = i
                ry = j
            if mapp[i][j] == 'B':
                bx = i
                by = j
    q.append((rx, ry, bx, by, d))

def move(_x, _y, _dx, _dy, _c):
    while mapp[_x+_dx][_y+_dy] != '#' and mapp[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c

def bfs():
    visit = []
    while q:
        # print(q)
        # print('visit:',visit)
        rx, ry, bx, by, d = q.pop(0)
        visit.append((rx, ry, bx, by))
        if d >= 10:
            break
        for k in range(len(dx)):
            nrx, nry, rc = move(rx, ry, dx[k], dy[k], 0)
            nbx, nby, bc = move(bx, by, dx[k], dy[k], 0)
            if mapp[nbx][nby] == 'O':
                continue
            else:
                if mapp[nrx][nry] == 'O':
                    print(d+1)
                    return
                else:
                    if nrx == nbx and nry == nby:
                        if rc > bc:
                            nrx = nrx - dx[k]
                            nry = nry - dy[k]
                        elif bc > rc:
                            nbx = nbx - dx[k]
                            nby = nby - dy[k]
                        else:
                            print("Move error")
                    # print('TF', (nrx, nry, nbx, nby) in visit)
                    if not (nrx, nry, nbx, nby) in visit:
                        visit.append((nrx, nry, nbx, nby))
                        q.append((nrx, nry, nbx, nby, d+1))
    print(-1)

init()
bfs()
