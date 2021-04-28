import sys

MAX_LEN = 600000


class Edit:

    def __init__(self, init_string):
        self.sting_L = init_string
        self.sting_R = []

    def command_L(self):
        if self.sting_L:
            self.sting_R.append(self.sting_L.pop())

    def command_D(self):
        if self.sting_R:
            self.sting_L.append(self.sting_R.pop())

    def command_B(self):
        if self.sting_L:
            self.sting_L.pop()

    def command_P(self, ch):
        self.sting_L.append(ch)

    def string_print(self):
        tmp = self.sting_R
        tmp.reverse()

        print(''.join(self.sting_L + tmp))


edit_data = list(sys.stdin.readline().strip())
editor = Edit(edit_data)

N = int(sys.stdin.readline())

for _ in range(N):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L':
        editor.command_L()
    elif command[0] == 'D':
        editor.command_D()

    elif command[0] == 'B':
        editor.command_B()

    elif command[0] == 'P':
        editor.command_P(command[1])

editor.string_print()
