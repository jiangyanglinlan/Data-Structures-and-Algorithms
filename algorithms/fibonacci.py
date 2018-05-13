import time
import functools


# 方法1: 自定义缓存装饰器
def cache(func):
    memo = dict()
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args not in memo:
            memo[args] = func(*args, **kwargs)
        return memo[args]
    return wrapper


@cache
def fib(n):
    if n <= 2:
        return 1
    return fib(n-2) + fib(n-1)


# 方法2: 使用内置缓存装饰器
@functools.lru_cache(8)
def fib2(n):
    if n <= 2:
        return 1
    return fib(n-2) + fib(n-1)


# 直接递归
def fib3(n):
    if n <= 2:
        return 1
    return fib3(n-2) + fib3(n-1)


# 计时装饰器
def run_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print(f'{args[1].__name__}耗时: {t2 - t1}')
        return f
    return wrapper


@run_time
def get_fib_list(n, func):
    fib_list = []
    for i in range(1, n+1):
        fib_list.append(func(i))
    return fib_list
        
    
if __name__ == '__main__':
    l = get_fib_list(30, fib)
    print(l)

    l = get_fib_list(30, fib2)
    print(l)

    l = get_fib_list(30, fib3)
    print(l)
