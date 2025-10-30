## PyInstaller

https://pyinstaller.org/en/stable/
```
pyinstaller /path/to/yourscript.py

单个文件 (-F, --onefile)
    pyinstaller --onefile script.py
    pyinstaller -F script.py

图标 (-i, --icon 需要ico格式)
    pyinstaller --onefile --icon=app.ico script.py
    

GUI隐藏控制台 (-w, --windowed, --noconsole)
    pyinstaller --onefile --noconsole script.py
    pyinstaller -F -w demo.py

静态资源
https://github.com/r0x0r/pywebview/tree/master/examples/todos
    pyinstaller -F -w --add-data 'index.html;.' demo.py


方式2
python -m PyInstaller app.spec
```

安装/ 常见问题
```
requests
pypdf
retrying
cairosvg

pip install -r requirements.txt
pip install pyinstaller

## 动态链接库（DLL）缺失
使用--hidden-import参数手动指定缺失的模块

## PE环境运行报错
RuntimeError: Failed to create a default .NET runtime, which would
                    have been "netfx" on this system. Either install a
                    compatible runtime or configure it explicitly via
                    `set_runtime` or the `PYTHONNET_*` environment variables
                    (see set_runtime_from_env).
[PYI-4504:ERROR] Failed to execute script 'hello' due to unhandled exception!
不能解决 pyinstaller --hidden-import=clr hello.py

原因：Windows 平台默认使用Edge浏览器 pythonnet（要求 .NET Framework 4.6.2 并安装了 Edge 运行时环境, 还依赖 WebView2 Runtime）
https://pywebview.idepy.com/guide/web_engine.html

不能解决：pip install pywebview[cef]
打包之后，大小120M
报错和之前一样，也依赖 .NET runtime
```


## 打包结果 demo.py

新建虚拟环境 pip install pywebview
```
import webview

if __name__ == '__main__':
    webview.create_window("Demo", "http://localhost")
    webview.start()
```

Ubuntu  16M  dist/
```
$ ls -lh dist/hello/
total 1.8M
-rwxr-xr-x 1 cnki cnki 1.8M Oct 29 14:51 hello
drwxrwxr-x 4 cnki cnki 4.0K Oct 29 14:51 _internal

$ ls _internal/
base_library.zip  libexpat.so.1  libmpdec.so.3         libuuid.so.1  webview
libbz2.so.1.0     libffi.so.8    libpython3.10.so.1.0  libz.so.1
libcrypto.so.3    liblzma.so.5   libssl.so.3           python3.10
```


Windows 18M dist/
```
$ ls -lh dist/hello/
total 3.1M
drwxr-xr-x 1 cnki 197121    0 Oct 29 14:57 _internal/
-rwxr-xr-x 1 cnki 197121 3.1M Oct 29 14:57 hello.exe*

$ ls _internal/
VCRUNTIME140.dll*                          api-ms-win-core-handle-l1-1-0.dll*              api-ms-win-crt-heap-l1-1-0.dll*
_asyncio.pyd*                              api-ms-win-core-heap-l1-1-0.dll*                api-ms-win-crt-locale-l1-1-0.dll*
_bz2.pyd*                                  api-ms-win-core-interlocked-l1-1-0.dll*         api-ms-win-crt-math-l1-1-0.dll*
_cffi_backend.cp39-win_amd64.pyd*          api-ms-win-core-libraryloader-l1-1-0.dll*       api-ms-win-crt-process-l1-1-0.dll*
_ctypes.pyd*                               api-ms-win-core-localization-l1-2-0.dll*        api-ms-win-crt-runtime-l1-1-0.dll*
_decimal.pyd*                              api-ms-win-core-memory-l1-1-0.dll*              api-ms-win-crt-stdio-l1-1-0.dll*
_elementtree.pyd*                          api-ms-win-core-namedpipe-l1-1-0.dll*           api-ms-win-crt-string-l1-1-0.dll*
_hashlib.pyd*                              api-ms-win-core-processenvironment-l1-1-0.dll*  api-ms-win-crt-time-l1-1-0.dll*
_lzma.pyd*                                 api-ms-win-core-processthreads-l1-1-0.dll*      api-ms-win-crt-utility-l1-1-0.dll*
_multiprocessing.pyd*                      api-ms-win-core-processthreads-l1-1-1.dll*      base_library.zip
_overlapped.pyd*                           api-ms-win-core-profile-l1-1-0.dll*             clr_loader/
_queue.pyd*                                api-ms-win-core-rtlsupport-l1-1-0.dll*          libcrypto-1_1.dll*
_socket.pyd*                               api-ms-win-core-string-l1-1-0.dll*              libffi-7.dll*
_ssl.pyd*                                  api-ms-win-core-synch-l1-1-0.dll*               libssl-1_1.dll*
_uuid.pyd*                                 api-ms-win-core-synch-l1-2-0.dll*               pyexpat.pyd*
api-ms-win-core-console-l1-1-0.dll*        api-ms-win-core-sysinfo-l1-1-0.dll*             python39.dll*
api-ms-win-core-datetime-l1-1-0.dll*       api-ms-win-core-timezone-l1-1-0.dll*            pythonnet/
api-ms-win-core-debug-l1-1-0.dll*          api-ms-win-core-util-l1-1-0.dll*                select.pyd*
api-ms-win-core-errorhandling-l1-1-0.dll*  api-ms-win-crt-conio-l1-1-0.dll*                setuptools-58.1.0.dist-info/
api-ms-win-core-file-l1-1-0.dll*           api-ms-win-crt-convert-l1-1-0.dll*              ucrtbase.dll*
api-ms-win-core-file-l1-2-0.dll*           api-ms-win-crt-environment-l1-1-0.dll*          unicodedata.pyd*
api-ms-win-core-file-l2-1-0.dll*           api-ms-win-crt-filesystem-l1-1-0.dll*           webview/
```


## Github Action

https://blog.996workers.org/archives/shi-yong-githubaction-jie-he-pyinstaller-ba-python-zi-dong-da-bao-cheng-exe-ying-yong

https://github.com/cmy2008/doc88_extractor/blob/main/.github/workflows/main.yml

https://github.com/JackMcKew/pyinstaller-action-windows