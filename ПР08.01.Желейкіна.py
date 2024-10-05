import random
from array import array

N = int(input("Введіть кількість випадкових чисел (N): "))
b = int(input("Введіть максимальне значення випадкових чисел (b): "))
M = int(input("Введіть кількість чисел, які треба додати в кінці (M): "))

arr = array('i', (random.randint(0, b) for i in range(N)))

for i in range(M):
    num = int(input(f"Введіть число {i + 1}: "))
    arr.append(num)

arr = array('i', sorted(arr, reverse=True))

print(list(arr))