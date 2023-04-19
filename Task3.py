# 2. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n, что φ(n)=A. Если А не является
# числом Фибоначчи, выведите число -1.

n = int(input("Введите проверяемое число: "))

if n == 0:
  print(1)
else:
  fib_prev, fib_next = 0, 1
  s = 2
  while fib_next <= n:
    if fib_next == n:
      print(s)
      break
    fib_prev, fib_next = fib_next, fib_prev + fib_next
    s += 1
  else:
    print(-1)
