def outer():
  def inner():
    global x
    x = x + 10
    return x
  return inner

x = 1000
foo = outer()
print(foo())
print(x)
del x
foo()

#

def outer():
  x = 1000
  def inner():
    nonlocal x
    x = x + 10
    return x
  return inner

x = 10000
foo = outer()
for i in range(4):
  print(foo())

