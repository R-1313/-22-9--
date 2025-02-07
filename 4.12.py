import math

def compare_areas(circle_radius, square_side):
  if not isinstance(circle_radius, (int, float)) or not isinstance(square_side, (int, float)):
    raise TypeError("Радиус и сторона должны быть числами.")

  if circle_radius < 0 or square_side < 0:
    raise ValueError("Радиус и сторона не могут быть отрицательными.")

  circle_area = math.pi * circle_radius**2
  square_area = square_side**2

  if circle_area > square_area:
    return "Площадь круга больше."
  elif square_area > circle_area:
    return "Площадь квадрата больше."
  else:
    return "Площади равны."


circle_radius = 6
square_side = 9

result = compare_areas(circle_radius, square_side)
print(result)