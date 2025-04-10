def find_first_greater_than_n(n):
  
  current_sum = 1.0  
  i = 2
  while True:
    if current_sum > n:
      return current_sum 
    current_sum += 1.0 / i
    i += 1

n = 3
result = find_first_greater_than_n(n)

if result is not None:
  print(f"Первое число, большее {n}: {result}")
else:
  print(f"Последовательность никогда не превышает {n}")


n = 10
result = find_first_greater_than_n(n)

if result is not None:
  print(f"Первое число, большее {n}: {result}")
else:
  print(f"Последовательность никогда не превышает {n}")