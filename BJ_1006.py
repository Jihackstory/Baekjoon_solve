import sys

T = int(sys.stdin.readline())
INF = int(1e9)

for _ in range(T):
    N, W = map(int, sys.stdin.readline().split())
    in_circle = list(map(int, sys.stdin.readline().split()))
    out_circle = list(map(int, sys.stdin.readline().split()))

    cover = [[] for i in range(2 * N)]
    num_cover = [[0, i] for i in range(2 * N)]
    tmp = []
    cur_node = 0
    total_count = 0
    for cur_node in range(N):

        if in_circle[cur_node] + out_circle[cur_node] <= W:
            cover[cur_node].append(cur_node + N)
            num_cover[cur_node][0] += 1

            cover[cur_node + N].append(cur_node)
            num_cover[cur_node + N][0] += 1

            total_count += 1

        if in_circle[cur_node] + in_circle[(cur_node + 1) % N] <= W:
            cover[cur_node].append((cur_node + 1) % N)
            num_cover[cur_node][0] += 1

            cover[(cur_node + 1) % N].append(cur_node)
            num_cover[(cur_node + 1) % N][0] += 1

            total_count += 1

        if out_circle[cur_node] + out_circle[(cur_node + 1) % N] <= W:
            cover[cur_node + N].append((cur_node + 1) % N + N)
            num_cover[cur_node + N][0] += 1

            cover[(cur_node + 1) % N + N].append(cur_node + N)
            num_cover[(cur_node + 1) % N + N][0] += 1

            total_count += 1

        if num_cover[cur_node][0] == 0:
            num_cover[cur_node][0] = INF

        if num_cover[cur_node + N][0] == 0:
            num_cover[cur_node + N][0] = INF

    count = 2 * N

    already_set = set()
    for _ in range(total_count):

        tmp = min(num_cover)
        if tmp[0] == INF:
            break

        # node1 = num_cover.index(tmp)
        node1 = tmp[1]
        node2 = cover[node1][0]

        if already_set.isdisjoint([node1, node2]):
            count -= 1
            already_set.update([node1, node2])

        cover[node1].remove(node2)
        num_cover[node1][0] -= 1
        if num_cover[node1][0] == 0:
            num_cover[node1][0] = INF

        cover[node2].remove(node1)
        num_cover[node2][0] -= 1
        if num_cover[node2][0] == 0:
            num_cover[node2][0] = INF

    print(count)
