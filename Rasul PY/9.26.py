def func(sum):
    count=0
    for i in range(1, 101):
        if sum % i == 0:
            count = count+1
    if count == 2:
        return True
    else: 
        return False

print("Простый числа")
for i in range(1, 101):
        if func(i):
            print(f"{i}", end="    ")
