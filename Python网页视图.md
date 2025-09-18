---
title: https://pywebview.flowrl.com/
since: 202508
link: https://github.com/r0x0r/pywebview/tree/master/examples
---


## QuickStart

```
# 不同系统依赖不一样
pip install pywebview
sudo apt install python3-pywebview

import webview
webview.create_window('Hello world', 'https://pywebview.flowrl.com/')
webview.start()

## 前端调试
webview.start(debug=True)


## 创建测试窗口
webview.create_window('Hello world', 'index.html')

window = webview.create_window(
    'Hello World',
    html='<h1>环境配置成功！</h1>'
)

window = webview.create_window(
    'Hello World'',
    'https://pywebview.flowrl.com/',
    width=800,
    height=600,
    resizable=True,
    frameless=False
)
```


## JS 调用 Python API

```
class WebApi:
    def login(self, username, password):
        print(f"用户名: {username}, 密码: {password}")
        return "登录成功"

api = WebApi()
window = webview.create_window('登录', 'http://localhost:8080', js_api=api)
window = webview.create_window('登录', 'login.html', js_api=WebApi())
webview.start()
```

前端 JS
```
<button onclick="handleButtonClick()">执行Python函数</button>

<script>
function handleButtonClick() {
    window.pywebview.api.login('aa', '123').then(response => {
        console.log('收到响应:', response)
    })
}

const login = async () => {
    const response = await window.pywebview.api.login('aa', '123')
    console.log(response)
}
</script>
```

## JS 调用 Python API (方式2)

```
def login(username, password):
    print(f"用户名: {username}, 密码: {password}")

window = webview.create_window('登录', 'login.html')
window.expose(login)

=== 前端
window.pywebview.api.login('aa', '123').then(response => {
    console.log('收到响应:', response)
})
```

## Python API 调用 JS

```
window = webview.create_window('登录', 'login.html', js_api=Api())

# 执行JS代码
window.evaluate_js('alert("操作完成")')

# 传递复杂数据
window.evaluate_js(f'updateChart({json.dumps(data)})')
```
