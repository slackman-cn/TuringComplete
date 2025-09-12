## import json

```
json_data = {
    id: 1
}

json_str = json.dumps(json_data)
json_data = json.loads(json_str)
```


## 随机数

```
生成0到32767范围内的随机数
echo $RANDOM
echo ${RANDOM:0:3}

python3 -c "import random; print(random.random())"       // 0 to 1
python3 -c "import random; print(random.randint(1, 10))" // 1 to 10

n=$(($minimum + $RANDOM % $maximum))
echo $(( $RANDOM % 50 + 1 ))
random_number=$(($RANDOM % ($max - $min + 1) + $min))
```

## import random

```
random.seed()
def genl (max):
    cur = 0
    while cur <= max:
        yield random.randint(0, 1000000000)
        cur = cur + 1
gen = genl(10000000)
gen.send(None)
with open("dataset", "w") as f:
    for i in gen:
        f.write(str(i) + '\n')
```

## Python 语法

```
def print_hi(name):
    print(f'Hi, {name}') 
    print('hello, ' + name)

if __name__ == '__main__':
    print_hi('PyCharm')


===== 变量
len('asdfa')
int('123'), float, bool, str(1234)
ii = None
type(ii)
3 / 2  结果1.5
3 //2  结果1  向下取整

if True:
  pass
elif a == 10 or a == 11:   # and,or,not
  pass
else:
  pass

===== 数组
arr = [''] * 5
arr = [None] * 5
arr = [
    '1',
    '3',
    '4'
]
arr[0] = '1'
arr[1] = '11'
```

## 字典, 列表, 循环

```
mylist = [1,2,3]
mylist.append(4)
len(list)

mydict = {}
mydict = {'name': 'xiao', 'age': 12}
mydict['name'] = 'xiao2'
len(mydict)   # 键值对
'name' in mydict
del mydict['name']

mytuple = ('aa', 'bb')  # 不可变

===== 循环
for v in mylist:
  pass
for k,v in mydict.items():  # 键值对
  pass
for in in range(1,10):    # 不包括10  (1,10,2)步长2
  pass

mydict.keys()
mydict.values()
mydict.items()  
```

## 面向对象

```
class ATM:
   def __init__(self, id, name):
      self.id = id
      self.name = name

   def show(self):
       print(self.id, self.name)

a1 = ATM('01', 'xiao')
a1.show()
print(a1.name)


class SubATM(ATM):   # 继承
   def show(self):
      pass
```

数据类
```
from dataclasses import dataclass,field
from typing import List
from pathlib import Path

@dataclass
class Job:
    pkg_name: str
    pkg_url: str = ""
    source_dir: str = field(default=Path.home().joinpath("source"))
    source_compression: str = "tar"
    build_separate_dir: int = 0
    build_commands: List[str] = field(default_factory=list)

p = Job(pkg_name="hello")
```


## 模块, 异常

```
https://docs.python.org/zh-cn/3/library/math.html
import math
math.sin(1)

标准库 https://docs.python.org/zh-cn/3/libray/index.html
import xxx
xxx.函数
xxx.变量

from xxx import 变量,函数
from xxx import *
```

IO模块, 异常
```
with open('./aaa.txt', 'r', encoding='utf-8') as f:
   txt = f.read()  # 全部内容  read(10)只读取10字节
   row = f.readline()  # while判断 row != ''
   lines = f.readlines()
   for row in lines:
      pass

with open('./output.txt', 'w', encoding='utf-8') as f:
  #  模式w 清空, 模式a 追加,  模式r+ 读写追加
  f.write('hello\n')

try:
  xxx()
except ValueError:
  print(xxxx)
except:
  print('all error')
else:
  print('no error')
finally:
  print('程序结束')
```
