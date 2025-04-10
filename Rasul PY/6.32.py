def ski_training():
    start_distance = 10.0
    increase_percent = 0.10
    distance = start_distance
    total_distance = 0.0
    day = 1
    day_exceeds_20km = None
    day_exceeds_100km = None

    while True:
        total_distance += distance

        if distance > 20 and day_exceeds_20km is None:
            day_exceeds_20km = day

        if total_distance > 100 and day_exceeds_100km is None:
            day_exceeds_100km = day

        if day_exceeds_20km is not None and day_exceeds_100km is not None:
            break

        if day > 100:
            break

        distance += distance * increase_percent
        day += 1

    return day_exceeds_20km, day_exceeds_100km

day_20km, day_100km = ski_training()

if day_20km is not None:
    print(f"Лыжник пробежит больше 20 км на {day_20km}-й день.")
else:
    print("Лыжник не пробежит больше 20 км.")

if day_100km is not None:
    print(f"Суммарный пробег превысит 100 км на {day_100km}-й день.")
else:
    print("Суммарный пробег не превысит 100 км.")