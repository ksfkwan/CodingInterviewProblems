def memoize(func):
    cache = {}
    def wrapper(arg):
        print(arg)      
        if arg not in cache:
            cache[arg] = func(arg)
        print(cache)
        return cache[arg]
    return wrapper

@memoize
def fibonacci(n):
    print(n)
    if n == 0:
        return 0
    elif n == 1 or n == -1:
        return 1
    elif n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    elif n < 0:
        return fibonacci(n + 2) - fibonacci(n + 1)

print(fibonacci(4))
