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

# def decorate(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs) 
#         print(args, kwargs)  
#     return wrapper
# def f(a=[5], b=[6]):
#     print(a, b)
#     a.append(3)
#     b.append(4)
# f = decorate(f)
# f([1], b=[2])
# f([1], b=[2])

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
