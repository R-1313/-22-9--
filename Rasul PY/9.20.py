def draw_divisibility_graph(n):
    
    for num in range(1, n + 1):
        divisor_count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                divisor_count += 1
        print(f"{num}{'+' * divisor_count}")

try:
    n = int(input("Попа"))
    if n <= 0:
        print("n должно быть положительным целым числом.")
    else:
        draw_divisibility_graph(n)
except ValueError:
    print("нога")
