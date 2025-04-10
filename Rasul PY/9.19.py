def count_divisors(number):
    count = 0
    countDel = []
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
            countDel.append(i)
    return count, countDel

for num in range(100, 141):
    divisor_count, countDel = count_divisors(num)
    print(f"Число: {num}, Количество делителей: {divisor_count}, deliteli: {countDel}")