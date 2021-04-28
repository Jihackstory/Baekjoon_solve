import sys
n_prob = int(sys.stdin.readline())
deque = []
for _ in range(n_prob):
    command = sys.stdin.readline().rstrip()
    if 'push_front' in command:
        deque.insert(0, int(command.split()[1]))
    elif 'push_back' in command:
        deque.append(int(command.split()[1]))
    elif command == 'pop_front':
        print(deque.pop(0)) if deque else print(-1)
    elif command == 'pop_back':
        print(deque.pop()) if deque else print(-1)
    elif command == 'size':
        print(len(deque))
    elif command == 'empty':
        print(0) if deque else print(1)
    elif command == 'front':
        print(deque[0]) if deque else print(-1)
    elif command == 'back':
        print(deque[-1]) if deque else print(-1)