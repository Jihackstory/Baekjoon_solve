import sys


class Queue:
    def __init__(self):

        self.queue = []
        self.size = 0
        self.empty = 1

    def command(self, command_list):

        if command_list[0] == 'push':
            self.push(command_list[1])

        elif command_list[0] == 'pop':
            self.pop()

        elif command_list[0] == 'size':
            print(self.size)

        elif command_list[0] == 'empty':
            print(self.empty)

        elif command_list[0] == 'front':
            if self.empty:
                print(-1)
            else:
                print(self.queue[0])

        elif command_list[0] == 'back':
            if self.empty:
                print(-1)
            else:
                print(self.queue[-1])

    def push(self, number):
        self.queue.append(number)
        self.empty = 0
        self.size += 1

    def pop(self):
        if self.empty:
            print(-1)
        else:
            print(self.queue.pop(0))
            self.size -= 1
            if not self.size:
                self.empty = 1


n = int(sys.stdin.readline())
queue = Queue()
for _ in range(n):
    command = list(sys.stdin.readline().split())
    queue.command(command)
