def check_count_less_than_20(n, numbers):

    if not isinstance(n, int):
        raise TypeError("n должно быть целым числом.")

    if not isinstance(numbers, (list, tuple)):
        raise TypeError("numbers должно быть списком или кортежем.")

    if n <= 0:
        raise ValueError("n должно быть натуральным числом (больше 0).")

    if len(numbers) != n:
        raise ValueError("Длина списка numbers должна быть равна n.")

    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("Все элементы списка numbers должны быть целыми числами.")

    count_less_than_20 = 0
    for num in numbers:
        if num < 20:
            count_less_than_20 += 1

    return count_less_than_20 == 5

try:
    n1 = 10
    numbers1 = [1, 2, 3, 4, 5, 20, 30, 40, 50, 60]
    result1 = check_count_less_than_20(n1, numbers1)
    print(f"Список {numbers1}: Количество чисел меньше 20 равно 5: {result1}")  # True

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")