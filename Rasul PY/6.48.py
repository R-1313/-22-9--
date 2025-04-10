def find_max_odd_digit_and_min_digit_index(number):

    if not isinstance(number, int):
        raise TypeError("Аргумент должен быть целым числом.")

    if number <= 0:
        raise ValueError("Аргумент должен быть натуральным числом (больше 0).")

    number_str = str(number)
    max_odd_digit = None
    min_digit = int(number_str[0]) 
    min_digit_index = 1 

    for i, digit_char in enumerate(number_str):
        digit = int(digit_char)
        index = i + 1 

        if digit % 2 != 0:
            if max_odd_digit is None or digit > max_odd_digit:
                max_odd_digit = digit

        if digit < min_digit:
            min_digit = digit
            min_digit_index = index

    return max_odd_digit, min_digit_index

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