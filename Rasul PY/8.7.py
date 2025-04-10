def find_first_less_than_a(a):
 
  if not 1 < a <= 1.5:
    return None 

  i = 2
  while True:
    number = 1 + (1 / i)
    if number < a:
      return number
    i += 1

a = 1.4
result = find_first_less_than_a(a)

if result is not None:
  print(f"Первое число, меньшее {a}: {result}")
else:
  print("Число a вне допустимого диапазона (1 < a <= 1.5)")


a = 1.2
result = find_first_less_than_a(a)

if result is not None:
  print(f"Первое число, меньшее {a}: {result}")
else:
  print("Число a вне допустимого диапазона (1 < a <= 1.5)")