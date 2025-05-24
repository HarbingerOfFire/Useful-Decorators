####Decorators#####
import os

try:
    __file__
except NameError:
    __file__ = os.getcwd()+"<stdin>"
    
import time
def stopwatch(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

def cache(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def log(func):
    def wrapper(*args, **kwargs):
        print(f"[{time.time()}] Function '{func.__name__}' called with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def log_file(filename=f"{__file__}.log"):
    def decorator(funct):
        print(f"Function '{funct.__name__}' will log to file: {filename}")
        def wrapper(*args, **kwargs):
            with open(filename, 'a') as f:
                f.write(f"[{time.time()}] Function '{funct.__name__}' called with arguments: {args} and keyword arguments: {kwargs}\n")
            return funct(*args, **kwargs)
        return wrapper
    return decorator

def retry(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            raise Exception(f"Function '{func.__name__}' failed after {max_retries} attempts")
        return wrapper
    return decorator

if __name__ == "__main__":
    # Example usage of decorators

    #@<your_decorator>
    def example_function(x, y):
        time.sleep(1)  # Simulate a time-consuming operation
        return x + y

    print(example_function(3, 4))
    #print(example_function(3, 4))  # This call should hit the cache when uncommented
