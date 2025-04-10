def count_grades(grades):

    if not isinstance(grades, (list, tuple)):
        raise TypeError("Аргумент должен быть списком или кортежем.")

    if not all(isinstance(grade, int) for grade in grades):
        raise ValueError("Все элементы списка должны быть целыми числами.")

    if not all(2 <= grade <= 5 for grade in grades):
        raise ValueError("Все элементы списка должны быть оценками в диапазоне от 2 до 5.")

    count_5 = grades.count(5)
    count_4 = grades.count(4)
    count_3 = grades.count(3)
    count_2 = grades.count(2)

    return count_5, count_4, count_3, count_2

try:
    grades1 = [5, 4, 3, 2, 5, 5, 4, 3, 2, 2]
    count_5, count_4, count_3, count_2 = count_grades(grades1)
    print(f"Оценки: {grades1}")
    print(f"  Пятерок: {count_5}, Четверок: {count_4}, Троек: {count_3}, Двоек: {count_2}")

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")