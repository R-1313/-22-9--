def compare_distances(kilometers, feet):
  if not isinstance(kilometers, (int, float)) or not isinstance(feet, (int, float)):
    raise TypeError("Расстояния должны быть числами.")

  if kilometers < 0 or feet < 0:
    raise ValueError("Расстояния не могут быть отрицательными.")

  kilometers_in_meters = kilometers * 1000
  feet_in_meters = feet * 0.3048

  if kilometers_in_meters < feet_in_meters:
    return "Расстояние в километрах меньше."
  elif feet_in_meters < kilometers_in_meters:
    return "Расстояние в футах меньше."
  else:
    return "Расстояния равны."

kilometers = 6
feet = 164

result = compare_distances(kilometers, feet)
print(result)