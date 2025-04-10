def find_min_max_digits(number):

    if not isinstance(number, int):
        raise TypeError("Аргумент должен быть целым числом.")

    if number <= 0:
        raise ValueError("Аргумент должен быть натуральным числом (больше 0).")

    number_str = str(number)
    max_digit = int(number_str[0]) 
    min_digit = int(number_str[0])

    for digit_char in number_str:
        digit = int(digit_char)

        if digit > max_digit:
            max_digit = digit

        if digit < min_digit:
            min_digit = digit

    return max_digit, min_digit

try:
    number = 123
    max_digit, min_digit = find_min_max_digits(number)
    print(f"В числе {number}:")
    print(f"  Максимальная цифра: {max_digit}")
    print(f"  Минимальная цифра: {min_digit}")

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")
