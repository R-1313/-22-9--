def compare_currents(resistance1, voltage1, resistance2, voltage2):

  if not all(isinstance(arg, (int, float)) for arg in [resistance1, voltage1, resistance2, voltage2]):
    raise TypeError("Сопротивления и напряжения должны быть числами.")

  if resistance1 <= 0 or resistance2 <= 0:
    raise ValueError("Сопротивления должны быть положительными.")

  try:
    current1 = voltage1 / resistance1
    current2 = voltage2 / resistance2
  except ZeroDivisionError:
    return "Сопротивление не может быть равно нулю."

  if current1 < current2:
    return "По первому участку протекает меньший ток."
  elif current2 < current1:
    return "По второму участку протекает меньший ток."
  else:
    return "Токи по обоим участкам равны."

resistance1 = 5
voltage1 = 12
resistance2 = 2
voltage2 = 12

result = compare_currents(resistance1, voltage1, resistance2, voltage2)
print(result)