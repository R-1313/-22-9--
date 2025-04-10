def is_product_less_than_10000(numbers):

    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Аргумент должен быть списком или кортежем.")

    if len(numbers) != 8:
        raise ValueError("Список должен содержать 8 чисел.")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Все элементы списка должны быть числами.")

    product = 1
    for num in numbers:
        product *= num

    return product < 10000

try:
    numbers1 = [1, 2, 3, 4, 5, 1, 1, 1]
    result1 = is_product_less_than_10000(numbers1)
    print(f"Произведение чисел {numbers1} меньше 10000: {result1}") 

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")