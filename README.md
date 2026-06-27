# Python Plus

一个增强版 Python 交互式解释器，在标准 Python REPL 中内置了常用 shell 命令，让命令行操作无需离开 Python 环境。

## 特性

- **内建 shell 命令**：直接在 Python 解释器中执行 `ls`、`cd`、`cls`（或 `clear`）
- **提示符显示当前路径**：`ps1` 提示符中实时展示当前工作目录，无需频繁 `pwd`
- **可扩展命令系统**：通过 `@python_plus.register(...)` 装饰器轻松注册自定义命令
- **完全兼容标准 REPL**：Python 语法和交互功能不受任何影响

## 快速开始

```bash
python main.py
```

启动后你将看到类似如下界面：

```
/home/quiser/projects/python_plus >>>
```

此时你可以像使用普通 Python 解释器一样编写代码，也可以直接使用内建命令：

## 内建命令

| 命令 | 用法 | 说明 |
|------|------|------|
| `ls` | `ls` 或 `ls /path/to/dir` | 列出当前或指定目录的文件 |
| `cd` | `cd /path/to/dir` 或 `cd ~` | 切换工作目录，支持 `~` 展开 |
| `cls` | `cls` | 清屏（Windows 用 `cls`，Unix 用 `clear`） |

## 自定义命令

通过装饰器即可注册新命令：

```python
@python_plus.register("hello")
def hello_func(name: str = "World"):
    print(f"Hello, {name}!")
```

支持带参数的命令调用，参数解析会自动处理引号和空格。

## 依赖

- Python 3.9+

标准库即可运行，无需额外安装依赖。

## 许可证

MIT
