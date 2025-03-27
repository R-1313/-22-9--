def find_max_odd_digit_and_min_digit_index(number):
    """
    Находит максимальную нечетную цифру и индекс минимальной цифры в числе.

    Args:
        number: Натуральное число (целое число больше 0).

    Returns:
        Кортеж из двух значений:
        - Максимальная нечетная цифра числа (или None, если не найдено).
        - Индекс (позиция) минимальной цифры в числе (при счете слева направо, начиная с 1).

    Raises:
        TypeError: Если аргумент не является целым числом.
        ValueError: Если аргумент не является натуральным числом (т.е. <= 0).
    """

    if not isinstance(number, int):
        raise TypeError("Аргумент должен быть целым числом.")

    if number <= 0:
        raise ValueError("Аргумент должен быть натуральным числом (больше 0).")

    number_str = str(number)
    max_odd_digit = None
    min_digit = int(number_str[0])  # Инициализируем минимальную цифру первой цифрой
    min_digit_index = 1  # Индекс начинается с 1

    for i, digit_char in enumerate(number_str):  # Используем enumerate для получения индекса
        digit = int(digit_char)
        index = i + 1  # Индекс начинается с 1

        if digit % 2 != 0:  # Проверяем, является ли цифра нечетной
            if max_odd_digit is None or digit > max_odd_digit:
                max_odd_digit = digit

        if digit < min_digit:
            min_digit = digit
            min_digit_index = index

    return max_odd_digit, min_digit_index


# Примеры использования:
try:
    number = 123456789
    max_odd_digit, min_digit_index = find_max_odd_digit_and_min_digit_index(number)
    print(f"В числе {number}:")
    if max_odd_digit is not None:
        print(f"  Максимальная нечетная цифра: {max_odd_digit}")
    else:
        print("  Нечетные цифры не найдены.")
    print(f"  Индекс минимальной цифры (слева направо): {min_digit_index}")


except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")