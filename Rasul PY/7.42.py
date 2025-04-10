def sum_of_even_numbers(numbers):

    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Аргумент должен быть списком или кортежем.")

    if len(numbers) != 10:
        raise ValueError("Список должен содержать 10 чисел.")

    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("Все элементы списка должны быть целыми числами.")

    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num

    return even_sum

try:
    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_sum1 = sum_of_even_numbers(numbers1)
    print(f"Сумма четных чисел в {numbers1}: {even_sum1}")  # Output: 30

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")