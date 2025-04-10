def calculate_average_mass(masses):

    if not isinstance(masses, (list, tuple)):
        raise TypeError("Аргумент должен быть списком или кортежем.")

    if not masses:
        raise ValueError("Список масс не может быть пустым.")

    if not all(isinstance(mass, (int, float)) for mass in masses):
        raise ValueError("Все элементы списка должны быть числами.")

    total_mass = sum(masses)
    average_mass = total_mass / len(masses)

    return average_mass

try:
    masses1 = [10, 20, 30, 40, 50]
    average_mass1 = calculate_average_mass(masses1)
    print(f"Средняя масса для {masses1}: {average_mass1}")

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")