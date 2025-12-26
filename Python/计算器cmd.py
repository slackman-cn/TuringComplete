import math
from decimal import Decimal

# 2个寄存器;  ADD a,b; a+=b
# 也可以用Stack
# 状态机怎么实现 (1,1) ADD (2,0)
class Calculator:
    def __init__(self):
        self.a = Decimal(0) # 正数位
        self.b = Decimal(0)
        self.af = Decimal(0.0) # 小数位
        self.bf = Decimal(0.0)
        self.ops = ''
        self.input_stream = []
    def clear(self):
        print(str.join( '', self.input_stream))
        self.input_stream = []
        self.a = Decimal(0) # 正数位
        self.b = Decimal(0)
        self.af = Decimal(0.0) # 小数位
        self.bf = Decimal(0.0)
        self.ops = ''
    # input num
    def input_dot(self):
        self.input_stream.append('.')
        if len(self.input_stream) == 1 or len(self.ops) == 0:
            self.af = Decimal(1.0)  # .2   1.2
        else:
            self.bf = Decimal(1.0)
    def input_num(self, n: int):
        self.input_stream.append(str(n))
        if len(self.ops) == 0:
            if self.af == 0:
               self.a = self.a * 10 + n
            else:
                self.af = self.af * 10 + n
        else:
            if self.bf == 0:
                self.b = self.b * 10 + n
            else:
                self.bf = self.bf * 10 + n
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
    def input_ops(self, ops: str):
        self.ops = ops
        self.input_stream.append(ops)
    def call_ops(self):
        if self.af > 0:
            while self.af > 10:
                self.af = self.af / 10
            self.a = self.a + self.af - 1
            self.af = 0
        if self.bf > 0:
            while self.bf > 10:
                self.bf = self.bf / 10
            self.b = self.b + self.bf - 1
            self.bf = Decimal(0)
        if self.b != 0:
            if self.ops == '+':
                self.a = self.a + self.b
            elif self.ops == '-':
                self.a = self.a - self.b
            elif self.ops == 'x':
                self.a = self.a * self.b
            elif self.ops == '÷':
                self.a = self.a / self.b
            self.b = Decimal(0)
        return self.a
    def ops_add(self):
        # 0+a; a+b; a+b+c
        # 0-a; a+(-b);
        self.input_ops('+')
        self.call_ops()
    def ops_minus(self):
        self.input_ops('-')
        self.call_ops()
    def ops_multiply(self):
        self.input_ops('x')
        self.call_ops()
    def ops_divide(self):
        self.input_ops('÷')
        self.call_ops()
    # SQRT a
    def ops_sqrt(self):
        self.call_ops()
        self.ops = 'sqrt'
        self.input_stream.append('<sqrt>')
        self.a = math.sqrt(self.a)
    def ops_sign(self):
        self.ops = 'sign'
        self.input_stream.append('<sign>')
        if self.b != 0:
            self.b = -self.b
        else:
            self.a = -self.a
    def ops_reci(self):
        self.call_ops()
        self.ops = 'reci'
        self.input_stream.append('<reci>')
        self.a = 1 / self.a
    def result(self):
        self.call_ops()
        print(f'Result: {self.a}')
        self.clear()

calc = Calculator()

board_input = {
    '0': calc.num_0,
    '1': calc.num_1,
    '2': calc.num_2,
    '3': calc.num_3,
    '4': calc.num_4,
    '5': calc.num_5,
    '6': calc.num_6,
    '7': calc.num_7,
    '8': calc.num_8,
    '9': calc.num_9,
    '.': calc.input_dot,
    '+': calc.ops_add,
    '-': calc.ops_minus,
    'x': calc.ops_multiply,
    '÷': calc.ops_divide,
    '=': calc.result,
    ##
    'SIGN': calc.ops_sign,
    'SQRT': calc.ops_sqrt,
    'RECI': calc.ops_reci,
}
sequence_list = [
    '1=',
    '1+23=',
    '1+23+45=',
    '2-3=',
    '2-3-4=',
    '2x3=',
    '1x2x3=',
    '2÷3=',
    '1÷2÷3='
]

sequence_list = [
    ['2', 'SIGN', '='],
    ['2', 'SIGN', 'SIGN', '='],
    ['1', '6', 'SQRT', '='],
    ['1', '6', 'SQRT', 'SQRT', '='],
    ['2', 'RECI', '='],
    ['2', 'RECI', 'RECI', '='],
]

sequence_list = [
    '.2='
    '1.2+23=',
]

for seq in sequence_list:
    for btn in seq:
        board_input[btn].__call__()
    print('-----------------')