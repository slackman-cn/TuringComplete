# nicegui

https://nicegui.cn/
```
python -m venv venv
source venv/bin/activate
pip install nicegui
pip install pyinstaller

默认安装nicegui-pack, 打包结果在dist/myapp, 大小129MB
nicegui-pack --name "myapp" main.py
```

## 支持 matplotlib

```
import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(0.0, 10000.0, 10)
y = numpy.log(x)
plt.title('Log Graph')
plt.plot(x, y, '-')

# Save the figure
plt.savefig("sample_plot.png")
plt.show()
```

https://zhuanlan.zhihu.com/p/670056910
```
import matplotlib
import numpy
from nicegui import ui

with ui.pyplot(figsize=(3, 2)):
    x = numpy.linspace(0.0, 10000.0, 10)
    y = numpy.log(x)
    matplotlib.pyplot.title('Log Graph')
    matplotlib.pyplot.plot(x, y, '-')

ui.run()
```


## 报错 SyntaxError: source code string cannot contain null bytes

解决办法
https://nicegui.io/documentation/section_pages_routing
```
from nicegui import native, ui

@ui.page('/other_page')
def other_page():
    ui.label('Welcome to the other side')

@ui.page('/dark_page', dark=True)
def dark_page():
    ui.label('Welcome to the dark side')

@ui.page('/')
def page():
    ui.link('Visit other page', other_page)
    ui.link('Visit dark page', dark_page)

ui.run(reload=False, port=native.find_open_port())
```


## pip list
```
Package                   Version
------------------------- ---------
aiofiles                  25.1.0
aiohappyeyeballs          2.6.1
aiohttp                   3.13.0
aiosignal                 1.4.0
altgraph                  0.17.4
annotated-types           0.7.0
anyio                     4.11.0
async-timeout             5.0.1
attrs                     25.4.0
bidict                    0.23.1
certifi                   2025.10.5
click                     8.3.0
docutils                  0.22.2
exceptiongroup            1.3.0
fastapi                   0.119.0
frozenlist                1.8.0
h11                       0.16.0
httpcore                  1.0.9
httptools                 0.7.1
httpx                     0.28.1
idna                      3.11
ifaddr                    0.2.0
itsdangerous              2.2.0
Jinja2                    3.1.6
markdown2                 2.5.4
MarkupSafe                3.0.3
multidict                 6.7.0
nicegui                   3.0.4
orjson                    3.11.3
packaging                 25.0
pip                       22.0.2
propcache                 0.4.1
pydantic                  2.12.1
pydantic_core             2.41.3
Pygments                  2.19.2
pyinstaller               6.16.0
pyinstaller-hooks-contrib 2025.9
python-dotenv             1.1.1
python-engineio           4.12.3
python-multipart          0.0.20
python-socketio           5.14.1
PyYAML                    6.0.3
setuptools                59.6.0
simple-websocket          1.1.0
sniffio                   1.3.1
starlette                 0.48.0
typing_extensions         4.15.0
typing-inspection         0.4.2
uvicorn                   0.37.0
uvloop                    0.21.0
watchfiles                1.1.0
websockets                15.0.1
wsproto                   1.2.0
yarl                      1.22.0
```