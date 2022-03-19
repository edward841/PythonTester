import functools
import time
from testingFiles import updateData

def fancytimer(outfunc):
    def decorator_output(func):
        def wrapper(*args, **kwargs):
            start = time.process_time()
            
            result = func(*args, **kwargs)
            
            end = time.process_time()
            outfunc(end-start)
            return result 
        return wrapper
    return decorator_output

def recordtime(output, version):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bt = time.process_time()
            result = func(*args, **kwargs)
            et = time.process_time()
            
            elapsed = et - bt
            args_repr = [repr(a) for a in args] 
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            updateData(output, version, signature, elapsed)
            return result
        return wrapper
    return decorator

@recordtime(output="fibbonacciTimes.csv", version="1")
def fibbonacci1(n):
    a = 1
    b = 1
    for _ in range(2,n):
        a,b = b, a+b
    return b

@recordtime(output="fibbonacciTimes.csv", version="2")
def fibbonacci2(n):
    if n <= 2:
        return 1
    return fibbonacci2(n-1) + fibbonacci2(n-2)

@recordtime(output="fibbonacciTimes.csv", version="3")
@functools.lru_cache
def fibbonacci3(n):
    if n <= 2:
        return 1
    return fibbonacci2(n-1) + fibbonacci2(n-2)

if __name__ == "__main__":
    print("Testing decorators in python")


    for i in range(1,10):
        print(fibbonacci3(i))
