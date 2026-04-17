Title: Python 装饰器入门
Date: 2026-04-10
Category: 技术
Tags: Python, 装饰器, 编程
Summary: 从零开始理解 Python 装饰器的原理与用法。
Description: 一篇关于 Python 装饰器的基础教程，涵盖函数装饰器和类装饰器的常见用法。

Python 装饰器是日常开发中非常实用的语法特性。本文从基础概念出发，逐步理解装饰器的工作方式。

## 什么是装饰器

装饰器本质上是一个函数，它接受一个函数作为参数，返回一个新的函数。通过 `@` 语法，可以简洁地为现有函数添加额外功能。

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("函数调用前")
        result = func(*args, **kwargs)
        print("函数调用后")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"你好，{name}！")
```

## 常见用途

- 日志记录
- 权限验证
- 缓存
- 性能计时

## 带参数的装饰器

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"你好，{name}！")
```

装饰器让代码更加优雅和可维护，值得在日常开发中多加运用。