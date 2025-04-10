def compare_densities(volume1, mass1, volume2, mass2):
  
  if not all(isinstance(arg, (int, float)) for arg in [volume1, mass1, volume2, mass2]):
    raise TypeError("Объемы и массы должны быть числами.")

  if volume1 <= 0 or volume2 <= 0:
    raise ValueError("Объемы должны быть положительными.")

  if mass1 < 0 or mass2 < 0:
    raise ValueError("Массы не могут быть отрицательными.")

  density1 = mass1 / volume1
  density2 = mass2 / volume2

  if density1 > density2:
    return "Материал первого тела имеет большую плотность."
  elif density2 > density1:
    return "Материал второго тела имеет большую плотность."
  else:
    return "Плотности материалов равны."

volume1 = 10
mass1 = 81
volume2 = 15
mass2 = 103

result = compare_densities(volume1, mass1, volume2, mass2)
print(result)