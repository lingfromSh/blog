---
title: 剑指Offer - Singleton 单例模式编写
date: 2022-08-26 11:50:11
tags:
    - Offer
    - Singleton
    - Coding Regulartion
---

# 剑指Offer - Singleton 单例模式


## 基础实现

初级水平

未能考虑多线程下的情况

```python
class Singleton:
    """用类变量实现单例模式"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = cls(*args, **kwargs)
            cls._instance = instance
        return cls._instance
```

## 线程安全实现

中级水平

考虑到了多线程可能不安全的场景，使用到了线程锁，但是每次锁的获取都非常耗时，应该考虑优化。

```python
import threading

class ThreadSafeSingleton:
    """用类变量和锁实现单例模式"""

    _instance = None
    _instance_lock = threading.Lock() 

    def __new__(cls, *args, **kwargs):
        # 获取线程锁进行创建
        if cls._instance_lock.acquire():

            if cls._instance is None:
                instance = cls(*args, **kwargs)
                cls._instance = instance

            cls._instance_lock.release()

        return cls._instance

```

## 优化的线程安全实现

高级水平

既考虑了线程安全场景又考虑了性能开销。出于题目的考量，已经非常好了。

```python
import threading

class ThreadSafeSingleton:
    """用类变量和锁实现单例模式"""

    _instance = None
    _instance_lock = threading.Lock() 

    def __new__(cls, *args, **kwargs):
        # 如果实例已经被创建，则直接返回已有实例实现单例需求
        if cls._instance is None and cls._instance_lock.acquire():
            # 如果实例未被创建，则获取线程锁进行创建
            instance = cls(*args, **kwargs)
            cls._instance = instance

            # 释放锁
            cls._instance_lock.release()

        return cls._instance

```

## 可复用的单例实现

```python

import threading
from inspect import isclass, getfullargspec
from dataclasses import dataclass


class ClassRequiredError(Exception):
    """装饰对象必须是类"""
    ...


def thread_safe_singleton(cls):
    """线程安全单例装饰器"""

    # 只能装饰类
    if not isclass(cls):
        raise ClassRequiredError

    original_new = getattr(cls, "__new__")
    setattr(cls, "_instance", None)
    setattr(cls, "_instance_lock", threading.Lock())

    def __new__(cls, *args, **kwargs):
        # 如果实例已经被创建，则直接返回已有实例实现单例需求
        if cls._instance is None and cls._instance_lock.acquire():
            
            # 使用类定义的创建方式创建
            try:
                instance = original_new(cls, *args, **kwargs)
            except TypeError:
                # 继承object的new
                instance = original_new(cls)
            
            cls._instance = instance

            # 释放锁
            cls._instance_lock.release()

        return cls._instance

    # 替换创建实现
    cls.__new__ = __new__
    return cls

```