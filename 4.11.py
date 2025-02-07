def compare_speeds(km_per_hour, meters_per_second):
  if not isinstance(km_per_hour, (int, float)) or not isinstance(meters_per_second, (int, float)):
    raise TypeError("Скорости должны быть числами.")

  if km_per_hour < 0 or meters_per_second < 0:
    raise ValueError("Скорости не могут быть отрицательными.")

  km_per_hour_in_meters_per_second = km_per_hour * 1000 / 3600 

  if km_per_hour_in_meters_per_second > meters_per_second:
    return "Скорость в километрах в час больше."
  elif meters_per_second > km_per_hour_in_meters_per_second:
    return "Скорость в метрах в секунду больше."
  else:
    return "Скорости равны."


km_per_hour = 72
meters_per_second = 201

result = compare_speeds(km_per_hour, meters_per_second)
print(result)