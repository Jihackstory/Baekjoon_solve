import sys


class Stack:

    def __init__(self):
        self.size = 0
        self.empty = 1
        self.top = -1
        self.stack_list = []

    def command(self, command_list):

        if command_list[0] == 'push':
            self.push(command_list[1])

        elif command_list[0] == 'pop':
            self.pop()

        elif command_list[0] == 'size':
            print(self.size)

        elif command_list[0] == 'empty':
            print(self.empty)

        elif command_list[0] == 'top':
            print(self.top)

    def push(self, number):
        self.stack_list.append(number)
        self.top = number
        self.size += 1
        self.empty = 0

    def pop(self):
        if self.empty:
            print('-1')
        else:
            print(self.stack_list.pop())
            self.size -= 1
            if not self.size:
                self.top = -1
                self.empty = 1
            else:
                self.top = self.stack_list[-1]


N = int(sys.stdin.readline())

stack_A = Stack()
for _ in range(N):

    command = list(sys.stdin.readline().split())
    stack_A.command(command)


