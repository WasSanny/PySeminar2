# 1. По данному целому неотрицательному n вычислите значение
# n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while


n = int(input("Введите число: "))

s = 1
result = 1

while (s <= n):
  result = result * s
  s += 1

print(result)

# Второй вариант задачи на факториал

# number = tempNumber= int(input("Введите n : "))
# factorialNumber = 1

# while (tempNumber != 1):
#   factorialNumber *= tempNumber
#   tempNumber -= 1

# print(f"факториал {number} = {factorialNumber}")