def fib(n):
  if n<=1:
    return n
  return fib(n-1) + fib(n-2)

# fib(8) = fib(7) + fib(6) = 21
# fib(7) = fib(6) + fib(5) = 13
# fib(6) = fib(5) + fib(4) = 8
# fib(5) = fib(4) + fib(3) = 5
# fib(4) = fib(3) + fib(2) = 3
# fib(3) = fib(2) + fib(1) = 2
# fib(2) = fib(1) + fib(0) = 1
# fib(1) = 1
# fib(0) = 0 



for i in range(40):
  print "{0} : {1}".format(i, fib(i))