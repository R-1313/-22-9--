'''Функция проверки простого числа'''
def func(sum):
    count=0
    for i in range(1, sum + 1 ):
        if sum % i == 0:
            count = count+1
    if count == 2:
        return True
    else: 
        return False


print("a) Полная таблица сложения (Вариант 1):")
for j in range(1, 10):
    for i in range(1, 10):
        if func(i+j):
            print(f"{i} + {j} = {i + j}", end="    ")
    print()






print("\nb) Полная таблица сложения (Вариант 2):")
for i in range(1, 10):
    for j in range(1, 10):
        if not func(i+j):
            print(f"{i} + {j} = {i + j}", end="    ")
    print()