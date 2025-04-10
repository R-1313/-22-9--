def process_numbers(n, numbers):

    if not isinstance(n, int):
        raise TypeError("n должно быть целым числом.")

    if not isinstance(numbers, (list, tuple)):
        raise TypeError("numbers должно быть списком или кортежем.")

    if n <= 0:
        raise ValueError("n должно быть натуральным числом (больше 0).")

    if len(numbers) != n:
        raise ValueError("Длина списка numbers должна быть равна n.")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Все элементы списка numbers должны быть числами.")

    abs_sum = 0
    for num in numbers:
        if num < 0:
            abs_sum += -num 
        else:
            abs_sum += num

    abs_product = 1
    for num in numbers:
        abs_val = num if num >= 0 else -num 
        abs_product *= abs_val

    pair_sums = []
    for i in range(n - 1):
        pair_sums.append(numbers[i] + numbers[i + 1])

    alternating_sum = 0
    sign = 1 
    for num in numbers:
        alternating_sum += sign * num
        sign *= -1  

    return abs_sum, abs_product, pair_sums, alternating_sum

try:
    n = 5
    numbers = [1, -2, 3, -4, 5]
    abs_sum, abs_product, pair_sums, alternating_sum = process_numbers(n, numbers)

    print(f"Для списка {numbers}:")
    print(f"  Сумма абсолютных значений: {abs_sum}")
    print(f"  Произведение абсолютных значений: {abs_product}")
    print(f"  Суммы пар соседних чисел: {pair_sums}")
    print(f"  Альтернирующая сумма: {alternating_sum}")

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")