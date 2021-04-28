import sys


class Deque:

    def __init__(self):
        self.data = []
        self.empty = 1
        self.size = 0
        self.front_back = [-1, -1]

    def command(self, command):
        if command[0] == 'push_front':
            self.push(command[1], 1)
            self.front_back[0] = command[1]

        elif command[0] == 'push_back':
            self.push(command[1], -1)
            self.front_back[1] = command[1]

        elif command[0] == 'pop_front':
            self.pop(0)

        elif command[0] == 'pop_back':
            self.pop(-1)

        elif command[0] == 'size':
            print(self.size)

        elif command[0] == 'empty':
            print(self.empty)

        elif command[0] == 'front':
            print(self.front_back[0])

        elif command[0] == 'back':
            print(self.front_back[-1])

        else:
            print('command error')

    def push(self, number, idx):
        if idx == -1:
            self.data.append(number)
        elif idx == 1:
            self.data = [number] + self.data
        self.front_back = [self.data[0], self.data[-1]]
        self.empty = 0
        self.size += 1

    def pop(self, idx):
        if self.empty:
            print(-1)
        else:
            print(self.front_back[idx])
            self.data.pop(idx)
            self.size -= 1
            if not self.size:
                self.empty = 1
                self.front_back = [-1, -1]
            else:
                self.front_back = [self.data[0], self.data[-1]]


N = int(sys.stdin.readline())

deque = Deque()

for _ in range(N):

    command_input = list(sys.stdin.readline().split())
    deque.command(command_input)

