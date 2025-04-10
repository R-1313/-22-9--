def find_666(numbers):

    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Аргумент должен быть списком или кортежем.")

    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("Все элементы списка должны быть целыми числами.")

    if numbers[-1] != 100:
        raise ValueError("Последовательность должна заканчиваться числом 100.")

    found_666 = False
    first_index = None
    for i, num in enumerate(numbers):
        if num == 666:
            found_666 = True
            first_index = i + 1 
            break  

    return found_666, first_index

try:
    numbers1 = [1, 2, 666, 4, 100]
    found, index = find_666(numbers1)
    print(f"Последовательность: {numbers1}")
    print(f"  Число 666 найдено: {found}")
    print(f"  Порядковый номер: {index}") 

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")