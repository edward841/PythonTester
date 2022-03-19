from functools import lru_cache
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.process_time()
        
        result = func(*args, **kwargs)
        
        end = time.process_time()
        elapsed = end - start
        
        return result 
    return wrapper

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

def out(x):
    print(x)

@fancytimer(outfunc=out)
def fibbonacci1(n):
    a = 1
    b = 1
    for _ in range(2,n):
        a,b = b, a+b
    return b

def fibbonacci2(n):
    if n <= 2:
        return 1
    return fibbonacci2(n-1) + fibbonacci2(n-2)

@lru_cache
def fibbonacci3(n):
    if n <= 2:
        return 1
    return fibbonacci2(n-1) + fibbonacci2(n-2)

if __name__ == "__main__":
    print("Testing decorators in python")


    for i in range(1,10):
        print(fibbonacci1(i))
