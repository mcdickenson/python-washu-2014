# setup
items = range(1, 5)

def sqr(x): return x**2

def cub(x): return x**3

# mapping
for x in items sqr(x)
map(sqr, items)
list(map((lambda x: x **2), items))

funcs = [sqr, cub]
for i in items:
    value = map(lambda x: x(i), funcs)
    print value

def mymap(aFunc, aSeq):
  result = []
  for x in aSeq: result.append(aFunc(x))
  return result

mymap(sqr, [1,2,3])

# reducing and filtering
range(-5, 5)
filter((lambda x: x < 0), range(-5,5))

from functools import reduce
reduce( (lambda x, y: x * y), items )

def myreduce(fnc, seq):
  total_so_far = seq[0]
  for next in seq[1:]:
    total_so_far = fnc(total_so_far, next)
  return total_so_far

L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
reduce( (lambda x,y:x+y), L)

reduce( (lambda x,y:x+y), map(len, L))

reduce( (lambda x,y:x+y), map(sqr, items))