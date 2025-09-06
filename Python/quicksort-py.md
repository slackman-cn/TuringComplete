https://www.geeksforgeeks.org/quick-sort-algorithm/

https://iyedb.github.io/algorithms/2014/05/09/sort-10-million.html
```
生成0到32767范围内的随机数
echo $RANDOM
echo ${RANDOM:0:3}

the range  
python3 -c "import random; print(random.random())"       // 0 to 1
python3 -c "import random; print(random.randint(1, 10))" // 1 to 10

n=$(($minimum + $RANDOM % $maximum))
echo $(( $RANDOM % 50 + 1 ))
random_number=$(($RANDOM % ($max - $min + 1) + $min))
```


简单功能，使用脚本实现，Python 优于 Bash
```
#!/usr/bin/env python
import random
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
