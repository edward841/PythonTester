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

def recordtime(output, version, maximum=10):
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
            updateData(output, version, signature, elapsed, maximum)
            return result
        return wrapper
    return decorator

