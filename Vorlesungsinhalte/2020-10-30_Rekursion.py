# Element der Fibonacci-Folge berechnen:
def fib(n):
  if n == 0:    # f(0) = 0
    return 0
  elif n == 1:  # f(1) = 1
    return 1
  else:         # f(n) = f(n-1) + f(n-2)
    return fib (n-1) + fib (n-2)

# Ackermann-Funktion berechnen:
def ack(m,n):
  if m == 0:    # A(0,n) = n+1
    return n+1
  elif n == 0:  # A(m,0) = A(m-1,1)
    return ack(m-1,1)
  else:         # A(m,n) = A(m-1,A(m,n-1))
    return ack(m-1, ack(m,n-1))

# Hailstone-Folge ausgeben:
def hailstone(n):
  print(n)
  if n!=1:
    if n % 2 == 0:
      hailstone(n//2)
    else:
      hailstone(3*n+1)
