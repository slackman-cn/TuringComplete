import math


class Calculator:
    a = 0
    b = 0
    ops = ''
    input_stream = []
    def __init__(self):
        pass
    def clear(self):
        print(self.input_stream)
        self.input_stream = []
        self.a = 0
        self.b = 0
        self.ops = ''
    def input_num(self, n: int):
        print(f'input: {n}')
        self.input_stream.append(str(n))
        if len(self.ops) == 0:
            self.a = self.a * 10 + n
        else:
            self.b = self.b * 10 + n
    # input num
    def num_0(self):
        self.input_num(0)
    def num_1(self):
        self.input_num(1)
    def num_2(self):
        self.input_num(2)
    def num_3(self):
        self.input_num(3)
    def num_4(self):
        self.input_num(4)
    def num_5(self):
        self.input_num(5)
    def num_6(self):
        self.input_num(6)
    def num_7(self):
        self.input_num(7)
    def num_8(self):
        self.input_num(8)
    def num_9(self):
        self.input_num(9)
    # input ops
    def ops_add(self):
        self.ops = 'add'
        self.input_stream.append('+')
    def ops_sqrt(self):
        self.ops = 'sqrt'
        self.input_stream.append('sqrt')
        print(math.sqrt(self.a))
    def result(self):
        print(f'{self.a}+{self.b}={self.a + self.b}')
        self.clear()
        return 'ok'

calc = Calculator()
board_button = ['1', '2', '3', '+', '1', '=']
board_click = [ calc.num_1, calc.num_2, calc.num_3, calc.ops_add, calc.num_1, calc.result ]

for x in board_click:
    x()
calc.result()