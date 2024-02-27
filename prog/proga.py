import random
import time
print("Введите размер массива:")
n = int(input())
arr = [random.uniform(-1000, 1000) for _ in range(n)]

max_val = arr[0]
min_val = arr[0]

start_time = time.time()

for i in range(1, n):
    if arr[i] > max_val:
        max_val = arr[i]
    if arr[i] < min_val:
        min_val = arr[i]

print(f"Мин = {min_val}; Макс = {max_val}")
print(f"Время: {time.time() - start_time}")
