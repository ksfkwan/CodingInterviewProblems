# def decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
# def g(a=[]):
#     a.append(1)
#     print(a)
# h = decorator(g)
# g()
# h()

import time
def timer(func):
    def wrapper(*args, **kwargs):
        a = time.time()
        output =
        b =
        print a - b
        return output
    return wrapper
def f(a, b):
    return a + b
f = timer(f)
f(1, 2)
