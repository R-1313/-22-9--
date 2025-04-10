def print_squares_less_than_n(n):
  i = 1
  while True:
    square = i * i
    if square > n:
      break 
    print(square, end=" ")
    i += 1
  print()
n = 50
print_squares_less_than_n(n)